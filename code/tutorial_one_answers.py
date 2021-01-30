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
    assert 'pandas' in sys.modules, "Sorry that's incorrect, you need to import pandas, please check you are using the correct import function."
    assert "pd" in userAnswer, "Watch out! Check that you are using the abbriviation pd when importing the pandas."
    assert 'matplotlib.pyplot' in sys.modules, "Sorry that's incorrect, you need to import pandas, please check you are using the correct import function."
    assert "plt" in userAnswer, "Watch out! Check that you are using the abbriviation plt when importing the matplotlib.pyplot."
    return "Correct Answer!"


# In[ ]:


def answer_2(userAnswer):
    assert myData = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c']), "Data frame is missing the new variable name"
    return "Nice Job"


# In[ ]:


def answer_3(userAnswer):
    return "Correct"

