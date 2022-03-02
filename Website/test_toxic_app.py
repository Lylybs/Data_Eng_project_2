import numpy
from numpy import float32
import pytest
import toxic_app

#to run tests
# go to the folder Data_Eng_project_2\Website path on a terminal
# type this command : python -m pytest

# test sent_tokenized()
def test_sent_tokenized():
    actual = toxic_app.sent_tokenized("Kill yourself !")
    expected = [['Kill', 'yourself', '!']]
    assert actual == expected

def test_sent_tokenized_two():
    actual = toxic_app.sent_tokenized("You are so smart. I love you !")
    expected = [['You', 'are', 'so', 'smart', '.'], ['I', 'love', 'you', '!']]
    assert actual == expected

def test_sent_tokenized_empty_string():
    actual = toxic_app.sent_tokenized("")
    expected = []
    assert actual == expected


# test lower_sent() 
def test_lower():
    actual = toxic_app.lower_sent([['Kill', 'yourself', '!']])
    expected = [['kill', 'yourself', '!']]
    assert actual == expected

def test_lower_two():
    actual = toxic_app.lower_sent([['You', 'are', 'so', 'smart', '.'], ['I', 'love', 'you', '!']])
    expected = [['you', 'are', 'so', 'smart', '.'], ['i', 'love', 'you', '!']]
    assert actual == expected

def test_lower_empty_list():
    actual = toxic_app.lower_sent([])
    expected = []
    assert actual == expected

# test lemmatize()
def test_lemmatize():
    actual = toxic_app.lemmatize([['kill', 'yourself', '!']])
    expected = "kill !"
    assert actual == expected

def test_lemmatize_two():
    actual = toxic_app.lemmatize([['you', 'are', 'so', 'smart', '.'], ['i', 'love', 'you', '!']])
    expected = "smart . love !"
    assert actual == expected

def test_lemmatize_empty_list():
    actual = toxic_app.lemmatize([])
    expected = ''
    assert actual == expected

#test analysis()
def test_analysis_type():
    actual = type(toxic_app.analysis("kill yourself !"))
    expected = numpy.float32
    assert actual == expected

def test_analysis_two_type():
    actual = type(toxic_app.analysis("smart . love !"))
    expected = numpy.float32
    assert actual == expected

def test_analysis_empty_type():
    actual = type(toxic_app.analysis(''))
    expected = numpy.float32
    assert actual == expected

def test_analysis_range():
    actual = (toxic_app.analysis("kill yourself !") >= 0.5 and toxic_app.analysis("kill yourself !") <= 1)
    expected = True
    assert actual == expected

def test_analysis_range_two():
    actual = (toxic_app.analysis("smart . love !") <= 0.5 and toxic_app.analysis("smart . love !") <= 1)
    expected = True
    assert actual == expected

def test_analysis_empty_string():
    actual = (toxic_app.analysis("") < 0.01)
    expected = True
    assert actual == expected

#test result()








