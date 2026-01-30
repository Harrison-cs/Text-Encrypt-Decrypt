def encrypt(message, key):
    encrypted = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                encrypted += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            else:
                encrypted += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        else:
            encrypted += char
    return encrypted

def decrypt(encrypted_message, key):
   decrypted = ""
   for char in encrypted_message:
       if char.isalpha():
           if char.islower():
               decrypted += chr((ord(char) - ord('a') - key) % 26 + ord('a'))
           else:
               decrypted += chr((ord(char) - ord('A') - key) % 26 + ord('A'))
       else:
           decrypted += char
   return decrypted

def main():
    choice = input("Would you like to (e)ncrypt or (d)ecrypt a message? ").lower()
    if choice == 'e':
        encryptt()
    elif choice == 'd':
        decryptt()
    else:
        print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")

def encryptt():
     message = input("Enter the message to encrypt: ")
     key = int(input("Enter the encryption key (0-25): "))

     encrypted_message = encrypt(message, key)
     print("Encrypted message:", encrypted_message)

def decryptt():
    message = input("Enter the message to decrypt: ")
    key = int(input("Enter the encryption key (0-25): "))

    decrypted_message = decrypt(message, key)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()