import sys
from typing import Any
import time
from datetime import datetime

class RangeMap:
  def __init__(self, src_start, dest_start, length):
    self.src_start = src_start
    self.src_end = src_start + length - 1
    self.offset = dest_start - src_start

class RangeMapper:
  def __init__(self):
    self.range_maps = []

  def add_range_map(self, src_start, dest_start, length):
    self.range_maps.append(RangeMap(src_start, dest_start, length))

  def map_number(self, number):
    for r in self.range_maps:
      if number >= r.src_start and number <= r.src_end:
        return number + r.offset
    return number

def part1():
  with open('05/input_05.txt', 'r') as file:
    lines = file.readlines()
    seeds = [int(x) for x in lines[0].split(' ')[1:]]

    map_map = {}
    i = 1
    while i < len(lines):
      line = lines[i]
      if line.strip() == '':
        i += 1
        continue

      if line[0].isalpha():
        types = tuple([s for s in line.split(' ')[0].split('-') if s != 'to'])
        i += 1

        range_mapper = RangeMapper()
        line = lines[i]
        while line and line[0].isdigit():
          numbers = [int(s) for s in line.split(' ')]
          range_mapper.add_range_map(numbers[1], numbers[0], numbers[2])

          i += 1
          if i >= len(lines):
            break
          line = lines[i].rstrip()

        map_map[types] = range_mapper

    key = "seed"
    output = seeds
    while key != "location":
      for ((source, dest)) in map_map.keys():
        if source == key:
          print("mapping: {} to {}".format(source, dest))
          key = dest
          range_mapper = map_map[(source, dest)]
          output = [range_mapper.map_number(o) for o in output]

  print("Part 1: " + str(min(output)))

def part2():
  with open('05/input_05.txt', 'r') as file:
    lines = file.readlines()
    seeds = [int(x) for x in lines[0].split(' ')[1:]]

    map_map = {}
    i = 1
    while i < len(lines):
      line = lines[i]
      if line.strip() == '':
        i += 1
        continue

      if line[0].isalpha():
        types = tuple([s for s in line.split(' ')[0].split('-') if s != 'to'])
        i += 1

        range_mapper = RangeMapper()
        line = lines[i]
        while line and line[0].isdigit():
          numbers = [int(s) for s in line.split(' ')]
          range_mapper.add_range_map(numbers[1], numbers[0], numbers[2])

          i += 1
          if i >= len(lines):
            break
          line = lines[i].rstrip()

        map_map[types] = range_mapper

    curr_min = sys.maxsize
    seed_num = 0
    while seed_num < len(seeds):
      start = seeds[seed_num]
      length = seeds[seed_num + 1]
      seed_range = range(start, start + length)
      print("mapping: ({:,}, {:,})".format(seed_range[0], seed_range[-1]))

      for i in seed_range:
        key = "seed"
        output = i
        while key != "location":
          for ((source, dest)) in map_map.keys():
            if source == key:
              key = dest
              range_mapper = map_map[(source, dest)]
              output = range_mapper.map_number(output)
        curr_min = min(curr_min, output)
        if i % 10000000 == 0:
          print("[{}] - [{:.0%}]: curr_min: {:,}".format(datetime.now(), (i-start)/length, curr_min))
      seed_num += 2

  print("Part 2: " + str(curr_min))


def main():
  part1()
  part2()

if __name__ == "__main__":
  main()
