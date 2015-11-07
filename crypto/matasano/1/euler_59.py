import repeatingxor as rx
import breakrepeatingxor as brx

data = open('p059_cipher.txt').read().strip().split(',')
enc = ''.join([chr(int(i)) for i in data])

brx.break_xor(enc)

quit()
# key is 'god'
key = 'god'
m = rx.rep_xor(enc, key).decode('hex')
print m

acc = 0
for c in m:
    acc += ord(c)

print 'ANS:', acc
