import code_index

print("Please Enter Your Word to Convert.")
user_word = str(input("Enter word or phrase: \n").lower())
morse_word = ""

for letter in user_word:
    if letter == " ":
        morse_letter = " "
    else:
        try:
            morse_letter = code_index.morse_key[letter]
        except KeyError:
            morse_letter = letter
    if morse_word == "":
        morse_word = morse_letter
    else:
        morse_word = morse_word + " | " + morse_letter

print(f"Your word in morse code is:\n {morse_word}")


morse_list = morse_word.split(" | ")
og_word = ""

for item in morse_list:
    if item == " ":
        result = " "
    else:
        result = [key for key, value in code_index.morse_key.items() if value == item]
    if og_word == "":
        og_word = result[0]
    else:
        og_word = og_word + result[0]

print(f"The Original Word Was: {og_word.capitalize()}")
