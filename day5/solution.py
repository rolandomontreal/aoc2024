data = open('./actualdata.txt').read().split('\n\n')

updates = data[1].splitlines()
rulesByLine = data[0].splitlines()

def filterValidUpdates(update: str):
  validUpdate = True
  i = 0
  pages = update.split(',')
  while validUpdate and i < len(pages) - 1:
    k = i + 1
    while validUpdate and k < len(pages):
      reverse = pages[k] + '|' + pages[i]
      if reverse in rulesByLine:
        validUpdate = False
      k += 1
    i += 1
  return validUpdate
  
validUpdates = list(filter(filterValidUpdates, updates))
sum = 0
for validUpdate in validUpdates:
  elements = validUpdate.split(',')
  start = len(elements) // 2
  end = start + 1
  middleElement = int(elements[start:end][0])
  sum += middleElement

print(sum)
