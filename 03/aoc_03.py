import string

def part1():
  sum = 0
  symbols = set(string.punctuation) - set('.')

  with open('03/input_03.txt', 'r') as file:
    lines = file.readlines()
    line_num = 0
    while line_num < len(lines):
      prev_line = lines[line_num - 1].rstrip() if line_num > 0 else None
      curr_line = lines[line_num].rstrip()
      next_line = lines[line_num + 1].rstrip() if line_num < len(lines) - 1 else None
      i = 0
      while i < len(curr_line):
        if curr_line[i] == '.' or curr_line[i] in symbols:
          i += 1
          continue
        elif curr_line[i].isdigit():
          start = (i - 1) if (i - 1) > 0 else 0

          num = 0
          while i < len(curr_line) and curr_line[i].isdigit():
            num = 10 * num + int(curr_line[i])
            i += 1
          end = i if i < len(curr_line) else len(curr_line) - 1

          is_part_number = False
          if prev_line:
            if any(c in symbols for c in prev_line[start:end+1]):
              is_part_number = True
          if (not is_part_number and
              curr_line[start] in symbols or
              curr_line[end] in symbols):
            is_part_number = True
          if not is_part_number and next_line:
            if any(c in symbols for c in next_line[start:end+1]):
              is_part_number = True

          if is_part_number:
            sum += num

          i += 1
      line_num += 1

    print("Part 1: " + str(sum))

def find_number(line, i):
  start = i
  while start >= 0 and line[start - 1].isdigit():
    start -= 1

  end = i
  while end < len(line) - 1 and line[end + 1].isdigit():
    end += 1

  num = 0
  for c in line[start:end+1]:
    num = 10 * num + int(c)
  return num

def part2():
  with open('03/input_03.txt', 'r') as file:
    lines = file.readlines()
    line_num = 0
    sum = 0
    while line_num < len(lines):
      prev_line = lines[line_num - 1].rstrip() if line_num > 0 else None
      curr_line = lines[line_num].rstrip()
      next_line = lines[line_num + 1].rstrip() if line_num < len(lines) - 1 else None
      i = 0
      nums = []
      while i < len(curr_line):
        if curr_line[i] == '*':
          if prev_line:
            if prev_line[i].isdigit():
              nums.append(find_number(prev_line, i))
            else:
              if i > 0 and prev_line[i-1].isdigit():
                nums.append(find_number(prev_line, i-1))
              if i < len(prev_line) - 1 and prev_line[i+1].isdigit():
                nums.append(find_number(prev_line, i+1))
          if i > 0 and curr_line[i-1].isdigit():
            nums.append(find_number(curr_line, i-1))
          if i < len(curr_line) - 1 and curr_line[i+1].isdigit():
            nums.append(find_number(curr_line, i+1))
          if next_line:
            if next_line[i].isdigit():
              nums.append(find_number(next_line, i))
            else:
              if i > 0 and next_line[i-1].isdigit():
                nums.append(find_number(next_line, i-1))
              if i < len(next_line) - 1 and next_line[i+1].isdigit():
                nums.append(find_number(next_line, i+1))

          if len(nums) == 2:
            print("YES: " + str(nums))
            sum += (nums[0] * nums[1])
          else:
            print("NO: " + str(nums))
          nums = []
        i += 1
      line_num += 1

  print("Part 2: " + str(sum))

def main():
  part1()
  part2()

if __name__ == "__main__":
  main()
