# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas

phonetic_code = pandas.read_csv("/Users/yeomsangyoon/Visual Studio/Practice File/100DaysOfPython#26/NATO-alphabet-start/nato_phonetic_alphabet.csv")
phonetic_code_dict = {row.letter: row.code for(index,row) in phonetic_code.iterrows()}
# print(phonetic_code_dict)
user_input = input("Enter word that you want: ").upper()
result = [phonetic_code_dict[letter] for letter in user_input]
print(result)