# assert 2 + 2 == 5

#class Transformer
# {"I":1, "V": 5, "X":10, "L": 50,"C":100, "D": 500, "M":1000}

'''
IV - 4
VI - 6
'''
class Transformer:
    def __init__(self, roman_number = "XIV"):
        self.roman_number = roman_number

def roman_to_decimal(roman_number):
    summ = 0
    tallies = {"I":1, "V": 5, "X":10, "L": 50,"C":100, "D": 500, "M":1000}
    for i in range(len(roman_number) - 1):
        left = roman_number[i]
        right = roman_number[i+1]
        if tallies[left] < tallies[right]:
            summ -= tallies[left]
        else:
            summ += tallies[left]
    summ += tallies[roman_number[-1]]
    return summ

tal = Transformer("MMMXIV")               
print(roman_to_decimal(tal.roman_number))
