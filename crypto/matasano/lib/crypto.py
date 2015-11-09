from Crypto.Cipher import *
import hackercodecs
import binascii
import string
import math

# Mathematics
def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

def modinv(a, m):
    '''Computes the modular inverse.
       @arg a the number to compute the inverse of.
       @arg m the modulus.
    '''
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m

# Encodings
def hextobase64(s):
    tmp = s.decode('hex')
    ret = tmp.encode('base64')
    return ret

def base64tohex(s):
    tmp = s.decode('base64')
    ret = tmp.encode('hex')
    return ret

# String Operations
def xor(s1, s2):
    return ''.join([chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2)])

# English-esque Scoring
def alpha(s):
    return ''.join(re.findall('[a-zA-Z]+', s))

def get_letter_freq_order(s):
    freq = {}
    chars = float(len(s))
    for i in range(ord('a'), ord('z') + 1):
        freq[chr(i)] = 0
    for c in s:
        freq[c] += 1
    cipher_freq = {}

    for key, val in freq.items():
        cipher_freq[key] = val / chars * 100.0

    return cipher_freq

def printable(s):
    return all(c in string.printable for c in s)

def freq_score(s):
    if not printable(s):
        return 10**10

    s = strip_string(s.lower()) # preprocess the string for characters only, all in lowercase
    if len(s) == 0:
        return 10**10

    cipher_freq = get_letter_freq_order(s) # get the incidence of each character in percentage

    freqs_eng = {'a': 8.167, 'b':1.492, 'c':2.782, 'd':4.253, 'e':12.702, 'f':2.228,
                 'g':2.015, 'h':6.094, 'i':6.966, 'j':0.153, 'k':0.772, 'l':4.025, 'm':2.406,
                 'n':6.749, 'o':7.507, 'p':1.929, 'q':0.095, 'r':5.987, 's':6.327, 't':9.056,
                 'u':2.758, 'v':0.978, 'w':2.360, 'x':0.150, 'y':1.974, 'z':0.074}

    # difference between actual english and cipher freq: higher is worse
    neg_score = 0
    for key, val in freqs_eng.items():
        neg_score += abs(cipher_freq[key] - val)

    return neg_score

# PKCS#7 Padding
def pkcs_pad(message, blocksize):
    padded = message
    if len(message) % blocksize == 0:
        return padded
    pad_amt = blocksize - (len(message) % blocksize)
    pad_val = chr(pad_amt)
    padded += pad_val * pad_amt
    return padded


