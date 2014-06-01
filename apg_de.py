#!/usr/bin/env python2
#
#
#
# by t3sl4/tesl23
#

import base64
import random
import string
from Crypto.Cipher import AES

decoded = ''

def makepasswd(bsize, key, spass, username, passfor, saveto, pad, dec, low, upp, pun):
  if bsize == '32':
    bsize = 32
  elif bsize == '16':
    bsize = 16
  elif bsize == '24':
    bsize = 24
  else:
    #TODO handle error
    print 'Error 1'

  passwd = ''
  if int(dec) > 0:
    i = 0
    while i < int(dec):
      passwd += ''.join(random.choice(string.digits))
      i += 1
  if int(low) > 0:
    i = 0
    while i < int(low):
      passwd += ''.join(random.choice(string.ascii_lowercase))
      i += 1
  if int(upp) > 0:
    i = 0
    while i < int(upp):
      passwd += ''.join(random.choice(string.ascii_uppercase))
      i += 1
  if int(pun) > 0:
    i = 0
    while i < int(pun):
      passwd += ''.join(random.choice(string.punctuation))
      i += 1

  shuffle = list(passwd)
  random.shuffle(shuffle)
  passwd = ''.join(shuffle)
  
  schar = spass
  if schar == 'r':
    passwd = passwd
  elif schar is 'd':
    cnt = 0
    passwd = list(passwd)
    for d in passwd:
      if d in string.digits:
        position = cnt
        break
      cnt += 1
    passwd.insert(0, passwd.pop(cnt))
    passwd = ''.join(passwd)
  elif schar is 'l':
    cnt = 0
    passwd = list(passwd)
    for l in passwd:
      if l in string.ascii_lowercase:
        position = cnt
        break
      cnt += 1
    passwd.insert(0, passwd.pop(cnt))
    passwd = ''.join(passwd)
  elif schar is 'u':
    cnt = 0
    passwd = list(passwd)
    for u in passwd:
      if u in string.ascii_uppercase:
        position = cnt
        break
      cnt += 1
    passwd.insert(0, passwd.pop(cnt))
    passwd = ''.join(passwd)
  elif schar is 'p':
    cnt = 0
    passwd = list(passwd)
    for p in passwd:
      if p in string.punctuation:
        position = cnt
        break
      cnt += 1
    passwd.insert(0, passwd.pop(cnt))
    passwd = ''.join(passwd)
  else:
    #TODO handle error
    print ''
    print 'Wrong choice!'

  padd = lambda s: s + (bsize - len(s) % bsize) * pad
  encAES = lambda c, s: base64.b64encode(c.encrypt(padd(s)))
  cipher = AES.new(key)
  encoded = encAES(cipher, passwd)
  ofile = open(saveto, 'a')
  ofile.write(passfor + '::'+ username + '::' + encoded + '\n')
  ofile.close()

def decryptpasswd(dkey, dpad, dpass):
  global decoded
  
  decAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(dpad)
  cipher = AES.new(dkey)
  decoded = decAES(cipher, dpass)
