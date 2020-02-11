import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk import RegexpParser

#Downloading packages
nltk.download('punkt');
nltk.download('averaged_perceptron_tagger');
nltk.download('maxent_ne_chunker');
nltk.download('words');

#Settings
inputPath = "wsj_0010_sample.txt"
outputPath = "wsj_0010_sample.txt.ne.nltk";

#Extracting data
file = open(inputPath, "r+");
content = file.read();
file.close();

#Tokenization
tokenizer = PunktSentenceTokenizer();
tokens = tokenizer.tokenize(content);

words = []
tagged = []
namedEnt = []

for sentence in tokens:
  # print(sentence)
  words += nltk.word_tokenize(sentence)
  tagged = nltk.pos_tag(words)
  #Named Entity Recognition
  namedEnt = nltk.ne_chunk(tagged, binary=True);

print("NameEnt: ", namedEnt); #Testing

#Creating output files
outFile = open(outputPath, "w");
for token in namedEnt:
  if(type(token[0]) != type("string")):
    for parts in token:
      outFile.write(parts[0] + "\t" + parts[1] + "\t")
    outFile.write("\n");
  else:
    outFile.write(token[0] + "\t" + token[1] + "\n");
outFile.close();