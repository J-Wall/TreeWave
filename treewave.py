#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 12:11:54 2023

@author: nasmaboumajdi
"""

## mytool 
import click 
from scripts import application
from scripts import optimal_K

@click.group()
def cli():
    """TreeWave: An alignment-free approach for phylogeny reconstruction based on Frequency Chaos Game Representation and Discrete Wavelet Transform."""
    pass

@cli.command()
@click.option('-k', '--k', type=int,required=True,help='K-mer length')
@click.argument('inputfile', type=click.Path(exists=True))
@click.argument('outputfile', type=click.Path())
def gettree(k,inputfile,outputfile):
    """Alignment-free phylogenetic tree inference"""
    application.NewickFromFasta(k, inputfile, outputfile)
    click.echo("newick file created")

@cli.command()
@click.option('k','--k',type=int,required=True,help='K-mer length')
@click.argument('inputfile',type=click.Path(exists = True))
@click.argument('outputfile',type=click.Path())
def getmatrix(k,inputfile,outputfile):
    """Cosine distance matrix computation"""
    application.matFromFasta(k,inputfile,outputfile)
    click.echo("distance matrix created and saved to file")


@cli.command()
@click.argument('genome',type=click.Path())
@click.option('--kmin','-kmin',type=int,required=True, help= 'The minimum K-mer length')
@click.option('--kmax','-kmax',type=int,required=True, help= 'The maximum K-mer length')
@click.argument('outputfile',type=click.Path())
def kmers_count(genome,kmin,kmax,outputfile):
    """Counts of possible kmers and distinct kmers among a genome for a specific Kmer range"""
    optimal_k.kmer_range(genome,kmin,kmax,outputfile)
    click.echo("Kmers distribution calculated and saved to file")

cli.add_command(gettree)
cli.add_command(getmatrix)
cli.add_command(kmers_count)
if __name__ == '__main__':
    cli()
