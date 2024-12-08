import time

data = open('./actualdata.txt').read()
resultdata = open('./resultpt1actualdata.txt').read()

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

def runGuardSimulation(obstaclePosition: list[int]):
  obsRow, obsCol = obstaclePosition[0], obstaclePosition[1]
  withoutNewline = ''.join(data.splitlines())
  startIndex = withoutNewline.find('^')
  matrix = list(map(list, data.splitlines()))
  rowIndex = startIndex // len(matrix) 
  colIndex = startIndex % len(matrix[0])
  matrix[obsRow][obsCol] = 'O'

  allStepCoordinates = set()
  moves = set()
  guardLeftMap = False
  loopDetected = False
  i = 0
  while not guardLeftMap and not loopDetected and i < 1000000:
    guard = matrix[rowIndex][colIndex]
    matrix[rowIndex][colIndex] = 'X'
    allStepCoordinates.add(str(rowIndex) + ',' + str(colIndex))
    guardLeftMap = not guardWillStayOnMap(matrix, rowIndex, colIndex, guard)
    if guardLeftMap:
      break
    thingInFrontOfGuard = getThingInFrontOfGuard(matrix, rowIndex, colIndex, guard)
    if thingInFrontOfGuard == '.' or thingInFrontOfGuard == 'X':
      nrUniqueMoves = len(moves)
      move = '[' + str(rowIndex) + ',' + str(colIndex) + ']->'
      rowIndex, colIndex = takeStep(matrix, rowIndex, colIndex, guard)
      move += '[' + str(rowIndex) + ',' + str(colIndex) + ']'
      moves.add(move)
      if nrUniqueMoves == len(moves):
        loopDetected = True
    else:
      turnRight(matrix, rowIndex, colIndex, guard)
    i += 1
  return {
    "guardLeftMap": guardLeftMap,
    "loopDetected": loopDetected,
  }

def getAllPossibleObstaclePositions():
  matrix = list(map(list, resultdata.splitlines()))
  positions = []
  for rowIndex in range(0, len(matrix)):
    for colIndex in range(0, len(matrix[rowIndex])):
      if matrix[rowIndex][colIndex] == 'X':
        positions.append([rowIndex, colIndex])
  return positions

possibleObstaclePositions = getAllPossibleObstaclePositions()
actualLoops = []
for position in possibleObstaclePositions:
  result = runGuardSimulation(position)
  if result["loopDetected"]:
    actualLoops.append(result)
print(len(actualLoops))
