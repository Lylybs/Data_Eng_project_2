import numpy
from numpy import float32
import pytest
import Website.toxic_app as ta
from conftest import client


def test_should_status_code_ok(client):

    response = ta.test_client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the" in response.data
    assert b"Flask User Management Example!" in response.data
    assert b"Need an account?" in response.data
    assert b"Existing user?" in response.data


#to run tests
# go to the folder Data_Eng_project_2\Website path on a terminal
# type this command : python -m pytest

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
def test_analysis_type():
    actual = type(ta.analysis("kill yourself !"))
    expected = numpy.float32
    assert actual == expected

def test_analysis_two_type():
    actual = type(ta.analysis("smart . love !"))
    expected = numpy.float32
    assert actual == expected

def test_analysis_empty_type():
    actual = type(ta.analysis(''))
    expected = numpy.float32
    assert actual == expected

def test_analysis_range():
    actual = (ta.analysis("kill yourself !") >= 0.5 and ta.analysis("kill yourself !") <= 1)
    expected = True
    assert actual == expected

def test_analysis_range_two():
    actual = (ta.analysis("smart . love !") <= 0.5 and ta.analysis("smart . love !") <= 1)
    expected = True
    assert actual == expected

def test_analysis_empty_string():
    actual = (ta.analysis("") < 0.01)
    expected = True
    assert actual == expected

#test result()







