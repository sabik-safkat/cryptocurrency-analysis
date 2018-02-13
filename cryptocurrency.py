import re
import os

# analyzing cryptocurrency
# designed by: Sabik Safkat
# 2.12.2018
# Dictionary source (positive, negative) : http://www.unc.edu/~ncaren/haphazard/

with open("negative.txt", "r") as f:
    negtext = f.read()
negtokens = negtext.split("\n")
negtokens[-1:] = []

with open("positive.txt", "r") as g:
    postext = g.read()
postokens = postext.split("\n")
postokens[-1:] = []


def tokenizer(thetext):
    thetokens = re.findall(r'\b\w[\w-]*\b', thetext.lower())
    return thetokens


def calculator(thetweet):
    numposwords = 0
    thetweettokens = tokenizer(thetweet)
    for word in thetweettokens:
        if word in postokens:
            numposwords += 1

    numnegwords = 0
    for word in thetweettokens:
        if word in negtokens:
            numnegwords += 1

    sum = (numposwords - numnegwords)
    return sum

dirname = os.getcwd()
for fname in os.listdir(dirname):
    if fname.startswith("positive"):
        continue
    if fname.startswith("negative"):
        continue
    if fname.startswith("cryptocurrency"):
        continue
    with open(fname, "r") as f:
        tweetstext = f.read()
    tweetstokens = tweetstext.split("\n")
    tweetstokens[-1:] = []

    posi = 1
    nega = 0

    numtweets = 0
    numpostweets = 0
    numnegtweets = 0
    numneuttweets = 0
    percentile = 0

    for tweet in tweetstokens:
        calc = calculator(tweet)
        if calc > posi:
            numpostweets += 1
            numtweets += 1
        elif calc < nega:
            numnegtweets += 1
            numtweets += 1
        else:
            numneuttweets += 1
            numtweets += 1
    if (numpostweets) == 0:
        percentile = 0
    else:
        percentile = (numpostweets/(numpostweets+numnegtweets))*100


    base = os.path.basename(fname)
    os.path.splitext(base)
    print(os.path.splitext(base)[0] + " " + "positivity" + " " + "percentile: " + str(percentile))


