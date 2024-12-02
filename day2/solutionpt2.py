rows = open('./actual_data.txt').read().strip().splitlines()

def stringOfNumsToArray(stringOfNums: str):
  stringifiedNumbers = stringOfNums.split()
  return list(map(int, stringifiedNumbers))

def isRowValid(nums: list[int]):
  # Verify is sorted
  numsCopy = nums.copy()
  if nums[0] < nums[1]:
    numsCopy.sort()
  else:
    numsCopy.sort(reverse=True)
  if nums != numsCopy:
    return False
  # Verify valid distance
  i = 0
  validDistance = True
  while i < len(nums) - 1 and validDistance:
    distance = abs(nums[i] - nums[i + 1])
    if distance > 3 or distance == 0:
      validDistance = False
    i += 1
  return validDistance

numberMatrix = list(map(stringOfNumsToArray, rows))
validRows = []
for row in numberMatrix:
  validRow = isRowValid(row)
  if (validRow):
    validRows.append(row)
  else:
    # Try repairing by removing one item at a time, then see if its valid
    i = 0
    while i < len(row) and not validRow:
      rowCopy = row.copy()
      del rowCopy[i]
      validRow = isRowValid(rowCopy)
      i += 1
    if validRow:
      validRows.append(row)
print(len(validRows))