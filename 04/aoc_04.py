from collections import deque
def part1():
  sum = 0

  with open('04/input_04.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
      winners = [x for x in line.split(':')[1].split('|')[0].split(' ') if x != '']
      scratchers = [x for x in line.split(':')[1].split('|')[1].rstrip().split(' ') if x != '']
      count = 0
      for scratcher in scratchers:
        if scratcher in winners:
          count += 1
      sum += pow(2, count - 1) if count >= 1 else 0

  print("Part 1: " + str(sum))

def part2():
  processed = 0
  with open('04/input_04.txt', 'r') as file:
    lines = file.readlines()
    cards = deque(range(0, len(lines)))
    while cards:
      card = cards.popleft()
      processed += 1
      line = lines[card]
      winners = [x for x in line.split(':')[1].split('|')[0].split(' ') if x != '']
      scratchers = [x for x in line.split(':')[1].split('|')[1].rstrip().split(' ') if x != '']
      count = 0
      for scratcher in scratchers:
        if scratcher in winners:
          count += 1
      if count >= 1:
        for i in range(1, count + 1):
          cards.append(card + i)

  print("Part 2: " + str(processed))

def main():
  part1()
  part2()

if __name__ == "__main__":
  main()
