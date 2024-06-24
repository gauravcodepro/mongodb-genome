#! /usr/bin/en python3
# Author Gaurav
# Universitat Potsdam
# Date 2024-6-24

class MongoDB:
    def mongodbprepare(gfffile, prepare):
    import pandas as pd
    """
     a mongodb class to prepare the genome annotations
     for the genomedb, you can prepare any gff file for the
     pymongodb as long as it meets the same gff pattern.
     since the genome annotations id will be duplicated ,
     implmented a list based nested iteration so that it can
     be inserted into mongodb as .insertMany()
    """
    if gfffile and prepare == "yes":
        with open(gfffile, "r") as gffread:
            with open("gfffilemod", "w") as gffwrite:
                gffwrite.write("column1" + "\t" + "column2" + "\t" +"column3" +"\t" + "column4" + "\t" + "column5" + "\t" + "column6" + "\t" + "column7" + "\t" + "column8" + "\t" + "column9\n")
                for line in gffread.readlines():
                    gffwrite.write(line)
                gffwrite.close()
    gffdataframe = pd.read_csv("gfffilemod", sep = "\t")
    genomeloc = gffdataframe["column1"]
    accession = gffdataframe["column2"]
    typeaccession = gffdataframe["column3"]
    start = gffdataframe["column4"]
    end = gffdataframe["column5"]
    length = gffdataframe["column6"]
    posstrand = gffdataframe["column7"]
    negstrand = gffdataframe["column8"]
    idlocation = gffdataframe["column9"]
    mongodbprepare = []
    for i in range(len(genomeloc)):
        for i in range(len(genomeloc)):
            mongodbprepare[genomeloc[i]] = [{genomeloc[i]: accession[i]}, {genomeloc[i]: typeaccession[i]},
                                        {genomeloc[i]: start[i]}, {genomeloc[i]:end[i]},
                                        {genomeloc[i]:length[i]}, {genomeloc[i]: posstrand[i]},
                                        {genomeloc[i]:negstrand[i]}, {genomeloc[i]: idlocation[i]}]dlocation[i]}])
    return mongodbprepare
 if __name__ == __main_:
     mongodbprepare(gfffile, prepare)
