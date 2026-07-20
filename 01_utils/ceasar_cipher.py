"""
Building a Caesar Cipher

Challenge: Secret Message Encryptor & Decryptor

Create a Python script that helps you send secret messages to your friend using simple encryption.

Your program should:
1. Ask the user if they want to (E)ncrypt or (D)ecrypt a message.
2. If encrypting:
   - Ask for a message and a numeric secret key.
   - Use a Caesar Cipher (shift letters by the key value).
   - Output the encrypted message.
3. If decrypting:
   - Ask for the encrypted message and key.
   - Reverse the encryption to get the original message.

Rules:
- Only encrypt letters; leave spaces and punctuation as-is.
- Make sure the letters wrap around (e.g., 'z' + 1 → 'a').

Bonus:
- Allow uppercase and lowercase letter handling
- Show a clean interface
"""

def encrypt(message, key): 
    #codifica uma mensagem ao deslocar as letras do alfabeto de acordo com a chave,
    #preservando maiúscular, minúsculas, espaços e pontuações.
    result = ""
    for char in message: #loop pelos caracteres da mensagem
        if char.isalpha(): #define o ponto de partida na tabela ascii, 65 para A e 97 para a
            base = ord('A') if char.isupper() else ord('a') 
            #shifted faz a matemática para a nova posição:
            #ord(char) - base converte a letra para um num de 0 a 25
            #+ key aplica o deslocamento
            #% 26 usa o operador módulo pra dar a volta no alfabeto se a letra passar de Z ou z
            #+ base converte de volta para o ascii correto daquela letra
            shifted = (ord(char) - base + key) % 26 + base
            result += chr(shifted) #converte o num ascii de volta p/ caractere e une ao resultado
        else:
            result += char
    return result

def decrypt(message, key):
    #decifra a mensagem ao inverter o deslocamento da chave (chave negativa)
    return encrypt(message, -key)

print("Secret message program")
choice = input("Do you want to E or D? ").strip().lower()

#Criptografando:
if choice == "e": 
    text = input("Enter your message: \n")
    try:
        key = int(input("Enter a number between 1 and 25: "))
        encrypted = encrypt(text, key)
        print("Encrypted message: ")
        print(encrypted)
    except ValueError: #Trata a possibilidade do usuário não digitar um número
        print("Invalid Key")
#Decriptografando:
elif choice == 'd':
    text = input("Enter your encrypted message: \n")
    try:
        key = int(input("Enter a number between 1 and 25: "))
        decrypted = decrypt(text, key)
        print("Decrypted message: ")
        print(decrypted)
    except ValueError:
        print("Invalid Key")
else:  #trata a possiblidade do usuário não escolher E ou D no menu
    print("Invalid choice")

    
