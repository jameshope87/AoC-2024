import os
import pathlib

DAY = 1

FILEPATH = os.path.join(pathlib.Path(__file__).parent.absolute(), f'day{DAY}input')
TESTPATH = os.path.join(pathlib.Path(__file__).parent.absolute(), f'day{DAY}test')

def filehandling(filename):
  list1 = []
  list2 = []
  with open(filename, "r") as f:
    for line in f . readlines():
      list1.append(int(line[:line.find(' ')].strip()))
      list2.append(int(line[line.find(' '):].strip()))
  list1.sort()
  list2.sort()
  #print(list1,list2)
  return list1, list2

def main(test = False):
  if test:
    locationIDs = filehandling(TESTPATH)
  else:
    locationIDs = filehandling(FILEPATH)

  sum = 0
  while len(locationIDs[0])>0:
    distance = abs(locationIDs[0].pop(0) - locationIDs[1].pop(0))
    #print(distance)
    sum += distance
  return sum


if __name__ == "__main__":
  print(main())
