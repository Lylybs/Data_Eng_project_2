import numpy
from numpy import float32
import pytest
import website.toxic_app as ta

#to run tests
# go to the folder Data_Eng_project_2 path on a terminal
# type this command : pytest


# test sent_tokenized()
def test_sent_tokenized():
    actual = ta.sent_tokenized("Kill yourself !")
    expected = [['Kill', 'yourself', '!']]
    assert actual == expected

def test_sent_tokenized_two():
    actual = ta.sent_tokenized("You are so smart. I love you !")
    expected = [['You', 'are', 'so', 'smart', '.'], ['I', 'love', 'you', '!']]
    assert actual == expected

def test_sent_tokenized_empty_string():
    actual = ta.sent_tokenized("")
    expected = []
    assert actual == expected


# test lower_sent() 
def test_lower():
    actual = ta.lower_sent([['Kill', 'yourself', '!']])
    expected = [['kill', 'yourself', '!']]
    assert actual == expected

def test_lower_two():
    actual = ta.lower_sent([['You', 'are', 'so', 'smart', '.'], ['I', 'love', 'you', '!']])
    expected = [['you', 'are', 'so', 'smart', '.'], ['i', 'love', 'you', '!']]
    assert actual == expected

def test_lower_empty_list():
    actual = ta.lower_sent([])
    expected = []
    assert actual == expected

# test lemmatize()
def test_lemmatize():
    actual = ta.lemmatize([['kill', 'yourself', '!']])
    expected = "kill !"
    assert actual == expected

def test_lemmatize_two():
    actual = ta.lemmatize([['you', 'are', 'so', 'smart', '.'], ['i', 'love', 'you', '!']])
    expected = "smart . love !"
    assert actual == expected

def test_lemmatize_empty_list():
    actual = ta.lemmatize([])
    expected = ''
    assert actual == expected

#test analysis()
def test_analysis():
    actualRes,actualStat = ta.analysis("kill yourself !")
    assert actualRes == "toxic"

def test_analysis_two_type():
    actualRes,actualStat = ta.analysis("smart . love !")
    assert actualRes == "not toxic"

def test_analysis_empty_type():
    actualRes,actualStat = ta.analysis('')
    assert actualRes == "not toxic"


