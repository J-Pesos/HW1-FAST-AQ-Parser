# write tests for parsers

from seqparser import (
    FastaParser,
    FastqParser,
)

import pathlib
import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2


def get_filepath(which):
    data_dir = pathlib.Path(__file__).resolve().parent.parent / "data"
    if which == "fasta":
        return data_dir / "test.fa"
    else:
        return data_dir / "test.fq"


def open_fastq_reference():
    f = pathlib.Path(__file__).resolve().parent / "fastq-check.txt"
    with f.open() as f:
        seqs = list(map(lambda l: l.strip().split("|"), f.readlines()))
    return seqs  # will be list of lists with seq, quality that were parsed from the test files using get-seq.sh


def open_fasta_reference():
    f = pathlib.Path(__file__).resolve().parent / "fasta-check.txt"
    with f.open() as f:
        seqs = list(map(lambda l: l.strip(), f.readlines()))
    return seqs  # will be a list of seqs, quality that were parsed from the test files using get-seq.sh


def test_FastaParser():
    """
    Write your unit test for your FastaParser
    class here. You should generate an instance of
    your FastaParser class and assert that it properly
    reads in the example Fasta File.
    """
    # Parse fasta file and store sequence entries line by line
    fasta = 'data/test.fa'
    parsed_fasta = FastaParser(fasta)
    file_lines = [sequence for sequence in parsed_fasta]

    # Ensure sequence0 is matched and that first part of tuple is seq string.
    seq0 = 'TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA'
    assert file_lines[0][0][0:3] == 'seq', 'Error, not a FastA file.' 
    assert file_lines[0][1] == seq0, 'Error, sequence does not match input file.'


def test_FastqParser():
    """
    Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """
    # Parse fastq file and store sequence entries line by line
    fastq = 'data/test.fq'
    parsed_fastq = FastqParser(fastq)
    file_lines = [sequence for sequence in parsed_fastq]
    
    # Ensure sequence0 and quality0 are matched and that first part of tuple is seq string.
    seq0 = 'TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG'
    qual0 = '*540($=*,=.062565,2>\'487\')!:&&6=,6,*7>:&132&83*8(58&59>\'8!;28<94,0*;*.94**:9+7"94(>7=\'(!5"2/!%"4#32='
    assert file_lines[0][0][0:3] == 'seq', 'Error, not a FastQ file.'
    assert file_lines[0][1] == seq0, 'Error, sequence does not match input file.'
    assert file_lines[0][2] == qual0, 'Error, quality does not match input file.'