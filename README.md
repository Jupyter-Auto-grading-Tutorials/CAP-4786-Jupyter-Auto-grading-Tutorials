# Jupyter Auto Grading Tutorials
Topics in Big Data Project 1 is to create a series of python jupyter notebook data analytics tutorials that give auto-feedback and record event. For example, the tutorial will first show students how to produce a bar graph in a jupyter notebook, and then evaluate if the student completed the task and record the score.

## The following is a list of the different tutorial sets we will cover
- Tutorial 1: Intro to Pandas <br /> 
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

- Tutorial 2: Data Visualization <br />
     - Basic Plotting with Matplotlib
          - Include titles, axes labels, and color-coding
          - Seaborn Plots
          - Scatter plot
          - Line plots
          - Bar graphs
          - Histograms

- Tutorial 3: Data Transformation <br />
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

- Tutorial 4: Data Analytics <br />
     - Correlation
     - Linear Regression and measuring error
          - Display the model's formula
          - Visualize the regression with a scatter + line plot
     - Decision Trees and measuring accuracy
          - Visualize the tree

Each Tutorial Set will include a **Lesson Worksheet**, a **Practice Exercise set**, and a **Quiz**

## Steps for Running Tutorials with nbgrader
The first thing we need to do to acces these tutorials is to set up the nbgrader
1. Install nbgrader 
     - For command prompt: `pip install nbgrader`
2. Open Jupyter Notebooks
3. Open the **Formgrader** Interface at the top of the Jupyter Notebooks
4. Create your course
5. Create/add students ids in database 
6. Create assignments
     - nbgrader will add an assignment folder to your hardware, where you can add the assignments students must complete
7. Autograde assignments

For questions about nbgrader and how to install it please refer to the following link: [nbgrader Resource Page](https://nbgrader.readthedocs.io/en/stable/).
