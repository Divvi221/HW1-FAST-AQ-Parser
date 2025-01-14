# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    #create an instance of the FastaParser class
    parse = FastaParser('data/test.fa')
    records = [record for record in parse]
    assert len(records) == 100 #100 tuples/sequences, check that all sequences are read
    assert records[0][1] == ("TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA") #check that sequence (second entry of the first tuple) is correct 
    assert records[1][1] == ("TCCGCCCGCTGTGCTGACGAGACTAGCAGGGAAATAAATAGAGGGTTTAGTTATACTCAGTAGGCAGTTCGATGGCTTATATCTAACTTCTTATTCCGAT") #check that sequence (second entry of the second tuple) is correct 

def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    with pytest.raises(ValueError):
        next(iter(FastaParser("tests/bad.fa"))) 

    with pytest.raises(ValueError):
        next(iter(FastaParser("tests/blank.fa")))

    assert next(iter(FastaParser("data/test.fq")))[0] == None #if it is a fastq file, first line == None
    assert next(iter(FastaParser("data/test.fa")))[0] != None #should not be an error if it is reading the correct file


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    parse = FastqParser('data/test.fq')
    records = [record for record in parse]
    assert records[0][1] == 'TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG' #check that the second entry of the tuple is as expected
    assert records[0][0] == 'seq0' #first entry of the first tuple
    assert records[0][2] == '*540($=*,=.062565,2>\'487\')!:&&6=,6,*7>:&132&83*8(58&59>\'8!;28<94,0*;*.94**:9+7"94(>7=\'(!5"2/!%"4#32=' #third entry of the first tuple

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    assert next(iter(FastqParser("data/test.fa")))[0] == None #assert that first entry is None if a .fa file is used
    assert next(iter(FastqParser("data/test.fq")))[0] != None #no error if the file is correct