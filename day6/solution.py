import time

data = open('./testdata.txt').read()

def printMatrix(m: list[list[str]]):
  for row in m:
    print(''.join(row))

def guardWillStayOnMap(matrix: list[list[str]], rowIndex: int, colIndex: int, guard: str):
  if guard == '^':
    return rowIndex - 1 >= 0
  elif guard == '>':
    return colIndex + 1 < len(matrix[0])
  elif guard == 'v':
    return rowIndex + 1 < len(matrix)
  else:
    return colIndex - 1 >= 0

def getThingInFrontOfGuard(matrix: list[list[str]], rowIndex: int, colIndex: int, guard: str):
  if guard == '^':
    return matrix[rowIndex - 1][colIndex]
  elif guard == '>':
    return matrix[rowIndex][colIndex + 1]
  elif guard == 'v':
    return matrix[rowIndex + 1][colIndex]
  else:
    return matrix[rowIndex][colIndex - 1]

def takeStep(matrix: list[list[str]], rowIndex: int, colIndex: int, guard: str):
  if guard == '^':
    matrix[rowIndex - 1][colIndex] = '^'
    return rowIndex - 1, colIndex
  elif guard == '>':
    matrix[rowIndex][colIndex + 1] = '>'
    return rowIndex, colIndex + 1
  elif guard == 'v':
    matrix[rowIndex + 1][colIndex] = 'v'
    return rowIndex + 1, colIndex
  else:
    matrix[rowIndex][colIndex - 1] = '<'
    return rowIndex, colIndex - 1

def turnRight(matrix: list[list[str]], rowIndex: int, colIndex: int, guard: str):
  newGuardDirection = ''
  if guard == '^':
    newGuardDirection = '>'
  elif guard == '>':
    newGuardDirection = 'v'
  elif guard == 'v':
    newGuardDirection = '<'
  elif guard == '<':
    newGuardDirection = '^'
  matrix[rowIndex][colIndex] = newGuardDirection

def runGuardSimulation(initialRun: bool):
  withoutNewline = ''.join(data.splitlines())
  startIndex = withoutNewline.find('^')
  matrix = list(map(list, data.splitlines()))
  rowIndex = startIndex // len(matrix) 
  colIndex = startIndex % len(matrix[0])

  allStepCoordinates = set()
  moves = set()
  guardLeftMap = False
  loopDetected = False
  i = 0
  while not guardLeftMap and not loopDetected and i < 10000:
    guard = matrix[rowIndex][colIndex]
    matrix[rowIndex][colIndex] = 'X'
    allStepCoordinates.add(str(rowIndex) + ',' + str(colIndex))
    guardLeftMap = not guardWillStayOnMap(matrix, rowIndex, colIndex, guard)
    if guardLeftMap:
      print('SOLUTION FOUND, BREAKING')
      break
    thingInFrontOfGuard = getThingInFrontOfGuard(matrix, rowIndex, colIndex, guard)
    if thingInFrontOfGuard == '.' or thingInFrontOfGuard == 'X':
      nrUniqueMoves = len(moves)
      move = '[' + str(rowIndex) + ',' + str(colIndex) + ']->'
      rowIndex, colIndex = takeStep(matrix, rowIndex, colIndex, guard)
      move += '[' + str(rowIndex) + ',' + str(colIndex) + ']'
      moves.add(move)
      if nrUniqueMoves == len(moves):
        print('NO NEW MOVE WAS DETECTED - CYCLE')
    else:
      turnRight(matrix, rowIndex, colIndex, guard)
    if i % 200 == 0:
      print(f'\n{i}\n')
      printMatrix(matrix)
    i += 1
  printMatrix(matrix)
  print(len(allStepCoordinates))
  if initialRun:
    return allStepCoordinates
  else:
    return {
      "guardLeftMap": guardLeftMap,
      "loopDetected": loopDetected,
      "moves": moves
    }

