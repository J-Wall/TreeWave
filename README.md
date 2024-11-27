# TreeWave
TreeWave is an open-source, user-friendly command line tool designed for alignment-free phylogeny reconstruction. It leverages the Frequency Chaos Game Representation (FCGR) to transform genomic sequences into a frequency matrix. Subsequently, TreeWave employs the Discrete Wavelet Transform (DWT) to perform genomic signal processing. TreeWave takes as input a multi-fasta file and returns resulting dendrogram as a newick file. 

If you use TreeWave in your research, please cite the following paper : 

Boumajdi, N., Bendani, H., Belyamani, L. et al. TreeWave: command line tool for alignment-free phylogeny reconstruction based on graphical representation of DNA sequences and genomic signal processing. BMC Bioinformatics 25, 367 (2024). https://doi.org/10.1186/s12859-024-05992-3

**TreeWave is designed to be compatible with macOS and Linux operating systems.**
## Features
### Basic features
- Import a multi-fasta file of any genome type and get a phylogenetic tree as a newick file.
- Import a multi-fasta file and get the cosine distance matrix as a CSV file. 
### Additional features 
- Import a fasta file of one genome and get the distributions of possible and distinct kmers among a specific range of k. 

## Requirements 
- Python 3.6 or higher
- pip (Python package installer)
- virtualenv (you can install it using pip install virtualenv if you don't have it)
## Installation
To install TreeWave, it is recommended to create and activate a virtual environment. This helps manage dependencies and avoid conflicts with other packages.
1.	Clone the repository or download compressed source code files and navigate to the folder TreeWave

```sh
git clone https://github.com/nasmaB/TreeWave.git
cd TreeWave 
```
2.	Open your terminal/Command Prompt, create virtual environment treewave_venv and activate it 
```sh
virtualenv treewave_venv 
source treewave_venv/bin/activate 
```
3. TreeWave installation using pip. Execute the following command in the root of TreeWave folder 
```sh
pip install -e . 
```
## Using TreeWave
To get an overview of the available commands and options in TreeWave, you can use the --help flag.
```sh
treewave --help
```
### Basic usage 
To use TreeWave for alignment-free phylogenetic tree inference, run the following command:
```sh
treewave gettree -k [KMER_LENGTH] [INPUTFILE] [OUTPUTFILE]
```
Replace [KMER_LENGTH] with the desired k-mer length, [INPUT_FILE] with the path to the multi-FASTA file containing genomic sequences, and [OUTPUT_FILE] with the desired path for the Newick output file.

**Example** : Phylogenetic tree inference of whole human mitochondrial genomes with k=9. Multi fasta file is under DATA folder. 
```sh
treewave gettree -k 9 Data/Human_MtDna/mtdna.fasta tree.nwk
```
### Suggested Visualization Tools for Newick Files
After running the provided command lines, you will obtain the phylogenetic trees as a Newick files. To visualize these Newick files, you can use one of the following tools:
-  FigTree : http://tree.bio.ed.ac.uk/software/figtree/
- iTOL (Interactive Tree of Life) : https://itol.embl.de/
- Phylo.io : https://phylo.io/

### Other usages
- **Generate cosine distance matrix from multi-fasta file**
```sh
treewave getmatrix -k [KMER_LENGTH] [INPUTFILE] [OUTPUTFILE]
```
Replace [KMER_LENGTH] with the desired k-mer length, [INPUT_FILE] with the path to the multi-FASTA file containing genomic sequences, and [OUTPUT_FILE] with the desired path for the csv output file containing the resulting cosine matrix.

- **Possible and distinct K-mers distribution among a genome for a range of k**
```sh
treewave getkmers [GENOME.FASTA] -kmin [KMIN] -kmax [KMAX] [OUTPUTFILE]
```
This command generates a csv file containing the number of total and distinct kmers among genome.fasta for each k in the range [KMIN,KMAX]
## License
This project is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html) - see the [*LICENSE*](LICENSE) file for details.

