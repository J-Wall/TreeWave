#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 12:11:54 2023

@author: nasmaboumajdi
"""

## mytool 
import click 
from app import application
from app import optimal_k

@click.group()
def cli():
    """TreeWave: An alignment-free approach for phylogeny reconstruction based on Frequency Chaos Game Representation and Discrete Wavelet Transform."""
    pass

@cli.command()
@click.option('-k', '--klength', type=int, required=True, help='K-mer length')
@click.argument('inputfile', type=click.Path(exists=True))
@click.argument('outputfile', type=click.Path())
def gettree(klength, inputfile, outputfile):
    """Alignment-free phylogenetic tree inference"""
    application.generate_newick_from_fasta(klength, inputfile, outputfile)
    click.echo(f"Newick file created at {outputfile}")

@cli.command()
@click.option('k', '--klength', type=int, required=True, help='K-mer length')
@click.argument('inputfile', type=click.Path(exists=True))
@click.argument('outputfile', type=click.Path())
def getmatrix(klength, inputfile, outputfile):
    """Cosine distance matrix computation"""
    application.get_matrix_from_fasta(klength, inputfile, outputfile)
    click.echo(f"Distance matrix created at {outputfile}")


@cli.command()
@click.argument('genome', type=click.Path(exists=True))
@click.option('--kmin', '-kmin', type=int, required=True, help='The minimum K-mer length')
@click.option('--kmax', '-kmax', type=int, required=True, help='The maximum K-mer length')
@click.argument('outputfile', type=click.Path())
def getkmers(genome, kmin, kmax, outputfile):
    """Counts of possible kmers and distinct kmers among a genome for a specific Kmer range"""
    optimal_k.count_kmers_in_range(genome,kmin,kmax,outputfile)
    click.echo("Kmers distribution calculated and saved to file")
    click.echo(f"Total, unique, and distinct kmers are counted within the provided range for k. Results are saved to {outputfile}")

cli.add_command(gettree)
cli.add_command(getmatrix)
cli.add_command(getkmers)
if __name__ == '__main__':
    cli()
