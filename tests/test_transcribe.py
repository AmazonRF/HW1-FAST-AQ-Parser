# write tests for transcribe functions

from seqparser import (
        transcribe,
        reverse_transcribe)

from seqparser import (
        FastaParser,
        FastqParser)



def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    seq = "TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA"
    assert transcribe(seq, False) == "ACUAACUUAGAAAACUCCCAGUGCCGGGCCUUCGGUCUUAAAGCCCCAGGAGACACCUAUAAUUAGCUCGGGUGUGCCACACUCAAGUCGCCGGGGGCGU"

    parseseq = FastaParser('data/test.fa')
    for seq in parseseq:
        assert transcribe(seq[1], False) == "ACUAACUUAGAAAACUCCCAGUGCCGGGCCUUCGGUCUUAAAGCCCCAGGAGACACCUAUAAUUAGCUCGGGUGUGCCACACUCAAGUCGCCGGGGGCGU"
        break
    


def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    seq = "TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA"
    assert transcribe(seq, True) == "UGCGGGGGCCGCUGAACUCACACCGUGUGGGCUCGAUUAAUAUCCACAGAGGACCCCGAAAUUCUGGCUUCCGGGCCGUGACCCUCAAAAGAUUCAAUCA"
    assert reverse_transcribe(seq) == "UGCGGGGGCCGCUGAACUCACACCGUGUGGGCUCGAUUAAUAUCCACAGAGGACCCCGAAAUUCUGGCUUCCGGGCCGUGACCCUCAAAAGAUUCAAUCA"
    
    parseseq = FastaParser('data/test.fa')
    for seq in parseseq:
        assert transcribe(seq[1], True) == "UGCGGGGGCCGCUGAACUCACACCGUGUGGGCUCGAUUAAUAUCCACAGAGGACCCCGAAAUUCUGGCUUCCGGGCCGUGACCCUCAAAAGAUUCAAUCA"
        assert reverse_transcribe(seq[1]) == "UGCGGGGGCCGCUGAACUCACACCGUGUGGGCUCGAUUAAUAUCCACAGAGGACCCCGAAAUUCUGGCUUCCGGGCCGUGACCCUCAAAAGAUUCAAUCA"
        break