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


def main():
  part1()

if __name__ == "__main__":
  main()
