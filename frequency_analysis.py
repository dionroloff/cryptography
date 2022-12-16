cipher = input("Type or paste some text to analyze its letter frequency:").upper()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

freq = {}
for c in alphabet:
    freq[c] = 0

letter_count = 0
for c in cipher:
    if c in freq:
        freq[c] += 1
        letter_count += 1

for c in freq:
    freq[c] = round(freq[c]/letter_count, 4)

for c in freq:
    print(c, ":", freq[c])