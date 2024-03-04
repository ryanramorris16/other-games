# Other Games

Other games is a collection of scripts to recreate various puzzles and simple games.

## sudoku_gen.py

Sudoku_gen.py is a script to generate a valid sudoku solution givena board state. This could be an empty board or solving a sudoku. Work in progress to remove numbers from the solution to create difficulty levels for various sudoku solutions.

## sudoku_interactable.py

Pygame script to create a sudoku board with a reset button to clear all of the numbers off the board. Work in progress to add a solve functionality and new board functionality from sudoku_gen.py

## To-Do

- sudoku_gen: optimize time to check if sudoku only has one valid solution after removing a digit
- sudoku_interactable: add call to sudoku_gen to populate the board when pressing "new" button
- sudoku_interactable: add call to sudoku_gen to solve the board given the current state of it
- sudoku_interactable: add call to sudoku_gen when board is full to check if board state matches correct solution