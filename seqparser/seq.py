# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    output = ""
    for i in seq:
        if i in ALLOWED_NUC:
            output+=TRANSCRIPTION_MAPPING[i]
    return output


def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    output = ""
    #REVERSE_TRANSCRIPTION = {v: k for k, v in TRANSCRIPTION_MAPPING.items()}
    #for i in seq:
    #    if i in REVERSE_TRANSCRIPTION.keys():
    #        output+=REVERSE_TRANSCRIPTION[i]
    for i in seq:
        if i in ALLOWED_NUC:
            output+=TRANSCRIPTION_MAPPING[i]
    return output[::-1]
