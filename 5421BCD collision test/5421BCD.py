"""
edited v2
电计1701
应承轩
201785071
"""
import pprint

if __name__ == '__main__':
    print('5421BCD collision test')

    base_5421BCD = [5, 4, 2, 1]
    base_binary = [8, 4, 2, 1]

    dec_to_5421BCD = {}

    for i in range(16):
        num = 0
        for (index, base) in enumerate(base_binary):
            if i & base:
                num += base_5421BCD[index]

        dec_to_5421BCD.setdefault(num, [])

        s = str(bin(i))[2:].rjust(4, '0')
        dec_to_5421BCD[num].append(s)

    print('结果显示数字5、6、7在5421BCD编码下具有重码')

    for k in list(dec_to_5421BCD.keys()):
        if k >= 10:
            del dec_to_5421BCD[k]

    pprint.pprint(dec_to_5421BCD)
