# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    output = "" #initialize output string
    for i in seq:
        if i in ALLOWED_NUC:
            output+=TRANSCRIPTION_MAPPING[i] #if i is an allowed nucleotide, append its RNA mapping to the output
        else:
            print("These nucleotides are not in the list of allowed nucleotides.")
    return output


def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    output = "" #initialize output string
    for i in seq:
        if i in ALLOWED_NUC:
            output+=TRANSCRIPTION_MAPPING[i] #if i is an allowed nucleotide, append its RNA mapping to the output
        else:
            print("These nucleotides are not in the list of allowed nucleotides.") 
    return output[::-1] #return the reverse of the transcription output
