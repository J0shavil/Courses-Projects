# TODO
import re

phrase = input("Text: ")

letter_count = 0

for char in phrase:
    if char.isalpha() and char.isascii():
        letter_count += 1

words = phrase.split()

word_count = len(words)

deduct_sentence = 0


if phrase[len(phrase) - 1] != "." and "!" and "?":
    deduct_sentence += 1


sentences = re.split(r"[.!?]", phrase)


sentences = [sentence.strip() for sentence in sentences if sentence.strip()]


sentence_count = len(sentences)

sentence_count -= deduct_sentence




L = float(letter_count / word_count) * 100
S = float(sentence_count / word_count) * 100

index = (0.0588 * L) - (0.296 * S) - 15.8


if index > 16:
    print("Grade 16+")
if index < 1:
    print("Before Grade 1")
if index < 16:
    print("Grade ", round(index))
