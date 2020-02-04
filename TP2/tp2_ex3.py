#Settings
filePath = "wsj_0010_sample.txt.conll";
outputFilePath = filePath + ".python_output.txt";
colOutputFilepath = filePath + ".col_output.txt";

modifiedTypes = ["SCONJ","SENT", "COMMA", "COLON"];
newTypes = ["CC", ".", ",", ":"]

#Opening files
file = open(filePath, "r+");
content = file.read();

#Splitting the content
lines = content.split("\n");

#print(lines[0]); #TEST

columns = [];

for line in lines:
  columns.append(line.split("\t"));

#Initialization of the variables
endStr = "";
colEndStr = "";
for column in columns:
  if len(column) >= 5:
    typeTemp = column[4]
    if typeTemp in modifiedTypes:
      #type to modify found
      index = modifiedTypes.index(typeTemp);
      typeTemp = newTypes[index];
    endStr += column[1] + "_" + typeTemp;
    endStr += " ";

    colEndStr += column[1] + "\t" + typeTemp;
    colEndStr += "\n";

#Creating output files
outFile = open(outputFilePath, "w");
outFile.write(endStr);
outFile.close();

outFile = open(colOutputFilepath, "w");
outFile.write(colEndStr);
outFile.close();
outFile.close();
