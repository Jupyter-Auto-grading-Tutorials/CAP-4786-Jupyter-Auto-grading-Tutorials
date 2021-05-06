# Jupyter Auto Grading Tutorials
Topics in Big Data Project 1 is to create a series of python jupyter notebook data analytics tutorials that give auto-feedback and record event. For example, the tutorial will first show students how to produce a bar graph in a jupyter notebook, and then evaluate if the student completed the task and record the score.

### The following is a list of the different tutorial sets we will cover
- Tutorial 1: Intro to Pandas
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

- Tutorial 2: Data Visualization
This tutorial will include the following subjects listed below:

- Basic Plotting with Matplotlib
     • Include titles, axes labels, and color-coding
- Seaborn Plots
     • Scatter plot
     • Line plots
     • Bar graphs
     • Histograms
     • Include titles, axes labels, and color-coding

- Tutorial 3: Data Transformation
This tutorial will teach students the following topics:

- Subsetting/Slicing
      • Based on conditions (loc)
      • Based on row number (iloc)
      • Return data frames with a subset of columns df[["mpg", "disp", "wt"]]
- Removing NAs: dropna()
- Sorting
- Groupby
- Agg
- Concat
- join and merge

- Tutorial 4: Data Analytics

The last tutorial for the project. It will teach students the following topics:

- Correlation
- Linear Regression and measuring error
        • Display the model's formula
        • Visualize the regression with a scatter + line plot
- Decision Trees and measuring accuracy
        •Visualize the tree

Each of the tutorial sets will include the a teaching worksheet, exercise set, and quiz
We impletmented NbGrader with our Quiz 1 successfully.

The first thing we need to do to acces these tutorials is to set up the nbgrader
Step 1: Install nbgrader (preferably ina virtual environment)

Step 2: Create your course

Step 3: Automatically add students ids in database 

Step 4: Create an assignment

Step 5: Autograde assignments
