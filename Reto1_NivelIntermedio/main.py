from datetime import date

discos_dict = [{
    'Name': 'Browneyes',
    'Artist': 'Lassito',
    'Year': '2022',
    'Price': 5.99,
    'Genre': 'Pop'
}, {
    'Name': 'Demons',
    'Artist': 'Slipknot',
    'Year': '1980',
    'Price': 15.99,
    'Genre': 'Black Metal'
}, {
    'Name': 'To the moon',
    'Artist': 'ABBA',
    'Year': '1994',
    'Price': 8.99,
    'Genre': 'Electro'
}, {
    'Name': 'Tite me preguntó',
    'Artist': 'Bad Bunny',
    'Year': '2022',
    'Price': 8.99,
    'Genre': 'Reggaeton'
}, {
    'Name': 'Highway to hell',
    'Artist': 'AC/DC',
    'Year': '1975',
    'Price': 8.99,
    'Genre': 'Rock'
}, {
    'Name': 'B Y O B',
    'Artist': 'System of a Down',
    'Year': '1990',
    'Price': 9.99,
    'Genre': 'Metal'
}, {
    'Name': 'Devil',
    'Artist': 'Ozzie Osborn',
    'Year': '1975',
    'Price': 12.99,
    'Genre': 'Death Metal'
}]

print('Bienvenido a la tienda de discos')
print('Esta es la lista de albums disponibles: ', discos_dict)

print('Para comprar, selecciona un album del 1 al 7')
Index = int(input()) - 1

print('Has elegido el album', discos_dict[Index])
print('Si es correcta tu selección, pulsa 0 para finalizar con tu compra')

Validate = int(input())

CurrentItem = discos_dict[Index]

Date = date.today()

Price = CurrentItem.get('Price')

if CurrentItem.get('Genre') == 'Electro' or CurrentItem.get(
        'Genre') == 'Black Metal':
    FinalPrice = Price * 0.7
    Discount = Price * 0.3
else:
    FinalPrice = Price
    Discount = 0

print('------------------------')
print('Tu ticket de compra:')
print('Fecha:', Date)
print('Descuento en tu compra:', Discount, 'euros')
print('Tu precio final es:', FinalPrice, 'euros')
print('¡Gracias por tu compra!')
print('------------------------')