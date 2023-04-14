from munkres import Munkres, DISALLOWED
import json
import pandas as pd
import numpy as np
import sys

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Usage: python magouilleuse_science_po.py <input_file>")
        sys.exit(1)
    
    file_name = sys.argv[1]

    # Load data 
    matching = pd.read_csv(file_name, index_col=0, sep=';') # cols = [time slot, course name, student name, student course choice rank]] 
    matching.replace(-1, DISALLOWED, inplace=True)
    matching.fillna(DISALLOWED, inplace=True)

    slots = matching['time_slot'].unique()

    student_names = list(matching['student_name'].unique())
    cur_weights = np.zeros(len(student_names))

    # For each time slot, we compute the matching
    # Possibly shuffle the slots to avoid bias

    for slot in slots:
        print("Slot: ", slot)
        matching_slot = matching[matching['time_slot'] == slot]
        
        n_students = matching_slot['student_name'].nunique()
        n_courses = matching_slot['course_name'].nunique()

        course_names = list(matching_slot['course_name'].unique())

        # Create the matrix
        # Duplicating courses to take into account multi course
        matrix = np.zeros((n_students, n_courses*n_students)) + np.inf

        for i, row in matching_slot.iterrows():
            student_name = row['student_name']
            course_name = row['course_name']
            rank = row['rank']
            course_id = course_names.index(course_name)
            matrix[student_names.index(student_name), course_id*n_students: course_id*n_students+n_students] = rank + cur_weights[student_names.index(student_name)]
        
        m = Munkres()
        indexes = m.compute(matrix)

        for id_student, id_course in indexes:
            id_course //= n_students
            print(student_names[id_student], " -> ",  course_names[id_course])
            cur_weights[id_student] += matrix[id_student, id_course]
        
        print("")
        
