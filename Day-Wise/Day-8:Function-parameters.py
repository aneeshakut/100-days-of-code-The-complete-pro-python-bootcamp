#Caesar Cipher

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt , type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(start_text,shift_amount,cipher_direction):
    end_text = ""
    for letter in start_text:
        position = alphabet.index(letter)
        if(cipher_direction == "decode"):
            shift_amount *= -1
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"The {cipher_direction}d message is {end_text}")

caesar(text,shift,direction)