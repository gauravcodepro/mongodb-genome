#!/usr/bin/env python3
# Author Gaurav 
# Universitat Potsdam
# Date 2024-6-24

import os
import pandas as pd


class MongoDB:

    def mongodbprepare(gfffile, prepare):
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
                gffwrite.write("column1" + "\t" + "column2" + "\t" +"column3" + "\t" +
                  "column4" + "\t" + "column5" + "\t" + "column6" + "\t" + "column7" +
                  "\t" + "column8" + "\t" + "column9\n")
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
                  "column4" + "\t" ''+ "column5" + "\t" + "column6" + "\t" + "column7" +
                  "\t" + "column8" + "\t" + "column9\n")
                    for line in gffread.readlines():
                        gffwrite.write(line)
                    gffwrite.close()
            gffdataframe = pd.read_csv("gfffilemod", sep = "\t")
            select1 = gffdataframe["column3"]
            select2 = gffdataframe["column4"]
            select3 = gffdataframe["column5"]
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
                  "column4" + "\t" ''+ "column5" + "\t" + "column6" + "\t" + "column7" +
                  "\t" + "column8" + "\t" + "column9\n")
                    for line in gffread.readlines():
                        gffwrite.write(line)
                    gffwrite.close()
            gffdataframe = pd.read_csv("gfffilemod", sep = "\t")
            select1 = gffdataframe["column3"]
            select2 = gffdataframe["column4"]
            select3 = gffdataframe["column5"]
            mongoprepareintron = {}
            for i in range(len(select1)):
                if select1 == "exon":
                    mongoprepareintron[select1[i]] = [{select1[i]: select2[i]}, {select1[i]: select3[i]}]
            return mongoprepareintron
    
    
