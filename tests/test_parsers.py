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
    
    blank_fa="tests/blank.fa"
    blank_parse = FastaParser(blank_fa)
    # with pytest.raises(ValueError):
    with pytest.raises(ValueError):
        for seq in blank_parse:
            break

    bad_fa="tests/bad.fa"
    bad_parse = FastaParser(bad_fa)
    # with pytest.raises(ValueError):
    with pytest.raises(ValueError):
        for seq in bad_parse:
            break
    


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """

    # with pytest.raises(ValueError):
    #     FastaParser('data/test.fq')
    # assert ValueError

    # FastaParser('data/test.fa')
    # assert ValueError

    test_fq = 'data/test.fq'
    test_fq_parse = FastaParser(test_fq)
    for seq in test_fq_parse:
        assert seq[0] is None
        break

    test_fa = 'data/test.fa'
    test_fa_parse = FastaParser(test_fa)
    for seq in test_fa_parse:
        assert len(seq[0])>0
        assert len(seq[1])>0
        assert isinstance(seq[0], str) == 1
        assert isinstance(seq[1], str) == 1
        assert all(char in "ATCG" for char in seq[1]) == 1
        

    

def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    blank_fq="tests/blank.fq"
    blank_parse = FastqParser(blank_fq)
    # with pytest.raises(ValueError):
    with pytest.raises(ValueError):
        for seq in blank_parse:
            break

    bad_fq="tests/bad.fq"
    bad_parse = FastaParser(bad_fq)
    # with pytest.raises(ValueError):
    for seq in bad_parse:
        assert seq[0] is None
    

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    #wrong parse: use fastq parse fasta
    test_fa = 'data/test.fa'
    test_fa_parse = FastqParser(test_fa)
    for seq in test_fa_parse:
        assert seq[0] is None
        break

    test_fq = 'data/test.fq'
    test_fq_parse = FastqParser(test_fq)
    for seq in test_fq_parse:
        assert len(seq)==3
        assert len(seq[1])>0
        assert seq[0].isalpha() == 0
        assert isinstance(seq[1], str) == 1
        assert all(char in "ATCG" for char in seq[1]) == 1