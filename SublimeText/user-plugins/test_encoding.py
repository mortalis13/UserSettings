
import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno

encs = [
  'ascii', 'big5', 'big5hkscs', 'cp037', 'cp424', 'cp437', 'cp500', 'cp720', 'cp737', 'cp775', 'cp850', 'cp852', 'cp855', 'cp856', 'cp857', 'cp858', 'cp860', 'cp861', 'cp862', 'cp863', 'cp864', 'cp865', 'cp866', 'cp869', 'cp874', 'cp875', 'cp932', 'cp949', 'cp950', 'cp1006', 'cp1026', 'cp1140', 'cp1250', 'cp1251', 'cp1252', 'cp1253', 'cp1254', 'cp1255', 'cp1256', 'cp1257', 'cp1258', 'euc_jp', 'euc_jis_2004', 'euc_jisx0213', 'euc_kr', 'gb2312', 'gbk', 'gb18030', 'hz', 'iso2022_jp', 'iso2022_jp_1', 'iso2022_jp_2', 'iso2022_jp_2004', 'iso2022_jp_3', 'iso2022_jp_ext', 'iso2022_kr', 'latin_1', 'iso8859_2', 'iso8859_3', 'iso8859_4', 'iso8859_5', 'iso8859_6', 'iso8859_7', 'iso8859_8', 'iso8859_9', 'iso8859_10', 'iso8859_11', 'iso8859_13', 'iso8859_14', 'iso8859_15', 'iso8859_16', 'johab', 'koi8_r', 'koi8_u', 'mac_cyrillic', 'mac_greek', 'mac_iceland', 'mac_latin2', 'mac_roman', 'mac_turkish', 'ptcp154', 'shift_jis', 'shift_jis_2004', 'shift_jisx0213', 'utf_32', 'utf_32_be', 'utf_32_le', 'utf_16', 'utf_16_be', 'utf_16_le', 'utf_7', 'utf_8', 'utf_8_sig'
]

class TestEncodingCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    print('Start Test ...\n')
    self.test4(edit)
  
  
  def test(self):
    text = 'Ã¡bcÃ³'
    total = ''
    
    for enc_enc in encs:
      for enc_dec in encs:
        res = '##ERROR##'
        
        try:
          res = text.encode(enc_enc).decode(enc_dec)
        except:
          print()
          
        total += '[' + enc_enc + ' - ' + enc_dec + ']: ' + res + '\n'
        # print('[' + enc_enc + ' - ' + enc_dec + ']: ' + res)
    
    sublime.set_clipboard(total)
    
    
  def test8(self):
    s = 'lÃ¡grimas'
    res = s.encode('latin1').decode('utf8')
    print(res)
    
    
  def test7(self):
    print(b'\x00\xa4'.decode('utf_16_be'))
    print(b'\x00\xa6'.decode('utf_16_be'))
    
  
  def test6(self):
    codes = [
      "81",
      "8d",
      "8f",
      "90",
      "9d"
    ]
    
    # path = 'path\\to\\folder'
    # infile = 'path\\to\\file'
    # file = open(infile, 'r', encoding='utf8')
    # # syms = file.readlines()
    # syms = file.read()
    # file.close()
    
    # if not os.path.exists(path):
    #   os.makedirs(path)
    # file = open(path + "qwe", 'w')
    # file.close()
    
    # namelist = syms.split('\n')
    # print(namelist)
    
    path = 'path\\to\\folder'
    
    for code in codes:
      subpath = path + code + "\\"
      infile = 'path\\to\\folder' + code + '.txt'
      
      file = open(infile, 'r', encoding='utf8')
      syms = file.read()
      namelist = syms.split('\n')
      file.close()
      
      for name in namelist:
        if not os.path.exists(subpath):
          os.makedirs(subpath)
        name = 'z' + name + 'z'
        file = open(subpath + name, 'w')
        # file = open(subpath + name, 'w', encoding='utf8')
        file.close()
      
    print('\nfinish')
    
    
    # for code in codes:
    #   out = ""
    #   codeh = int(code, 16)
      
    #   for i in range(0, 256):
    #     try:
    #       res = bytes([i, codeh]).decode()
    #       resf = res + " - " + str(i) + " - " + hex(i)[2:] + " " + code
    #       # out += resf + "\n"
    #       out += res + "\n"
          
    #       # res1 = str(i) + " - " + res + " - \\" + hex(i)[1:] + "\\x" + code
    #       # print(res1)
    #     except Exception as e:
    #       x=1
    #       # print(str(i) + " - " + str(e))
          
    #   outfile = "path\\to\\folder" + code + ".txt"
    #   file = open(outfile, 'w', encoding='utf8')
    #   file.write(out)
    #   file.close()
      
    # print('finish')
    
    
    # out = ""
    # for i in range(0, 256):
    #   try:
    #     res = bytes([i, 0x81]).decode()
    #     out += res + "\n"
    #     print(str(i) + " - " + res + " - \\" + hex(i)[1:] + "\\x81")
    #   except Exception as e:
    #     print(str(i) + " - " + str(e))
        
    # outfile = "path\\to\\folder"
    # file = open(outfile, 'w', encoding='utf8')
    # file.write(out)
    # file.close()
    
    
    # for i in range(0, 256):
    #   try:
    #     res = bytes([i]).decode('cp1252')
    #     print(str(i) + " - " + res)
    #   except Exception as e:
    #     print(str(i) + ' - no: ' + str(e))
    
    # test = 'c'
    
    # enc0 = 'utf8'
    # temp = test.encode(enc0)
    
    # for enc in encs:
    #   try:
    #     res = temp.decode(enc)
    #     print(enc + ": " + res)
    #   except:
    #     print("[" + enc + "]")
    #     continue
    
    
    # for enc in encs:
    #   try:
    #     res = test.encode(enc)
    #     print(enc + ": " + str(res))
    #   except:
    #     print("[" + enc + "]")
    #     continue
    
    
    # enc = 'utf8'
    # res = test.encode(enc)
    # print(enc + ": " + str(res))
    
    
    # filen='fileName'
    # filen='zсz'
    # filen=filen.encode('utf8').decode('cp1252')
    
    # filen=b'\xc3\x91\xc2\x81'.decode('utf8')
    # comm='adb pull "/storage/sdcard0/1-docs/' + filen + '.txt" ' + '"path\\to\\folder"'
    # subprocess.check_output(comm)
    
    # # print('\nfinish')
  
  
  def test5(self):
    view = self.view
    
    i = 0x20
    j = 0x1c
    bb = bytearray([i, j])
    bs = str(int.from_bytes(bb, byteorder='big', signed=False))
    
    view.insert(edit, view.size(), bs)
    # print(bs)
    
    
  def test4(self, edit):
    view = self.view
    print('qwe')
    count = 0
    
    for i in range(0x00, 0xff):
    # for i in range(0x00, 0x01):
      for j in range(0x00, 0xff):
        try:
          bb = bytearray([i, j])
          # ch = bb.decode('utf_16_be')
          ch = bb.decode('utf8')
          
          # ch = bb.decode('utf_16_be').encode('iso8859_15')
          # ch = ch.decode('iso8859_15')
          
          add = '\t\t\t'
          count += 1
          if count == 7:
            count = 0
            add = '\n'
          
          # bs = ('%0.2x' % i) + ('%0.2x' % j)
          bs = ('%0.2x' % i) + ' ' + ('%0.2x' % j)
          # bs = str(int.from_bytes(bb, byteorder='big', signed=False))
          bs +=  ' : ' + ch + add
          view.insert(edit, view.size(), bs)
          
          # print(bs + ': ' + ch)
          # print(': ' + ch)
        except:
          # bs = ('%0.2x' % i) + (' %0.2x' % j)
          # bs += ' :: error\n'
          # view.insert(edit, view.size(), bs)
          continue
          
    print('\nfinish')
    
  
  def test3(self):
    for i in range(0x00, 0xff):
      for j in range(0x00, 0xff):
        
        try:
          bb = bytearray([i, j])
          ch = bb.decode('utf_16_be')
          
          bs = ('%0.2x' % i) + ('%0.2x' % j)
          print(bs + ': ' + ch)
        except:
          bs = ('%0.2x' % i) + ('%0.2x' % j)
          print(bs + ': error')
        
        
    # for i in range(0x00, 0xff):
    #   for j in range(0x00, 0xff):
    #     bb = bytearray([i, j])
    #     ch = bb.decode('utf_16_be')
        
    #     # bs = hex(i) + hex(j)
    #     bs = ('%0.2x' % i) + ('%0.2x' % j)
        
    #     print(bs + ': ' + ch)
    
    print('\nfinish')
    
    
  def test2(self):
    b1=0xc2
    b2=0xb5
    
    b=[b1, b2]
    bb=bytearray([b1, b2])
    s = str(bb)
    
    r1=bb.decode()
    
    # s = b''
    # s = b1 + b2
    # s[0] = b1
    # s[1] = b2
    
    print(s)
    print(r1)
    print(bb)
    
    
  def test1(self):
    s='r'
    sb=s.encode()
    sb=" ".join("{:02x}".format(ord(c)) for c in s)
    print(sb)
  