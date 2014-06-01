#!/usr/bin/env python2
#
# Copyright (C) <2014> <t3sl4/tesla23>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>
#
# --------------------------------------------------------------------
# Generate random password
# && encrypt it into a file
# || decrypt an existing password
#
# Project will be maintained @
#
# https://github.com/t3sl4/apg-tool
#
#

import base64
import random
import string
from Crypto.Cipher import AES

passwd = ''
decoded = ''

def makepasswd(bsize, key, spass, username, passfor, saveto, pad, dec, low, upp, pun):
  global passwd

  if bsize == '32':
    bsize = 32
  elif bsize == '16':
    bsize = 16
  elif bsize == '24':
    bsize = 24
  else:
    #TODO handle error
    print 'Error 1'

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
