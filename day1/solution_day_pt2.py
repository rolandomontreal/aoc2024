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

def mapOccurences(nums: list[int]):
  output = {}
  for num in nums:
    if num in output:
      output[num] += 1
    else:
      output[num] = 1
  return output

def calculateSumOfSimilarityScore(nums: list[int], frequencyMap: dict[int, int]):
  scores = []
  for n in nums:
    if n in frequencyMap:
      score = n * frequencyMap[n]
      scores.append(score)
  return sum(scores)

unsortedColumns = parseNumberColumns(data)
# Not really needed with sorted columns, but a bit neeter
sortedColumns = sortColumnsOrRows(unsortedColumns)
mappedByNrOccurences = mapOccurences(sortedColumns[1])
similarityScoreSum = calculateSumOfSimilarityScore(sortedColumns[0], mappedByNrOccurences)
print(similarityScoreSum)
