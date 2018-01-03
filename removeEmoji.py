import re
import sys

NON_BMP_RE = re.compile(u"[^\U00000000-\U0000d7ff\U0000e000-\U0000ffff]", flags=re.UNICODE)

def filter_out_emoji(text):
    return NON_BMP_RE.sub(u'', unicode(text, 'utf-8'))

if __name__=="__main__":
    if(len(sys.argv)<3):
        print("usage: python removeEmoji.py rawInputFile outputFile")
        sys.exit(-1)
    else:
        inputFile=sys.argv[1]
        outputFile=sys.argv[2]
        fWriter=open(outputFile,"w")
        with open(inputFile,"r") as f:
            for line in f:
                fWriter.write("%s\n" % filter_out_emoji(line.strip()).encode("utf-8").strip())
        fWriter.close()

