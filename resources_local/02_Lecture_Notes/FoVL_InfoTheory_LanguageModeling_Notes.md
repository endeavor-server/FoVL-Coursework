Foundations of Vision and Language

Information Theory and Language Modeling — Complete Study Notes

Based on the lecture deck by Sidharth Ranjan (FoVL-InfoTheory-LanguageModeling)

## Lecture outline

Zipf’s law

Shannon’s approach to language

Entropy

Information-theoretic measures (joint & conditional entropy, chain rule, mutual information, KL divergence)

Language modeling

N-gram / Markov models (evaluation, smoothing, backoff, interpolation)

SRILM toolkit (practical)

Noisy-channel model (appendix)

# 1. Representing the Structure of Language

There are two broad ways to describe language:

Rule-based: Describe grammatical rules — e.g., English sentences have subjects, verbs, objects, and so on.

Statistical: Study the statistical structure of language:

How frequently do words occur?

How predictable is one word from another?

How much information does a word carry?

Do most words in a corpus occur with an average frequency?

## 1.1 Normal distribution vs. word frequencies

Many phenomena follow a normal (bell-shaped) distribution: very few observations with extremely low values, many with average values, very few with extremely high values. Examples: the sum of rolling three dice, life expectancy in Finland, heights of children in the same school year.

Key point: Word frequencies are different! They do NOT cluster around an average — a handful of words are extremely frequent and the vast majority are rare. This is captured by Zipf’s law.

# 2. Zipf’s Law

Zipf’s law denotes a surprising regularity in the way word frequencies are structured. Named after George Kingsley Zipf (1902–1950).

### History

## 2.1 Statement of the law

If we count each word and order the words by frequency, each word i gets a frequency fᵢ and a rank rᵢ. Zipf’s law says:

fᵢ ∝ 1 / rᵢ      equivalently      f × r ≈ k (constant)

The most frequent word occurs about twice as often as the 2nd most frequent, three times as often as the 3rd, and so on.

On a log–log plot of frequency vs. rank, Zipfian data fall on a straight line with slope ≈ −1. (Slide figure: Brown corpus, with the predicted line for k = 100,000, i.e., f × r = 100,000.)

A linear-scale plot (frequency vs. rank, top 100 words) shows a sharp ‘L’ shape: the, of, and, to, a, in, that, is … dominate, followed by a long tail.

## 2.2 Observations

Some words are used very frequently — mostly grammatical (function) words: the, of, and, to, a, in, …

Many words are used very rarely (the ‘long tail’).

So language has a very uneven frequency distribution.

Frequent words are short; rare words tend to be longer.

Zipf’s law holds across languages (slide shows Zipf curves for many languages), which raises the question: why should language have this particular statistical structure?

## 2.3 Why are word frequencies Zipfian?

Principle of least effort: If we have to use a word very often, it saves time and energy if that word is very short.

Communication efficiency and robustness:

Shorter words carry a higher risk of being misheard, so they do not carry a lot of information, but they convey it efficiently.

Longer words carry more information and are more reliably identified, but at a higher processing cost.

Language appears to balance efficiency and robustness (a trade-off).

Efficiency — minimises the physical and cognitive effort required by the speaker to produce language.

Robustness — ensures the listener can reconstruct the intended meaning in the presence of noise and distractions.

Benefits of knowing Zipf’s law:

Helps us understand the statistical properties and structure of language.

Guides the design of better NLP systems (e.g., vocabulary size, handling rare/unseen words).

(The deck also links the video ‘The Zipf Mystery’ for further viewing.)

# 3. Shannon’s Approach to Language

## 3.1 Motivation (Insights)

If language has such strong statistical regularities, can we actually quantify them?

Can we measure: predictability, uncertainty, information, redundancy?

Claude Shannon & World War II — communication and code-breaking: how can information be represented computationally?

## 3.2 Historical background: Shannon and Turing

World War II (1939–1945); Bell Labs (1943) — where Claude E. Shannon and Alan Turing met.

Code makers & code breakers: Shared interests: chess, crossword puzzles, typewriters. Turing showed Shannon his paper ‘On Computable Numbers, with an Application to the Entscheidungsproblem’ (1936).

Conversation: They discussed the powers and limits of an idealised computing machine and the possibility of machines ‘learning to think’. Shannon: why not feed ‘cultural things’ like music to an electronic brain? Turing: he was after ‘just a mundane brain’. (Note: in 1943 neither the transistor nor the electronic computer existed yet.) Their common vision: LOGIC.

Summary: Turing encoded instructions as numbers (decimal numbers as zeros and ones); Shannon made codes for switches and relays. Both played a ‘game of symbols and mapping’ — mapping one set of objects onto another (e.g., logical operators ↔ electric circuits; algebraic functions ↔ machine instructions).

ENIGMA: By the war’s end, ENIGMA deciphering processed thousands of intercepts a day — information processing on an unprecedented scale. Key idea: the probability of some fact (e.g., an Enigma setting or a submarine location); evidence that rules out possibilities decreases uncertainty. Turing cared about the data that changed the probability (a ‘weight of evidence’). Shannon’s similar thoughts led to A Mathematical Theory of Cryptography (1945).

## 3.3 Shannon’s thoughts — Redundancy

A Mathematical Theory of Cryptography (1945; declassified 1949): a stream of encrypted data looks like junk; the goal is to find the real pattern. This motivated him to study the patterns of language (tangible and countable).

Patterns in language = Redundancy (an aid to understanding/recovering). Language is not random — it contains redundancy.

Example: wherever the letter q appears, the following u is redundant. After q, a u is expected — no surprise, so it contributes no information.

Question raised: how much can a text be reduced in length without losing any information?

Each event has a probability that depends on the state of the system and perhaps also on its previous history.

## 3.4 Shannon’s approach

He examined statistical structure in terms of how much of a message influences the probability of the next symbol.

Language is a dynamic system whose future course is conditioned by its past history.

He worked this out empirically using English text.

## 3.5 Framework: Shannon’s nᵗʰ-order approximation

Symbols: an alphabet of 27 characters (26 letters + space). Strings were generated using a table of random numbers, with progressively more statistical knowledge of English:

Inference: Sequences increasingly ‘look’ like English as the order increases.

# 4. Entropy

## 4.1 Shannon’s entropy (1948)

Precursor: Nyquist and Hartley’s formula (1928): H = n log s.

Measures information, choice and uncertainty as a function of probabilities.

It is the average logarithm of the improbability (unexpectedness) of the message.

H = − Σᵢ pᵢ log₂ pᵢ    (pᵢ = probability of each message; measured in bits)

H(X) = Σₓ p(x) log 1/p(x) = E[ log 1/p(X) ]

Surprisal (self-information) of an outcome:

S = − log p(X) = log ( 1 / p(X) )

Entropy = average uncertainty of a symbol / random variable = expected surprise.

Rare events (low p) have high surprisal; certain events (p = 1) have zero surprisal.

Entropy does NOT truly represent the randomness in the sequence — it only measures the relative differences in the frequencies of each symbol.

Interpretation: the average length of the message (in bits) needed to transmit an outcome efficiently.

## 4.2 Worked examples

## 4.3 Activity: quantifying predictability and redundancy

Guessing a sentence letter by letter / word by word (“A SMALL OBLONG READING LAMP ON THE D… → Desk”): as context accumulates, the next item becomes easier to predict.

Context reduces uncertainty — the basic intuition behind language modeling!

Efficient communication system: make the chance of error as small as you wish.

Message encoding: remove redundancy to increase efficiency, or add redundancy to enable error correction (robustness).

Shannon hypothesised this working over electrical communication devices (flip-flops) → The Mathematical Theory of Communication (1949) — the Noisy Channel Model.

## 4.4 English has ~50% built-in redundancy

Source: Shannon, “Prediction and Entropy of Printed English” (1950/51).

Hypothesis: Hypothesis: to represent 26 options in binary you need 5 bits (2⁴ = 16 is not enough; 2⁵ = 32 is). If English were completely random, every letter would carry a full 5 bits.

Observation: For English text longer than ~8 letters, the actual information drops to about 2.3 bits per character. Letters follow strict statistical patterns: seeing t-h-e-r-e-f-o-r- you fill in ‘e’; you can read ‘Ths sntnc s stll rdbl’; you spot typos instantly because they violate expected patterns.

Conclusion: 2.3 bits ≈ half of the raw 5-bit capacity, so English is about 50% redundant.

# 5. Information-Theoretic Measures

## 5.1 Joint entropy

The amount of information needed on average to specify the values of both X and Y:

H(X,Y) = − Σₓ Σᵧ p(x,y) log p(x,y)

## 5.2 Conditional entropy

H(Y|X) is how much extra information one still needs to supply on average to communicate Y given that one already knows X:

H(Y|X) = Σₓ p(x) H(Y|X=x)

= Σₓ p(x) [ − Σᵧ p(y|x) log p(y|x) ]

= − Σₓ Σᵧ p(x,y) log p(y|x)    (using p(x,y) = p(x) p(y|x))

Key insight: Language modeling is fundamentally about conditional probability and therefore conditional uncertainty.

## 5.3 Chain rule

H(X,Y) = −E[log p(x,y)] = −E[log p(x) + log p(y|x)] = H(X) + H(Y|X)

H(X₁,…,Xₙ) = H(X₁) + H(X₂|X₁) + … + H(Xₙ|X₁,…,Xₙ₋₁)

The information required to specify X and Y is the information required to specify X, plus the additional information required to specify Y once X is known.

## 5.4 Mutual information

I(X;Y) is the reduction in uncertainty of one random variable due to knowing the other — the amount of information one RV contains about the other.

H(X,Y) = H(X) + H(Y|X) = H(Y) + H(X|Y)

I(X;Y) = H(X) − H(X|Y) = H(Y) − H(Y|X)

I(X;Y) = H(X) + H(Y) − H(X,Y) = Σₓ,ᵧ p(x,y) log [ p(x,y) / (p(x) p(y)) ]

Strongly related X and Y → knowing X tells a lot about Y → high MI.

Knowing X tells almost nothing about Y → low MI (independent variables: I = 0).

Venn-diagram view: H(X) and H(Y) are two overlapping circles; the overlap is I(X;Y), the non-overlapping parts are H(X|Y) and H(Y|X), and the union is H(X,Y). Mutual information is literally the part of uncertainty the two variables share.

## 5.5 Relative entropy (Kullback–Leibler divergence)

For two probability mass functions p(x), q(x) over the same event space:

D(p‖q) = Σₓ p(x) log [ p(x) / q(x) ] = Eₚ[ log p(X)/q(X) ]

Measures how different two probability distributions are.

Interpretation: the average number of bits wasted by encoding events from distribution p with a code based on a not-quite-right distribution q.

D(p‖q) ≥ 0, equals 0 only when p = q, and is not symmetric (D(p‖q) ≠ D(q‖p) in general).

## 5.6 Summary of measures

## 5.7 In-class exercise (with model answers)

# 6. Entropy and Natural Language

A language model m is a probability distribution over sentences. Let w = next word, h = history of words seen so far.

Conditional entropy: H(Y|X) = Σ p(x) H(Y|X=x) = −E[log p(Y|X)]

Pointwise conditional entropy (surprisal): H(w|h) = − log₂ m(w|h) — the measure of surprise on seeing the next word.

Total conditional entropy (total surprisal):

H_total = − Σⱼ₌₁ⁿ log₂ m(wⱼ | w₁,…,wⱼ₋₁) = − log₂ m(w₁,…,wₙ)    (by the chain rule)

## 6.1 Perplexity

Ĥ = H_total / N    (average surprise (number of choices) per word)

PP(w) = 2^Ĥ = m(w₁,…,wₙ)^(−1/N) = ᴺ√( 1 / m(w₁,…,wₙ) )

Intuitively, the (weighted) number of possible next words that can follow any word.

Lower perplexity = better language model, i.e., the model makes relatively confident (correct) predictions.

Reflects the LM’s preference for predictability over randomness.

## 6.2 Open questions

How are we able to predict each other? Because of the structure of language, the freedom of language decreases as we look at longer strings of words — entropy decreases as the order of Shannon’s approximation increases.

How are structures imposed on our speech patterns? Through statistical properties of language: we narrow our repertoire to fit what we are exposed to (Zipf’s law). This is common in human and non-human communication systems.

# 7. Language Modeling

## 7.1 Predicting sequences

“He put the coffee …” — to predict upcoming words we can assign a probability to each possible next word.

“I will be back soonish” is likelier than “I will be bassoon dish” (important in speech recognition, ASR).

Models that assign probabilities to sequences of words are called language models (LMs). (Reference: Jurafsky & Martin, SLP3, Ch. 3.)

## 7.2 N-gram models and the Markov assumption

The simplest LM is the n-gram model: a sequence of N words (2-gram, 3-gram, 4-gram …) is used to estimate the probability of the last word in the n-gram.

Markov assumption: the probability of a word depends only on a fairly recent, finite number of previous words.

N-grams directly model the probability of a sequence of observations. An n-gram model is also called a Markov model or Markov chain.

Example sentence  S: “He put the coffee on the table”

### Maximum-likelihood estimation (counting)

Bigram probability = count of the bigram C(wₙ₋₁wₙ), normalised by the sum of all bigrams sharing the same first word — which equals the unigram count of wₙ₋₁:

P(wₙ | wₙ₋₁) = C(wₙ₋₁wₙ) / Σ_w C(wₙ₋₁w) = C(wₙ₋₁wₙ) / C(wₙ₋₁)

Trigram:  P(coffee | put the) = C(put the coffee) / C(put the)

In practice: count occurrences in a corpus (e.g., grep “put the coffee”).

## 7.3 Markov chain as a weighted finite-state machine

States = words; arcs = transition probabilities. This is a type of weighted finite-state machine.

A start distribution π = [0.7, 0.1, 0.2] gives the probability of starting with He, cool or is.

Example from slide: P(is he cool) = π(is) × P(He|is) × P(cool|He) = 0.2 × 0.5 × 0.3 = 0.03.

Transition probabilities in the slide figure (each row sums to 1):

# 8. Training and Evaluating N-gram Models

## 8.1 Methodology

Use a training set to build the language model and a separate test set to evaluate it. Don’t train on the test corpus!

Model accuracy is reported via likelihood, log-likelihood and perplexity.

## 8.2 Extrinsic vs. intrinsic evaluation

Extrinsic: Performance on an application-oriented task (e.g., ASR, MT).

Intrinsic: Quality measured independently of any application — perplexity.

## 8.3 Model accuracy metrics

Likelihood: Probability of the observed test data given model M:

P(W_test | M) = Π_{w ∈ W_test} P(w | M)

Log-likelihood: Likelihood multiplies very small numbers → underflow; taking logs fixes this:

log P(W_test | M) = Σ_{w ∈ W_test} log P(w | M)

Perplexity: PP(w) = 2^Ĥ = m(w₁,…,wₙ)^(−1/N). Here N = total number of word tokens in the test set + total number of sentences (</s> tokens).

The higher the estimated probability of the word sequence, the lower the perplexity.

Must be computed with a model that has no knowledge of the test set.

Perplexities of two LMs are only comparable if they use identical vocabularies.

Slide example (Jurafsky & Martin, Wall Street Journal: trained on 38M words, tested on 1.5M words) — longer context gives lower perplexity:

## 8.4 Model performance & the problem of zeros

N-gram models perform well when the test corpus resembles the training corpus — in real life that is often not the case.

Goal: build a robust model that generalises well.

Problem of zeros: many valid n-grams never appear in training, so MLE gives them probability 0 (and any sentence containing them gets probability 0 → infinite perplexity). Slide example: bigram counts from 9,222 sentences of the Berkeley Restaurant Project are mostly zeros (e.g., ‘want want’, ‘eat i’).

Solution idea: ‘steal’ probability mass from seen events and give it to unseen ones, to generalise better.

## 8.5 Out-of-vocabulary (OOV) & rare words — smoothing

Smoothing methods improve performance:

Add-1 (Laplace) smoothing

Add-k smoothing

Absolute discounting

Good–Turing discounting

Witten–Bell discounting

Kneser–Ney smoothing

P_MLE(wᵢ|wᵢ₋₁) = c(wᵢ₋₁,wᵢ) / c(wᵢ₋₁)

P_Add-1(wᵢ|wᵢ₋₁) = [ c(wᵢ₋₁,wᵢ) + 1 ] / [ c(wᵢ₋₁) + V ]    (V = vocabulary size)

P_Add-k(wₙ|wₙ₋₁) = [ C(wₙ₋₁wₙ) + k ] / [ C(wₙ₋₁) + kV ]

P_AbsDisc(wᵢ|wᵢ₋₁) = [ C(wᵢ₋₁wᵢ) − d ] / Σᵥ C(wᵢ₋₁v)  +  λ(wᵢ₋₁) P(wᵢ)    (subtract a fixed discount d from every seen count, give the freed mass to the unigram distribution)

Further techniques: interpolation and backoff. OOV words are usually mapped to a special <UNK> token.

## 8.6 N-gram hierarchy, backoff and interpolation

Hierarchy: If there are no examples of the trigram (wₙ₋₂wₙ₋₁wₙ), estimate P(wₙ|wₙ₋₂wₙ₋₁) using the bigram P(wₙ|wₙ₋₁); if no bigram, use the unigram P(wₙ).

Backoff (Katz 1987): Non-linear method: estimates are allowed to back off through progressively shorter histories:

P̂(wᵢ|wᵢ₋₂wᵢ₋₁) = P(wᵢ|wᵢ₋₂wᵢ₋₁) if C(wᵢ₋₂wᵢ₋₁wᵢ) > 0;   α₁P(wᵢ|wᵢ₋₁) if C(trigram) = 0 and C(wᵢ₋₁wᵢ) > 0;   α₂P(wᵢ) otherwise

Problem with backoff: If bigram w₁w₂ is frequent but trigram w₁w₂w₃ is rare, the rarity may be meaningful (a ‘grammatical null’) rather than data sparsity or chance — so one may not want to back off.

Simple linear interpolation: Construct a linear combination (weighted average) of unigram, bigram and trigram estimates; uses different contextual histories as appropriate:

P(wₙ|wₙ₋₂wₙ₋₁) = λ₃P(wₙ|wₙ₋₂wₙ₋₁) + λ₂P(wₙ|wₙ₋₁) + λ₁P(wₙ),   λ₁ + λ₂ + λ₃ = 1

Best approach in practice: simple linear interpolation of n-grams + smoothed probabilities for OOV words (best smoothing technique).

## 8.7 Setting smoothing parameters (hyperparameter tuning)

How to pick the best λ? Not by trying values on the test set.

Split data into Training / Dev (held-out, ~10–20%) / Test. Pick the λ that gives the best result on the dev set, use that λ to get smoothed counts from training, then report results of that final model on the test data.

# 9. In-Class Language-Modeling Activity (with worked solutions)

Training data (adapted from Jurafsky & Martin 2015). The deck asks Q1 and Q2 over three sentences — (a) <s> Sam I do I like </s>, (b) <s> Sam I am </s>, (c) <s> Sam I do like linguistics </s> — and repeats (c) as a per-word problem on the next slide:

<s> I am Sam </s>

<s> Sam I am </s>

<s> Sam I like </s>

<s> Sam I do like </s>

<s> do I like Sam </s>

### Counts from the training data

### Practical tasks

Create bigram and unigram LMs on a toy dataset and evaluate them on an unseen test set.

Check how the model performs on OOV words.

Show how smoothing fixes the OOV / zero-probability problem.

Repeat the exercise on a larger dataset — the Brown corpus (brown-train, brown-dev, brown-test).

# 10. SRILM — The SRI Language Modeling Toolkit

Used for building and applying statistical LMs, primarily for speech recognition, statistical tagging, segmentation and machine translation.

Components: a set of C++ class libraries (LMs, data structures, utilities) and executable programs built on them (training LMs, testing, tagging/segmenting text, etc.).

Runs on UNIX and Windows.

## 10.1 Pipeline

## 10.2 Training command (ngram-count)

Example:  ngram-count -text train.txt -order 2 -lm bigram.lm -unk -addsmooth 1

## 10.3 Testing command (ngram)

Example:  ngram -lm bigram.lm -ppl test.txt -debug 2

## 10.4 File formats

Count file: each line is an n-gram followed by its count. For the toy training data (order 2): <s> 5, <s> I 1, <s> Sam 3, <s> do 1, I 5, I am 2, I like 2, I do 1, am 2, am Sam 1, am </s> 1, Sam 5, Sam </s> 2, Sam I 3, </s> 5, like 3, like </s> 2, like Sam 1, do 2, do like 1, do I 1.

LM file (ARPA format): each line = log₁₀ probability, the n-gram, and log₁₀ back-off weight.

Test output: ngram -ppl prints one summary block per file: sentences, words, OOVs, zeroprobs, total logprob (log base 10), ppl and ppl1.

Worked example (slide output for test-q1.txt):

file sample-data/test-q1.txt: 2 sentences, 8 words, 0 OOVs  /  0 zeroprobs, logprob= −3.1604  ppl= 2.07033  ppl1= 2.48342

ppl uses N = #words + #</s> = 8 + 2 = 10:   ppl = 10^(−logprob / N) = 10^(3.1604 / 10) = 10^0.31604 = 2.0703

ppl1 uses N = #words only = 8 (sentence ends excluded):   ppl1 = 10^(3.1604 / 8) = 10^0.39505 = 2.4834

Because SRILM reports log₁₀ probabilities, perplexity is 10^(−logprob/N); this equals 2^Ĥ with Ĥ in bits. OOV words are excluded from N and reported separately, and zeroprobs counts in-vocabulary words that still got probability 0.

Documentation: http://www.speech.sri.com/projects/srilm/manpages/

# 11. Appendix — Shannon’s Noisy Channel Model

Aim: optimise throughput and accuracy when communicating in the presence of noise.

Duality between compression (remove all redundancy) and transmission accuracy (add controlled redundancy so the input can be recovered despite noise).

Goal: encode the message to occupy minimal space while keeping enough redundancy to detect and correct errors.

W (message) → encoder → X → channel p(y|x) → Y → decoder → Ŵ (reconstructed message)

Channel capacity: the rate at which information can be transmitted with arbitrarily low probability of failing to recover the input. Capacity is reached by choosing an input distribution p(X) that maximises I(X;Y):

C = max_{p(X)} I(X;Y)

## Linguistics and the noisy channel

In linguistics we can’t control the encoding; we want to decode the observed output O to the most likely input I:

Î = argmax_I p(I | O) = argmax_I p(I) · p(O | I)    (Bayes’ rule; p(O) is constant)

p(I) = the language model;  p(O|I) = the channel probability.

Applications: machine translation, optical character recognition (OCR), speech recognition.

# 12. Key Points to Remember

Word frequencies are Zipfian (f ∝ 1/r), not normal; frequent words are short — a balance of speaker effort (efficiency) and listener recovery (robustness).

Shannon modelled language as a stochastic process; higher-order approximations look increasingly like English, showing that context reduces uncertainty.

Entropy H = −Σ p log₂ p = expected surprisal = minimal average bits per symbol. Fair coin = 1 bit; 8-sided die = 3 bits.

English carries ~2.3 bits/letter vs. 5 bits raw → ~50% redundancy.

H(X,Y) = H(X) + H(Y|X);  I(X;Y) = H(X) − H(X|Y) is symmetric;  D(p‖q) measures bits wasted coding p with q.

Language models assign probabilities to word sequences; n-gram models use the Markov assumption and MLE counts.

Evaluate intrinsically with perplexity PP = 2^(H/N); lower is better (WSJ: unigram 962 → bigram 170 → trigram 109); never train or tune on the test set.

Zeros/OOV words break MLE models → smoothing (Laplace, add-k, Good–Turing, Kneser–Ney…), backoff, interpolation; tune λ on a dev set.

SRILM: ngram-count to train (‑order, ‑lm, ‑unk, ‑addsmooth), ngram to test (‑ppl, ‑debug 2).

Noisy channel: Î = argmax p(I)·p(O|I) — the LM supplies p(I).
