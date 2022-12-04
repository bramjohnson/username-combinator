name = "Toast"
overlap = 4 # Can put two words back to back without any overlap
word_txt = "words_alpha.txt"

name = name.lower()
overlap = min(len(name), overlap)
words = [x.rstrip() for x in open(word_txt, 'r').readlines()]

combinator = {}
for idx in range(len(name) + 1):
    combinator[idx] = []

for word in words:
    for idx in range(len(name) + 1):
        start_word = name[:idx]
        end_word = name[idx:]
        if (len(start_word) >= overlap) and start_word in word:
            usrnm = word[:word.find(start_word) + len(start_word)] + end_word
            combinator[len(start_word)].append((word, usrnm))
            pass
        if (len(end_word) > overlap) and end_word in word:
            usrnm = start_word + word[word.find(end_word):]
            combinator[len(end_word)].append((word, usrnm))
            pass

usrnm_set = set()
for key in combinator:
    for combinations in combinator[key]:
        usrnm_set.add(combinations[1])

f = open('out.txt', 'w+')
for entry in usrnm_set:
    f.write(entry.capitalize() + "\n")