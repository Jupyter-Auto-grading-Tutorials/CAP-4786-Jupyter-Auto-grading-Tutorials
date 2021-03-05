## Author Kelly Rivera

# Import needed packages
import pandas as pd
import matplotlib.pyplot as plt
import sys


## Creating our functions

# The functions below will act as our correct answers to the tutorial 1 questions

# Answer to question 1
def answer_1(userAnswer):
    assert 'pandas' in sys.modules, "Sorry that's incorrect, you need to import pandas, please check you are using the correct import function."
    assert "pd" in userAnswer, "Watch out! Check that you are using the abbriviation pd when importing the pandas."
    assert 'matplotlib.pyplot' in sys.modules, "Sorry that's incorrect, you need to import pandas, please check you are using the correct import function."
    assert "plt" in userAnswer, "Watch out! Check that you are using the abbriviation plt when importing the matplotlib.pyplot."
    return "Correct Answer!"


# Answer to question 2
def answer_2(userAnswer):
    assert isinstance(userAnswer, type(pd.DataFrame())), str(userAnswer) + "should be a pandas dataframe"
    assert len(userAnswer) == 3, "Number of rows in the dataframe should be 3"
    assert len(userAnswer.columns) == 2, "Number of columns in the dataframe should be 2."
    assert sorted(list(userAnswer.columns.values)) == ['a', 'b'], "The column names should be a and b."
    
    return "Nice Job"


# Answer to question 3
def answer_3(userAnswer):
    assert isinstance(userAnswer, type(pd.DataFrame())), str(userAnswer) + "should be a pandas dataframe"
    assert len(userAnswer.columns) == 5, "Number of columns should be 5."
    assert sorted(list(userAnswer.columns.values)) == ['carat', 'cut', 'clarity', 'depth', 'price'], "The column names should be carat, cut, clarity, depth, price."
    
    return "Great Job"

# Answer to question 4
def answer_4(userAnswer):
    return "Correct"



