import os
import pathlib
from collections import Counter

DAY = 3

FILEPATH = os.path.join(pathlib.Path(__file__).parent.absolute(), f'day{DAY}input')
TESTPATH = os.path.join(pathlib.Path(__file__).parent.absolute(), f'day{DAY}test')

def filehandling(filename, part2):

  with open(filename, "r") as f:
    for line in f . readlines():
      find_mults(line, part2)
  return

def find_mults(line, part2):
  enabled = True
  while True:
    start = line.find('mul(')
    if part2 and enabled:
      start_dont = line.find("don't()")
      if start_dont < start:
        enabled = False
        line = line[start_dont:]
    if part2 and not enabled:
      start_do = line.find("do()")
      if start_do < start:
        enabled = True
        line = line[start_dont:]
    if start == -1:
      break
    line = line[start:]
    end = line.find(')')+1
    if end == 0:
      break
    candidate = line[:end]
    valid = check_validity(candidate)
    if valid and enabled:
      mult_list.append(valid)
    line = line[4:]
  

def check_validity(candidate):
  if ' ' not in candidate:
    commaPos = candidate.find(',')
    if commaPos > 0:
      num1 = candidate[4:commaPos]
      num2 = candidate[commaPos+1:candidate.find(')')]
      if num1.isnumeric() and num2.isnumeric():
        numpair = (int(num1), int(num2))
        return numpair
  return False

def mul(input_list):
  return sum([i[0]*i[1] for i in mult_list])

def main(test = False, part2 = False):
  if test:
    filehandling(TESTPATH, part2)
  else:
    filehandling(FILEPATH, part2)


if __name__ == "__main__":
  mult_list = []
  main(False, True)
  print(mult_list)
  print(mul(mult_list))
