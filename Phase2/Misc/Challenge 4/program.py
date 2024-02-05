import codecs

a = [63, 71, 46, 125, 83, 94, 52, 44, 41, 35, 84, 103, 70, 40, 61, 99, 101, 79, 68, 55, 46, 66, 60, 36, 115, 66, 67, 57, 54, 72, 70, 113, 126, 80, 44, 110, 76, 118]
b = [76, 62, 64, 9, 40, 49, 69, 28, 26, 82, 39, 20, 53, 27, 78, 82, 87, 121, 42, 88, 64, 114, 82, 86, 64, 117, 118, 15, 89, 124, 112, 69, 15, 97, 28, 88, 60, 11]

s = input('Enter flag: ')

x = ''.join([chr(a^b) for a,b in zip(a,b)])

out = codecs.decode(x,'rot-13')

if s == out:
    print('Correct')
else:
    print('Wrong')