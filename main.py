#day_8_final_project

import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
   
print(art.logo)

continuing = True

while continuing:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  def caesar(plain_text,shifted_ammount,direction_of_user):
    end_text = ""
    if direction == "decode":
      shifted_ammount *= -1
    for i in plain_text:
      if i in alphabet:
        position = alphabet.index(i)
        new_position = position + shifted_ammount
        end_text += alphabet[new_position]  
      else:
        end_text += i

    print(f"Here's the {direction_of_user}d result : {end_text}")

  shift = shift % 26

  caesar(plain_text=text,shifted_ammount=shift,direction_of_user=direction)

  restart = input("Type 'yes' if you want to go again.Otherwise type 'no' \n ").lower()

  if restart == "no":
    continuing = False
    print("GoodBye")