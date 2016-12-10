# [2016-12-09] Challenge #294 [Hard] Rack management 3
# https://www.reddit.com/r/dailyprogrammer/comments/5hcd0x/20161209_challenge_294_hard_rack_management_3/

import copy, random, timeit

original_row = "sd?zeioao?mluvepesceinfxt?wyiru?ie?giator?t??nuefje?l?odndrotpewlgoobiinysagacaqski?aeh?rbhaervtnl?m"
words = [[line.strip(), 0] for line in open("enable1.txt") if len(line.strip()) < 21]
letters = "abcdefghijklmnopqsrtuvwxyz"
scores = [1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]
practice = False
test = [6,0,0,5,5,3,6,6,5,0,6,7,1,2,1]
iteration = 0
tilescores = dict(zip("abcdefghijklmnopqrstuvwxyz?", [1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10,0]))
char_freq = {'a': 22, 'c': 15, 'b': 9, 'e': 25, 'd': 16, 'g': 13, 'f': 7, 'i': 23, 'h': 10, 'k': 6, 'j': 1, 'm': 11, 'l': 17, 'o': 19, 'n': 20, 'q': 0, 'p': 12, 's': 24, 'r': 21, 'u': 14, 't': 18, 'w': 5, 'v': 4, 'y': 8, 'x': 2, 'z': 3}

def calcScore(word):
  return sum(j * tilescores[char] for j, char in enumerate(word, 1))

def sortWord(word):
  word = "".join([p[0] for p in sorted([[letter, char_freq[letter]] for letter in word], key=lambda x: x[1])])
  return word

def bestWord(hand):
  cutoff = 30
  bestword = ["", 0, ""]
  perm_unknown = hand.count("?")
  for word in words:
    unknown = perm_unknown
    temp_hand = hand[:]
    score_word = word[0][:]
    yes = True
    for index, letter in enumerate(word[2]):
      if letter in temp_hand:
        temp_hand = temp_hand.replace(letter, "", 1)
      elif unknown > 0:
        # score_word = score_word[:index] + "?" + score_word[index + 1:]
        score_word = score_word.replace(letter, '?', 1)
        unknown -= 1
      else:
        yes = False
        break
    if yes:
      if cutoff < 0:
        break
      else:
        cutoff -= 1
      temp_score = calcScore(score_word)
      if temp_score > bestword[1]:
        bestword = [word[0], temp_score, score_word]
  return bestword

if __name__ == "__main__":
  for index, item in enumerate(words):
    words[index][1] = calcScore(item[0])
    words[index].append(sortWord(item[0]))
  words = sorted(words, key=lambda x: x[1], reverse=True)
  mainCounter = 0
  start = timeit.default_timer()
  while 1:
    bestWord(''.join(random.choice("abcdefghijklmnopqrstuvwxyz?") for x in range(20)))
    mainCounter += 1
    if mainCounter == 100:
      print(timeit.default_timer() - start)
      mainCounter = 0