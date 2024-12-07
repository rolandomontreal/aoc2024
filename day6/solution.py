import time

data = open('./testdata.txt').read()
matrix = list(map(list, data.splitlines()))

def printMatrix(m: list[list[str]]):
  for row in m:
    print(''.join(row))

def guardDirection(guardSymbol: str):
  if guardSymbol == '^':
    return 'north'
  elif guardSymbol == '>':
    return 'east'
  elif guardSymbol == 'v':
    return 'south'
  elif guardSymbol == '<':
    return 'west'

def canTakeNextStep(rowIndex: int, colIndex: int, guard: str):
  if guard == '^':
    return rowIndex - 1 >= 0
  elif guard == '>':
    return colIndex + 1 < len(matrix[0])
  elif guard == 'v':
    return rowIndex + 1 < len(matrix)
  else:
    return colIndex - 1 >= 0

def getThingInFrontOfGuard(rowIndex: int, colIndex: int, guard: str):
  if guard == '^':
    return matrix[rowIndex - 1][colIndex]
  elif guard == '>':
    return matrix[rowIndex][colIndex + 1]
  elif guard == 'v':
    return matrix[rowIndex + 1][colIndex]
  else:
    return matrix[rowIndex][colIndex - 1]

def takeStep(rowIndex: int, colIndex: int, guard: str):
  if guard == '^':
    matrix[rowIndex][colIndex] = 'X'
    matrix[rowIndex - 1][colIndex] = '^'
    return rowIndex - 1, colIndex
  elif guard == '>':
    matrix[rowIndex][colIndex] = 'X'
    matrix[rowIndex][colIndex + 1] = '>'
    return rowIndex, colIndex + 1
  elif guard == 'v':
    matrix[rowIndex][colIndex] = 'X'
    matrix[rowIndex + 1][colIndex] = 'v'
    return rowIndex + 1, colIndex
  else:
    matrix[rowIndex][colIndex] = 'X'
    matrix[rowIndex][colIndex - 1] = '<'
    return rowIndex, colIndex - 1

def turnRight(rowIndex: int, colIndex: int, guard: str):
  newGuard = ''
  if guard == '^':
    newGuard = '>'
  elif guard == '>':
    newGuard = 'v'
  elif guard == 'v':
    newGuard = '<'
  elif guard == '<':
    newGuard = '^'
  matrix[rowIndex][colIndex] = newGuard
  
withoutNewline = ''.join(data.splitlines())
startIndex = withoutNewline.find('^')
rowIndex = startIndex // len(matrix) 
colIndex = startIndex % len(matrix[0])

i = 0
while i < 1000:
  time.sleep(.3)
  guard = matrix[rowIndex][colIndex]
  direction = guardDirection(matrix[rowIndex][colIndex])
  canTakeStep = canTakeNextStep(rowIndex, colIndex, guard)
  if not canTakeStep:
    break
  thingInFrontOfGuard = getThingInFrontOfGuard(rowIndex, colIndex, guard)
  if thingInFrontOfGuard == '.' or thingInFrontOfGuard == 'X':
    rowIndex, colIndex = takeStep(rowIndex, colIndex, guard)
  else:
    turnRight(rowIndex, colIndex, guard)
  if i % 1 == 0:
    print(f'\n{i}\n')
    printMatrix(matrix)
  i += 1
