import pandas
data = pandas.read_csv("./11_Nato_Phonetic/nato_phonetic_alphabet.csv")

#Loop through rows of a data frame
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter Name:").upper()
output = [phonetic_dict[letter] for letter in word]
print(output)