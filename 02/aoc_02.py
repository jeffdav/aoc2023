def part1():
  counts = { "red": 12, "green": 13, "blue": 14 }
  sum = 0

  with open('input_02.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
      valid = True
      line = line.rstrip()
      game = int(line.split(':')[0].split(' ')[1])
      grabs = line.split(':')[1].split(';')
      for grab in grabs:
        if not valid:
          break
        grab = grab.strip()
        colors = grab.split(',')
        for color in colors:
          num, c = color.strip().split(' ')
          if (int(num) > counts[c]):
            valid = False
            break

      if valid:
        sum += game

  print("Part 1: " + str(sum))

def part2():
  sum = 0
  with open('input_02.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
      red = 0
      green = 0
      blue = 0
      line = line.rstrip()
      grabs = line.split(':')[1].split(';')
      for grab in grabs:
        grab = grab.strip()
        colors = grab.split(',')
        for color in colors:
          color = color.strip()
          num = int(color.split(' ')[0])
          c = color.split(' ')[1]
          red = num if c == "red" and num > red else red
          green = num if c == "green" and num > green else green
          blue = num if c == "blue" and num > blue else blue
      sum += red * green * blue

  print("Part 2: " + str(sum))

def main():
  part1()
  part2()

if __name__ == "__main__":
  main()
