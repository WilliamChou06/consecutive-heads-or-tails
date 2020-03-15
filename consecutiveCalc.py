import random

numberOfStreaks = 0
numberOfExperiments = 1000
listSize = 100

for experimentNumber in range(numberOfExperiments):
  sampleList = []
  consecutiveAmount = 0

  for randomFlip in range(listSize):
    randomNumber = random.randint(0, 1)
    if (randomNumber == 0):
      sampleList.append('H')
    else:
      sampleList.append('T')
  
  for i, item in enumerate(sampleList):
    currentValue = item

    if (consecutiveAmount == 6):
      consecutiveAmount = 0
      numberOfStreaks += 1

    if (i != len(sampleList) - 1 and currentValue == sampleList[i + 1]):
      consecutiveAmount += 1
    else:
      consecutiveAmount = 0
  
  # print(sampleList)

print(f'{numberOfStreaks} streaks of 7 in {str(listSize * experimentNumber)} total numbers')