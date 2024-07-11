# mongodb-genome

- python class to prepare the genome files for the mongodb atlas
- since the genome annotations id will be same, implmented a list based nested iteration so that it can be inserted into ``` mongodb as .insertMany() ```
- below is the UML for the following class.

<img src = "https://github.com/gauravcodepro/mongodb-genome/blob/main/UML.png" >
  
```
# if you are executing from the specific directory then
import os
os.chdir("path/dir/fasta/gff")
mongodbprepare("samplefile.gff", prepare= "yes")
fastaindex("samplefile.fasta", prepare= "yes")
exonparse("samplefile.gff", prepare= "yes")
intronparse("samplefile.gff", prepare= "yes")
exonseq("samplefile.gff", "samplefile.fasta", mongoexonprepareseq)
intronseq("samplefile.gff", "samplefile.fasta", mongointronprepareseq)
goparsemongo("GO_slim_sample.txt")
```

Gaurav

