Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print (olá Mundo.!')
       
SyntaxError: invalid syntax
>>> print (Olá Mundo ...)
SyntaxError: invalid syntax
>>> print ('Olá Mundo')
Olá Mundo
>>> cls
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    cls
NameError: name 'cls' is not defined
>>> clear
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> 
=============================== RESTART: Shell ===============================
>>> 7+4
11
>>> print (7+4)
11
>>> print ('7'+'4')
74
>>> '7'+'4'
'74'
>>> 7=3
SyntaxError: can't assign to literal
>>> 7+10
17
>>> print ('Olá', 5)
Olá 5
>>> print ('Olá', 5)
Olá 5
>>> nome = 'Luciano'
>>> idade = 46
>>> peso = 95.5
>>> print (nome,idade,peso)
Luciano 46 95.5
>>> nome = input ('Qual o seu nome')

>>> nome = input ('Qual o seu nome: ')
Qual o seu nome: Márcia
>>> idade = input ('Qual sua idade: ')
Qual sua idade: 47
>>> peso = input ('Qual o seu peso: ')
Qual o seu peso: 60
>>> print (nome, idade, peso)
Márcia 47 60
>>> 
=== RESTART: C:/Users/IEUser/Desktop/scripts-python/Aula04-print_input).py ===
Qual é o seu nome: Enzo
Qual é a sua idade: 14
Qual é o seu peso: 50.2
Enzo 14 50.2
>>> 
=== RESTART: C:/Users/IEUser/Desktop/scripts-python/Aula04-print_input).py ===
Qual é o seu nome: Tereza
Qual é a sua idade: 56
Qual é o seu peso: 76
Tereza 56 76
>>> 
