import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


def generate_phonetic():
    username = input("Type your name: ").upper()

    try:
        spelled_name_dict = [phonetic_dict[letter] for letter in username]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(spelled_name_dict)


generate_phonetic()