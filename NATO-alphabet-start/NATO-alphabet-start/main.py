import pandas as pd
nato_dataframe = pd.read_csv("nato_phonetic_alphabet.csv")
letter_dict = {row.letter: row.code for (index, row) in nato_dataframe.iterrows()}

name = input("Input a name: ").strip().upper()

letter_array = [letter_dict[letter] for letter in name]
print(letter_array)





