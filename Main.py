import re;
from Variables import *;

def main():
    outputFile = open(outputFileName, 'w');
    outputFile.truncate();
    outputFile.write("erumpent\nj1kb4rrbduujb6fqvurrqdbvoc\n");
    outputFile.close();
    with open(readFileName) as f:
        for line in f:
            solveInstance(line);

def solveInstance(line):
    outputFile = open(outputFileName, 'w');
    obstaclesText = "";
    coText = "";
    line = line[2:line.__len__()];
    if line.find('#')!=-1:
        obstaclesText = line[line.find('#')+1:line.__len__()];
        line = line[0:line.find('#')-1];
    coText = line;
    coTextArray = map(float, re.split('\d+.?\d+',coText));
    print coTextArray;
    outputFile.close();

if __name__ == "__main__":
    main();