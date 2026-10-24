import json
OUT = "/Users/endeavoracademy/Claude/POS_Tagging_Lab/Nikhil Saini-G25AIT2067-NLTK-POS-Tagging.ipynb"
nb = json.load(open("/Users/endeavoracademy/Claude/POS_Tagging_Lab/template.ipynb"))
def src(c): return "".join(c["source"])
def code(text): return {"cell_type": "code", "metadata": {}, "source": text.strip() + "\n", "outputs": [], "execution_count": None}
def md(text): return {"cell_type": "markdown", "metadata": {}, "source": text.strip() + "\n"}

HEADER = md('''
# Name: Nikhil Saini
# Roll No: G25AIT2067

NLTK tutorial on sentence segmentation, tokenization, stemming, POS tagging and frequency counting.
The tutorial cells are as given in class. My work is in the exercise cells: the stemmer exercise,
Exercise 1a, Exercise 1b, Exercise 2 and Exercise 3. After each exercise I added a short note on what I found.
''')

STEM_CODE = code('''
# Exercise: Use the best stemmer on below list of words and report your results.
stem_words = [ "alumnus", "running", "alumnu", "alumni", "alumna", "alumnae", "cats", "catty", "cat", "chocolates", "chocolatey", "choco", "children" ]

from nltk.stem import PorterStemmer, LancasterStemmer
from nltk.stem.snowball import SnowballStemmer

# try the three English stemmers in NLTK side by side
stemmers = {"Porter": PorterStemmer(), "Snowball": SnowballStemmer("english"), "Lancaster": LancasterStemmer()}

print(f"{'word':12s}" + "".join(f"{name:12s}" for name in stemmers))
for word in stem_words:
    print(f"{word:12s}" + "".join(f"{s.stem(word):12s}" for s in stemmers.values()))

print()
print("Best stemmer here: Snowball. It keeps 'alumnus', gives run / cat / alumna / chocol;")
print("Porter cuts 'alumnus' to 'alumnu' and Lancaster over-cuts 'alumni' and 'children'.")
''')

STEM_MD = md('''
**What I found**

- Snowball (Porter2) is the best of the three here. It leaves "alumnus" alone, and gives running -> run, cats -> cat, alumnae -> alumna, chocolates -> chocol.

- Porter is almost the same but cuts "alumnus" to "alumnu", which is not a word.

- Lancaster is too aggressive: "alumni" and "alumna" both become "alumn", and "children" becomes "childr".

- None of them can join the Latin plurals. alumnus / alumni / alumna / alumnae end up as three or four different stems, and "children" never becomes "child". A stemmer only chops suffixes, it does not know irregular forms.

- "catty" -> "catti" and "chocolatey" staying as it is show that a stem does not have to be a real word.
''')

EX1A_CODE = code('''
# Exercises

# Tag each sentence below with parts of speech categories and comment about the assigned tags. If the assigned tags are wrong, what are the mistakes that the tagger is making?

# Note: Use the perceptron tagger for this homework.

# Colorless green ideas sleep furiously.
# A bright, colorful rainbow appeared today.
# A villager went to city to sell his property along with his wife.
# I saw the man with a telescope.
# We will sell gasoline to anyone in a glass container.
# Get the cat with the gloves.

# [Hint]
# Step-1: Create a new file "document_taging.txt" with above sentences.
# Step-2: Tokenize each sentence in the file.
# Step-3: Assign POS tag to each word in the sentence and then output the tagged sentences.

# [Your code starts from here]

import nltk
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Step 1: put the six sentences in a file, one per line
sentences = [
    "Colorless green ideas sleep furiously.",
    "A bright, colorful rainbow appeared today.",
    "A villager went to city to sell his property along with his wife.",
    "I saw the man with a telescope.",
    "We will sell gasoline to anyone in a glass container.",
    "Get the cat with the gloves.",
]
with open("document_taging.txt", "w") as f:
    f.write("\\n".join(sentences))

# Step 2 and 3: read the file back, tokenize each line and tag it with the perceptron tagger
with open("document_taging.txt") as f:
    for line in f:
        tokens = word_tokenize(line.strip())
        print(pos_tag(tokens))
        print()
''')
EX1A_MD = md('''
**My comments on the tags**

- **Colorless green ideas sleep furiously.** Colorless/NNP is wrong, it should be JJ. The word is not in the tagger's training data, it is capitalised and at the start of the sentence, so the tagger guesses "proper noun". green/JJ, ideas/NNS, sleep/VBP, furiously/RB are all right. The tagger does not care that the sentence is meaningless (Chomsky's example); it only looks at grammar, and the grammar is fine.

- **A bright, colorful rainbow appeared today.** All correct. today/NN is how the Penn Treebank tags it (a noun used as a time adverbial).

- **A villager went to city to sell his property along with his wife.** All correct. Both "to" get TO, which is the Penn convention even though the first is a preposition and the second an infinitive marker.

- **I saw the man with a telescope.** All tags correct, but the sentence is ambiguous (did I use the telescope, or did the man have it?). POS tags cannot show that. The ambiguity is in the parse, in where "with a telescope" attaches, not in the tags.

- **We will sell gasoline to anyone in a glass container.** anyone/NN is the Penn Treebank convention for this indefinite pronoun, so it is acceptable, though a pronoun tag would make more sense. glass/NN is right (a noun modifying "container"). The funny reading (anyone who is inside a glass container) is again an attachment problem.

- **Get the cat with the gloves.** All correct, Get/VB as an imperative. Same attachment ambiguity as the telescope sentence (cat wearing gloves, or using gloves to get it).

- **Overall:** the only real tagging error in the six sentences is Colorless -> NNP. The strange meanings come from syntactic ambiguity, which a POS tagger is not meant to resolve.
''')

EX1B_CODE = code('''
# Find the top 10 most frequent POS tags using brown corpus!

import nltk
nltk.download('brown')
nltk.download('universal_tagset')
from nltk.corpus import brown
from nltk.probability import FreqDist

# keep only the tags, then count them
tags = [tag for (word, tag) in brown.tagged_words()]
fdist_tag = FreqDist(tags)

print("Total tags   :", fdist_tag.N())
print("Distinct tags:", fdist_tag.B())
print("\\nTop 10 tags (Brown tagset):")
for tag, count in fdist_tag.most_common(10):
    print(f"  {tag:6s} {count:8d}   {100*count/fdist_tag.N():5.2f}%")

# same thing with the 12-tag universal tagset, easier to read
tags_u = [tag for (word, tag) in brown.tagged_words(tagset='universal')]
fdist_u = FreqDist(tags_u)
print("\\nTop 10 tags (universal tagset):")
for tag, count in fdist_u.most_common(10):
    print(f"  {tag:6s} {count:8d}   {100*count/fdist_u.N():5.2f}%")
''')
EX1B_MD = md('''
**What I found**

- NN (singular noun) is the most common tag, about 13% of all 1,161,192 tokens, followed by IN (preposition) and AT (article).

- Brown uses 472 distinct tags, because it marks many sub-types (for example NN-TL for a noun in a title).

- With the universal tagset NOUN alone is almost a quarter of the corpus. This is why the DefaultTagger('NN') from earlier is a sensible baseline.
''')

EX2_CODE = code('''
# Homework

# Exercise 2.1.1: Do a frequency distribution analysis of words on Penn Treebank (PTB) corpus considering a) Universal tagset b) PTB tagset and answer the following questions.  Verbally describe how the results differ from those that we obtained in class for the Brown corpus.

# 1] How many words are there in the corpus?
# 2] How many distinct words are there in the corpus?
# 3] What is the most frequent word?
# 4] How often does 'the' occur in the corpus?
# 5] List out top 10 frequent words in the corpus.

# [Your code starts here]

import nltk
nltk.download('treebank')        # Download PTB corpus
nltk.download('universal_tagset')
nltk.download('brown')
from nltk.corpus import treebank, brown
from nltk.probability import FreqDist

def word_stats(tagged_words, name):
    words = [word for (word, tag) in tagged_words]
    fdist = FreqDist(words)
    print(f"----- {name} -----")
    print("1] Total words        :", fdist.N())
    print("2] Distinct words     :", fdist.B())
    print("3] Most frequent word :", repr(fdist.max()))
    print("4] Count of 'the'     :", fdist['the'], f"({100*fdist.freq('the'):.2f}%)")
    print("5] Top 10 words       :", fdist.most_common(10))
    print()
    return fdist

# a) universal tagset
fd_ptb_u = word_stats(treebank.tagged_words(tagset='universal'), "PTB words, universal tagset")
# b) PTB tagset
fd_ptb   = word_stats(treebank.tagged_words(), "PTB words, PTB tagset")
# Brown again in the same format, so I can compare
fd_brown = word_stats(brown.tagged_words(), "Brown words (for comparison)")
''')
EX2_MD = md('''
**How the results differ from the Brown corpus**

- The tagset makes no difference to the word counts. a) and b) give identical numbers, because the tagset only changes the tag column; the words are the same tokens either way.

- Size: the NLTK Treebank sample is small, 100,676 tokens and 12,408 distinct words, against 1,161,192 tokens and 56,057 distinct words in Brown. Brown is about 11 times bigger.

- Most frequent "word": in PTB it is the comma "," (4,885), not "the". In Brown "the" (62,713) wins easily. PTB is Wall Street Journal text with long sentences full of commas and numbers.

- "the" is 4,045 tokens, 4.02% of PTB, versus 62,713, 5.40% of Brown. The Zipf shape is the same (one word takes a big share of the corpus) but a bit weaker in PTB. Counting "the" and "The" together gives 4,762.

- The PTB top 10 contains odd tokens like "*-1" and "0". These are trace / empty elements that the Treebank annotators insert for moved or dropped constituents. Brown has nothing like that. Apart from those, both top 10 lists are the usual function words: the, of, to, a, in, and.
''')

EX3_CODE = code('''
# Homework

# Exercise 2.3.1: Do a frequency distribution analysis of POS tags on Penn Treebank (PTB) corpus considering a) Universal tagset b) PTB tagset and answer the following questions.

# 1] How many tags are there in the corpus?
# 2] How many distinct tags are there in the corpus?
# 3] What is the most frequent tag?
# 4] How often does 'RB' occur in the corpus?
# 5] List out top 10 frequent tags in the corpus.

# [Your code starts here]

import nltk
nltk.download('treebank')        # Download PTB corpus
nltk.download('universal_tagset')
from nltk.corpus import treebank
from nltk.probability import FreqDist

def tag_stats(tagged_words, name, adverb_tag):
    tags = [tag for (word, tag) in tagged_words]
    fdist = FreqDist(tags)
    print(f"----- {name} -----")
    print("1] Total tags        :", fdist.N())
    print("2] Distinct tags     :", fdist.B())
    print("3] Most frequent tag :", fdist.max())
    print(f"4] Count of 'RB'     : {fdist['RB']}   (adverb tag here is {adverb_tag}: {fdist[adverb_tag]})")
    print("5] Top 10 tags       :")
    for tag, count in fdist.most_common(10):
        print(f"     {tag:8s} {count:7d}   {100*count/fdist.N():5.2f}%")
    print()
    return fdist

# a) universal tagset
fd_u = tag_stats(treebank.tagged_words(tagset='universal'), "PTB tags, universal tagset", "ADV")
# b) PTB tagset
fd_p = tag_stats(treebank.tagged_words(), "PTB tags, PTB tagset", "RB")
''')
EX3_MD = md('''
**What I found**

- Total tags = total words = 100,676 in both cases, one tag per token.

- Distinct tags: 46 with the PTB tagset, only 12 with the universal tagset, because the universal set collapses NN / NNS / NNP / NNPS into NOUN, VB / VBD / VBG / VBN / VBP / VBZ into VERB, and so on.

- Most frequent tag: NN (13,166) in PTB, NOUN (28,867) in universal. Same answer as Brown: nouns rule.

- "RB" occurs 2,822 times in the PTB tagset. In the universal tagset there is no RB at all; adverbs are ADV, which has 3,171 (RB + RBR + RBS together).

- The PTB top 10 has -NONE- (6,592) in fifth place. That is the tag of the trace / empty elements seen in Exercise 2; the universal tagset maps it to X (6,613). Brown has no such tag.
''')

out = [HEADER]
for c in nb["cells"]:
    s = src(c)
    if c["cell_type"] == "code":
        c["outputs"] = []; c["execution_count"] = None
        if s.startswith("# Exercise: Use the best stemmer"): out += [STEM_CODE]; continue
        if "Tag each sentence below" in s: out += [EX1A_CODE, EX1A_MD]; continue
        if s.startswith("# Find the top 10 most frequent POS tags"): out += [EX1B_CODE]; continue
        if "Exercise 2.1.1" in s: out += [EX2_CODE, EX2_MD]; continue
        if "Exercise 2.3.1" in s: out += [EX3_CODE]; continue
    out.append(c)
nb["cells"] = out
json.dump(nb, open(OUT, "w"), indent=1, ensure_ascii=False)
print("wrote", OUT, "cells", len(out))
