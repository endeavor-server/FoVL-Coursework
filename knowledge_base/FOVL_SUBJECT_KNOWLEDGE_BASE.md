# Foundations of Vision and Language (FoVL) — Comprehensive Subject Knowledge Base
## Post Graduate Diploma in Artificial Intelligence (PGD AI) / M.Tech AI
**Institution:** Indian Institute of Technology Jodhpur  
**Course Code:** AIL7260 / FoVL  
**Instructor:** Sidharth Ranjan  
**Master Document Version:** Autumn 2026  

---

## Table of Contents
1. [Course Overview, Pedagogy, and Scope](#1-course-overview-pedagogy-and-scope)
2. [Module 1: Cognitive Foundations and the Nature of Language](#2-module-1-cognitive-foundations-and-the-nature-of-language)
   - [1.1 What is Language? (A Window to the Mind)](#11-what-is-language-a-window-to-the-mind)
   - [1.2 The Concentric Layers of Linguistics](#12-the-concentric-layers-of-linguistics)
   - [1.3 The Symbolic Function (Form–Meaning Pairs and Projected Reality)](#13-the-symbolic-function-formmeaning-pairs-and-projected-reality)
   - [1.4 The Interactive Function (Transmission and Inferential Reconstruction)](#14-the-interactive-function-transmission-and-inferential-reconstruction)
   - [1.5 Case Studies: Pirahã, Deb Roy's "Birth of a Word", and Vsauce "The Zipf Mystery"](#15-case-studies-pirahã-deb-roys-birth-of-a-word-and-vsauce-the-zipf-mystery)
   - [1.6 Marr's Tri-Level Hypothesis in AI and Perception](#16-marrs-tri-level-hypothesis-in-ai-and-perception)
   - [1.7 Definitions of AI, the Turing Test, and the Total Turing Test](#17-definitions-of-ai-the-turing-test-and-the-total-turing-test)
   - [1.8 Disciplinary Distinctions: NLP vs. CL vs. NLU](#18-disciplinary-distinctions-nlp-vs-cl-vs-nlu)
   - [1.9 Early NLU Milestones: ELIZA vs. SHRDLU](#19-early-nlu-milestones-eliza-vs-shrdlu)
   - [1.10 The Pervasive Challenge of Linguistic Ambiguity](#110-the-pervasive-challenge-of-linguistic-ambiguity)
   - [1.11 Distributional Semantics (Firth) and Limits of Form-Only Models](#111-distributional-semantics-firth-and-limits-of-form-only-models)
3. [Module 2: Information Theory, Language Modeling, and Statistical NLP](#3-module-2-information-theory-language-modeling-and-statistical-nlp)
   - [2.1 Word Frequencies: Normal Distributions vs. Zipf's Law](#21-word-frequencies-normal-distributions-vs-zipfs-law)
   - [2.2 Shannon's N-th Order Approximations of English](#22-shannons-n-th-order-approximations-of-english)
   - [2.3 Mathematical Information Theory (Surprisal, Entropy, Joint, Conditional, Mutual Information, KL Divergence)](#23-mathematical-information-theory)
   - [2.4 Language Modeling and the Markov Assumption](#24-language-modeling-and-the-markov-assumption)
   - [2.5 Intrinsic Evaluation and Perplexity](#25-intrinsic-evaluation-and-perplexity)
   - [2.6 The Zero-Probability Dilemma and Smoothing Techniques](#26-the-zero-probability-dilemma-and-smoothing-techniques)
   - [2.7 The SRILM Toolkit Practical Pipeline](#27-the-srilm-toolkit-practical-pipeline)
   - [2.8 Shannon's Noisy Channel Model in Computational Linguistics](#28-shannons-noisy-channel-model-in-computational-linguistics)
4. [Module 3: Sequence Tagging, POS Tagging, and Syntactic Analysis](#4-module-3-sequence-tagging-pos-tagging-and-syntactic-analysis)
   - [3.1 Part-of-Speech Tagging and Tagsets (Penn Treebank vs. Universal Dependencies)](#31-part-of-speech-tagging-and-tagsets)
   - [3.2 Taxonomy of Taggers (Rule-Based, Regex, N-gram, Generative vs. Discriminative)](#32-taxonomy-of-taggers)
   - [3.3 Hidden Markov Models (HMM) for Sequence Labeling](#33-hidden-markov-models-hmm-for-sequence-labeling)
   - [3.4 The Three Classical HMM Problems and Algorithms (Forward, Viterbi, Baum-Welch)](#34-the-three-classical-hmm-problems-and-algorithms)
   - [3.5 Chunking, Shallow Parsing, and IOB Encoding](#35-chunking-shallow-parsing-and-iob-encoding)
   - [3.6 Syntactic Structure Formalisms: Constituency vs. Dependency](#36-syntactic-structure-formalisms-constituency-vs-dependency)
   - [3.7 Structural and Attachment Ambiguities](#37-structural-and-attachment-ambiguities)
5. [Module 4: Modern Methods — Word Embeddings and Distributional Semantics](#5-module-4-modern-methods--word-embeddings-and-distributional-semantics)
   - [4.1 Limitations of Discrete Symbolic Representations](#41-limitations-of-discrete-symbolic-representations)
   - [4.2 Word2Vec Architecture (Continuous Bag-of-Words vs. Skip-Gram)](#42-word2vec-architecture-cbow-vs-skip-gram)
   - [4.3 The Softmax Bottleneck and Skip-Gram with Negative Sampling (SGNS)](#43-the-softmax-bottleneck-and-skip-gram-with-negative-sampling-sgns)
   - [4.4 Geometric and Compositional Properties of Word Vectors](#44-geometric-and-compositional-properties-of-word-vectors)
   - [4.5 Evaluation: Word Analogies and Semantic Similarity](#45-evaluation-word-analogies-and-semantic-similarity)
6. [Module 5: Computer Vision Foundations and Applied Object Detection](#6-module-5-computer-vision-foundations-and-applied-object-detection)
   - [5.1 Image Representation, Filtering, and Classical Features](#51-image-representation-filtering-and-classical-features)
   - [5.2 Spatio-Temporal Descriptors: HOF (Histogram of Optical Flow) and MBH (Motion Boundary Histograms)](#52-spatio-temporal-descriptors-hof-and-mbh)
   - [5.3 Object Detection Paradigms (Two-Stage vs. One-Stage Detectors)](#53-object-detection-paradigms-two-stage-vs-one-stage)
   - [5.4 Semantic Segmentation (FCN, U-Net, DeepLab with Atrous Convolutions)](#54-semantic-segmentation-fcn-u-net-deeplab)
   - [5.5 Individual Mini CV Project: Robustness Analysis of YOLO11n under Blur and Sharpening](#55-individual-mini-cv-project-robustness-analysis-of-yolo11n)
7. [Module 6: Fully Worked Problem Sets, In-Class Activities, and Solutions](#7-module-6-fully-worked-problem-sets-in-class-activities-and-solutions)
   - [6.1 Information Theory Worked Numerical Problems](#61-information-theory-worked-numerical-problems)
   - [6.2 Language Modeling Toy Corpus Activity (Complete Worked Steps)](#62-language-modeling-toy-corpus-activity)
   - [6.3 Core Cognitive Discussion Questions and Model Answers](#63-core-cognitive-discussion-questions-and-model-answers)
8. [Master Bibliography and Literature](#8-master-bibliography-and-literature)

---

## 1. Course Overview, Pedagogy, and Scope

Foundations of Vision and Language (FoVL) explores the theoretical, statistical, cognitive, and deep-learning methodologies required to bridge visual perception and linguistic communication. 

### Course Logistics & Teaching Format
- **Program:** Post Graduate Diploma in Artificial Intelligence (PGD AI) / M.Tech AI, IIT Jodhpur
- **Instructor:** Sidharth Ranjan
- **Schedule:** Friday 6:00 PM – 7:30 PM & Saturday 2:30 PM – 4:00 PM (Hybrid: Google Meet / CS101, CSE Building)
- **Pedagogy:**
  - Alternating theory lectures, blackboard/writing-pad conceptual derivations, and interactive laboratory coding sessions.
  - Two distinct halves: **Traditional Methods** (8 lectures on symbolic/statistical NLP, information theory, HMMs, CFGs, and classical feature engineering) and **Modern Methods** (8 lectures on distributed representations, Word2Vec, deep convolutional vision architectures, sequence models, and vision-language integration).

---

## 2. Module 1: Cognitive Foundations and the Nature of Language

### 1.1 What is Language? (A Window to the Mind)
Language is not merely a communication tool; it reflects human conceptualization. It serves as a "window to the mind," providing observable insight into the nature, organization, and systematicity of thoughts. We study language computationally to:
1. Formalize its underlying systematic structure.
2. Characterize how communicative functions are realized by symbolic grammar.
3. Model cognitive information processing in computational systems.

### 1.2 The Concentric Layers of Linguistics
Linguistics is organized into hierarchically nested concentric layers:
1. **Phonetics:** Physical acoustic and articulatory properties of speech sounds.
2. **Phonology:** Discrete, contrastive cognitive sound units (phonemes) within a specific language.
3. **Morphology:** The internal composition of words from meaningful sub-units (morphemes, e.g., root + affixes).
4. **Syntax:** Grammatical rules governing how words combine into hierarchical phrases and sentences.
5. **Semantics:** Literal, truth-conditional meaning of words, phrases, and compositional sentences.
6. **Pragmatics:** Meaning in social context, discourse intent, speech acts, and inferential interpretation.

### 1.3 The Symbolic Function (Form–Meaning Pairs and Projected Reality)
- **The Linguistic Symbol:** A symbol is a conventional pairing of a physical **Form** (acoustic speech signal, written orthographic string, or physical sign) with a **Meaning** (a mental semantic concept).
- **Projected Reality:** Language does not directly point to physical objects in the external universe; it reflects our *mental conceptualization* (projected reality). When hearing the word *"cat"* [kæt], the mind accesses the mental concept **CAT** synthesized from integrated perceptual sensory inputs (shape, fur texture, purring sound) without needing an actual animal physically present.
- **Under-specification in Language:** Linguistic form provides minimal skeletal instructions. Consider:
  $$\text{"The cat jumped over the wall."}$$
  The physical trajectory of the jump is not geometrically specified by the words. It could be:
  - (a) An ascending arc landing onto the top of the wall.
  - (b) A short hop onto the wall and back.
  - (c) A leap dropping down from a height onto the wall.
  - (d) A full parabolic arc clearing the wall and landing on the other side.
  The human hearer infers the default reading (d) by integrating physical world knowledge.

### 1.4 The Interactive Function (Transmission and Inferential Reconstruction)
- **The Transmission Model:** Speaker conceptualizes thought $C_S \to$ encodes into symbolic form $S \to$ transmits across acoustic/visual channel $\to$ Hearer decodes $S \to$ reconstructs thought $C_H$.
- Because language under-specifies reality, $C_H$ is an **inferential reconstruction**, never an identical clone of $C_S$.

### 1.5 Case Studies: Pirahã, Deb Roy's "Birth of a Word", and Vsauce "The Zipf Mystery"

#### 1. The Pirahã Language (Daniel Everett)
- **Context:** An Amazonian hunter-gatherer tribe of ~400 individuals living on the Maici River in Brazil.
- **Linguistic Anomalies:** The language lacks number words, numerals, counting systems, abstract color words, and grammatical past/future tense. Mothers recognize every child by face and name but cannot count how many children they have.
- **The Recursion Controversy:**
  - In 2002, Hauser, Chomsky, and Fitch published their landmark thesis that **syntactic recursion** (embedding clauses inside clauses without limit: *"John knows that Mary thinks that Bill saw..."*) is the defining, uniquely human component of the narrow faculty of language (FLN).
  - Daniel Everett demonstrated that Pirahã grammar exhibits no syntactic recursion, no clausal conjunctions (`and`/`or`), and no center-embedding.
  - MIT linguists Ted Gibson and Steve Piantadosi parsed a corpus of 1,000 recorded Pirahã sentences using automated grammar search techniques and found zero statistical evidence of recursive structure.
  - *Theoretical Implication:* If a natural human language functions successfully without recursion, recursion cannot be an obligatory genetic component of Universal Grammar. Culture can directly shape grammatical architecture ("the grammar of happiness").

#### 2. "Birth of a Word" (Deb Roy, MIT Media Lab)
- **Methodology:** 250,000 hours of continuous audio/video recorded across 3 years in a home environment (90,000 hours of video analyzed, 7 million words transcribed).
- **Phonetic Drift:** Traced the child's acoustic approximation of a form-meaning pair over 6 months from infant babble `gaga` $\to$ `guga` $\to$ `wada` $\to$ `water`.
- **Caregiver Linguistic Scaffolding:** Plotting the mean length of utterance (MLU) of parents revealed that caregiver speech complexity dipped to a sharp local minimum at the exact birth moment of each new word, providing simplified linguistic scaffolding before rising again.
- **Wordscapes:** Spatial movement tracking ("space-time worms") demonstrated that word acquisition is grounded in physical environments (`water` acquired in the kitchen, `bye` at the front door).

#### 3. "The Zipf Mystery" (Vsauce)
- Exploration of power-law dynamics across human communication, city populations, earthquake magnitudes, and website traffic.
- Explores Zipf's principle of least effort, Pareto 80/20 distributions, and Benoit Mandelbrot's random typing demonstration (monkeys typing on a typewriter with a space bar naturally produce a power law of word lengths, yet fail to explain power laws over fixed semantic sets like planet names or weekdays).

### 1.6 Marr's Tri-Level Hypothesis in AI and Perception
David Marr (*Vision*, 1982) posited that any information-processing mechanism must be decoupled into three analytical tiers:
1. **Computational Level (Why / Goal):** What problem does the system solve, why is this goal appropriate, and what is the logic of the mapping from input to output?
2. **Algorithmic and Representational Level (What / Method):** What representations are used for input and output, and what step-by-step transformation algorithm is executed?
3. **Implementational / Physical Level (How / Substrate):** How are the algorithmic representations realized physically in silicon gates, GPU registers, or biological synapses?
- *Key Lesson:* Replicating biological wetware or running neural networks does not excuse an engineer from understanding the computational theory behind the task.

### 1.7 Definitions of AI, the Turing Test, and the Total Turing Test
- Russell and Norvig structure AI across two axes:
  - *Thinking Humanly* (Cognitive Science) vs. *Thinking Rationally* (Laws of Thought / Formal Logic).
  - *Acting Humanly* (Turing Test) vs. *Acting Rationally* (Rational Intelligent Agents).
- **The Turing Test (Alan Turing, 1950):** An operational imitation game where an interrogator converses textually with an unseen human and machine.
- **Critique of the Classic Turing Test:**
  - Non-constructive and non-reproducible; depends on the credulity of human judges.
  - Ignores physical perception and environmental interaction.
- **The Total Turing Test:** Requires Computer Vision (perceiving scenes) and Robotics/Actuation (manipulating objects in the physical world) alongside Natural Language Processing.

### 1.8 Disciplinary Distinctions: NLP vs. CL vs. NLU
- **Natural Language Processing (NLP):** Engineering and application-oriented. Transforms text/speech into structured utility (Translation, Search, Speech Recognition, Sentiment Analysis).
- **Computational Linguistics (CL):** Scientific inquiry. Employs computational models to test hypotheses regarding the human language faculty.
- **Natural Language Understanding (NLU):** The cognitive milestone: extracting intent, resolving discourse context, modeling common ground, and reasoning over world knowledge.

### 1.9 Early NLU Milestones: ELIZA vs. SHRDLU
- **ELIZA (Joseph Weizenbaum, 1966):** Simulated a psychotherapist using surface pattern matching, keyword detection, and script substitution rules.
  - *Takeaway:* Plausible surface responses do **not** imply internal understanding.
- **SHRDLU (Terry Winograd, 1972):** A robotic system operating inside a simulated "Blocks World" containing colored blocks, cones, and boxes.
  - Integrated syntax, procedural semantics, planning, and environmental grounding (e.g., *"Find a block which is taller than the one you are holding and put it into the box"*).
  - *Limitation:* Brittle hand-coded micro-planner logic that could not generalize beyond its toy microworld.

### 1.10 The Pervasive Challenge of Linguistic Ambiguity
Ambiguity permeates every linguistic level:
- *Acoustic Segmentation:* *"recognize speech"* vs. *"wreck a nice beach"*.
- *Lexical Category:* *"book"* (Noun: *"read a book"* vs. Verb: *"book a flight"*); *"British Left Waffles on Falkland Islands"*.
- *Syntactic Attachment:* *"At last, a computer that understands you like your mother"* (3 distinct parses); *"I shot an elephant in my pajamas"*.
- *Word Sense:* *"bank"* (financial institution vs. river embankment).
- *Discourse Coreference:* *"The city councilmen refused the demonstrators a permit because they feared/advocated violence"* (Winograd Schema).

### 1.11 Distributional Semantics (Firth) and Limits of Form-Only Models
- **J.R. Firth (1957):** *"You shall know a word by the company it keeps."* Statistical co-occurrence approximates semantic similarity.
- **The Octopus Test (Bender & Koller, ACL 2020):**
  - An intelligent underwater octopus intercepts a telegraph cable between two humans (A and B). By observing millions of token exchanges, the octopus learns to predict tokens perfectly. However, when human A asks for instructions to build an emergency coconut raft to escape a bear, the octopus cannot ground the words in physical utility.
  - *Core Truth:* Models trained strictly on linguistic **form** cannot infer communicative intent or grounded truth-conditional **meaning**.

---

## 3. Module 2: Information Theory, Language Modeling, and Statistical NLP

### 2.1 Word Frequencies: Normal Distributions vs. Zipf's Law
Natural language vocabulary distributions do not follow a Gaussian normal distribution. They follow a **Power Law**:

$$\mathbf{f_i \propto \frac{1}{r_i} \implies f_i \times r_i \approx k}$$

- $f_i$ is frequency, $r_i$ is rank. On a log-log plot ($\log f$ vs. $\log r$), the distribution produces a linear line with slope $\approx -1$.
- A tiny subset of grammatical words (`the`, `of`, `and`, `to`, `a`) comprises over 50% of any corpus tokens.
- Half of the unique word types in any vocabulary appear only once (**hapax legomena**).

### 2.2 Shannon's N-th Order Approximations of English
In 1948, Claude Shannon generated synthetic text using increasing statistical constraints from a 27-character alphabet (26 letters + space):
1. *Zero-order:* Independent uniform characters: `XFOML RXKHRJFFJU...`
2. *First-order letter:* Characters drawn from unigram frequencies: `OCRO HLI RGWR NMIELIS...`
3. *Second-order letter:* Bigram letter transitions: `ON IE ANTSOUTINYS ARE T INCTORE ST BE S DEAM...`
4. *Third-order letter:* Trigram letter transitions: `IN NO IST LAT WHEY CRATICT FROURE BIRS GROCID PONDENISEN...`
5. *First-order word:* Words drawn independently from word frequencies: `REPRESENTING AND SPEEDILY IS AN GOOD APT OR COME CAN...`
6. *Second-order word:* Bigram word pairs: `THE HEAD AND IN FRONTAL ATTACK ON AN ENGLISH WRITER THAT THE CHARACTER OF THIS POINT IS THEREFORE ANOTHER METHOD...`

### 2.3 Mathematical Information Theory

#### Surprisal
$$S(x) = \log_2 \frac{1}{P(x)} = -\log_2 P(x) \quad \text{(bits)}$$

#### Shannon Entropy
$$H(X) = -\sum_{x \in \mathcal{X}} P(x) \log_2 P(x)$$
- *Fair Coin:* $H(X) = 1.0\text{ bit}$.
- *Fair 8-sided Die:* $H(X) = \log_2 8 = 3.0\text{ bits}$.
- *English Redundancy:* Raw English requires $\lceil \log_2 26 \rceil = 5\text{ bits/char}$. For text length $>8$, actual entropy drops to $\approx 2.3\text{ bits/char}$, revealing **$\approx 50\%$ built-in redundancy**.

#### Joint and Conditional Entropy
$$H(X, Y) = -\sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} P(x, y) \log_2 P(x, y)$$
$$H(Y \mid X) = -\sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} P(x, y) \log_2 P(y \mid x)$$

#### Information-Theoretic Chain Rule
$$H(X, Y) = H(X) + H(Y \mid X) = H(Y) + H(X \mid Y)$$
$$H(X_1, \dots, X_n) = \sum_{i=1}^n H(X_i \mid X_1, \dots, X_{i-1})$$

#### Mutual Information
$$I(X; Y) = H(X) - H(X \mid Y) = \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} P(x, y) \log_2 \frac{P(x, y)}{P(x)P(y)}$$
- Measures reduction in uncertainty of $X$ given $Y$. Non-negative, symmetric, and equals zero if and only if $X$ and $Y$ are independent.

#### Relative Entropy (Kullback–Leibler Divergence)
$$D_{KL}(P \parallel Q) = \sum_{x \in \mathcal{X}} P(x) \log_2 \frac{P(x)}{Q(x)}$$
- Measures the coding inefficiency of using distribution $Q$ to model true distribution $P$. Always $D_{KL} \ge 0$, and $D_{KL}(P \parallel Q) \ne D_{KL}(Q \parallel P)$.

### 2.4 Language Modeling and the Markov Assumption
By the probability chain rule:
$$P(w_1, \dots, w_N) = \prod_{k=1}^N P(w_k \mid w_1, \dots, w_{k-1})$$

The **Markov Assumption** restricts conditioning history to $n-1$ words:
- Unigram: $P(W) = \prod_{k=1}^N P(w_k)$
- Bigram: $P(W) = \prod_{k=1}^N P(w_k \mid w_{k-1})$
- Trigram: $P(W) = \prod_{k=1}^N P(w_k \mid w_{k-2}, w_{k-1})$

Maximum Likelihood Estimation via counts:
$$P_{MLE}(w_k \mid w_{k-1}) = \frac{C(w_{k-1}, w_k)}{C(w_{k-1})}$$

### 2.5 Intrinsic Evaluation and Perplexity
- **Log-Likelihood:** $\log_2 P(W_{test}) = \sum_{k=1}^N \log_2 P(w_k \mid w_{k-n+1}^{k-1})$
- **Perplexity ($PP$):** Inverse probability normalized by test length $N$:
  $$PP(W) = P(w_1, \dots, w_N)^{-\frac{1}{N}} = 2^{-\frac{1}{N} \sum_{k=1}^N \log_2 P(w_k \mid w_{k-1})} = 2^{\hat{H}}$$
  - Represents the weighted average branching factor per token. **Lower perplexity indicates higher predictive accuracy.**

### 2.6 The Zero-Probability Dilemma and Smoothing Techniques
If an n-gram has count 0 in training, $P_{MLE} = 0$, causing test perplexity to become infinite ($PP = \infty$). Smoothing redistributes probability mass to unseen events:

1. **Laplace (Add-1) Smoothing:**
   $$P_{\text{Laplace}}(w_k \mid w_{k-1}) = \frac{C(w_{k-1}, w_k) + 1}{C(w_{k-1}) + V} \quad (V = |\mathcal{V}|)$$
2. **Add-$k$ (Lidstone) Smoothing:**
   $$P_{\text{Add-}k}(w_k \mid w_{k-1}) = \frac{C(w_{k-1}, w_k) + k}{C(w_{k-1}) + kV} \quad (0 < k < 1)$$
3. **Absolute Discounting:**
   $$P_{\text{Abs}}(w_k \mid w_{k-1}) = \frac{\max(C(w_{k-1}, w_k) - d, 0)}{C(w_{k-1})} + \frac{d \cdot |\{w : C(w_{k-1}, w) > 0\}|}{C(w_{k-1})} P(w_k)$$
4. **Jelinek–Mercer Linear Interpolation:**
   $$P_{\text{Interp}}(w_k \mid w_{k-2}, w_{k-1}) = \lambda_3 P_{MLE}(w_k \mid w_{k-2}, w_{k-1}) + \lambda_2 P_{MLE}(w_k \mid w_{k-1}) + \lambda_1 P_{MLE}(w_k)$$
5. **Katz Backoff:** Backs off to $(n-1)$-gram scaled by normalization weight $\alpha$ if count is zero.
6. **Kneser–Ney Smoothing:** Replaces unigram base with the **Continuation Probability**:
   $$P_{\text{continuation}}(w) = \frac{|\{w_{i-1} : C(w_{i-1}, w) > 0\}|}{\sum_{w'} |\{w_{i-1} : C(w_{i-1}, w') > 0\}|}$$

### 2.7 The SRILM Toolkit Practical Pipeline
- **Training Command:**
  ```bash
  ngram-count -text train.txt -order 2 -lm bigram.lm -unk -addsmooth 1
  ```
- **ARPA File Format:**
  Stores `log10_prob \t n-gram \t log10_backoff`.
- **Testing Command:**
  ```bash
  ngram -lm bigram.lm -ppl test.txt -debug 2
  ```
  - `ppl`: Uses $N = \text{words} + \text{sentences}$ (includes `</s>`).
  - `ppl1`: Uses $N = \text{words only}$ (excludes `</s>`).
  - Formula: $ppl = 10^{-\frac{\text{logprob}}{N}}$.

### 2.8 Shannon's Noisy Channel Model in Computational Linguistics
$$\hat{I} = \arg\max_I P(I \mid O) = \arg\max_I \underbrace{P(O \mid I)}_{\text{Channel Model}} \cdot \underbrace{P(I)}_{\text{Language Model}}$$
- Decouples decoding into prior grammaticality $P(I)$ and channel observation likelihood $P(O \mid I)$ (Speech Recognition, Machine Translation, Spell Checking).

---

## 4. Module 3: Sequence Tagging, POS Tagging, and Syntactic Analysis

### 3.1 Part-of-Speech Tagging and Tagsets
- **Penn Treebank (45 tags):** Detailed syntactic distinctions (`NN`, `NNS`, `NNP`, `NNPS`, `VB`, `VBD`, `VBG`, `VBN`, `VBP`, `VBZ`, `JJ`, `RB`, `IN`, `DT`).
- **Universal Dependencies (17 tags):** Coarse cross-linguistic categories (`NOUN`, `VERB`, `ADJ`, `ADV`, `PRON`, `DET`, `ADP`, `PROPN`, `AUX`, `PUNCT`).

### 3.2 Taxonomy of Taggers
- *Rule-based / Lookup:* Morphological regex and lexicon lookup.
- *N-gram / Unigram:* Maximum frequency baseline.
- *Generative Models:* Hidden Markov Models ($P(W, T)$).
- *Discriminative Models:* MEMMs, CRFs, Averaged Perceptron ($P(T \mid W)$ directly).

### 3.3 Hidden Markov Models (HMM) for Sequence Labeling
Modeled as $\lambda = (A, B, \pi)$:
- States $Q = \{q_1, \dots, q_N\}$ (tags).
- Transitions $a_{ij} = P(t_j \mid t_i) = \frac{C(t_i, t_j)}{C(t_i)}$.
- Emissions $b_j(k) = P(w_k \mid t_j) = \frac{C(t_j, w_k)}{C(t_j)}$.
- Priors $\pi_i = P(t_i \mid \text{start})$.

### 3.4 The Three Classical HMM Problems and Algorithms
1. **Evaluation / Likelihood ($P(W \mid \lambda)$):** Forward Algorithm (dynamic programming, $\mathcal{O}(T \cdot |S|^2)$).
2. **Decoding ($T^* = \arg\max_T P(T \mid W)$):** Viterbi Algorithm (dynamic programming trellis with backpointers).
3. **Learning / Parameter Estimation:** Baum–Welch (Expectation–Maximization, EM) Algorithm.

### 3.5 Chunking, Shallow Parsing, and IOB Encoding
- Identifies flat non-recursive syntactic spans (e.g., Noun Phrase chunks).
- **IOB Scheme:** `B-Chunk` (Beginning), `I-Chunk` (Inside), `O` (Outside).
  - Example: `United (B-ORG) airlines (I-ORG) bought (O) planes (B-PROD)`

### 3.6 Syntactic Structure Formalisms: Constituency vs. Dependency
- **Constituency Formalism (Context-Free Grammar / CFG):**
  - Production rules $A \to \alpha$ grouping words into nested phrases ($S \to NP \; VP$, $VP \to V \; NP$).
  - Captures hierarchical constituency tests (Pronoun substitution, Movement, Coordination).
- **Dependency Formalism:**
  - Direct binary directed relations (**arcs**) between lexical words without non-terminal phrase nodes.
  - Links a **Head** (governor) to a **Dependent** (modifier) with labels: `nsubj`, `obj`, `iobj`, `amod`, `det`, `prep`, `pobj`.
  - Highly effective for free word-order languages.

### 3.7 Structural and Attachment Ambiguities
- Prepositional Phrase attachment: *"I shot an elephant in my pajamas"*
  - *VP Attachment:* shooting occurred in pajamas.
  - *NP Attachment:* elephant was wearing pajamas.

---

## 5. Module 4: Modern Methods — Word Embeddings and Distributional Semantics

### 4.1 Limitations of Discrete Symbolic Representations
One-hot vectors ($\mathbf{w} \in \{0, 1\}^{|\mathcal{V}|}$) suffer from extreme sparsity, high dimensionality ($|\mathcal{V}| > 100,000$), and orthogonal geometry:
$$w_{\text{hotel}}^\top w_{\text{motel}} = 0$$
One-hot encodings carry zero intrinsic notion of semantic similarity.

### 4.2 Word2Vec Architecture (CBOW vs. Skip-Gram)
Mikolov et al. (2013) proposed learning low-dimensional dense continuous vectors $\mathbb{R}^d$ ($d \approx 100\text{--}300$):
- **Continuous Bag-of-Words (CBOW):** Predicts center word $w_t$ from surrounding context words.
- **Skip-Gram:** Predicts context words within window $m$ given center word $w_t$.
  - Objective: Maximize log probability of context words:
    $$\mathcal{L}(\theta) = \sum_{t=1}^T \sum_{-m \le j \le m, j \ne 0} \log P(w_{t+j} \mid w_t)$$
    $$P(w_o \mid w_c) = \frac{\exp(v_{w_o}'^\top v_{w_c})}{\sum_{w \in \mathcal{V}} \exp(v_w'^\top v_{w_c})}$$

### 4.3 The Softmax Bottleneck and Skip-Gram with Negative Sampling (SGNS)
Computing the denominator over all $|\mathcal{V}|$ words is computationally prohibitive. **Negative Sampling (SGNS)** reformulates the problem as binary logistic regression: distinguish true context word $(w_c, w_o)$ from $K$ noise words $(w_c, w_{n_i})$ sampled from unigram distribution raised to the $3/4$ power ($P_n(w) \propto U(w)^{3/4}$):
$$\mathcal{L}_{\text{SGNS}} = \log \sigma(v_{w_o}'^\top v_{w_c}) + \sum_{i=1}^K \mathbb{E}_{w_i \sim P_n(w)} \left[ \log \sigma(-v_{w_i}'^\top v_{w_c}) \right]$$

### 4.4 Geometric and Compositional Properties of Word Vectors
Dense embeddings exhibit linear vector compositionality:
$$v_{\text{King}} - v_{\text{Man}} + v_{\text{Woman}} \approx v_{\text{Queen}}$$
$$v_{\text{Paris}} - v_{\text{France}} + v_{\text{Italy}} \approx v_{\text{Rome}}$$
Cosine similarity measures semantic closeness:
$$\text{sim}(u, v) = \frac{u^\top v}{\|u\|_2 \|v\|_2}$$

---

## 6. Module 5: Computer Vision Foundations and Applied Object Detection

### 6.1 Classical Features & Spatio-Temporal Descriptors
- **Histogram of Optical Flow (HOF):** Quantizes spatial motion vectors across consecutive video frames into orientation bins.
- **Motion Boundary Histograms (MBH):** Computes spatial derivatives of horizontal and vertical optical flow components ($\frac{\partial u}{\partial x}, \frac{\partial u}{\partial y}, \frac{\partial v}{\partial x}, \frac{\partial v}{\partial y}$). Cancels camera motion and isolates true foreground action boundaries.

### 6.2 Object Detection Paradigms
- **Two-Stage Detectors (R-CNN, Fast R-CNN, Faster R-CNN):** Stage 1 generates Region Proposals via Selective Search or Region Proposal Networks (RPN); Stage 2 performs RoI pooling, bounding-box regression, and classification. High accuracy, slower frame rate.
- **One-Stage Detectors (YOLO, SSD, RetinaNet):** Predicts class probabilities and box coordinates directly from feature maps in a single feedforward pass. Optimized for real-time throughput.

### 6.3 Semantic Segmentation
- Pixel-level classification:
  - **FCN (Fully Convolutional Networks):** Replaces dense layers with $1 \times 1$ convolutions and transposed convolutions.
  - **U-Net:** Contracting encoder + expansive decoder with high-resolution skip connections.
  - **DeepLab:** Utilizes Atrous (Dilated) Convolutions to expand receptive field without losing spatial resolution, alongside Atrous Spatial Pyramid Pooling (ASPP).

### 6.4 Applied Mini CV Project: Robustness Analysis of YOLO11n
- **Dataset:** COCO128 (128 images, 80 classes).
- **Model:** Pretrained Ultralytics **YOLO11n** (inference/validation mode).
- **Experimental Findings:**

| Experimental Stage | Precision | Recall | mAP@0.5 | mAP@0.5:0.95 |
| :--- | :---: | :---: | :---: | :---: |
| **Stage 1: Clean Baseline** | **0.6633** | **0.5894** | **0.6696** | **0.5024** |
| **Stage 2: Gaussian Blur ($9 \times 9$)** | **0.6784** | **0.5351** | **0.6168** | **0.4434** |
| **Stage 3: Unsharp Masking** | **0.6672** | **0.5294** | **0.6274** | **0.4569** |

- **Key Takeaways:**
  - Blur acts as a spatial low-pass filter, erasing fine edges and causing recall to drop from 0.5894 to 0.5351 (small objects like distant boats and park benches vanished).
  - Unsharp masking ($cv2.addWeighted$) restored ~23% of the lost localization accuracy ($mAP@0.5:0.95$ recovered to 0.4569) and eliminated false positive hallucinated boxes, but could not mathematically restore erased recall.

---

## 7. Module 6: Fully Worked Problem Sets, In-Class Activities, and Solutions

### 7.1 Information Theory Worked Numerical Problems

#### Problem 1: Entropy of an 8-Sided Die
$$H(X) = -\sum_{i=1}^8 \frac{1}{8} \log_2 \frac{1}{8} = 8 \times \left( -\frac{1}{8} \times (-3) \right) = \mathbf{3.0\text{ bits}}$$

#### Problem 2: Entropy of a Fair Coin Toss
$$H(X) = -\left[ 0.5 \log_2 0.5 + 0.5 \log_2 0.5 \right] = \mathbf{1.0\text{ bit}}$$

#### Problem 3: Weather ($X$) and Umbrella ($Y$) Joint & Mutual Information
Given: $P(\text{Sun}) = 0.7$, $P(\text{Rain}) = 0.3$; $P(\text{Umbrella} \mid \text{Rain}) = 0.9$, $P(\text{Umbrella} \mid \text{Sun}) = 0.1$.
1. Joint Probabilities:
   - $P(\text{Sun}, \text{No}) = 0.63$
   - $P(\text{Sun}, \text{Yes}) = 0.07$
   - $P(\text{Rain}, \text{No}) = 0.03$
   - $P(\text{Rain}, \text{Yes}) = 0.27$
2. Marginal Probabilities: $P(\text{No Umbrella}) = 0.66$, $P(\text{Umbrella}) = 0.34$.
3. Conditional Entropy:
   $$H(Y \mid X) = 0.7 \times 0.4690 + 0.3 \times 0.4690 = \mathbf{0.4690\text{ bits}}$$
4. Marginal Entropy:
   $$H(Y) = -(0.66 \log_2 0.66 + 0.34 \log_2 0.34) = \mathbf{0.9248\text{ bits}}$$
5. Mutual Information:
   $$I(X; Y) = H(Y) - H(Y \mid X) = 0.9248 - 0.4690 = \mathbf{0.4558\text{ bits}}$$

### 7.2 Language Modeling Toy Corpus Activity (Complete Worked Steps)
**Training Corpus:**
1. `<s> I am Sam </s>`
2. `<s> Sam I am </s>`
3. `<s> Sam I like </s>`
4. `<s> Sam I do like </s>`
5. `<s> do I like Sam </s>`

**Count Tables:**
- $C(\text{<s>}) = 5, C(\text{I}) = 5, C(\text{Sam}) = 5, C(\text{am}) = 2, C(\text{like}) = 3, C(\text{do}) = 2, C(\text{</s>}) = 5$.
- Bigrams: $C(\text{<s>}, \text{Sam}) = 3, C(\text{Sam}, \text{I}) = 3, C(\text{I}, \text{am}) = 2, C(\text{am}, \text{</s>}) = 1$.

**Evaluation of $S =$ `<s> Sam I am </s>`:**
$$P(S) = P(\text{Sam} \mid \text{<s>}) \times P(\text{I} \mid \text{Sam}) \times P(\text{am} \mid \text{I}) \times P(\text{</s>} \mid \text{am})$$
$$P(S) = \frac{3}{5} \times \frac{3}{5} \times \frac{2}{5} \times \frac{1}{2} = 0.6 \times 0.6 \times 0.4 \times 0.5 = \mathbf{0.072}$$
$$\log_{10} P(S) = -1.14267$$

**Perplexity ($N = 4$ tokens, including `</s>`):**
$$PP(S) = 10^{-\frac{-1.14267}{4}} = 10^{0.28567} \approx \mathbf{1.9305}$$

**Handling Unseen Words:**
For $S_2 =$ `<s> Sam I do like linguistics </s>`, `linguistics` was unseen ($C=0 \implies P_{MLE}=0 \implies PP=\infty$). Laplace or Lidstone smoothing redistributes mass across vocabulary size $V=6$, preventing zero probability.

### 7.3 Core Cognitive Discussion Questions and Model Answers
1. *Q1: If a machine produces a completely appropriate response to a sentence, does that mean it understands the sentence?*
   - **Answer:** No. Weizenbaum's ELIZA demonstrated that superficial syntactic keyword reflection mimics understanding without constructing an internal model of semantic intent or situation truth.
2. *Q2: What is the difference between processing language and understanding language?*
   - **Answer:** *Processing* is mechanical transformation (tokenizing, parsing, computing conditional probabilities). *Understanding* requires mapping form to communicative intent, grounding symbols in perceptual experience, and resolving pragmatic implications.
3. *Q3: If a model learns statistical patterns from enormous amounts of text, what exactly has it learned?*
   - **Answer:** It has learned the statistical distributional topology of surface linguistic form. As demonstrated by Bender & Koller (2020), form alone lacks external referential truth and communicative intentionality.

---

## 8. Master Bibliography and Literature
1. D. Jurafsky and J. H. Martin, *Speech and Language Processing*, 3rd ed. draft, 2024.
2. C. D. Manning and H. Schütze, *Foundations of Statistical Natural Language Processing*, MIT Press, 1999.
3. D. Marr, *Vision: A Computational Investigation into the Human Representation and Processing of Visual Information*, W. H. Freeman, 1982.
4. C. E. Shannon, "A Mathematical Theory of Communication," *Bell System Technical Journal*, vol. 27, 1948.
5. C. E. Shannon, "Prediction and Entropy of Printed English," *Bell System Technical Journal*, vol. 30, 1951.
6. G. K. Zipf, *Human Behavior and the Principle of Least Effort*, Addison-Wesley, 1949.
7. A. M. Turing, "Computing Machinery and Intelligence," *Mind*, vol. 59, no. 236, pp. 433–460, 1950.
8. T. Winograd, *Understanding Natural Language*, Academic Press, 1972.
9. J. Weizenbaum, "ELIZA—a computer program for the study of natural language communication between man and machine," *CACM*, 1966.
10. E. M. Bender and A. Koller, "Climbing towards NLU: On Meaning, Form, and Understanding in the Age of Data," in *Proc. ACL*, 2020.
11. A. Ettinger, "What BERT Is Not: Lessons from a New Suite of Psycholinguistic Diagnostics for Language Models," *TACL*, vol. 8, 2020.
12. T. Mikolov, K. Chen, G. Corrado, and J. Dean, "Efficient Estimation of Word Representations in Vector Space," *arXiv:1301.3781*, 2013.
13. J. Redmon, S. Divvala, R. Girshick, and A. Farhadi, "You Only Look Once: Unified, Real-Time Object Detection," in *CVPR*, 2016.
