def main():
    readFile = open("robots.mat.txt");
    outputFile = open("output.txt", 'w');
    outputFile.truncate();
    outputFile.write("erumpent\nj1kb4rrbduujb6fqvurrqdbvoc\n");
    for line in readFile:
        solveInstance(line,outputFile);
    readFile.close();
    outputFile.close();

def solveInstance(line,outputFile):
    x = 10;

if __name__ == "__main__":
    main();