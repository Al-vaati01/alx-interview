# Island Perimeter

![Project Status](https://img.shields.io/badge/status-in%20progress-yellow)
![Python Version](https://img.shields.io/badge/python-3.4.3-blue)
![PEP 8 Style](https://img.shields.io/badge/style-PEP%208%20v1.7-green)

## Table of Contents
- [Description](#description)
- [Tasks](#tasks)
- [Usage](#usage)
- [Author](#author)

---

## Description

This project implements a Python function to calculate the perimeter of an island represented as a grid. The grid consists of cells where:
- 0 represents water.
- 1 represents land.
- Each cell is square, with a side length of 1.
- Cells are connected horizontally/vertically (not diagonally).
- The grid is rectangular, with its width and height not exceeding 100.
- The grid is completely surrounded by water.
- There is only one island (or nothing).
- The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).



## Tasks

### 0. Island Perimeter
**Mandatory**
Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in the grid.

### Example
```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))  # Output: 12
```

### Usage
**Clone the repository:**
```
git clone https://github.com/your-username/alx-interview.git
```
**Navigate to the project directory:**
```
cd alx-interview/0x09-island_perimeter
```
**Execute the main script to test the ```island_perimeter``` function:**

```
./0-main.py
```
## Author

Author: Alvin Vaati

