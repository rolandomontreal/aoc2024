data = open('./actualdata.txt').read()

byLines = data.strip().splitlines()
nrRows = len(byLines)
nrColumns = len(byLines[0])
joined = ''.join(byLines)

rowIndex = 0
count = 0
while rowIndex <= nrRows - 3:
  startColumn = 0
  while startColumn <= nrColumns - 3:
    startIndex = rowIndex * nrColumns + startColumn
    section1 = joined[startIndex:startIndex+3]
    startSection2 = startIndex + nrColumns
    section2 = joined[startSection2:startSection2+3]
    startSection3 = startIndex + nrColumns * 2
    section3 = joined[startSection3:startSection3+3]
    # section1, 2 and three are now a 3 x 3 substring of the entire file, very easy
    # to check diagonally now
    southEast = section1[0:1] + section2[1:2] + section3[2:3]
    northWest = southEast[::-1]
    southWest = section1[2:3] + section2[1:2] + section3[0:1]
    northEast = southWest[::-1]
    startColumn += 1
    if (southEast == 'MAS' or northWest == 'MAS') and (southWest == 'MAS' or northEast == 'MAS'):
      count += 1
    
  rowIndex += 1

print(count)
