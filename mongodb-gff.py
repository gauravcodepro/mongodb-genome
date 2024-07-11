#!/usr/bin/env python3
# Author Gaurav
# Date 2024-6-24
# a mongodb class to prepare the genome annotations for the genomedb, you can prepare any gff file for the
# pymongodb as long as it meets the same gff pattern. since the genome annotations id will be duplicated ,
# implmented a list based nested iteration so that it can be inserted into mongodb as .insertMany()

import os
import pandas as pd

class MongoDB:
    

    def mongodbprepare(gfffile, prepare):
        if gfffile and prepare == "yes":
            with open(gfffile, "r") as gffread:
                with open("gfffilemod", "w") as gffwrite:
                    gffwrite.write("column1" + "\t" + "column2" + "\t" +"column3" + "\t" +
                    "column4" + "\t" + "column5" + "\t" + "column6" + "\t" + "column7" +
                    "\t" + "column8" + "\t" + "column9\n")
                for line in gffread.readlines():
                    gffwrite.write(line)
                gffwrite.close()
        gffdataframe = pd.read_csv("gfffilemod", sep = "\t")
        genomeloc = gffdataframe["column1"].to_list()
        accession = gffdataframe["column2"].to_list()
        typeaccession = gffdataframe["column3"].to_list()
        start = gffdataframe["column4"].to_list()
        end = gffdataframe["column5"].to_list()
        length = gffdataframe["column6"].to_list()
        posstrand = gffdataframe["column7"].to_list()
        negstrand = gffdataframe["column8"].to_list()
        idlocation = gffdataframe["column9"].to_list()
        mongodbprepare = []
        for i in range(len(genomeloc)):
            for i in range(len(genomeloc)):
                mongodbprepare[genomeloc[i]] = [{genomeloc[i]: accession[i]}, {genomeloc[i]: typeaccession[i]},
                                        {genomeloc[i]: start[i]}, {genomeloc[i]:end[i]},
                                        {genomeloc[i]:length[i]}, {genomeloc[i]: posstrand[i]},
                                        {genomeloc[i]:negstrand[i]}, {genomeloc[i]: idlocation[i]}]dlocation[i]}])
        return mongodbprepare

    def fastaindex(pathfasta, mongopreparefasta):
        if pathfasta and monopreparefasta == "yes":
            readfasta = [i.strip() for i in open(pathfasta, "r").readlines()]
            fastaseq = {}
            for i in readfasta:
                if i.startswith(">"):
                    path = i.strip()
                    if i not in fastaseq:
                        fastaseq[i] = ""
                    continue
                fastaseq[path] += i.strip()
            fasta_seq = list(fastaseq.values())
            fasta_names = [i.replace(">", "")for i in (list(fastaseq.keys()))]
            fasta_len = []
            for i in range(len(fasta_seq)):
                fasta_len.append(len(fasta_seq[i]))
            mongopreparefasta = {}
            for i in range(len(fasta_names)):
                mongopreparefasta[fasta_names[i]] = [{fasta_names[i]: fasta_len[i]}, {fasta_names[i]: fasta_seq[i]}]
            return mongopreparefasta

    def exonparse(pathgff, mongoprepareexon):
        if pathgff and mongoprepareexon:
            with open(gfffile, "r") as gffread:
                with open("gfffilemod", "w") as gffwrite:
                    gffwrite.write("column1" + "\t" + "column2" + "\t" +"column3" + "\t" +
                  "column4" + "\t" + "column5" + "\t" + "column6" + "\t" + "column7" +
                  "\t" + "column8" + "\t" + "column9\n")
                    for line in gffread.readlines():
                        gffwrite.write(line)
                    gffwrite.close()
            gffdataframe = pd.read_csv("gfffilemod", sep = "\t")
            select1 = gffdataframe["column3"].to_list()
            select2 = gffdataframe["column4"].to_list()
            select3 = gffdataframe["column5"].to_list()
            mongoprepareexon = {}
            for i in range(len(select1)):
                if select1 == "exon":
                    mongoprepareexon[select1[i]] = [{select1[i]: select2[i]}, {select1[i]: select2[i]}]
            return mongoprepareexon

    def intronparse(pathgff, mongoprepareintron):
        if pathgff and mongoprepareintron:
            with open(gfffile, "r") as gffread:
                with open("gfffilemod", "w") as gffwrite:
                    gffwrite.write("column1" + "\t" + "column2" + "\t" +"column3" + "\t" +
                  "column4" + "\t" + "column5" + "\t" + "column6" + "\t" + "column7" +
                  "\t" + "column8" + "\t" + "column9\n")
                    for line in gffread.readlines():
                        gffwrite.write(line)
                    gffwrite.close()
            gffdataframe = pd.read_csv("gfffilemod", sep = "\t")
            select1 = gffdataframe["column3"].to_list()
            select2 = gffdataframe["column4"].to_list()
            select3 = gffdataframe["column5"].to_list()
            mongoprepareintron = {}
            for i in range(len(select1)):
                if select1 == "exon":
                    mongoprepareintron[select1[i]] = [{select1[i]: select2[i]}, {select1[i]: select3[i]}]
            return mongoprepareintron

    def exonseq(pathgff, pathfasta, mongoexonprepareseq):
        if pathgff and pathfasta and mongoprepareexonseq:
            readfasta = [i.strip() for i in open(pathfasta, "r").readlines()]
            fastaseq = {}
            for i in readfasta:
                if i.startswith(">"):
                    path = i.strip()
                    if i not in fastaseq:
                        fastaseq[i] = ""
                    continue
                fastaseq[path] += i.strip()
            fasta_seq = list(fastaseq.values())
            fasta_names = [i.replace(">", "")for i in (list(fastaseq.keys()))]
            fastaparsedict = {}
            for i in range(len(fasta_seq)):
                fastaparsedict[fasta_seq[i]] = fasta_names[i]
            with open(gfffile, "r") as gffread:
                with open("gfffilemod", "w") as gffwrite:
                    gffwrite.write("column1" + "\t" + "column2" + "\t" +"column3" + "\t" +
                  "column4" + "\t" + "column5" + "\t" + "column6" + "\t" + "column7" +
                  "\t" + "column8" + "\t" + "column9\n")
                    for line in gffread.readlines():
                        gffwrite.write(line)
                    gffwrite.close()
            gffdataframe = pd.read_csv("gfffilemod", sep = "\t")
            exonpresent = gffdataframe["column1"].to_list()
            select1 = gffdataframe["column3"].to_list()
            select2 = gffdataframe["column4"].to_list()
            select3 = gffdataframe["column5"].to_list()
            exonseq ={}
            for i in range(len(select1)):
                if select1 == "exon":
                    exonseq[exonpresent[i]] = [select1[i], select2[i], select3[i]]
            exonseqprepare = {}
            exonseqkeys = list(exonseq.keys())
            exonseqvalues = list(exonseq.values())
            for i in range(len(exonseqkeys)):
                for j in range(len(fasta_seq)):
                    if exonseqkeys[i] == fasta_names[i]:
                        exonseqprepare[exonseqkeys[i]] == fasta_seq[i][exonseqvalues[i][0]:exonseqvalues[i][1]]
                    return exonseqprepare

    def intronseq(pathgff, pathfasta, mongointronprepareseq) :
        if pathgff and pathfasta and mongoprepareintronseq:
            readfasta = [i.strip() for i in open(pathfasta, "r").readlines()]
            fastaseq = {}
            for i in readfasta:
                if i.startswith(">"):
                    path = i.strip()
                    if i not in fastaseq:
                        fastaseq[i] = ""
                    continue
                fastaseq[path] += i.strip()
            fasta_seq = list(fastaseq.values())
            fasta_names = [i.replace(">", "")for i in (list(fastaseq.keys()))]
            fastaparsedict = {}
            for i in range(len(fasta_seq)):
                fastaparsedict[fasta_seq[i]] = fasta_names[i]
            with open(gfffile, "r") as gffread:
                with open("gfffilemod", "w") as gffwrite:
                    gffwrite.write("column1" + "\t" + "column2" + "\t" +"column3" + "\t" +
                  "column4" + "\t" + "column5" + "\t" + "column6" + "\t" + "column7" +
                  "\t" + "column8" + "\t" + "column9\n")
                    for line in gffread.readlines():
                        gffwrite.write(line)
                    gffwrite.close()
            gffdataframe = pd.read_csv("gfffilemod", sep = "\t")
            intronpresent = gffdataframe["column1"].to_list()
            select1 = gffdataframe["column3"].to_list()
            select2 = gffdataframe["column4"].to_list()
            select3 = gffdataframe["column5"].to_list()
            intronseq ={}
            for i in range(len(select1)):
                if select1 == "exon":
                    intronseq[intronpresent[i]] = [select1[i], select2[i], select3[i]]
            intronseqprepare = {}
            intronseqkeys = list(intronseq.keys())
            intronseqvalues = list(intronseq.values())
            for i in range(len(intronseqkeys)):
                for j in range(len(fasta_seq)):
                    if intronseqkeys[i] == fasta_names[i]:
                        intronseqprepare[intronseqkeys[i]] == fasta_seq[i][intronseqvalues[i][0]:intronseqvalues[i][1]]
                    return exonseqprepare

    def goparsemongo(go_anntoations):
        with open(go_anntoations, "r") as goannotate:
            with open("goannotatemod.txt", "w") as gowrite:
                for line in goannotate.readlines():
                    if "!" not in line:
                        gowrite.write(line)
                    goannotatewrite.close()
        mongoprepareontologycomb1 = []
        mongoprepareontologycomb2 = []
        mongoprepareontologycomb3 = []
        mongoprepareontologycomb4 = []
        mongoprepareontologycomb5 = []
        with open("goannotatemod.txt", "r") as gowrite:
            for line in gowrite.readlines():
                if len(line) <= 3:
                    continue
                else:
                    mongoprepareontologycomb1.append({line.strip().split("\t")[0]: line.strip().split("\t")[1]})
                    mongoprepareontologycomb2.append({line.strip().split("\t")[0]: line.strip().split("\t")[2]})
                    mongoprepareontologycomb3.append({line.strip().split("\t")[0]: line.strip().split("\t")[3]})
                    mongoprepareontologycomb4.append({line.strip().split("\t")[1]: line.strip().split("\t")[2]})
                    mongoprepareontologycomb5.append({line.strip().split("\t")[1]: line.strip().split("\t")[3]})
