Foundations of Vision and Language

Introduction: Language — Complete Study Notes

Based on the lecture deck by Sidharth Ranjan (FoVL-Introduction-Language, 50 slides) + summaries of the four class videos

## Lecture outline

Course administration, pedagogy and textbooks

What is language? What does language do?

Language as symbolic communication (form–meaning pairs, concepts, projected reality)

Language as interactive communication (the transmission model)

Language understanding and AI: Marr’s tri-level hypothesis, definitions of AI, the Turing test

NLP vs. CL vs. NLU

Early NLU systems: ELIZA (1966) and SHRDLU (1972)

Building blocks of NLU and a typical NLP/CL setup

Main challenges: ambiguity

Data-driven (empirical) approaches — Firth, Shannon — and their limits

Closing discussion questions, readings

# 1. Course Administration and Pedagogy

## 1.1 Logistics

Class timings: 6:00–7:30 PM Friday and 2:30–4:00 PM Saturday.

Hybrid classroom: online via Google Meet, offline in CS101 (CSE Building). Materials on Google Classroom.

Lecture slides are strictly for class reference — they cannot be shared, copied or circulated (disciplinary action otherwise).

## 1.2 Structure of the Language part of the course

Two halves of 8 lectures each: Traditional Methods (8 lectures) and Modern Methods (8 lectures).

Goal: introduce students to the range of methods in NLP / Computational Linguistics (CL).

The first half focuses on morphological, lexical and syntactic analysis of natural-language data.

Some linguistics background is assumed — ask whenever a term is unfamiliar.

## 1.3 Pedagogy

Special focus on applications and practical knowledge; theory and practice sessions alternate.

Writing pad + slides + lab demos; in-class exercises — bring laptops.

## 1.4 Textbooks

# 2. What is Language?

## 2.1 Language as a window to the mind

Language reflects patterns of thought — conceptualisation.

Language offers a window to the mind (cognitive functions); it provides insight into the nature, structure and organisation of ideas and thoughts.

We study language to describe its systematicity, its structure and its functions, and how those functions are realised by the language system.

Slide figure: the ‘layers of linguistics’ wheel — from the centre outward: Phonetics (speech sounds) → Phonology (phonemes) → Morphology (words) → Syntax (phrases and sentences) → Semantics (literal meaning of phrases and sentences) → Pragmatics (meaning in the context of discourse).

## 2.2 Two kinds of question

## 2.3 What is language for?

We take language for granted, yet we rely on it all day for a range of functions: shopping, talking to friends, talking on the phone, expressing opinions, arguing or insulting someone, and so on.

Thought experiment — which behaviours could be accomplished without language? Telepathy? Browsing the internet? Sending email? (Almost none: even these are language-mediated.)

Language allows quick and effective expression and provides a well-developed means for encoding and transmitting complex and subtle ideas.

It does this through two functions: the symbolic function and the interactive function.

# 3. The Symbolic Function

## 3.1 Symbols = form + meaning

Language expresses itself using symbols (‘bits of language’). A symbol may be:

a meaningful sub-part of a word (dis- as in distaste),

a whole word (cat, run, tomorrow),

a string of words (He couldn’t write the entire musical piece).

Form: A symbol consists of a form paired with a conventional meaning (a form–meaning pair). The form may be spoken, written or signed.

Meaning: The conventional ideational or semantic content associated with the symbol.

Key claim: Language does not directly represent the external world; it represents our conceptualised experience (thoughts) of the world.

## 3.2 Projected reality

The word cat is not the actual animal. It is a symbolic representation that lets us mentally access the concept even when no cat is physically present. (Slide figure 1.1: the form [kæt] paired with a picture of a cat — ‘a symbolic assembly of form and meaning’.)

## 3.3 Form–meaning pair, concepts and percepts (levels of representation)

The picture represents the meaning conventionally paired with the form pronounced in English as [kæt].

The meaning associated with a linguistic symbol is linked to a particular mental representation termed a concept.

Concepts in turn derive from percepts. Example — a pear: different parts of the brain perceive its shape, colour, texture, taste, smell, etc.; this diverse perceptual information from the world ‘out there’ is integrated into a single mental image (a representation available to consciousness), which gives rise to the concept PEAR.

## 3.4 Examples: four kinds of ‘reality’ language can point at

## 3.5 Example: how much does language actually specify?

The cat jumped over the wall.

A range of interpretations: the behaviour described by jump has the potential to involve a variety of trajectory shapes — slide figure 1.3 shows four possible trajectories: (a) an arc up onto the wall, (b) a short hop up and back on top, (c) a drop down onto the wall from above, (d) a full arc up, over and down the other side.

The sentence itself does not pick one; the listener infers the most plausible one (normally (d)) from world knowledge.

# 4. The Interactive Function

We use language to get our ideas across, i.e., to communicate.

Slide figure 1.4 (the interactive function): a Speaker utters [kæt]; a Hearer forms a thought-bubble containing a cat.

The hearer’s thought is a reconstruction — it is built from symbols plus inference, so it need not be identical to the speaker’s rich conceptualisation.

## 4.1 Illustrations shown in class (videos)

Pirahã language — Daniel Everett went to the Amazon as a missionary and became a linguist; the Pirahã language has no number words, no fixed past/future tense, and a structure that challenges conventional grammar and fundamental ideas about human cognition and language (documentary The Amazon Code).

Birth of a Word — Deb Roy (MIT) recorded 90,000 hours of home video to watch his infant son’s ‘gaaaa’ slowly turn into ‘water’ — data-rich evidence of how a form–meaning pair is acquired (TED talk).

## 4.2 Video summaries (transcripts in Downloads)

### Pirahã language — short film (SLICE, ‘Life-Changing Encounter’, ~10 min)

Daniel Everett arrived on the Maici River (Amazonas, Brazil) in 1977, aged 25, as a missionary; the previous missionary left after an hour, leaving him with two phrases he could not even repeat.

Field method with no shared language: pick up objects, point, elicit names, day after day — the same ostensive form–meaning pairing the lecture describes (§3). His teacher was a Pirahã man; the segment ‘awe/awi’ means ear, skin, foreigner, hand or Brazil-nut shell depending only on tone.

What the language lacks: no colour words, no past or future tense, and no number words — MIT research suggests the Pirahã may be the only culture without numeracy. Mothers do not know how many children they have, but know every child’s name and face.

What the culture has instead: an encyclopaedic knowledge of thousands of local species, and a life lived in the present — activities follow the needs of the moment, not worries about the future.

The contentment he saw undermined his missionary premise (people must first feel ‘lost’ to want saving); he describes converting others as ‘colonialism of the mind’.

### Mystery of Pirahã — full documentary (SLICE, ‘Inside the Pirahã World’, ~50 min)

Expands the short film into the scientific controversy. The ~400 Pirahã live in four villages on the Maici; the language can be spoken, hummed, sung or whistled. Everett is one of three outsiders who speak it.

Personal arc: 25 years of missionary work produced no converts; Everett became an atheist, his marriage ended and his children did not speak to him for two years.

The linguistic claim: Pirahã grammar shows no evidence of recursion — embedding a clause inside a clause without limit (‘John said that Bill said that Mary said …’). If a language has a longest possible sentence, it lacks recursion.

Why it matters: in 2002 Noam Chomsky (with Hauser and Fitch) proposed that recursion is the core of the narrow language faculty — the innate, genetic universal grammar. One language without recursion would mean recursion cannot be the universal basis of language. Chomsky’s camp dismissed the work (‘can’t have anything to do with the nature of language’); Everett received hate mail and was accused of racist research; a Brazilian linguistics department boycotted his talk.

Everett’s deeper claim: culture can shape not just vocabulary but the whole grammar — the Pirahã focus on the present yields a grammar with only present tense and no recursion, ‘a grammar of happiness’. Most linguists hold that grammatical variation (e.g. verb-medial vs verb-final order) does not correlate with culture, which is why this is radical.

The test: Ted Gibson and Steve Piantadosi (MIT) planned a field expedition, but Brazil’s FUNAI refused Everett entry (his missionary past plus complaints from US linguists). They instead built a corpus of ~1,000 recorded Pirahã sentences (mostly from the earlier missionary Steve Sheldon) and searched a very large space of candidate grammars, with and without recursion, for the best fit. Result: no clear evidence of recursive structure — no clausal ‘and’/‘or’ conjunction, no complex embedding. Critics reply that the grammar-search method has no track record and that the language ‘is based on a recursive procedure’ regardless.

Epilogue: the government has since built a clinic, houses, electricity and a school where Pirahã children learn Portuguese and counting — empowerment versus loss of a unique culture and of ‘a source of data on how the mind works’.

### Birth of a Word — Deb Roy, TED 2011 (~20 min)

Roy (MIT Media Lab) wired every room of his house with fish-eye cameras and microphones and recorded 8–10 hours a day for three years: about 250,000 hours of audio-video, of which ~90,000 hours of video were analysed and over seven million words of home speech transcribed (with privacy safeguards).

Method: motion analysis extracts ‘space-time worms’ showing where people moved, so transcription could focus on the speech environment around his son — everything he heard from father, mother and nanny, and everything he produced.

The headline clip: a half-year of his son’s attempts compressed to 40 seconds, the form drifting from ‘gaga’ through ‘guga’ and ‘wada’ to ‘water’ — a form–meaning pair being tuned toward the adult form.

Finding 1 — the 503 words he produced by his second birthday were plotted against the complexity (utterance length) of caregiver speech containing each word. Caregiver speech dipped to its simplest exactly when each word was born and then rose again: all three caregivers unconsciously restructured their language to meet the child — a tight feedback loop, or scaffolding.

Finding 2 — ‘wordscapes’: tagging every moment the child heard ‘water’ and mapping where it happened shows the action concentrated in the kitchen; ‘bye’ clusters at the front door. The visual/activity context of a word predicts the order of acquisition — words are learned together with what they are about.

Extension: the same event-plus-conversation idea applied to television content and ~3 billion social-media comments a month to map how public ‘common ground’ drives conversation.

### The Zipf Mystery — Vsauce (linked from the Information Theory lecture, ~20 min)

‘The’ is about 6% of everything we say; the n-th most frequent word occurs roughly 1/n as often as the most frequent, giving a straight line on a log–log plot — Zipf’s law, found in every language including undeciphered ancient ones, and also in city sizes, earthquake magnitudes, citations, surnames and more.

Pareto connection: Zipf’s law is the discrete form of the Pareto distribution; about 18% of word types account for over 80% of tokens (the 80/20 rule).

Explanations surveyed: (1) Zipf’s own principle of least effort — speakers prefer few words, listeners prefer many, and the compromise yields the curve; (2) Mandelbrot’s ‘random typing’ argument — monkeys hitting keys produce Zipf-like word frequencies because longer words are exponentially less likely yet exponentially more numerous, so the law might be a mathematical inevitability; but random typing cannot explain why constrained sets (planets, elements, weekdays, invented alien names) are also Zipfian, so the pattern seems built into how we think; (3) preferential attachment (‘rich get richer’ — the paper-clip chain demonstration); (4) critical points where conversation changes topic. Probably all of these collude.

Consequences: ~100 words make up about half of any text; nearly half of the distinct words in a book occur only once (hapax legomena, e.g. ‘quizzaciously’); rare words are hard to interpret in ancient corpora, and forgetting follows a similar curve.

# 5. Natural Language Understanding and AI

## 5.1 The guiding questions

Can machines understand language?

Can machines think?

Can machines carry out information-processing like the mind?

Can we ‘reverse-engineer’ cognitive processes such as language and perception?

This is where computer vision, natural language understanding and artificial intelligence come together.

## 5.2 Marr’s tri-level hypothesis

David Marr (Vision, 1982) proposed that any machine carrying out an information-processing task must be understood at three levels:

Motivated by the rise of computers: programmers understand problems by computing things (level 1) with an algorithm (level 2) that runs on certain hardware (level 3).

Three example problems on the slide: build a system that recognises whether an image contains a cat; build a system that parses a sentence; build a system that makes a robot fly.

## 5.3 What is AI?

Slide figure 1.1 (Russell & Norvig): definitions of AI organised in four categories:

Wikipedia (slide): AI is the intelligence of machines and the branch of computer science that aims to create it — “the study and design of intelligent agents”, an agent being a system that perceives its environment and takes actions that maximise its chances of success. John McCarthy coined the term in 1956: “the science and engineering of making intelligent machines.” Central problems: reasoning, knowledge, planning, learning, communication, perception, and the ability to move and manipulate objects.

## 5.4 Acting humanly: the Turing test

Alan Turing’s 1950 article Computing Machinery and Intelligence discussed conditions for considering a machine intelligent: “Can machines think?” ←→ “Can machines behave intelligently?”

The Turing test (Imitation Game) is an operational definition of intelligence: a human interrogator converses through a screen with a human and an AI system and must tell which is which.

Problems with the Turing test (slide): (1) it is not reproducible, constructive, or amenable to mathematical analysis; (2) it ignores physical interaction with the interrogator and the environment → hence the Total Turing test, which requires perception and actuation.

## 5.5 What would a computer need to pass the Turing test?

# 6. NLP, CL and NLU

NLP → computational systems that process human language for a wide range of applications (slide montage: translation, assistants, search, speech).

Vending-machine analogy (slide): how do we connect human communication with machine behaviour? A machine must map an utterance onto an action.

# 7. Early NLU Systems

## 7.1 The 1970s goal

Building a machine capable of language understanding was an attractive goal for AI practitioners in the 70s; at that time ‘computational linguistics’, ‘cognitive science’ and ‘natural language processing’ were not totally distinct.

Aim: a machine that can carry out a conversation like a human being. If a machine can fool you into thinking it is human, have we reached natural language understanding? (The lecture’s answer: no — see ELIZA.)

## 7.2 ELIZA — an early ‘chatbot’ (1966)

Developed by Joseph Weizenbaum (MIT); simulated a (Rogerian) psychotherapist.

ELIZA’s responses (shown in capitals on the slide) were based on pattern matching rather than any real analysis — e.g. “my boyfriend made me come here” → “YOUR BOYFRIEND MADE YOU COME HERE”; “I am unhappy” → “DO YOU THINK COMING HERE WILL HELP YOU NOT TO BE UNHAPPY?”; a mention of ‘mother’ → “TELL ME MORE ABOUT YOUR FAMILY” (transcript from Boden 1977).

## 7.3 SHRDLU (Terry Winograd, 1972)

More than a conversational agent: it used language to report on its environment, to plan actions, and to reason about the implications of what was said to it.

Models how we understand our world via language — connects language with a representation of an environment.

Operates in a ‘micro-world’ of coloured blocks, pyramids and a box on a table (slide figure). Example dialogue: “Pick up a big, red block.” — “OK.” / “Grasp the pyramid.” — “I DON’T UNDERSTAND WHICH PYRAMID YOU MEAN.” / “Find a block which is taller than the one you are holding and put it into the box.” — “BY ‘IT’, I ASSUME YOU MEAN THE BLOCK WHICH IS TALLER THAN THE ONE I AM HOLDING. OK.” / “What does the box contain?” — “THE BLUE PYRAMID AND THE BLUE BLOCK.” / “Can a pyramid support a pyramid?” — “I DON’T KNOW.”

The name comes from ETAOIN SHRDLU — the first two columns of keys on a Linotype machine, i.e. the most frequent letters of English in order (a Zipfian aside).

### What SHRDLU achieved

Domain-specific understanding of language: question answering and executing commands in English.

An early parser of English based on a grammar.

Put together the component parts of a cognitive system in one model — a ‘working proof’ of the idea of language as procedural / algorithmic.

Makes the simulation of ‘understanding’ more convincing (resolving ‘it’, asking for clarification, admitting ignorance).

# 8. Building Blocks of NLU and a Typical NLP/CL Setup

## 8.1 Building blocks

Datasets — usually a text corpus (may be multi-modal); sometimes they must be collected / annotated / crowdsourced; may be multilingual (e.g. Universal Dependencies); may target specific areas (child language, learner corpora, eye-tracking).

Formal / computational processing — using symbolic (rule-based) grammars, e.g. the English Resource Grammar, or stochastic / machine-learning algorithms.

Validation by comparison with human performance — ‘performance’ metrics (e.g. BLEU) and cognitive metrics (harder to pin down).

## 8.2 A typical NLP/CL setup (method)

Use corpora / text resources; rule-based (formal) grammars, quantitative methods, mathematical formalisms; metrics for evaluation.

Workflow:

## 8.3 The NLP Trinity (slide figure)

Three axes: Problem (morph analysis → part-of-speech tagging → parsing → semantics), Language (Hindi, Marathi, English, French, …) and Algorithm (HMM, MEMM, CRF, RNN, …). Any piece of NLP work is a point in this space.

The companion figure orders problems by increased complexity of processing: Morphology → POS tagging → Chunking → Parsing → Semantics → Discourse and Coreference.

# 9. Main Challenge: Ambiguity

At last, a computer that understands you like your mother. — McDonnell-Douglas advertisement, 1985

## 9.1 Structural (syntactic) ambiguity

## 9.2 Other kinds of ambiguity (same sentence)

Speech recognition — how do we distinguish the spoken utterance from “… a computer that understands your lie cured mother”? (acoustic / segmentation ambiguity).

Word-sense ambiguity — how do we know ‘mother’ here means ‘a female parent’ rather than ‘a cask or vat used in vinegar-making’?

Attachment ambiguity — Copy the local patient files to disk: is it the patients or the files that are local?

# 10. Is NLP a Massive Knowledge-Engineering Project?

The alternative to hand-coding knowledge is the data-driven, empirical view, which has two intellectual roots:

## 10.1 Inspired from linguistics — distributional information

Correlations (co-occurrences) found in language data are important sources of information.

“You shall know a word by the company it keeps.” — J. R. Firth, 1957 (the distributional hypothesis behind word embeddings).

## 10.2 Claude Shannon’s information theory

Shannon was not concerned with what a message means; he focused on how surprising or uncertain it is.

The information content of a message depends on its probability, not its meaning.

## 10.3 Computational linguistics without linguistics?

A long-standing trend, stronger with deep learning and neural models: ever-larger training sets and more powerful training techniques yield impressive performance.

Costs: impossibly large datasets and computational power are required; divisions open between ‘high-’ and ‘low-resource’ languages.

Language models that only use linguistic form to predict the next word do not learn meaning / communicative intent (Bender & Koller 2020, ‘Climbing towards NLU’).

Powerful models like BERT are still insensitive to negation and to event prediction based on roles (Ettinger 2020, ‘What BERT is Not’).

Open problem: how to learn from rare but informative events? (Recall Zipf — most informative words are rare.)

Today’s world (slide): ChatGPT, Gemini, Claude, Mistral, Copilot, Perplexity, DeepSeek — all large language models trained on form; the same questions apply to them.

# 11. Closing Discussion (with model answers)

# 12. Next Class and Readings

Next class: How can we computationally represent the structure of language?

## Reading and references

Lillian Lee, “I’m sorry Dave, I’m afraid I can’t do that”: Linguistics, Statistics, and Natural Language Processing circa 2001 (also available as an online talk).

Mark Steedman, Romantics and Revolutionaries: What Theoretical and Computational Linguists Need to Know about Each Other (But Were Afraid to Ask), Linguistic Issues in Language Technology.

Emily M. Bender & Alexander Koller, Climbing towards NLU: On Meaning, Form, and Understanding in the Age of Data, ACL 2020.

Allyson Ettinger, What BERT Is Not: Lessons from a New Suite of Psycholinguistic Diagnostics for Language Models, TACL vol. 8, 2020.

# 13. Glossary

# 14. Key Takeaways

Language is a system of conventional form–meaning symbols; it transmits a conceptualised reality, not reality itself, and the hearer must reconstruct the thought by inference.

Two questions drive the course: how to manipulate strings of words (engineering) and what representational system could produce the behaviour (cognitive modelling).

Linguistic form under-specifies meaning (“The cat jumped over the wall” has several trajectories; “understands you like your mother” has three structural readings): ambiguity is the central challenge.

Marr’s three levels — computation (why), algorithm (what), implementation (how) — separate the problem from its mechanism; do not confuse copying the hardware with solving the problem.

The Turing test defines intelligence behaviourally; its limits (non-reproducible, no physical interaction) motivate the Total Turing test and the list of capabilities an NLU system needs.

NLP maps Language → Information; CL maps Language → Model; NLU is the shared goal.

ELIZA shows that an appropriate-looking response is not understanding; SHRDLU shows language can be modelled procedurally when tied to a representation of the environment.

NLU work = corpus + formal/computational model + validation against human performance.

The empirical view (Firth’s distributional idea + Shannon’s probability-based information) makes language computational — but form-only models still miss meaning, negation and roles (Bender & Koller 2020; Ettinger 2020).
