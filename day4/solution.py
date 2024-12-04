data = open('./actualdata.txt').read()

def parseStringAndFindAllPossibleStrings(stringInput: str, strLength: int):
  splittedByLines = stringInput.strip().splitlines()
  matrix = list(map(list, splittedByLines))
  nrRows = len(matrix)
  nrColumns = len(matrix[0])
  allSubStrings = []
  subStringsArrFormat = []
  for rowIndex in range(0, len(matrix)):
    for colIndex in range(0, len(matrix[0])):
      # East and west direction
      if colIndex + strLength <= nrColumns:
        subString = matrix[rowIndex][colIndex:colIndex + strLength]
        # East
        subStringsArrFormat.append(subString)
        # West
        subSCopy = subString.copy();
        subSCopy.reverse()
        subStringsArrFormat.append(subSCopy)
      # South and north direction
      if rowIndex + strLength <= nrRows:
        # South
        subString = []
        i = rowIndex
        while i < rowIndex + strLength:
          subString.append(matrix[i][colIndex])
          i += 1
        subStringsArrFormat.append(subString)
        # North
        subSCopy = subString.copy();
        subSCopy.reverse()
        subStringsArrFormat.append(subSCopy)
        # Diagonal (South east, south west etc)
      if rowIndex + strLength <= nrRows and colIndex + strLength <= nrColumns:
        i = rowIndex
        k = colIndex
        southEast = []
        southWest = []
        while i < rowIndex + strLength and k < colIndex + strLength:
          # South east
          southEast.append(matrix[i][k])
          invertedColumnIndex = (nrColumns - 1) - k
          # South west
          southWest.append(matrix[i][invertedColumnIndex])
          i += 1
          k += 1
        northWest = southEast.copy()
        northWest.reverse()
        subStringsArrFormat.append(southEast)
        subStringsArrFormat.append(northWest)
        northEast = southWest.copy()
        northEast.reverse()
        subStringsArrFormat.append(southWest)
        subStringsArrFormat.append(northEast)
  allSubStrings = list(map(lambda sarr: ''.join(sarr), subStringsArrFormat))
  return allSubStrings

def filterForXmasString(item):
  return item == 'XMAS'
        
possibleStrings = parseStringAndFindAllPossibleStrings(data, 4)
allXmas = list(filter(filterForXmasString, possibleStrings))
print(allXmas)
print(len(allXmas))