import sys
from os import listdir, system, makedirs
from os.path import isfile, join, exists
from subprocess import call

def listFiles(dir):
    return [f.split(".")[0] for f in listdir(dir) if isfile(join(dir, f))]

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        lang = sys.argv[1]
        totalNumOfProblems = int(sys.argv[2])

    if not exists(lang):
        makedirs(lang)

    havingProblems = set(listFiles(lang))
    missingProblems = [p for p in range(1, totalNumOfProblems + 1) if str(p) not in havingProblems]
    
    for p in missingProblems:
        system("leetcode show " + str(p) + " -g -x -d false -l " + lang + " -o " + lang)