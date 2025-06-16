from PIL import Image

org_img = Image.open('original_image.png')
org_pixelMap = org_img.load()
enc_img = Image.new(org_img.mode, org_img.size)
enc_pixelsMap = enc_img.load()

msg = input("Enter the message:\t")
msg_index = 0
msg_len = len(msg)

for row in range(org_img.size[0]):
    for col in range(org_img.size[1]):
        pixel = org_pixelMap[row, col]
        r = pixel[0]
        g = pixel[1]
        b = pixel[2]

        if row == 0 and col == 0:
            ascii_val = msg_len
            enc_pixelsMap[row, col] = (ascii_val, g, b)
        elif msg_index < msg_len:
            c = msg[msg_index]
            ascii_val = ord(c)
            enc_pixelsMap[row, col] = (ascii_val, g, b)
            msg_index += 1
        else:
            enc_pixelsMap[row, col] = (r, g, b)

org_img.close()
enc_img.show()
enc_img.save("encrypted_image.png")
enc_img.close()
