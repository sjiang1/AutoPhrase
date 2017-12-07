import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

if __name__=="__main__":
    jsonFilename=sys.argv[1]
    txtFilename=sys.argv[2]
    fWriter=open(txtFilename,"w")
    with open(jsonFilename,"r") as f:
        for line in f:
            d=json.loads(line)
            fWriter.write("%s\n" % d["content"].encode("utf-8"))
    fWriter.close()
