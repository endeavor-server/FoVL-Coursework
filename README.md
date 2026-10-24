# Foundations of Vision and Language (FoVL) — Coursework Repository
**Course Code:** AIL7260 / FoVL  
**Program:** Post Graduate Diploma in Artificial Intelligence (PGD AI) / M.Tech AI  
**Institution:** Indian Institute of Technology Jodhpur  
**Instructor:** Sidharth Ranjan  
**Student:** Nikhil Saini (Roll No. G25AIT2067)  
**Academic Year:** 2026–2027 (Autumn 2026)  

---

## 📌 Repository Overview

This repository maintains the complete, synchronized knowledge base, lecture synthesis, practical lab notebooks, and project deliverables for the **Foundations of Vision and Language (FoVL)** curriculum at IIT Jodhpur.

It consolidates all materials from the official course schedule, Google Classroom, and the central course spreadsheet:
- **Official Google Sheet Source:** [IIT Jodhpur PGD-AI Master Course Tracker (FoVL Tab)](https://docs.google.com/spreadsheets/d/1xqmJ7fPf4Ggp-OFoImH0jCpzIIFCp1saNLIPcvqiJg0/edit?gid=1641191067#gid=1641191067)

---

## 📂 Repository Layout

```text
FoVL_Coursework/
├── README.md                                # Master repository documentation and guide
├── knowledge_base/
│   └── FOVL_SUBJECT_KNOWLEDGE_BASE.md       # Comprehensive 8-section subject knowledge base
├── resources/
│   └── FOVL_COURSE_RESOURCES_INDEX.md       # Catalog of all 42 course resources from Google Sheet
├── notebooks/
│   ├── G25AIT2067_FoVL_CV_Project.ipynb     # Individual Mini CV Project notebook (YOLO11n on COCO128)
│   └── cv_analysis.md                       # Experimental analysis on blur, sharpening, and mAP
└── lectures/                                # Lecture notes and topic outlines
```

---

## 📖 Master Subject Knowledge Base

The primary reference document for this course is located in:
👉 **[`knowledge_base/FOVL_SUBJECT_KNOWLEDGE_BASE.md`](knowledge_base/FOVL_SUBJECT_KNOWLEDGE_BASE.md)**

It provides comprehensive coverage across six core thematic modules:
1. **Module 1: Cognitive Foundations and Nature of Language**
   - The symbolic function (form–meaning pairing, concepts vs. percepts, projected reality).
   - Under-specification in natural language (*"The cat jumped over the wall"*).
   - Case studies: Pirahã language (Daniel Everett vs. Chomsky's Universal Grammar recursion debate), Deb Roy's MIT study (*"Birth of a Word"*), and Vsauce (*"The Zipf Mystery"*).
   - David Marr's Tri-Level Hypothesis (Computational, Algorithmic/Representational, Implementational/Physical).
   - Definitions of AI, the Turing Test, and the Total Turing Test.
   - Disciplinary distinctions: NLP (engineering) vs. CL (cognitive science) vs. NLU (comprehension).
   - Early NLU systems: ELIZA (1966 pattern matching) vs. SHRDLU (1972 procedural semantics).
   - Linguistic ambiguity (Acoustic, Lexical, Syntactic Attachment, Scope, Semantic, Pragmatic).
   - J.R. Firth's Distributional Hypothesis and the limits of form-only language models (Bender & Koller 2020 Octopus Test; Ettinger 2020 BERT psycholinguistic diagnostics).
2. **Module 2: Information Theory, Statistical Language Modeling & SRILM**
   - Power-law word frequency distributions vs. Gaussian normal distributions.
   - Zipf's Law ($f_i \propto 1/r_i \iff f \times r \approx k$) and the Principle of Least Effort.
   - Shannon's N-th order approximations of English (zero-order, character unigram/bigram/trigram, word bigrams).
   - Mathematical Information Theory: Surprisal, Shannon Entropy ($H$), Joint Entropy, Conditional Entropy, Chain Rule, Mutual Information ($I$), and Relative Entropy / KL Divergence ($D_{KL}$).
   - Language Modeling with the Markov Assumption (Unigram, Bigram, Trigram).
   - Intrinsic model evaluation via Log-Likelihood and Perplexity ($PP = 2^{\hat{H}}$).
   - Zero-probability dilemmas and smoothing: Laplace (Add-1), Add-$k$, Absolute Discounting, Jelinek-Mercer Linear Interpolation, Katz Backoff, and Kneser-Ney Continuation Probability.
   - Complete SRILM Toolkit pipeline (`ngram-count`, `ngram`, ARPA file structure, `ppl` vs. `ppl1`).
   - Shannon's Noisy Channel Model ($\hat{I} = \arg\max P(O \mid I) P(I)$).
3. **Module 3: Sequence Tagging, POS Tagging & Syntactic Formalisms**
   - Part-of-Speech Tagging: Penn Treebank (45 tags) vs. Universal Dependencies (17 tags).
   - Tagger architectures: Rule-based, Regex, Unigram, HMM (Generative), CRF / Averaged Perceptron (Discriminative).
   - Hidden Markov Models (HMM) for POS tagging: State transitions ($A$), emissions ($B$), and priors ($\pi$).
   - The Three Classic HMM Problems: Evaluation (Forward Algorithm), Decoding (Viterbi Algorithm), and Learning (Baum-Welch / EM).
   - Chunking and Named Entity Recognition (NER) via IOB Encoding (`B-`, `I-`, `O`).
   - Syntactic Formalisms: Constituency (Context-Free Grammars / Phrase Structure) vs. Dependency (Direct Head-to-Dependent Arcs).
   - Prepositional Phrase attachment ambiguity (*"I shot an elephant in my pajamas"*).
4. **Module 4: Modern Methods — Word Embeddings & Distributional Semantics**
   - Sparse one-hot vectors and the orthogonality failure.
   - Dense distributed representations: Word2Vec Continuous Bag-of-Words (CBOW) and Skip-Gram.
   - Softmax normalization bottleneck and Skip-Gram with Negative Sampling (SGNS) logistic objective.
   - Geometric vector algebra and compositionality ($v_{\text{King}} - v_{\text{Man}} + v_{\text{Woman}} \approx v_{\text{Queen}}$).
5. **Module 5: Computer Vision Foundations & Applied Project**
   - Spatio-temporal motion descriptors: Histogram of Optical Flow (HOF) and Motion Boundary Histograms (MBH).
   - Object detection frameworks: Two-stage (R-CNN, Fast R-CNN, Faster R-CNN) vs. One-stage (YOLO, SSD, RetinaNet).
   - Semantic segmentation (FCN, U-Net, DeepLab with Atrous Convolutions and ASPP).
   - Applied Mini CV Project: Evaluating Ultralytics YOLO11n on COCO128 under $9 \times 9$ Gaussian blur and unsharp masking.
6. **Module 6: Worked Numerical Problem Sets and Class Discussions**
   - Step-by-step solutions to entropy calculations (8-sided die: 3.0 bits; coin toss: 1.0 bit).
   - Full derivation of joint entropy, conditional entropy, and mutual information for the Weather-Umbrella problem.
   - Complete worked manual calculations for bigram MLE probabilities and perplexities on the 5-sentence toy corpus (`<s> I am Sam </s>`).
   - Model answers for the core cognitive discussion questions (ELIZA, understanding vs. processing, form vs. meaning).

---

## 🛠️ Practical Deliverables & Notebooks

- **Individual Mini CV Project:** [`notebooks/G25AIT2067_FoVL_CV_Project.ipynb`](notebooks/G25AIT2067_FoVL_CV_Project.ipynb)
  - Target Model: Pretrained Ultralytics YOLO11n (`yolo11n.pt`).
  - Dataset: COCO128.
  - Evaluation:
    - Clean Baseline: Precision = 0.6633, Recall = 0.5894, mAP@0.5 = 0.6696, mAP@0.5:0.95 = 0.5024.
    - Gaussian Blur ($9 \times 9$): Precision = 0.6784, Recall = 0.5351, mAP@0.5 = 0.6168, mAP@0.5:0.95 = 0.4434.
    - Unsharp Masking: Precision = 0.6672, Recall = 0.5294, mAP@0.5 = 0.6274, mAP@0.5:0.95 = 0.4569.
  - Full writeup: [`notebooks/cv_analysis.md`](notebooks/cv_analysis.md).

---

## 📚 Course Resources Catalog

The complete tabular index containing all 42 entries from the central course sheet (videos, slides, lab sessions, and announcements) is documented in:
👉 **[`resources/FOVL_COURSE_RESOURCES_INDEX.md`](resources/FOVL_COURSE_RESOURCES_INDEX.md)**

---

## 👨‍🎓 Author & Coursework Details
- **Student Name:** Nikhil Saini
- **Roll Number:** G25AIT2067
- **Email:** nikhilsaini@iitj.ac.in
- **Academic Program:** Post Graduate Diploma in Artificial Intelligence (PGD AI)
- **Institution:** Indian Institute of Technology Jodhpur
