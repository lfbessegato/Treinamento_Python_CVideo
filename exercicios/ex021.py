print('Exercício 21 - Criando um Player MP3 ')
from pygame import mixer
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
x = input('Digite algo para parar...')


