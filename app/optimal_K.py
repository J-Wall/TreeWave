#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 14:05:11 2024

@author: nasmaboumajdi
"""

import pandas as pd

def read_fasta(file_path):
    """Reads a FASTA file and returns the DNA sequence."""
    with open(file_path, 'r') as f:
        f.readline()
        sequence = ''.join(line.strip() for line in f)
    return sequence

def count_kmers(sequence, k):
    """Counts the number of total, unique, and distinct k-mers in a DNA sequence."""
    total_kmers = len(sequence) - k + 1
    kmers_dict = {}
    for i in range(total_kmers):
        kmer = sequence[i:i+k]
        if kmer in kmers_dict:
            kmers_dict[kmer] += 1
        else:
            kmers_dict[kmer] = 1
    unique_kmers = len(kmers_dict)
    distinct_kmers = sum(1 for count in kmers_dict.values() if count == 1)
    return total_kmers, unique_kmers, distinct_kmers


def kmer_range(file,kmin,kmax,outfile):
    results = []
    sequence = read_fasta(file)
    for k in range(kmin,kmax+1):
        total_kmers,unique_kmers,distinct_kmers = count_kmers(sequence,k)
        results.append({'k':k,'total kmers':total_kmers,'unique kmers':unique_kmers,'distinct kmers':distinct_kmers})
    df = pd.DataFrame(results)
    df.to_csv(outfile)

