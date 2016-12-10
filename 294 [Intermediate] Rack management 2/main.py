# [2016-12-09] Challenge #294 [Hard] Rack management 3
# https://www.reddit.com/r/dailyprogrammer/comments/5hcd0x/20161209_challenge_294_hard_rack_management_3/

import copy, random, timeit

original_row = "sd?zeioao?mluvepesceinfxt?wyiru?ie?giator?t??nuefje?l?odndrotpewlgoobiinysagacaqski?aeh?rbhaervtnl?m"
words = [[line.strip(), 0] for line in open("enable1.txt") if len(line.strip()) < 11]
letters = "abcdefghijklmnopqsrtuvwxyz"
scores = [1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]
practice = False
test = [6,0,0,5,5,3,6,6,5,0,6,7,1,2,1]
iteration = 0
tilescores = dict(zip("abcdefghijklmnopqrstuvwxyz?", [1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10,0]))

def calcScore(word):
  return sum(j * tilescores[char] for j, char in enumerate(word, 1))

def bestWord(hand):
  for word in words:
    temp_hand = copy.deepcopy(hand)
    yes = True
    for letter in word[0]:
      if letter in hand:
        temp_hand.replace(letter, '', 0)
      else:
        yes = False
        break
    if yes:
      return word

if __name__ == "__main__":
  for index, item in enumerate(words):
    words[index][1] = calcScore(item[0])
    words[index][0] = item[0] #''.join(sorted(item[0]))
  words = sorted(words, key=lambda x: x[1], reverse=True)
  start = timeit.default_timer()
  for i in range(100):
    print(bestWord(''.join(random.choice('abcdefghijklmnopqsrtuvwxyz') for _ in range(10))))
  stop = timeit.default_timer()
  print(stop - start)