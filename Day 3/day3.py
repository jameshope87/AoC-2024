import os
import pathlib
from collections import Counter

DAY = 1

FILEPATH = os.path.join(pathlib.Path(__file__).parent.absolute(), f'day{DAY}input')
TESTPATH = os.path.join(pathlib.Path(__file__).parent.absolute(), f'day{DAY}test')

def filehandling(filename):

  with open(filename, "r") as f:
    for line in f . readlines():
      find_mults(line)
  
  return
def part1Pass():
  pass

def part2Pass():
  pass

def main(test = False, part2 = False):
  if test:
    locationIDs = filehandling(TESTPATH)
  else:
    locationIDs = filehandling(FILEPATH)
  if part2:
    return(part2Pass())
  else:
    part1Pass()


if __name__ == "__main__":
  print(main(False, True))
