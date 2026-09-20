PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

names = [product.split()[0] for product in PRICE_LIST.split('\n')]
prices = [int(product.split()[1][:-1]) for product in PRICE_LIST.split('\n')]

new_dict = dict(zip(names, prices))
print(new_dict)
