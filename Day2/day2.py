import os
import pathlib
from collections import Counter

DAY = 2

FILEPATH = os.path.join(pathlib.Path(__file__).parent.absolute(), f'day{DAY}input')
TESTPATH = os.path.join(pathlib.Path(__file__).parent.absolute(), f'day{DAY}test')

class Report:
  def __init__(self, levels):

    self.levels = levels
    #self.differences = self.calc_diffs()
    self.safety = self.check_safety(self.levels)
    self.damp_safety = self.dampener()
    
  def calc_diffs(self,levels_list):
    diffs = []
    for levelid, level in enumerate(levels_list):
      if levelid == 0:
        continue
      else:
        diff = level - levels_list[levelid-1]
        diffs.append(diff)
    return diffs
  
  def check_safety(self, levels_list):
    self.differences = self.calc_diffs(levels_list)
    if all([diff>0 for diff in self.differences]) or all([diff<0 for diff in self.differences]):
      if all([abs(diff)>0 and abs(diff)<4 for diff in self.differences]):
        return True
    return False
  
  def dampener(self):
    if self.safety:
      return True
    else:

      for idx, x in enumerate(self.levels):
        if self.check_safety(self.levels[:idx]+self.levels[idx+1:]):
          return True
      return False

def filehandling(filename):
  reports = []
  with open(filename, "r") as f:
    reports = [Report([int(x) for x in line.split()]) for line in f.readlines()]
    
  return reports

def part1Pass(filename):
  reports = filehandling(filename)
  safties = [report.safety for report in reports]
  damp_safeties = [report.damp_safety for report in reports]
  print(safties)
  print(damp_safeties)
  return sum(safties), sum(damp_safeties)

def part2Pass(lists_to_check):
  pass

def main(test = False, part2 = False):
  if test:
    return part1Pass(TESTPATH)
  else:
    return part1Pass(FILEPATH)

if __name__ == "__main__":
  result = main(False, True)
  print(f"Truesafeties: {result[0]}\nDampened Safeties: {result[1]}")