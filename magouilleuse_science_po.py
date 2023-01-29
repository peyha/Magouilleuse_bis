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
    matching = pd.read_csv(file_name, index_col=0, sep=';')
    matching.replace(-1, DISALLOWED, inplace=True)
    matching.fillna(DISALLOWED, inplace=True)
    student_names = matching.index
    course_names = matching.columns

    matrix = matching.values.tolist()

    m = Munkres()
    indexes = m.compute(matrix)

    for id_student, id_course in indexes:
        print(student_names[id_student], " -> ",  course_names[id_course])
