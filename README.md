
This is a script made in order to run a "magouilleuse", an algorithm to match students with courses when each of them rank them.

To run this script, you will need Python 3 and some packages that you can install with pip by running the command: 

`pip install -r requirements.txt`

You will need a csv file where columns are your courses and lines corresponds to the students.
On each cell, you have the rank of this course for the corresponding student from 1 to n. If the student cannot have this course, it should be -1.

You can then run the algorithm with the command:

`python magouilleuse_science_po.py <csv file path>`

For instance, if we run 

`python magouilleuse_science_po.py choix_cours.csv`

the program prints 

`Jacques  ->  maths1

Louis  ->  anglais1

Jean  ->  physique1

Ulysse  ->  Pipeau1`
