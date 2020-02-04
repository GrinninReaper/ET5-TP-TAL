import xml.etree.ElementTree as ET

#Settings
filePath = 'formal-tst.NE.key.04oct95_sample.txt.se.xml';
outputFilePath = filePath + ".python_output.txt";

#Opening files to extract data
data_tree = ET.parse(filePath);
data_root = data_tree.getroot();
print(data_root.tag); #TEST

#Initializing variables
numberOfWords = 0;
dictionnary = [];
counter = [];
types = [];
fqce = [];

#Creating analization variables
wordTemp = "";
typeTemp = "";
indexTemp = 0;

#Analyzing data
for entry in data_root.iter('specific_entity'):
  print(entry.find('string').text);
  # for child in entry:
  #   print(child.tag);
  wordTemp = entry.find('string').text
  # print(wordTemp)
  if wordTemp in dictionnary:
    #already known word
    index = dictionnary.index(wordTemp)
    counter[index] += 1;
  else:
    #unknown word
    dictionnary.append(wordTemp)
    counter.append(1)
    typeTemp = entry.find('type').text.split(".")[]
    types.append(typeTemp);

  numberOfWords += 1;

#Printing the results
print(dictionnary);
print(types);
print(counter);
print("Number of worsd" + str(numberOfWords));
print(len(counter));

for count in counter:
  fqce.append(count/numberOfWords);

print(fqce);

#Creating output files
outFile = open(outputFilePath, "w");
outFile.write("Entité nommée\tType\tNombre d'occurences\tProportion dans le texte\n");
for i in range(len(counter)-1):
    line = dictionnary[i] + "\t" + types[i] + "\t" + str(counter[i]) + "\t" + str(fqce[i]) +"\n"
    outFile.write(line);
outFile.close();