Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
99999999999999999999999999999+1
100000000000000000000000000000
2**200
1606938044258990275541962092341162602522202993782792835301376
#в версияз 2.х было бы в конце приписана еще L
1j*1J
(-1+0j)
2+1j*3
(2+3j)
(2+1j)*3
(6+3j)
(2+1j)*(3+4.5j)
(1.5+12j)
0O1
1
0O16
14
0x12
18
0x4.5
SyntaxError: invalid syntax
0x4f
79
0x10
16
0xFF
255
0xf
15
0xa
10
0xb
11
0xc
12
0xd
13
0xi
SyntaxError: invalid hexadecimal literal
0xf
15
0xe
14
0xg
SyntaxError: invalid hexadecimal literal
0x0
0
0x1
1
0x2
2
#0x это шестанадцатиричная система
0b1
1
0b10
2
0b11
3
0b111
7
0b1111
15
0b11111
31
ob111111
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    ob111111
NameError: name 'ob111111' is not defined
0b111111
63
#0b бинарная
0o10
8
00377
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
0o377
255
0xFF
255
0b1111111
127
0b11111111
255
#по умолчанию десятичная, но
oct(64)hex(64)bin(64)
SyntaxError: invalid syntax
oct(64), hex(64), bin(64)
('0o100', '0x40', '0b1000000')
# int(str, base) строка в число, беря во внимание заданную систему исчисления
int(10,16)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    int(10,16)
TypeError: int() can't convert non-string with explicit base
#str!!!
int('10', 16)
16
int('F',16)
15
int(255,8)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    int(255,8)
TypeError: int() can't convert non-string with explicit base

int('255',8)
173
int(100101,2)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    int(100101,2)
TypeError: int() can't convert non-string with explicit base
int('1010011',2)
83
int('1+10j')
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    int('1+10j')
ValueError: invalid literal for int() with base 10: '1+10j'
int('2')
2
eval(0x10)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    eval(0x10)
TypeError: eval() arg 1 must be a string, bytes or code object
eval('0x10')
16




x=0xffffffffffffffffffffff
x
309485009821345068724781055
oct(x)
'0o177777777777777777777777777777'
hex(x)
'0xffffffffffffffffffffff'
bin(x)
'0b1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
