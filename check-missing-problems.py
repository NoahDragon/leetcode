import sys
from os import listdir, system
from os.path import isfile, join
from subprocess import call

def listFiles(dir):
    return [f.split(".")[0] for f in listdir(dir) if isfile(join(dir, f))]

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        dir = sys.argv[1]
        totalNumOfProblems = int(sys.argv[2])

    havingProblems = set(listFiles(dir))
    missingProblems = [p for p in range(1, totalNumOfProblems) if str(p) not in havingProblems]
    
    for p in missingProblems:
        system("leetcode show " + str(p) + " -g -x -d false -l bash")