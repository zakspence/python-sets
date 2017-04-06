showroom = {'Corvette', 'Accord', 'Model S', 'Woodie'}
print(showroom)
length = len(showroom)
print('length of showroom is {}'.format(length))
showroom.add('Corvette')
print(showroom)
new_stock = {'Explorer', 'Beetle'}
showroom.update(new_stock)
print(showroom)
showroom.discard('Woodie')
print('after woodie: {}'.format(showroom))
junkyard = {'lemon', 'junker', 'Corvette', 'Model S', 'Ferrari'}
common_cars = junkyard.intersection(showroom)
print('common cars = {}'.format(common_cars))
showroom = showroom.union(junkyard, showroom)
print(showroom)
junkyard.discard('lemon')
print(junkyard)

