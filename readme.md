
# Sudoku Solver

A simple Soduku puzzle solver using : 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

This solver uses the pygame library for a very simple interface that allows us to see the original board and the number added to that board once it is solved. 

For the solving we are using two algorithms, a *Brute-force* algorithm and a *Backtracking* algorithm. 

## Brute-force

The *Brute-force* algorithm uses a very simple principle. It first **reads** the board to find all the empty cells in it, **fills** all the empty cells with random numbers from 1 to 9 and then verifies if the board is **valid** according to the soduku game rules. 

If the board is valid it is then displayed, if it is not valid the board is reset to its original value and another try is attempted. 

I have added a dictionnary that keeps track of all the board tried during the solving process in order to avoid having the same board twice. Having the same board twice would mean that we can try solving a puzzle indefinitely which is not desirable since this algorithm already takes quite some time to solve a simple puzzle. 

## Backtracking

The *Backtracking* algorithm is a bit more complex since it uses both backtracking and recursion. The algorithm first **finds** an empty cell in the board and then begins to try putting numbers in that cell. Once a number has been put in it the algorithm will check if the cell is **valid** or not by checking rows, columns, and then the 3x3 square. 

If the cell is valid, it will move to the next empty cell. If the cell is not valid it will try another number. If the algorithm is stuck in a cell and cannot find a valid number it will use recursion to go back to the previous cell and try a new number it that cell. This way, the algorithm will be able to adapt the number it puts in each cell based on the validity of the current cell. 

## How to use

To use one of the algorithm you simple have to choose between: 

    self.solve_with_brute_force() 
    self.solve_with_backtracking()

By choosing one of these methods in the **sudoku.py** file (line 76) you will be choosing between one of the two algorithms.

You can also choose between one of the sudoku puzzles py inputting one of these :

    sudoku
    sudoku_2
    sudoku_3
    sudoku_4
    evil_sudoku

This can be input in line 101 of the **sudoku.py** file. 

Once the program is launched you can simply click on the **_solve_** button that appears in the pygame window and the puzzle should be solved. 

Please note that if you are using the *Brute-force* algorithm it may take a long time to solve a puzzle, depending on the difficulty and number of empty cells in it. 

## Algorithm Complexity

Here is the algorithms complexity calculated.

|           | Brute-force   | Backtracking |
| :-------: | :-----------: | :----------: |
| Complexity|  O(n^2)       |  O(9^n)      |
||||

We have calculated this complexity based of a few factors.

For the *Brute-force* algorithm we have taken into account:
* read_board; O(n^2)
* fill_board; O(n^2)
* get_available_numbers; O(1)
* is_valid_board; O(n)
* solve_board; O(n^2)
* print_board; O(n^2)

Out of all of these functions the highest algorithm complexity was of **_O(n^2)_**. 
This is because the functions have very basic tasks to execute. They will for example check a row or column but they will only do it once for each function since we are using the check functions on a full board. 

For the *Backtracking* algorithm we have taken into account:
* solve; O(9^n)
* valid; O(1)
* print_board; O(n^2)
* find_empty; O(n^2)

Here it is a bit different because the algorithm is inherently more complex. It uses backtracking and recursive while the *Brute-force* one only uses a very basic backtracking method. 
The complexity was actually quite similar for most of the functions but one, the solve function. Because we have to check each cell with each numbers (ranging from 1 to 9) in the worst case scenario we would have to check all 9 numbers in all empty cells (very unlikely but still possible). Meaning that the complexity can be as high as **_O(n^9)_**.  
<br>

If we check complexity alone we might be inclined to think that the *Brute-force* algorithm is the better one since its complexity is much lower than the *Backtracking* algorithm but, let's check the time of execution of each algorithm before taking a decision. 


## Time of execution
This time of execution has been found after running the algorithms a few times.

Only the first Sudoku puzzle has been added for the time of execution of the *Brute-force* algorithm because after the first puzzle it would have taken 10 minutes + per try depending on your luck and a lot more for the Evil Sudoku. 

Therefore, for finding which algorithm is the faster and more adaptable only the first Sudoku puzzle is necessary if we take a look at the time of execution of the *Backtracking* algorithm

|            | Brute-force   | Backtracking |
| :--------: | :-----------: | :----------: |
| Sudoku     | 0.7 - 32.8s   | 0.003s       |
| Sudoku 2   |       /       | 0.012s       |
| Sudoku 3   |       /       | 0.003s       |
| Sudoku 4   |       /       | 0.06s        |
| Evil Sudoku|       /       | 0.04s        |
||||

As we can see, the *Backtracking* algorithm takes less time than the *Brute-force* algorithm even on the harder puzzle. 
For the first puzzle the fastest time I have gotten with the first algorithm is around **_0.7_** seconds while for the second algorithm the fastest time I have gotten is around **_0.003_** seconds for the first puzzle and **_0.04_** for the harder. 

Even the harder puzzle is solved much faster with a *Backtracking* algorithm. 

## Conclusion

We can conclude by saying that the *Backtracking* algorithm seems to be much more efficient than the *Brute-force* algorithm to solve sudoku puzzle no matter the puzzle we are trying to solve. By using a semi-intelligent algorithm that can go back it allows it to solve the puzzle faster by adapting the choices it makes. 
