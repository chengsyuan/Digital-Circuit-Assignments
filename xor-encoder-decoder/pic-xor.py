# %%
import cv2

tip = cv2.imread('tip.jpg')
key = cv2.imread('gg.jpg')

tip_shape = tip.shape
key_shape = key.shape

print('size of tip: {}'.format(tip_shape))
print('size of key: {}'.format(key_shape))

tip = tip.reshape((-1))
key = key.reshape((-1))
print('first 1 byte of 密钥图片', tip[:1])
print('first 8 byte 被加密图片', key[:8])

# encode
pointer = 0
for i in range(tip.shape[0]):
    int_of_pixel = tip[i]

    for i in range(8):
        # get base value of key
        bit_of_tip = (int_of_pixel >> i) % 2

        key[pointer] = key[pointer] ^ bit_of_tip
        pointer += 1

print('first 8 byte of 目标图片', key[:8])
# key = key.reshape(key_shape)
#
# cv2.imwrite('encoded.jpg',key)


# decode
pointer = 0
for i in range(tip.shape[0]):
    int_of_pixel = tip[i]

    for i in range(8):
        # get base value of key
        bit_of_tip = (int_of_pixel >> i) % 2

        key[pointer] = key[pointer] ^ bit_of_tip
        pointer += 1

print('first 8 byte of 还原的目标图片', key[:8])

# key = key.reshape(key_shape)
#
# cv2.imwrite('decoded.jpg',key)