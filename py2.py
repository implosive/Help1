print "Welcome to text encrypter 1.0!"
text = str(raw_input('What message would you like to encrypt? '))
variance = int(raw_input('By how much would you like to step the text? '))
encoded = ""
textLength = len(text)
alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print textLength
count = 0
while(count < textLength):
	print count
	characterPush = text[count]
	newText = []
	newText.extend(characterPush)
	print characterPush
	count = count + 1
print newText