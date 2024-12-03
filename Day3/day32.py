import os
import pathlib
from collections import Counter

DAY = 3

FILEPATH = os.path.join(pathlib.Path(__file__).parent.absolute(), f'day{DAY}input')
TESTPATH = os.path.join(pathlib.Path(__file__).parent.absolute(), f'day{DAY}test')

def filehandling(filename, part2):

  with open(filename, "r") as f:
    content = f.read()
    find_mults(content, part2)
  return

def find_mults(content, part2):
  global enabled
  for charid, char in enumerate(content):
    if content[charid:charid+4] == 'do()':
      enabled = True
    if content[charid:charid+7] == "don't()":
      enabled = False
    print(content[charid:charid+4])
    if content[charid:charid+4] == 'mul(':
      end = content[charid:].find(')')+charid+1
      if end == 0:
        break
      candidate = content[charid:end]
      valid = check_validity(candidate)
      if valid and enabled:
        mult_list.append(valid)
      
  

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

def mul():
  return sum([i[0]*i[1] for i in mult_list])

def main(test = False, part2 = False):
  if test:
    filehandling(TESTPATH, part2)
  else:
    filehandling(FILEPATH, part2)

enabled = True
if __name__ == "__main__":
  mult_list = []
  
  main(False, True)
  print(mult_list)
  print(mul())
