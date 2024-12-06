data = open('./actualdata.txt').read()
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

printMatrix(matrix)
withoutNewline = ''.join(data.splitlines())
startIndex = withoutNewline.find('^')
rowIndex = startIndex // len(matrix) 
colIndex = startIndex % len(matrix[0])

i = 0
guardStillOnMap = True
while i < 10000 and guardStillOnMap:
  direction = guardDirection(matrix[rowIndex][colIndex])
  if direction == 'north':
    if rowIndex - 1 < 0:
      guardStillOnMap = False
      continue
      # Break here somehow
    thingInFrontOfGuard = matrix[rowIndex - 1][colIndex]
    if thingInFrontOfGuard == '.' or thingInFrontOfGuard == 'X':
      matrix[rowIndex][colIndex] = 'X'
      matrix[rowIndex - 1][colIndex] = '^'
      rowIndex -= 1
    if thingInFrontOfGuard == '#':
      matrix[rowIndex][colIndex] = '>'
  elif direction == 'east':
    if colIndex + 1 >= len(matrix[0]):
      guardStillOnMap = False
      continue
      # Break here somehow
    thingInFrontOfGuard = matrix[rowIndex][colIndex + 1]
    if thingInFrontOfGuard == '.' or thingInFrontOfGuard == 'X':
      matrix[rowIndex][colIndex] = 'X'
      matrix[rowIndex ][colIndex + 1] = '>'
      colIndex += 1
    if thingInFrontOfGuard == '#':
      matrix[rowIndex][colIndex] = 'v'
  elif direction == 'south':
    if rowIndex + 1 >= len(matrix):
      guardStillOnMap = False
      continue
      # Break here somehow
    thingInFrontOfGuard = matrix[rowIndex + 1][colIndex]
    if thingInFrontOfGuard == '.' or thingInFrontOfGuard == 'X':
      matrix[rowIndex][colIndex] = 'X'
      matrix[rowIndex + 1][colIndex] = 'v'
      rowIndex += 1
    if thingInFrontOfGuard == '#':
      matrix[rowIndex][colIndex] = '<'
  elif direction == 'west':
    if colIndex - 1 < 0:
      guardStillOnMap = False
      continue
      # Break here somehow
    thingInFrontOfGuard = matrix[rowIndex][colIndex - 1]
    if thingInFrontOfGuard == '.' or thingInFrontOfGuard == 'X':
      matrix[rowIndex][colIndex] = 'X'
      matrix[rowIndex ][colIndex - 1] = '<'
      colIndex -= 1
    if thingInFrontOfGuard == '#':
      matrix[rowIndex][colIndex] = '^'
  if i % 100 == 0:
    print(f'\n{i}\n')
    printMatrix(matrix)
  i += 1

totalPlaces = 0
for row in matrix:
  for column in row:
    if column == 'X':
      totalPlaces += 1
# In the solution, do not update the grid the last time, so there will be an '^' or similar on the "map"
totalPlaces += 1

print(totalPlaces)