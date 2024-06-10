#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: nasmaboumajdi
"""

## application


import math
import numpy as np
from Bio import SeqIO
import pywt
import pandas as pd
from collections import Counter
from scipy.spatial import distance
import biotite.sequence.phylo as phylo



def generate_newick_from_fasta(k, inputfile, outputfile):
    sequences,seq_labels,chaos_list = prepare_sequences(inputfile, k)
    waves = apply_discrete_wavelet_transform(chaos_list)
    dist_cosine = compute_cosine_matrix(waves)
    newick_str = generate_upgma_newick(dist_cosine, seq_labels)
    with open(outputfile, 'w') as file:
            file.write(newick_str)


def get_matrix_from_fasta(k,inputfile, outputfile):
    sequences,seq_labels,chaos_list = prepare_sequences(inputfile, k)
    waves = apply_discrete_wavelet_transform(chaos_list)
    dist_cosine = compute_cosine_matrix(waves)
    df_mat = pd.DataFrame(dist_cosine,index=seq_labels,columns=seq_labels)
    df_mat.to_csv(outputfile)


def prepare_sequences(inputfile, k):
      seq_labels = []  
      sequences = []     
      chaos_list = []                     
      fasta_sequences = SeqIO.parse(open(inputfile), 'fasta')
      for fasta in fasta_sequences:
          identifiant = fasta.id
          sequence = fasta.seq
          seq_labels.append(identifiant)
          sequences.append(sequence)
          c = dna_embedding(sequence, k)
          chaos_list.append(c)
      return sequences,seq_labels,chaos_list

def dna_embedding(sequence, k):
    length = len(sequence)
    d = count_kmers(sequence,k)
    p = kmers_probabilities(d,length)
    c = frequency_chaos_game_representation(p,k)
    return c 


def frequency_chaos_game_representation(probabilities, k):
    array_size = int(math.sqrt(4**k))
    chaos = [[0] * array_size for _ in range(array_size)]

    maxx, maxy, posx, posy = array_size, array_size, 1, 1

    for key, value in probabilities.items():
        for char in key:
            if char == "T":
                posx += maxx / 2
            elif char == "C":
                posy += maxy / 2
            elif char == "G":
                posx += maxx / 2
                posy += maxy / 2
            maxx /= 2
            maxy /= 2

        chaos[int(posy - 1)][int(posx - 1)] = value

        maxx, maxy, posx, posy = array_size, array_size, 1, 1

    return chaos

def count_kmers(sequence, k):
    kmer_count = Counter(sequence[i:i+k] for i in range(len(sequence) - k + 1) if 'N' not in sequence[i:i+k])
    return kmer_count

def kmers_probabilities(kmer_count, N):
    probabilities = {key: value / (N - len(key) + 1) for key, value in kmer_count.items()}
    return probabilities



def apply_discrete_wavelet_transform(chaos_list):
    wave = []
    for i in range(0,len(chaos_list)):
        coeffs = pywt.wavedec2(chaos_list[i], 'haar', level=5)
        features = np.concatenate([np.concatenate(c).ravel() for c in coeffs])
        wave.append(features)
    return wave
 
#### distance matrix 
def compute_cosine_matrix(object_list):
     dist_cosine = np.zeros((len(object_list),len(object_list))) 
     for i in range(0,len(object_list)):             
        for j in range(0,len(object_list)):
           if(i!=j):
                dist_cosine[i][j] = distance.cosine(object_list[i].flatten(),object_list[j].flatten())
     return dist_cosine

def generate_upgma_newick(dist_cosine, seq_labels):
    tree = phylo.upgma(dist_cosine)
    newick_str = tree.to_newick(include_distance=False,labels=seq_labels)
    return newick_str




    
