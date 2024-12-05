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

def fixInvalidUpdate(update: str):
  i = 0
  pages = update.split(',')
  while i < len(pages) - 1:
    k = i + 1
    while k < len(pages):
      reverse = pages[k] + '|' + pages[i]
      if reverse in rulesByLine:
        tmpEl1 = pages[k]
        pages[k] = pages[i]
        pages[i] = tmpEl1
      k += 1
    i += 1
  return pages


invalidUpdates = list(filter(lambda update: update not in validUpdates, updates))
fixedUpdates = list(map(fixInvalidUpdate, invalidUpdates))
sum = 0
for u in fixedUpdates:
  sum += int(u[len(u) // 2])

print(sum)
