person = {'first_name':'Fiona', 'last_name': 'Meisner', 'hobby': 'Hiking'}
print(person)

first_name = person['first_name']
last_name = person.get('last_name')

middle_name = person.get('middle_name')
# Fiona Meisner
print(first_name,middle_name,last_name)

person['job'] = 'secretary'
print(person['job'])

person.update({'hobby': 'Painting'})
print(person['hobby'])

person.pop('last_name')
print(person)
