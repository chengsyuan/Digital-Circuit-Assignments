# %%
tips = 'ABSTRACT Relevance estimation is among the most important tasks' \
       ' in the rank- ing of search results. Current relevance estimation' \
       ' methodologies mainly concentrate on text matching between the query' \
       ' and Web documents, link analysis and user behavior models.'
print('tips = {}'.format(tips))

key = 'user:root,pwd:e3d8h12e'
print('key = {}'.format(key))

secret = ''

# experiment1: 对tip中每个字符的最后一位进行xor

# encoder
pointer = 0
for char in key:
    for i in range(8):
        # get base value of key
        bit_of_key = (ord(char) >> i) % 2

        # get ord of tips
        int_of_tips = ord(tips[pointer])

        secret += chr(int_of_tips ^ bit_of_key)
        pointer += 1
print('secret = {}'.format(secret))

# decoder
pointer = 0
key_decode = ''
for start in range(0, len(secret), 8):
    t = 0
    for i in range(8):
        # get last bit
        last_bit_of_secret = ord(secret[start + i]) % 2
        last_bit_of_tip = ord(tips[start + i]) % 2

        # decode by xor
        bit_of_key = last_bit_of_secret ^ last_bit_of_tip
        base = (1 << i)
        t += bit_of_key * base

    # encode int to acsii char
    key_decode += chr(t)
print('key_decode = {}'.format(key_decode))