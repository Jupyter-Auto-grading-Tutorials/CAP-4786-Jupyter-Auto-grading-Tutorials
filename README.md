# Jupyter Auto Grading Tutorials
#### Project Description
This project is a series of python jupyter notebook data analytics tutorials that give auto-feedback and record event. For example, the tutorial will first show students how to produce a bar graph in a jupyter notebook, and then evaluate if the student completed the task and record the score.

#### Goals & Motivations
To teach individuals a basic understanding of python and how to utilize it. We wanted to build four tutorial series that each include a teaching lesson, practice exercises, and a quiz. We completed all four teaching lessons, quizzes, and their corresponding answer sheets, all run with no bugs. The practice exercise questions are complete but the corresponding answer sheets need to be worked on. This project was done so that anyone wishing to learn the basics of python can do so easily.


## The following is a list of the different tutorial sets we cover
Each Tutorial Set includes a **Lesson Worksheet**, **Practice Exercises**, and a **Quiz**
- **Tutorial 1: Intro to Pandas** <br /> 
This tutorial will consist of the following subjects:
     - Create a data frame from scratch
     - Import a data frame from file
     - Explain what an index is vs. a column
     - Data Frame describe() function
     - Colum calculations: mean, count, sd
     - Add columns and rows
     - Add new columns based on calculations and based on other columns
     - Rename and Delete columns
     - Save a data frame to file

<img src="https://github.com/Jupyter-Auto-grading-Tutorials/CAP-4786-Jupyter-Auto-grading-Tutorials/blob/main/images/Lesson1.PNG" height="400">

- **Tutorial 2: Data Visualization** <br />
     - Basic Plotting with Matplotlib
          - Include titles, axes labels, and color-coding
          - Seaborn Plots
          - Scatter plot
          - Line plots
          - Bar graphs
          - Histograms

- **Tutorial 3: Data Transformation** <br />
     - Subsetting/Slicing
          - Based on conditions (loc)
          - Based on row number (iloc)
          - Return data frames with a subset of columns df[["mpg", "disp", "wt"]]
     - Removing NAs: dropna()
     - Sorting
     - Groupby
     - Agg
     - Concat
     - join and merge

<img src="https://github.com/Jupyter-Auto-grading-Tutorials/CAP-4786-Jupyter-Auto-grading-Tutorials/blob/main/images/Quiz3.PNG" height="400">

- **Tutorial 4: Data Analytics** <br />
     - Correlation
     - Linear Regression and measuring error
          - Display the model's formula
          - Visualize the regression with a scatter + line plot
     - Decision Trees and measuring accuracy
          - Visualize the tree


## Steps for Running Tutorials with nbgrader
The first thing we need to do to acces these tutorials is to set up the nbgrader
1. Install nbgrader 
     - For command prompt: `pip install nbgrader`
2. Open Jupyter Notebooks
3. Open the **Formgrader** Interface at the top of the Jupyter Notebooks

<img src="https://github.com/Jupyter-Auto-grading-Tutorials/CAP-4786-Jupyter-Auto-grading-Tutorials/blob/main/images/nbgraderTerminal.PNG" height="300">

5. Create your course
6. Create/add students ids in database 
7. Create assignments
     - nbgrader will add an assignment folder to your hardware, where you can add the assignments students must complete

<img src="https://github.com/Jupyter-Auto-grading-Tutorials/CAP-4786-Jupyter-Auto-grading-Tutorials/blob/main/images/Formgrader.PNG" height="250">

8. Autograde assignments

For questions about nbgrader and how to install it please refer to the following link: [nbgrader Resource Page](https://nbgrader.readthedocs.io/en/stable/).

## Software versions 
- Python 3
- Jupyter Notebooks
- Chrome 
- Libraries
     - Matplotlib
     - Pandas
     - Numpy

### Project Engineers
Kelly Rivera & Matthew Montada
### Professor
Dr. Sean Mondesire
