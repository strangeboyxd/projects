alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

eORd = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(plain_text, shift_amount, direction):
  cipher_text = ""
  if eORd == "encode":
    direction = 1
  elif eORd == "decode":
    direction = -1
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount * direction
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")

caesar(text, shift, 1)


#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.