leiviska = float(input('Anna leiviskat: '))
naula = float(input('Anna naulat: '))
luoti = float(input('Anna luodit: '))

leiviskanaulaluotigramma = leiviska * 20 * 32 * 13.3 + naula * 32 * 13.3 + luoti * 13.3

leiviskakg = leiviskanaulaluotigramma / 1000

print(f'Massa nykymittojen mukaan: ')

massangramosuus = leiviskanaulaluotigramma % 1000

print(f'{int(leiviskakg)} kilogrammaa ja {massangramosuus:.0f} grammaa')