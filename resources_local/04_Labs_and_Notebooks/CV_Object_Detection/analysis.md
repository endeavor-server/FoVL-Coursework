### A. Effect of blur — 3 marks

- Blurring with the 9 x 9 Gaussian kernel hurt the detector on every metric that matters for localisation: mAP@0.5 fell from 0.6696 to 0.6168 and mAP@0.5:0.95 fell from 0.5024 to 0.4434, so the strict metric lost about 6 points.
- Recall dropped the most, 0.5894 to 0.5351. The blur washes out edges and small objects, so the model simply misses them. In 000000000109.jpg (the riverside) the original run found 10 objects including a boat and two benches; on the blurred copy only 6 remained, all low confidence persons (0.30 to 0.40), and the boat and benches were gone.
- Precision actually went up slightly, 0.6633 to 0.6784. The model only keeps the boxes it is sure about, so the ones it still reports tend to be right. It is not a real improvement, because it comes with far fewer detections.
- Blur also creates some odd boxes. In 000000000009.jpg (the lunch box) the blurred run reported 7 objects instead of 5, adding a "spoon 0.34" and a "bowl 0.27" that do not exist. Big, high contrast objects survive: the broccoli was still found at 0.88 and the bowls at 0.92 and 0.77.

### B. Why sharpening? — 2 marks

- I used unsharp masking, written by hand with OpenCV: blur the image a little more (Gaussian, sigma 1.5), subtract that smooth version from the image to get the edge detail, and add the detail back with weight 1.0. In code it is `cv2.addWeighted(img, 2.0, smooth, -1.0, 0)`, which also keeps the image size unchanged.
- The idea is that Gaussian blur mostly removes the high frequency part of the image (edges, texture). Unsharp masking amplifies whatever high frequency content is left, so edges become steeper again and the detector's early layers get stronger gradients to work with. It cannot bring back information that the blur deleted, it can only boost what survived.

### C. Did sharpening help? — 4 marks

- Partly. Both localisation metrics improved over the blurred stage: mAP@0.5 went 0.6168 to 0.6274 (+0.0106) and mAP@0.5:0.95 went 0.4434 to 0.4569 (+0.0135). So the boxes that are found are placed a bit better, which is what sharper edges should give.
- Recall did not recover. It went 0.5351 to 0.5294, slightly worse, and stays far below the original 0.5894. The objects lost in Stage 2 are still lost: in 000000000109.jpg the sharpened image gives only 4 objects (persons at 0.45 and 0.53), the boat and benches never come back.
- Precision went down a little, 0.6784 to 0.6672, but it is still above the baseline 0.6633. Sharpening also removed the two false boxes in the lunch box image: the sharpened run reports 5 objects again, the same set as the original, with broccoli at 0.89 and bowls at 0.93, 0.76, 0.61.
- On the crowded baseball picture 000000000357.jpg nothing much changed: 8 objects originally, 9 blurred, 9 sharpened, with person confidences around 0.7 to 0.85 in all three. So the effect depends on the image: it helps medium sized objects, does little for large ones, and cannot rescue small ones.
- Overall the sharpened result (mAP@0.5:0.95 0.4569) is still well under the original 0.5024. Sharpening recovers roughly a quarter of what blur took away.

### D. Final conclusion — 1 mark

I would keep it, but with modest expectations. It is one cheap OpenCV call, it does not touch the model, and on this data it gave back about 1 point of mAP@0.5 and 1.4 points of mAP@0.5:0.95 while also removing a couple of false boxes. The downside is small: recall and precision each moved by less than 0.01, essentially noise. What it cannot do is undo the blur, since recall stays about 6 points below the clean images. So it is a sensible low cost pre-processing step, not a fix for blurry input.
