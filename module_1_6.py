my_dict={'Krasnogorsk':143404,'Vladivostok': 503202,'St Petersburg':706805}
print(my_dict)
print(my_dict.get('Krasnogorsk'))
print(my_dict.get('Sochi', 'такого значения нет'))
my_dict.update({'Tomsk': 412500,
                  'Ulan - Bator': 8899})
print(my_dict)
my_dict.pop('Vladivostok')
print(my_dict)
a={'Vladivostok':503202}
print(a.values())

my_set={0,3,2,1,0,3,2,1}
print(my_set)
my_set={0,3,2,1,0,3,2,1,'Number', (9,1,2)}
print(my_set)
print(my_set.discard(2))
print(my_set)

