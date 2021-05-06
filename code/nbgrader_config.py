c = get_config()

"""
Begin additions by nbgrader quickstart
##############################################################################
"""

# You only need this if you are running nbgrader on a shared
# server set up.
c.CourseDirectory.course_id = "jupyter-autograding"

# Update this list with other assignments you want
c.CourseDirectory.db_assignments = [
    dict(name = "quiz_1")
    ]

# Change the students in this list with that actual students in
# your course
c.CourseDirectory.db_students = [
    dict(id = "one", first_name = "Kelly", last_name = "Coder"),
    dict(id = "two", first_name = "Matthew", last_name = "Write")
]
