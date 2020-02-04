import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk import RegexpParser

inputPath = "wsj_0010_sample.txt"
outputPath = "wsj_0010_sample.txt.pos.nltk";

inputFile = open(inputPath, "r+");
content = inputFile.read();
inputFile.close();

nltk.download('averaged_perceptron_tagger');

contentSplit = word_tokenize(content);
print("After Split:",contentSplit);
tokens_tag = pos_tag(contentSplit);
print("After Token:",tokens_tag)
# patterns= """mychunk:{<NN.?>*<VBD.?>*<JJ.?>*<CC>?}"""
# chunker = RegexpParser(patterns)
# print("After Regex:",chunker)
# output = chunker.parse(tokens_tag)
# print("After Chunking",output)

#Creating output files:
outFile = open(outputPath, "w");
str =""
for outputBuffer in tokens_tag:
  outFile.write(outputBuffer[0] + "\t" + outputBuffer[1] + "\n");
# for i in range(len(output)-1):
#     line = (output[i]) + "\t" + str(fqce[i]) +"\n"
#     outFile.write(line);
# outFile.write(str);

outFile.close();