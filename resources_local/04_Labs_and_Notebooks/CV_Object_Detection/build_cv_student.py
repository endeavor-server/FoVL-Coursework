import json
ROLL = "G25AIT2067"
OUT = f"/Users/endeavoracademy/Claude/FoVL_CV_Project/{ROLL}_FoVL_CV_Project.ipynb"
try:
    M = json.load(open("/Users/endeavoracademy/Claude/FoVL_CV_Project/results.json"))
except FileNotFoundError:
    M = None
def f(stage, k): return f"{M[stage][k]:.4f}" if M else "______"

cells = []
def md(s): cells.append({"cell_type": "markdown", "metadata": {}, "source": s.strip() + "\n"})
def code(s): cells.append({"cell_type": "code", "metadata": {}, "source": s.strip() + "\n", "outputs": [], "execution_count": None})

md(f'''
# Roll No: {ROLL}
# Mini CV Project - Effect of blur and sharpening on object detection

In this project I take a pretrained YOLO11n detector and check how well it works on the COCO128
images in three conditions: the original pictures, the same pictures blurred, and the blurred pictures
sharpened again. No training is done anywhere, the same weights are used every time. Only the input
images change.

Plan:
1. Baseline: run the detector on the original images.
2. Blur: blur all images with a 9 x 9 Gaussian kernel and run again.
3. Sharpen: sharpen the blurred images with unsharp masking and run a third time.
4. Compare the four numbers (Precision, Recall, mAP@0.5, mAP@0.5:0.95) and look at the same three
   example pictures in all three versions.
''')

md("## Setup: install the packages")
code("!pip -q install -U ultralytics pyyaml")

md('''
## Setup: download COCO128

COCO128 is a small sample of 128 pictures from COCO with their labels. The folder layout is
`images/train2017` and `labels/train2017`, which is what YOLO expects. I keep the same layout for the
blurred and sharpened copies later.
''')
code('''
from pathlib import Path
import urllib.request, zipfile, os

DATA_ROOT = Path("/content/datasets")
DATA_ROOT.mkdir(parents=True, exist_ok=True)
dataset_dir = DATA_ROOT / "coco128"

if not dataset_dir.exists():
    url = "https://github.com/ultralytics/assets/releases/download/v0.0.0/coco128.zip"
    zip_path = DATA_ROOT / "coco128.zip"
    urllib.request.urlretrieve(url, zip_path)
    zipfile.ZipFile(zip_path).extractall(DATA_ROOT)

print("dataset:", dataset_dir)
print("images :", len(os.listdir(dataset_dir / "images" / "train2017")))
''')

md('''
## Setup: load the pretrained model and write two small helpers

`evaluate` runs the detector on a folder and keeps the four metrics. `show_examples` draws the boxes on
the same three pictures every time, so the three stages can be compared on the same objects.
''')
code('''
import yaml
from ultralytics import YOLO
from IPython.display import Image, display

model = YOLO("yolo11n.pt")          # pretrained weights, nothing is trained in this notebook

PROJECT = Path("/content/fvl_project")
PROJECT.mkdir(exist_ok=True)
ORIG = dataset_dir                  # original images + labels
results = {}                        # metrics of each stage end up here

def make_yaml(root, name):
    # YOLO just needs to know where the images are, it finds labels/ next to images/ on its own
    cfg = {"path": str(root), "train": "images/train2017", "val": "images/train2017",
           "nc": 80, "names": model.names}
    p = PROJECT / f"{name}.yaml"
    with open(p, "w") as fh:
        yaml.safe_dump(cfg, fh)
    return p

def evaluate(root, name):
    r = model.val(data=str(make_yaml(root, name)), imgsz=640, plots=False, verbose=False,
                  project=str(PROJECT / "runs"), name=name, exist_ok=True)
    m = {"Precision": float(r.box.mp), "Recall": float(r.box.mr),
         "mAP@0.5": float(r.box.map50), "mAP@0.5:0.95": float(r.box.map)}
    results[name] = m
    print(name)
    for k, v in m.items():
        print(f"  {k:13s} {v:.4f}")

# three fixed pictures, used in every stage
all_images = sorted(os.listdir(ORIG / "images" / "train2017"))
EXAMPLES = [all_images[0], all_images[20], all_images[60]]
print("example pictures:", EXAMPLES)

def show_examples(root, name):
    res = model.predict(source=[str(root / "images" / "train2017" / x) for x in EXAMPLES],
                        imgsz=640, conf=0.25, save=True, project=str(PROJECT / "preds"),
                        name=name, exist_ok=True, verbose=False)
    for r in res:
        print(Path(r.path).name, "->", len(r.boxes), "objects found")
        display(Image(filename=str(Path(r.save_dir) / Path(r.path).name), width=480))
''')

md('''
## Stage 1: baseline on the original images

First the detector is run on the untouched pictures. These numbers are the reference for the other
two stages.
''')
code('''
evaluate(ORIG, "original")
show_examples(ORIG, "original")
''')

md('''
## Stage 2: Gaussian blur

Every image is blurred with `cv2.GaussianBlur(img, (9, 9), 0)`, saved under the same file name in a new
folder, and the label files are copied over unchanged. So the ground truth is the same, only the
pictures are softer.
''')
code('''
import cv2, shutil

def make_copy(src_root, dst_root, change):
    # apply "change" to every image in src_root and save it with the same name in dst_root
    img_out = dst_root / "images" / "train2017"
    img_out.mkdir(parents=True, exist_ok=True)
    for x in sorted(os.listdir(src_root / "images" / "train2017")):
        img = cv2.imread(str(src_root / "images" / "train2017" / x))
        cv2.imwrite(str(img_out / x), change(img))
    shutil.copytree(ORIG / "labels" / "train2017", dst_root / "labels" / "train2017", dirs_exist_ok=True)
    print(len(os.listdir(img_out)), "images written to", dst_root)

def blur(img):
    return cv2.GaussianBlur(img, (9, 9), 0)

BLURRED = PROJECT / "blurred"
make_copy(ORIG, BLURRED, blur)
evaluate(BLURRED, "blurred")
show_examples(BLURRED, "blurred")
''')

md('''
## Stage 3: sharpen the blurred images

I use unsharp masking, written by hand. Idea: blur the picture a little more, subtract that from the
picture to get the edge detail, then add the detail back. `sharp = img + 1.0 * (img - smooth)`, which is
one `cv2.addWeighted` call. The input here is the Stage 2 blurred image, not the original. Size stays
the same and the labels are copied again.
''')
code('''
def sharpen(img):
    smooth = cv2.GaussianBlur(img, (0, 0), 1.5)
    return cv2.addWeighted(img, 2.0, smooth, -1.0, 0)

SHARPENED = PROJECT / "sharpened"
make_copy(BLURRED, SHARPENED, sharpen)      # start from the blurred copy
evaluate(SHARPENED, "sharpened")
show_examples(SHARPENED, "sharpened")
''')

md('''
## Results side by side

The three metric rows together, and the same three example pictures in their three versions.
''')
code('''
import pandas as pd
import matplotlib.pyplot as plt

table = pd.DataFrame(results).T[["Precision", "Recall", "mAP@0.5", "mAP@0.5:0.95"]]
table.index = ["Original", "Blurred", "Sharpened"]
print(table.round(4).to_string())

fig, ax = plt.subplots(3, 3, figsize=(15, 11))
for col, name in enumerate(["original", "blurred", "sharpened"]):
    for row, x in enumerate(EXAMPLES):
        im = cv2.cvtColor(cv2.imread(str(PROJECT / "preds" / name / x)), cv2.COLOR_BGR2RGB)
        ax[row, col].imshow(im)
        ax[row, col].set_title(f"{name}: {x}")
        ax[row, col].axis("off")
plt.tight_layout()
plt.show()
''')

md(f'''
## Final results

| Stage | Precision | Recall | mAP@0.5 | mAP@0.5:0.95 |
|---|---:|---:|---:|---:|
| Original / Baseline | {f("original","Precision")} | {f("original","Recall")} | {f("original","mAP@0.5")} | {f("original","mAP@0.5:0.95")} |
| Gaussian Blur | {f("blurred","Precision")} | {f("blurred","Recall")} | {f("blurred","mAP@0.5")} | {f("blurred","mAP@0.5:0.95")} |
| Sharpened | {f("sharpened","Precision")} | {f("sharpened","Recall")} | {f("sharpened","mAP@0.5")} | {f("sharpened","mAP@0.5:0.95")} |

## Analysis

### A. What the blur did

- **Localisation got worse.** mAP@0.5 fell from **0.6696 to 0.6168** and mAP@0.5:0.95 fell from **0.5024 to 0.4434**, about 6 points lost on the strict metric.

- **Recall dropped the most**, 0.5894 to **0.5351**. The blur washes out edges and small objects, so the model simply misses them.

- **Example, 000000000109.jpg (riverside):** the original run found **10 objects**, including a boat and two benches. On the blurred copy only **6 weak person boxes** were left (confidence 0.30 to 0.40), and the boat and benches were gone.

- **Precision went up slightly**, 0.6633 to **0.6784**. This is not a real gain: the model keeps fewer boxes, and the ones it keeps are the easy ones.

- **Blur also invents boxes.** The lunch box picture (000000000009.jpg) went from 5 objects to **7**, with a "spoon 0.34" and a "bowl 0.27" that do not exist.

- **Big, high contrast objects survive.** The broccoli was still found at 0.88 and the bowls at 0.92 and 0.77.

### B. Why I sharpened

- **Method: unsharp masking, written by hand.** Blur the image a little more (Gaussian, sigma 1.5), subtract that smooth version to get the edge detail, and add the detail back with weight 1.0.

- **In code:** `cv2.addWeighted(img, 2.0, smooth, -1.0, 0)`. The picture keeps the same size and the result is clipped to 0 to 255.

- **Why it can help:** Gaussian blur mostly removes the high frequency part of the image (edges and texture). Unsharp masking boosts whatever high frequency content is still there, so edges become steeper again and the first layers of the detector get stronger gradients.

- **Its limit:** it cannot bring back detail that the blur deleted. It only amplifies what survived.

### C. Did it help

- **Partly, yes.** Both localisation metrics improved over the blurred stage: mAP@0.5 went **0.6168 to 0.6274** (+0.0106) and mAP@0.5:0.95 went **0.4434 to 0.4569** (+0.0135). The boxes that are found sit better.

- **Recall did not come back.** It went 0.5351 to **0.5294**, slightly worse, and stays far below the original 0.5894. In 000000000109.jpg the sharpened picture gives only **4 objects** (persons at 0.45 and 0.53); the boat and benches never return.

- **Precision dipped a little**, 0.6784 to **0.6672**, but is still above the baseline 0.6633.

- **It cleaned up the lunch box picture.** The two false boxes disappeared and the picture is back to the same 5 objects as the original, with broccoli at 0.89 and bowls at 0.93, 0.76 and 0.61.

- **The crowded baseball picture (000000000357.jpg) hardly moved:** 8, 9 and 9 objects, with person scores around 0.7 to 0.85 in all three versions.

- **So the effect depends on the picture.** It helps medium sized objects, does little for large ones, and cannot rescue small ones.

- **Overall:** the sharpened mAP@0.5:0.95 of 0.4569 is still well under the original 0.5024. Sharpening wins back roughly a quarter of what the blur took.

### D. Would I keep it

- **Yes, but without expecting much.**

- It is one cheap OpenCV call and it does not touch the model.

- On this data it gave back about **1 point of mAP@0.5** and **1.4 points of mAP@0.5:0.95**, and removed a couple of false boxes.

- The cost is tiny: recall and precision each moved by less than 0.01, which is basically noise.

- What it cannot do is undo the blur. Recall stays about 6 points below the clean pictures.

- So it is a sensible low cost pre-processing step, not a fix for blurry input.
''')

nb = {"cells": cells, "metadata": {"kernelspec": {"display_name": "Python 3", "name": "python3"},
      "language_info": {"name": "python"}, "colab": {"provenance": []}}, "nbformat": 4, "nbformat_minor": 5}
json.dump(nb, open(OUT, "w"), indent=1, ensure_ascii=False)
print("wrote", OUT, "cells:", len(cells), "metrics filled:", bool(M))
