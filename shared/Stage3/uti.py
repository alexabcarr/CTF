data = ''
key = ''

enc = ''
for x in range(len(data)):
	enc+= chr(ord(data[x]) ^ ord(key[x%len(key)]))
#print(enc)


hint = open("","")
dec = ''
for x in range(len(enc)):
	dec+= chr(ord(enc[x]) ^ ord(key[x%len(key)]))

print(dec)

hint.close()

