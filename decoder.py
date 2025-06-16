from PIL import Image

enc_img = Image.open('encrypted_image.png')
enc_pixelMap = enc_img.load()

msg = ""
msg_index = 0

for row in range(enc_img.size[0]):
    for col in range(enc_img.size[1]):
        pixel = enc_pixelMap[row, col]
        r = pixel[0]

        if row == 0 and col == 0:
            msg_len = r
        elif msg_index < msg_len:
            msg += chr(r)
            msg_index += 1

enc_img.close()

print("The hidden message is:\n")
print(msg)
