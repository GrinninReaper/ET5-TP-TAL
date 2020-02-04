import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk import RegexpParser

inputPathTags = "POSTags_PTB_Universal_Linux.txt"
inputPath1 = "wsj_0010_sample.txt.pos.nltk"
outputPath1 = "wsj_0010_sample.txt.pos.univ.nltk";
inputPath2 = "wsj_0010_sample.txt.pos.ref"
outputPath2 = "wsj_0010_sample.txt.pos.univ.ref";

inputFileTags = open(inputPathTags, "r+");
contentTags = inputFileTags.read();
inputFileTags.close();

inputFile1 = open(inputPath1, "r+");
content1 = inputFile1.read();
inputFile1.close();

inputFile2 = open(inputPath2, "r+");
content2 = inputFile2.read();
inputFile2.close();

nltk.download('averaged_perceptron_tagger');

contentSplitTags = contentTags.split();
#print("After Split:",contentSplitTags);
arrayTagsKeys=[];
arrayTagsValues=[];
for i in range(len(contentSplitTags)):
  if(i%2==0):
    arrayTagsKeys.append(contentSplitTags[i])
  else:
    arrayTagsValues.append(contentSplitTags[i])

#print("arrayTagsKeys:",arrayTagsKeys);
#print("\narrayTagsValues:",arrayTagsValues);

contentSplit1 = content1.split();
arrayContentKeys1=[];
arrayContentValues1=[];
for i in range(len(contentSplit1)):
  if(i%2==0):
    arrayContentKeys1.append(contentSplit1[i])
  else:
    arrayContentValues1.append(contentSplit1[i])
#print("\nAfter Split:",contentSplit1);

contentSplit2 = content2.split();
arrayContentKeys2=[];
arrayContentValues2=[];
for i in range(len(contentSplit2)):
  if(i%2==0):
    arrayContentKeys2.append(contentSplit2[i])
  else:
    arrayContentValues2.append(contentSplit2[i])
#print("\nAfter Split:",contentSplit2);

print("\n");
writeTag = False;
tagToWrite = "";
#Creating output files:
outFile1 = open(outputPath1, "w");
for j in range(len(arrayContentKeys1)):
  for i in range(len(arrayTagsKeys)):
    if(arrayContentValues1[j] == arrayTagsKeys[i]):
      tagToWrite = arrayTagsValues[i]
      print("arrayContentValues1[i]="+arrayContentValues1[j]+" arrayTagsKeys[i]=" + arrayTagsKeys[i] + " tagToWrite=" + tagToWrite)
      writeTag = True
  if(writeTag):
    outFile1.write(arrayContentKeys1[j] + "\t");
    outFile1.write(tagToWrite + "\n");
    writeTag = False;
outFile1.close();

print("\n");
print("\n");

writeTag = False;
outFile2 = open(outputPath2, "w");
for j in range(len(arrayContentKeys2)):
  for i in range(len(arrayTagsKeys)):
    if(arrayContentValues2[j] == arrayTagsKeys[i]):
      tagToWrite = arrayTagsValues[i]
      print("arrayContentValues2[i]="+arrayContentValues2[j]+" arrayTagsKeys[i]=" + arrayTagsKeys[i] + " tagToWrite=" + tagToWrite)
      writeTag = True
  if(writeTag):
    outFile2.write(arrayContentKeys2[j] + "\t");
    outFile2.write(tagToWrite + "\n");
    writeTag = False;
outFile2.close();