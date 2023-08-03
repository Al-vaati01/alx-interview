# LOCKBOXES
```def canUnlockAll(boxes)``` - takes n number of locked boxes. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

The method determines if all the boxes can be opened.
- ```boxes``` is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
- There can be keys that do not have boxes
- The first box ```boxes[0]``` is unlocked
- Returns ```True``` if all boxes can be opened, else returns ```False```

```shell
# Test

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

# output
$ ./main_0.py
True
True
False

```
#### AUTHOR
Alvin vaati
