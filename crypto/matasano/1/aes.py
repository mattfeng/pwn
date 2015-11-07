from Crypto.Cipher import AES

def decrypt_ecb(cip, key):
    cip += '\x00' * (16 - len(cip) % 16) # padding
    obj = AES.new(key, AES.MODE_ECB)
    return obj.decrypt(cip)

if __name__ == '__main__':
    cip = open('7.txt').read().replace('\n', '').strip().decode('base64')
    print decrypt_ecb(cip, 'YELLOW SUBMARINE')
