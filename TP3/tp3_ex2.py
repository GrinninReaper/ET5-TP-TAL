import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk import RegexpParser

inputPath = "wsj_0010_sample.txt"
outputPath = "wsj_0010_sample.txt.chk.nltk";

inputFile = open(inputPath, "r+");
content = inputFile.read();
inputFile.close();

nltk.download('averaged_perceptron_tagger');
nltk.download('punkt');

contentSplit = word_tokenize(content);
print("After Split:",contentSplit);
tokens_tag = pos_tag(contentSplit);
print("After Token:",tokens_tag)
patterns= """groupeNom:{<JJ.*><NN.*>}
                        {<NN.*><NN.*>}
                        {<JJ.*><JJ.*><NN.*>}
                        {<JJ.*><NN.*><NN.*>}
          """
chunker = RegexpParser(patterns)
print("After Regex:",chunker)
output = chunker.parse(tokens_tag)
#for outputBuf in output:
  #print("After Chunking",outputBuf);

#Creating output files:
outFile = open(outputPath, "w");
for outputBuffer in output:
  if(len(outputBuffer[0][0]) > 1):
    for outBufferSplit in outputBuffer:
      if(len(outBufferSplit[0]) > 2):
        outFile.write(outBufferSplit[0] + "\t" + outBufferSplit[1] + "\t")
    outFile.write("\n");
outFile.close();