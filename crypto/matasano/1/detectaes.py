import aes
from breakrepeatingxor import hamming_d
import operator

def detect_aes(s):
    acc_edit_dist = 0
    count = 0
    for i in range(0, len(s) / 16, 2):
        block1 = s[i*16:i*16+16]
        block2 = s[i*16+16:i*16+32]
        acc_edit_dist += hamming_d(block1, block2)
        count += 1
    avg_edit_dist = acc_edit_dist / float(count)
    return avg_edit_dist

def repeated_block(text):
    '''
    Detect ECB mode. If the text has a repeated block, it means
    that the plaintext was likely encoded using ECB mode.
    '''
    block_length = 16
    blocks = [text[i*block_length:block_length*(i+1)] for i in range(int(len(text)/block_length))]
    if len(set(blocks)) != len(blocks):
        return True
    return False

if __name__ == '__main__':
    l = []
    for line in open('8.txt').readlines():
        line = line.strip().decode('hex')
        if repeated_block(line):
            print line.encode('hex')
