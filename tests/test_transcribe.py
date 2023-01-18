# write tests for transcribes
import pytest
from seqparser import transcribe, reverse_transcribe

SEQ = "ACTGAACCC"


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
    Write your unit test for the
    transcribe function here.
    """
    # Ensure that sequences are properly transcribed.
    assert transcribe(SEQ) == 'UGACUUGGG', 'Transcription module error.'


def test_reverse_transcribe():
    """
    Write your unit test for the
    reverse transcribe function here.
    """
    # Ensure that sequences are properly reverse_transcribed.
    assert reverse_transcribe(SEQ) == 'GGGUUCAGU', 'Reverse transcription module error.'