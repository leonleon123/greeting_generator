import json
import re
import random
from autocorrect import Speller

speller = Speller()
level = 6
error = {
    "EN":"Couldn't generate any sentece, please try again.",
    "SI":"Žal sestavljanje stavka ni uspelo, prosimo poskusite ponovno."
}

def beautifySentence(a):
    tmp = a
    tmp=tmp.replace(" !", "!").replace(" ,", ",").replace(" .", ".")
    tmp=tmp.replace("!", "! ").replace(",", ", ").replace(".", ". ")
    tmp=re.sub("  *", " ", tmp)
    return tmp

def generate(keywords, length, iteration, language):
    if iteration == 0: return error[language]
    with open(f"data{language}.txt") as file:
        freqs = "".join(file.readlines()).lower()
    distributed={}
    for i in range(len(freqs)-level):
        if freqs[i:i+level] not in distributed:
            distributed[freqs[i:i+level]] = [freqs[i+level]]
        distributed[freqs[i:i+level]].append(freqs[i+level])
    ngrams = list(distributed)
    rand_index = random.randint(0,len(ngrams))
    result = ngrams[rand_index]
    i = rand_index
    beginning = ""
    while ngrams[i][0] != " ":
        beginning = ngrams[i][0] + beginning
        i-=1
    for i in range(length):
        if not result[i:i+level] in distributed:
            continue
        result+=random.choice(distributed[result[i:i+level]])
    if any(x in result[level:] for x in keywords):
        if language == "EN":
            return speller.autocorrect_sentence(beautifySentence(beginning[:-1]+result))
        return beautifySentence(beginning[:-1]+result)
    else:
        return generate(keywords, length, iteration - 1, language)

if __name__ == "__main__":
    # print(generate(["vesel","valentin"],200, 40,"SI"))
    print(generate(["happy","valentin"],200, 40,"EN"))