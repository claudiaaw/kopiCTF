''' PIL_HideText1.py
hide a short message (255 char max) in an image
the image has to be .bmp or .png format
and the image mode has to be 'RGB'
'''
from PIL import Image
def encode_image(img, msg):
    """
    use the red portion of an image (r, g, b) tuple to
    hide the msg string characters as ASCII values
    red value of the first pixel is used for length of string
    """
    char_length = len(msg)
    # limit length of message to 255
    if char_length > 255:
        print("text too long! (don't exeed 255 characters)")
        return False
    if img.mode != 'RGB':
        print("image mode needs to be RGB")
        return False
    # use a copy of image to hide the text in
    encoded = img.copy()
    width, height = img.size
    index = 0

    # convert flag to bits
    flagBytes_str = ''.join(format(ord(x), 'b') for x in msg)
    length = len(flagBytes_str) # change length to length of bits

    print (flagBytes_str)
    print (length)

    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
            byte_r, byte_g, byte_b = format(r, "08b"), format(g, "08b"), format(b, "08b")
            #print (byte_r, byte_g, byte_b)
            if index <= length-1:
                c = flagBytes_str[index]
                print (c)
                #asc = ord(c)
                #byte_asc = format(asc, "08b")
                #print (byte_asc)
                new_byte_r = ""
                new_byte_r = byte_r[0:-1] + c
            else:
                new_byte_r = byte_r
            new_byte_r = int(new_byte_r, 2)
            encoded.putpixel((col, row), (new_byte_r, g , b))
            index += 1
    return encoded

def binStrToInt(binary_str):
    length = len(binary_str)
    num = 0
    for i in range(length):
        num = num + int(binary_str[i])
        num = num * 2
        return num / 2

def decode_image(img):
    """
    check the red portion of an image (r, g, b) tuple for
    hidden message characters (ASCII values)
    """
    width, height = img.size
    msg = ""
    index = 0
    for row in range(height):
        for col in range(width):
            try:
                r, g, b = img.getpixel((col, row))
            except ValueError:
                # need to add transparency a for some .png files
                r, g, b, a = img.getpixel((col, row))
            # first pixel r value is length of message
            if row == 0 and col == 0:
                length = r
            elif index <= length:
                msg += chr(r)
            index += 1
    return msg
# pick a .png or .bmp file you have in the working directory
# or give full path name
original_image_file = "image.png"
#original_image_file = "Beach7.bmp"
img = Image.open(original_image_file)
# image mode needs to be 'RGB'
print(img, img.mode)  # test
# create a new filename for the modified/encoded image
encoded_image_file = "enc_" + original_image_file
# don't exceed 255 characters in the message
secret_msg = """kopi{in53cur3}"""
print(len(secret_msg))  # test
img_encoded = encode_image(img, secret_msg)
if img_encoded:
    # save the image with the hidden text
    img_encoded.save(encoded_image_file)
    print("{} saved!".format(encoded_image_file))
    # view the saved file, works with Windows only
    # behaves like double-clicking on the saved file
    import os
    os.startfile(encoded_image_file)
    '''
    # or activate the default viewer associated with the image
    # works on more platforms like Windows and Linux
    import webbrowser
    webbrowser.open(encoded_image_file)
    '''
    # get the hidden text back ...
    img2 = Image.open(encoded_image_file)
    hidden_text = decode_image(img2)
    print("Hidden text:\n{}".format(hidden_text))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
##### edited version#######
from PIL import Image 

def encode_image(img,binInd):
	length = len(binInd)
	
	if img.mode!='RGB':
		print('image mode not RGB')
		return False
	encoded = img.copy()
	width, height = img.size 
	index =0
	for row in range(height):
		for col in range(width):
			r,g,b = img.getpixel((col,row))
			r1 = bin(r)
 
        if row == 0 and col ==0 and index<length:
				asc = length
			elif index<= length:
				c = msg[index-1]
				asc = ord(c)
			else:
				asc =r
			encoded.putpixel((col,row),(asc,g,b))
			index+=1
	return encoded

	
def decode_image(img):
	 
    width, height = img.size
    msg = ""
    index = 0
    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))	
            # first pixel r value is length of message
            if row == 0 and col == 0:
                length = r
            elif index <= length:
                msg += chr(r)

            index += 1
    return msg
	
secret_msg= "usnsgrp{ml53myp3}"
individual = list(secret_msg)
binInd =[]
for i in individual:
	temp = ord(i)
	binTemp = bin(temp)[2:].zfill(8)
	tempList = list(binTemp)
	for j in tempList:
		binInd.append(j)

img = Image.open('randomImage.png')
encodedImg = encode_image(img, binInd)

if encodedImg:
	encodedImg.save('newrandomImage.png')
	
	
img2 = Image.open('newrandomImage.png')
hidden_text =decode_image(img2)
print('Hidden text:\n{}'.format(hidden_text))
