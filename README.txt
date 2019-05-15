To run type:
py hw4.py [file of input] [file to output to]
Example:
py hw4.py board.txt output.txt

File constraints:
The file should be 9 lines long each with 9 integers seperated by spaces.
Zeros represent a blank space in the sudoku board.
Example input:
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9

Output file:
The solution to the sudoku board will be written to the output file if there is a solution.
If there is no solution, nothing will be written to the file.
The output will be similarly formated to the input file, but without zeros since its a solution.
Example output:
5 3 2 6 7 8 9 1 4 
6 4 7 1 9 5 3 2 8 
1 9 8 2 3 4 5 6 7 
8 1 9 7 6 4 4 5 3 
4 2 6 8 5 3 7 9 1 
7 5 3 9 2 1 8 4 6 
3 6 1 5 5 7 2 8 4 
2 8 7 4 1 9 6 3 5 
2 5 4 3 8 6 1 7 9 

Example run:
py hw4.py board.txt out.txt


Initial Board
-------------

5 3 0 | 0 7 0 | 0 0 0
6 0 0 | 1 9 5 | 0 0 0
0 9 8 | 0 0 0 | 0 6 0
---------------------
8 0 0 | 0 6 0 | 0 0 3
4 0 0 | 8 0 3 | 0 0 1
7 0 0 | 0 2 0 | 0 0 6
---------------------
0 6 0 | 0 0 0 | 2 8 0
0 0 0 | 4 1 9 | 0 0 5
0 0 0 | 0 8 0 | 0 7 9


There is a solution
-------------------

5 3 2 | 6 7 8 | 9 1 4
6 4 7 | 1 9 5 | 3 2 8
1 9 8 | 2 3 4 | 5 6 7
---------------------
8 1 9 | 7 6 4 | 4 5 3
4 2 6 | 8 5 3 | 7 9 1
7 5 3 | 9 2 1 | 8 4 6
---------------------
3 6 1 | 5 5 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
2 5 4 | 3 8 6 | 1 7 9