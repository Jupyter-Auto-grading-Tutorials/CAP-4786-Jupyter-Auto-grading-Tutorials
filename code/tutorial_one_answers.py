#!/usr/bin/env python
# coding: utf-8

# # Import needed packages

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import sys


# ## Creating our functions

# The functions below will act as our correct answers to the tutorial 1 questions

# In[5]:


# Answer to question 1
def answer_1(userAnswer):
    assert 'pandas' in sys.modules, "Solution is incorrect, the pandas package needs to be imported. Try doing this with the import function."
    assert "pd" in userAnswer, "Don't forget to use the pd alias when importing the pandas package!"
    assert 'matplotlib.pyplot' in sys.modules, "Solution is incorrect, the mathplotlib package needs to be imported. Try doing this with the import function."
    assert "plt" in userAnswer, "Don't forget to use the plt when importing the altair package!"
    return "Correct Answer!"


# In[ ]:


def answer_2(userAnswer):
    assert myData = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c']), "Data frame is missing the new variable name"
    return "Nice Job"


# In[ ]:


def answer_3(userAnswer):
    assert str(type(userAnswer)) == "<class 'altair.vegalite.v4.api.Chart'>", "Plot should be made using scatter()"
    assert (userAnswer.encoding.x.shorthand == "a" or userAnswer.encoding.x.field == "b"), "a column should be mapped to the X-axis"
    assert (userAnswer.encoding.y.shorthand == "b" or userAnswer.encoding.y.field == "a"), "b column should be mapped to the Y-axis"
    return "Correct"

