__author__ = "Omri Naim"

#This program is implementin bruth-force attack
#Input: a cipher text
#Output: plain text 

letters="abcdefghijklmnopqrstuvwxyz"
cipher=None
while cipher is None:
	cipher = input("Enter your cipher text: ")
	for symbol in cipher:
		if letters.find(symbol) == -1 and symbol != " ":
			print("Cipher text can be only from the alphabet..")
			cipher=None
			break;
for key in range(len(letters)):
	decipher=""
	for symbol in cipher:
		if(symbol==" "):
			decipher=decipher+" "
			continue;
		#find the locatin of the symbol in the alphabet
		#decrease the key from the positoin to shift the letter
		num = letters.find(symbol)
		num = num-key
		#if the shift position is negative ,we add the len of alphabet in order to run cyclic.
		if(num<0):
			num=num+len(letters)
		decipher=decipher+letters[num]
	print("Key #%s: %s" %(key,decipher))
	
