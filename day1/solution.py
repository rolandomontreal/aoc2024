data = open('./actual_data.txt').read()

def parseNumberColumns(textWithNumberColumns: str):
  rawData = textWithNumberColumns.strip()
  rows = rawData.splitlines()
  columns = []
  for rowIndex in range(0, len(rows)):
    stringifiedNumbers = rows[rowIndex].split()
    for columnIndex in range(0, len(stringifiedNumbers)):
      num = int(stringifiedNumbers[columnIndex])
      if rowIndex == 0:
        column = [num]
        columns.append(column)
      else:
        columns[columnIndex].append(num)
  return columns

def sortColumnsOrRows(grid: list[list[int]]):
  output = []
  for columnOrRow in grid:
    arr = columnOrRow.copy()
    arr.sort()
    output.append(arr)
  return output

def calculateDistances(sortedColumns: list[list[int]]):
  output = sortedColumns.copy()
  distances = []
  for rowIndex in range(0, len(sortedColumns[0])):
    column1 = sortedColumns[0]
    column2 = sortedColumns[1]
    d = abs(column1[rowIndex] - column2[rowIndex])
    distances.append(d)
  output.append(distances)
  return output

unsortedColumns = parseNumberColumns(data)
sortedColumns = sortColumnsOrRows(unsortedColumns)
augmentedMatrix = calculateDistances(sortedColumns)
print(sum(augmentedMatrix[2]))