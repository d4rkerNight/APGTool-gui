#!/usr/bin/env python
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
# https://github.com/t3sl4/
#
#

import os
import sys
import string
import apg_de
from apg_de import *

if (sys.version_info[:2] < (3,0)):
  import tkFileDialog
  from Tkinter import *
else:
  import tkinter.filedialog
  from tkinter import *

# encrypt
bsize = key = username = passfor = saveto = spass = pad = dec = low = upp = pun = ''
sel_spass = sel_pad = sel_dec = sel_low = sel_upp = sel_pun = ''
ce = cce = une = pfe = ''

# decrypt
dkey = dpad = dpass = ''
dke = lbdata = ''
sel_dpad = ''

def cvalidate(centry):
  global ce
  
  ce = centry
  word_len = len(centry)
  if word_len != int(bsize.get()):
    error = Label(root, fg = 'red', text = 'Cipher[%s] < %s' % (word_len, bsize.get()))
    error.pack()
    error.place(x = 110, y = 200)
    return False
  else:
    #TODO error.pack_forget()
    ok = Label(root, fg = 'dark green', text = 'Cipher[%s]        ' % (bsize.get()))
    ok.pack()
    ok.place(x = 110, y = 200)
    return True

def ccvalidate(ccentry):
  global cce
  
  cce = ccentry
  if ccentry != key.get():
    error = Label(root, fg = 'red', text = 'Cipher does not match')
    error.pack()
    error.place(x = 110, y = 245)
    return False
  else:
    #TODO error.pack_forget()
    ok = Label(root, fg = 'dark green', text = 'Cipher match               ')
    ok.pack()
    ok.place(x = 110, y = 245)
    return True

def unvalidate(unentry):
  global une

  une = unentry
  if unentry == '':
    error = Label(root, fg = 'red', text = 'Enter usename')
    error.pack()
    error.place(x = 110, y = 290)
    return False
  else:
    #TODO error.pack_forget()
    ok = Label(root, text = '                        ')
    ok.pack()
    ok.place(x = 110, y = 290)
    return True

def pfvalidate(pfentry):
  global pfe

  pfe = pfentry
  if pfentry == '':
    error = Label(root, fg = 'red', text = 'Enter description')
    error.pack()
    error.place(x = 110, y = 335)
    return False
  else:
    #TODO error.pack_forget()
    ok = Label(root, text = '                           ')
    ok.pack()
    ok.place(x = 110, y = 335)
    return True

def stvalidate(sttext):
  if sttext == '':
    error = Label(root, fg = 'red', text = 'Choice directory')
    error.pack()
    error.place(x = 110, y = 380)
    return False
  else:
    #TODO error.pack_forget()
    ok = Label(root, text = '                           ')
    ok.pack()
    ok.place(x = 110, y = 380)
    return True

def dkvalidate(dkentry):
  global dke

  dke = dkentry
  if dkentry == '':
    error = Label(root, fg = 'red', text = 'Enter Key')
    error.pack()
    error.place(x = 420, y = 320)
    return False
  else:
    #TODO error.pack_forget()
    ok = Label(root, text = '                        ')
    ok.pack()
    ok.place(x = 110, y = 290)
    return True

def validate_enc():
  global ce, cce, une, pfe, saveto
  
  spin_dec()
  spin_low()
  spin_upp()
  spin_pun()
  padding()
  radio()
  if cvalidate(ce) == ccvalidate(cce) == unvalidate(une) == pfvalidate(pfe) == stvalidate(saveto) == True:
    apg_de.makepasswd(bsize.get(), key.get(), spass, username.get(), passfor.get(), saveto, pad, dec, low, upp, pun)
    enctext = Text(root, fg = 'dark green', height = 1, width = 30, wrap = NONE)
    enctext.insert(INSERT, apg_de.passwd)
    enctext.pack()
    enctext.place(x = 90, y = 460)
  #else:
    #TODO handle error

def validate_dcpt():
  global dkey, dpad, dpass

  dcpad()
  if dkey is not None and dpad is not None and dpass is not None:
    apg_de.decryptpasswd(dkey.get(), dpad, dpass)
    dctext = Text(root, fg = 'dark green', height = 1, width = 41, wrap = NONE)
    dctext.insert(INSERT, apg_de.decoded)
    dctext.pack()
    dctext.place(x = 420, y = 435)
  #else:
    #TODO handle error

def radio():
  global spass
  spass = sel_spass.get()
def padding():
  global pad
  pad = sel_pad.get()
def spin_dec():
  global dec
  dec = sel_dec.get()
def spin_low():
  global low
  low = sel_low.get()
def spin_upp():
  global upp
  upp = sel_upp.get()
def spin_pun():
  global pun
  pun = sel_pun.get()
def dcpad():
  global dpad
  dpad = sel_dpad.get()

def toolbar():
  menu = Menu(root)
  root.config(menu = menu)
  filemenu = Menu(menu)
  menu.add_cascade(label = 'File', menu = filemenu)
  filemenu.add_separator()
  filemenu.add_command(label = 'Exit', command = root.destroy)
  helpmenu = Menu(menu)
  menu.add_cascade(label = 'Help', menu = helpmenu)
  helpmenu.add_command(label = 'About', command = root.destroy)

def enc_button():  
  encbut = Button(root, text = "Encrypt", command = validate_enc)
  encbut.pack(side = LEFT)
  encbut.place(x = 10, y = 460)

def dcpt_button():
  dcptbut = Button(root, text = "Decrypt", command = validate_dcpt)
  dcptbut.pack(side = LEFT)
  dcptbut.place(x = 350, y = 460)

def browse():
  global saveto

  filedest = tkFileDialog.asksaveasfilename(defaultextension = txt, parent = root, title = 'Choose a file')
  sttext = Text(root, fg = 'dark green', height = 1, width = 38, wrap = NONE)
  sttext.insert(INSERT, filedest)
  sttext.pack()
  sttext.place(x = 10, y = 433)
  saveto = filedest

def openfile():  
  file = tkFileDialog.askopenfile(parent=root,mode='r',title='Choose a file')
  data = file.readlines()
  file.close()
  data = [dt.rstrip() for dt in data]
  lb_pass(data)

def enc_option():
  global sel_spass
  global sel_dec
  global sel_low
  global sel_upp
  global sel_pun
  
  sel_radio = StringVar()
  sel_spin_dec  = StringVar()
  sel_spin_dec.set('4')
  sel_spin_low  = StringVar()
  sel_spin_low.set('4')
  sel_spin_upp  = StringVar()
  sel_spin_upp.set('4')
  sel_spin_pun  = StringVar()
  sel_spin_pun.set('4')
  
  label1 = Label(root, text = 'Password:')
  label1.pack()
  label1.place(x = 10, y = 10)
  label2 = Label(root, text = 'Start with')
  label2.pack()
  label2.place(x = 120, y = 10)
  label3 = Label(root, text = 'Number of')
  label3.pack()
  label3.place(x = 220, y = 10)
  
  separator1 = Frame(root, height = 2, bd = 1, relief = SUNKEN)
  separator1.pack()
  separator1.place(width = 275, x = 10, y = 28)
  
  rlabel = Label(root, text = 'Random')
  rlabel.pack()
  rlabel.place(x = 10, y = 30)
  radio1 = Radiobutton(root, variable = sel_radio, value = 'r')
  radio1.select()
  radio1.pack()
  radio1.place(x = 135, y = 30)
  
  dlabel = Label(root, text = 'Decimals')
  dlabel.pack()
  dlabel.place(x = 10, y = 50)
  radio2 = Radiobutton(root, variable = sel_radio, value = 'd', command = radio)
  radio2.pack()
  radio2.place(x = 135, y = 50)
  dspin = Spinbox(root, from_ = 0, to = 10, width = 2, textvariable = sel_spin_dec, command = spin_dec)
  dspin.pack()
  dspin.place(x = 240, y = 48)
  
  llabel = Label(root, text = 'Lowercases')
  llabel.pack()
  llabel.place(x = 10, y = 70)
  radio3 = Radiobutton(root, variable = sel_radio, value = 'l', command = radio)
  radio3.pack()
  radio3.place(x = 135, y = 70)
  lspin = Spinbox(root, from_ = 0, to = 10, width = 2, textvariable = sel_spin_low, command = spin_low)
  lspin.pack()
  lspin.place(x = 240, y = 68)
  
  ulabel = Label(root, text = 'Uppercases')
  ulabel.pack()
  ulabel.place(x = 10, y = 90)
  radio4 = Radiobutton(root, variable = sel_radio, value = 'u', command = radio)
  radio4.pack()
  radio4.place(x = 135, y = 90)
  uspin = Spinbox(root, from_ = 0, to = 10, width = 2, textvariable = sel_spin_upp, command = spin_upp)
  uspin.pack()
  uspin.place(x = 240, y = 88)
  
  plabel = Label(root, text = 'Punctuations')
  plabel.pack()
  plabel.place(x = 10, y = 110)
  radio5 = Radiobutton(root, variable = sel_radio, value = 'p', command = radio)
  radio5.pack()
  radio5.place(x = 135, y = 110)
  pspin = Spinbox(root, from_ = 0, to = 10, width = 2, textvariable = sel_spin_pun, command = spin_pun)
  pspin.pack()
  pspin.place(x = 240, y = 108)
  
  sel_spass = sel_radio
  sel_dec = sel_spin_dec
  sel_low = sel_spin_low
  sel_upp = sel_spin_upp
  sel_pun = sel_spin_pun

def cipher_frame():
  global bsize
  global key
  global sel_pad
  
  var_padoptm = StringVar()
  var_padoptm.set('&')
  var_blcoptm = StringVar()
  var_blcoptm.set('32')
  var_digits = list(string.punctuation)
  
  padlabel = Label(root, text = 'Padding')
  padlabel.pack()
  padlabel.place(x = 10, y = 148)
  padoptm = OptionMenu(root, var_padoptm, *var_digits)
  padoptm.pack()
  padoptm.place(x = 10, y = 171)
  sel_pad = var_padoptm

  blocktext = Label(root, text = 'Key Size')
  blocktext.pack()
  blocktext.place(x = 80, y = 148)
  blcoptm = OptionMenu(root, var_blcoptm, '16', '24', '32')
  blcoptm.pack(fill = X, expand = True)
  blcoptm.place(x = 80, y = 171)
  bsize = var_blcoptm
  
  clabel = Label(root, text = 'Enter Key')
  clabel.pack()
  clabel.place(x = 10, y = 223)
  ccmd = root.register(cvalidate), '%s'
  centry = Entry(root, bd = 3, show = '*', validate = 'focusout', validatecommand = ccmd)
  key = centry
  centry.pack()
  centry.place(x = 110, y = 220)

def conf_cipher():  
  cclabel = Label(root, text = 'Confirm Key')
  cclabel.pack()
  cclabel.place(x = 10, y = 268)
  cccmd = root.register(ccvalidate), '%s'
  ccentry = Entry(root, bd = 3, show = '*', validate = 'focusout', validatecommand = cccmd)
  ccentry.pack()
  ccentry.place(x = 110, y = 265)

def username():
  global username
  
  unlabel = Label(root, text = 'Username')
  unlabel.pack()
  unlabel.place(x = 10, y = 313)
  uncmd = root.register(unvalidate), '%s'
  unentry = Entry(root, bd = 3, validate = 'focusout', validatecommand = uncmd)
  username = unentry
  unentry.pack()
  unentry.place(x = 110, y = 310)

def pass_for():
  global passfor
  
  pflabel = Label(root, text = 'Password For')
  pflabel.pack()
  pflabel.place(x = 10, y = 358)
  pfcmd = root.register(pfvalidate), '%s'
  pfentry = Entry(root, bd = 3, validate = 'focusout', validatecommand = pfcmd)
  passfor = pfentry
  pfentry.pack()
  pfentry.place(x = 110, y = 355)

def save_to():
  stlabel = Label(root, text = 'Save Data To')
  stlabel.pack()
  stlabel.place(x = 10, y = 403)
  savebut = Button(root, text = 'Browse', command = browse)
  savebut.pack()
  savebut.place(x = 110, y = 398)

def bdecrypt():
  global dkey
  global dpass
  global decoded
  global sel_dpad

  var_padoptm = StringVar()
  var_padoptm.set('&')
  var_punct = list(string.punctuation)
  
  separator2 = Frame(root, height = 720, width = 2, bd = 1, relief = SUNKEN)
  separator2.pack()
  separator2.place(x = 340, y = 0)
  dfile = Button(root, text = 'Open File', command = openfile)
  dfile.pack()
  dfile.place(x = 350, y = 250)

  dulabel = Label(root, text = 'Password')
  dulabel.pack()
  dulabel.place(x = 350, y = 300)

  dklabel = Label(root, text = 'Enter Key')
  dklabel.pack()
  dklabel.place(x = 350, y = 345)
  dkcmd = root.register(dkvalidate), '%s'
  dkentry = Entry(root, bd = 3, show = '*', validate = 'focusout', validatecommand = dkcmd)
  dkey = dkentry
  dkentry.pack()
  dkentry.place(x = 420, y = 342)
  
  dpadlabel = Label(root, text = 'Padding')
  dpadlabel.pack()
  dpadlabel.place(x = 350, y = 390)
  dpadoptm = OptionMenu(root, var_padoptm, *var_punct)
  dpadoptm.pack()
  dpadoptm.place(x = 420, y = 388)
  sel_dpad = var_padoptm

  dcpass = Label(root, text = 'Password')
  dcpass.pack()
  dcpass.place(x = 350, y = 435)  
  
def lb_pass(data):
  global lbdata
  
  lbdata = Listbox(root, height = 14, width = 45)
  lbdata.pack()
  lbdata.place(x = 350, y = 28)
  for item in data:
    lbdata.insert(END, item)
  lbdata.bind('<ButtonRelease-1>', get_selection)

def get_selection(event):
  global lbdata
  global dpass
  
  sel = lbdata.curselection()
  dsel_data = lbdata.get(int(sel[0]))
  dsel_pass = dsel_data.split('::', 2)
  dpass = dsel_pass[2]
  dutext = Text(root, fg = 'dark green', height = 1, width = 41, wrap = NONE)
  dutext.insert(INSERT, dpass)
  dutext.pack()
  dutext.place(x = 420, y = 297)
    

if __name__ == '__main__':
  root = Tk()
  root.title('Advanced Password Generator Tool')
  root.geometry('720x490')
  toolbar()
  enc_button()
  enc_option()
  cipher_frame()
  conf_cipher()
  username()
  pass_for()
  save_to()
  bdecrypt()
  dcpt_button()
  root.mainloop()
