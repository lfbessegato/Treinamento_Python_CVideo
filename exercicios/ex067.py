print('Exercícios:067 - Tabuada v3.0')
while True:
    num = int(input('Quer ver a tabuada de qual valor: '))
    print('-=' * 30)
    if num < 0:
        break
    for c in range(0, 11):
        print(f'{num:2} x {c:2} = {num * c:2}')
    print('-=' * 30)
print('PROGRAMA TABUADA ENCERRADO ... Volte Sempre.')
