import re

def part1():
  nums = "0123456789"
  sum = 0

  with open('input_01.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
      line_nums = [c for c in line if c in nums]
      ref_nums = [line_nums[0], line_nums[len(line_nums) - 1]]
      ref_num = 10 * int(ref_nums[0]) + int(ref_nums[1])
      sum += ref_num

    print("Part 1: " + str(sum))

def part2():
  nums = "0123456789"
  alpha_nums = {"one": 1, "two": 2, "three": 3, "four": 4,
                "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
  sum = 0

  with open('input_01.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
      line_nums = []
      line = line.rstrip()
      for i in range(len(line)):
        if line[i] in nums:
          line_nums.append(int(line[i]))
        else:
          for key in alpha_nums.keys():
            if line[i:].startswith(key):
              line_nums.append(alpha_nums[key])

      ref_nums = [line_nums[0], line_nums[len(line_nums) - 1]]
      ref_num = 10 * int(ref_nums[0]) + int(ref_nums[1])
      sum += ref_num

    print("Part 2: " + str(sum))

def main():
  part1()
  part2()

if __name__ == "__main__":
  main()
