from collections import deque

class caesarCipher(object):
	
	def __init__(self, message, key):
		self.message = message
		self.key = key
		
	def encrypt(self):
		encryptedMessage = []
	
		for letter in self.message.lower():
			if letter.isalpha():
				alphabet = deque('abcdefghijklmnopqrstuvwxyz')
				pos = alphabet.index(letter)
				alphabet.rotate(-pos)
				encryptedMessage.append(alphabet[self.key-1])
			else:
				encryptedMessage.append(' ')
		
		return ''.join(encryptedMessage)
	
	def decrypt(self):
		encryptedMessage = []
	
		for letter in self.message.lower():
			if letter.isalpha():
				alphabet = deque('abcdefghijklmnopqrstuvwxyz')
				pos = alphabet.index(letter)
				alphabet.rotate(-pos)
				alphabet = list(reversed(alphabet))
				encryptedMessage.append(alphabet[self.key-2])
			else:
				encryptedMessage.append(' ')
		
		return ''.join(encryptedMessage)

def main():
	message = input("Input a message to encrypt or decrypt\n")
	key = int(input("Input the key to be used for encryption/decryption\n"))
	
	cipher = caesarCipher(message, key)
	
	choice = input("What would you like to do with the message? 1. Encrypt 2. Decrypt\n")
	
	if choice == '1':
		print("Your encrypted message =", cipher.encrypt())
		
	elif choice == '2':
		print("Your decrypted message =", cipher.decrypt())

if __name__ == '__main__':
	main()
