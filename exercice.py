#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_first_part_of_name(name):
	a= (name.capitalize()).split("-")
	return a[0]

def get_random_sentence(animals, adjectives, fruits):
	random_animal = animals[random.randrange(len(animals))]
	random_adjective = adjectives[random.randrange(len(adjectives))]
	random_fruits = fruits[random.randrange(len(fruits))]
	return f"Aujourd'hui, j'ai vu un {random_animal} s'emparer d'un panier {random_adjective} plein de {random_fruits}."

def encrypt(text, shift):
	encrypted_text = ""
	shift %= 26
	for i in text:
		if i.isupper():
			if (ord(i) + shift) > ord("Z"):
				encrypted_text += chr(ord(i)-26+shift)
			else:
				encrypted_text += chr(ord(i)+shift)
		elif i.islower():
			if (ord(i) + shift) > ord("z"):
				encrypted_text += chr(ord(i)-26+shift)
			else:
				encrypted_text += chr(ord(i)+shift)
		else:
			encrypted_text += i
	return encrypted_text.upper()

def decrypt(encrypted_text, shift):
	decrypted_text = ""
	shift %= 26
	for i in encrypted_text:
		if i.isupper():
			if (ord(i) - shift) < ord("A"):
				decrypted_text += chr(ord(i)+26-shift)
			else:
				decrypted_text += chr(ord(i)-shift)
		elif i.islower():
			if (ord(i) - shift) > ord("a"):
				decrypted_text += chr(ord(i)+26-shift)
			else:
				decrypted_text += chr(ord(i)-shift)
		else:
			decrypted_text += i
	return decrypted_text.lower()


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))
	
	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
