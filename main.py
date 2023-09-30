import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

username = input("Type your name: ").upper()

spelled_name_dict = [phonetic_dict[letter] for letter in username]
