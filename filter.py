
def checkNum(word):
    for s in word:
        if(s in ['0','1','2','3','4','5','6','7','8','9']):
            return True
    return False


def checkStopWord(word):
    if(word in ["and","the","for","of","via","from"]):
        return True
    return False


fWriter=open("results/filtered_phrases.txt","w")

with open("results/AutoPhrase_multi-words.txt","r") as f:
    for line in f.readlines():
        line=line.strip()
        splitted=line.split("\t")
        score=float(splitted[0])
        phrase_part=splitted[1]
        if(score<0.5):
            continue
        phrase_words=phrase_part.split(" ")
        if(len(phrase_words)>4):
            continue
        flag=[len(word)<=2 for word in phrase_words]
        if(sum(flag)>=1):
            continue
        ifNum=[checkNum(word) for word in phrase_words]
        if(sum(ifNum)>=1):
            continue
        ifStopwords=[checkStopWord(word) for word in phrase_words]
        if(sum(ifStopwords)>=1):
            continue
        #print(line)
        fWriter.write("%s\n" % phrase_part)

fWriter.close()

