import Caesar_art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', \
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
run = True
def caesar(first_text, direction, shift):
    second_text = ""
    new_location = 0
    shift = shift % 26
    if direction == "decode":
        shift *= -1
    for letter in first_text:
        if letter in alphabet:
            location = alphabet.index(letter)
            new_location = location + shift
            second_text += alphabet[new_location]
        else:
            second_text += letter
    print("The {0}d text is '{1}'".format(direction,second_text))

print(Caesar_art.logo)
while (run ==True):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt : \n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(first_text= text, direction=direction, shift=shift)
    i_n = input("If you want to continue, type 'yes' and you don't want, type 'n' :\n")
    if i_n == 'n':
        run = False