# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    #here is my code:
    rna_seq = ""    #here store the result
    for nucleotide in seq:
        rna_seq += TRANSCRIPTION_MAPPING.get(nucleotide, "")
    return rna_seq

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    #here is my code:
    rna_seq = ""    #here store the result
    for nucleotide in seq:
        rna_seq += TRANSCRIPTION_MAPPING.get(nucleotide, "")
    return rna_seq[::-1]