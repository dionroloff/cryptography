cipher = input("Type or paste some text to analyze its letter frequency:").upper()

class Attack:
    def __init__(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.freq = {}

    def calculate_freq(self, cipher):
        for c in self.alphabet:
            self.freq[c] = 0

        letter_count = 0
        for c in cipher:
            if c in self.freq:
                self.freq[c] += 1
                letter_count += 1

        for c in self.freq:
            self.freq[c] = round(self.freq[c]/letter_count, 4)

    def print_freq(self):
        new_line_count = 0
        for c in self.freq:
            print(c, ":", self.freq[c], ' ', end='')
            if new_line_count % 3 == 2:
                print()
            new_line_count += 1

attack = Attack()
attack.calculate_freq(cipher)
attack.print_freq()