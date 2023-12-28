chosen_word = 'apple'
lines = []
guess = 'p'
# for word in chosen_word:
#     lines.append('_' * len(word))

word_length = len(chosen_word)

'''
for _ in chosen_word:
    lines += '_'

'''

for _ in range(word_length):
    lines += '_'

for position in range(word_length):
    letter = chosen_word[position]

    if letter == guess:
        lines[position] = letter
print(lines)
