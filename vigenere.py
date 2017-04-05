original=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
##key=key
encryptionList = [['k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j'],['e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d'],['y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x']]


plaintext="asdfqwerpofsdtrylookingfurtherqwperokeorkalmosttherelkasdfposdfjpasndflasdfnctfisfunapsdfkasdfrkwapung(kopictf{in53cur3})umpezmdmpzemdmpzwahadungfufcizmsaojmmmqxntygqmmmay"



##encode###
def encrypt(text):
	plainList = list(text)
	ciphertext=""
	for i in range(0,len(plainList)):
		if plainList[i].isalpha() ==True:
			org = original.index(plainList[i])
			if i%3==0:
				ciphertext+= encryptionList[0][org]
			elif i%3==1:
				ciphertext+= encryptionList[1][org]
			
			else:
				ciphertext+= encryptionList[2][org]
		else:
			ciphertext+=plainList[i]

	return(ciphertext)


##decode##
def decrypt(text):
	plainList = list(text)
	originaltext = ""
	position =0
	for i in range(0,len(plainList)):
		if plainList[i].isalpha()==True:
			if i%3==0:
				position = encryptionList[0].index(plainList[i])
			elif i%3==1:
				position = encryptionList[1].index(plainList[i])
			else:
				position = encryptionList[2].index(plainList[i])
			originaltext+=original[position]	
		else:
			originaltext+=plainList[i]
	return(originaltext)			
	
encrypted = encrypt(plaintext)
decrypted = decrypt(encrypted)

print(encrypted)
print(decrypted)
