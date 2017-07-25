# [2016-10-21] Challenge #288 [Hard] Adjacent Numbers problems
# https://www.reddit.com/r/dailyprogrammer/comments/58n2ca/20161021_challenge_288_hard_adjacent_numbers/

perms = [ (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1) ]

def main(size):
  grid = [[1 for i in range(size)] for i in range(size)][:]
  while 1:
    newGrid = iterateGrid(grid)[:]
    if minify(newGrid) == minify(grid):
      printGrid(newGrid)
      break
    else:
      grid = newGrid
    printGrid(newGrid)

def minify(grid):
  y = []
  for x in grid:
    y.append("".join(str(i) for i in x))
  return "".join(y)

def printGrid(grid):
  for index,row in enumerate(grid):
    print("|".join([str(i) for i in row]))
    if index != len(grid):
      print("-" * (2 * len(row) - 1))

def iterateGrid(grid):
  # x, y starting at 0,0 in the top-left
  for y,row in enumerate(grid):
    for x,column in enumerate(row):
      required = list(range(1,column + 1))
      for position in perms:
        test_y = y + position[0]
        test_x = x + position[1]
        if test_y >= 0 and test_y < len(grid) and test_x >= 0 and test_x < len(row):
          number = grid[test_y][test_x]
          if number in required:
            required.remove(number)
        if required == []:
          grid[y][x] += 1
        break
  return grid

if __name__ == "__main__":
  main(3)
