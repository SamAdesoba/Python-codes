dict_play = {'name': 'Tolani', 'age': 34, 'length': '2'+'inches'}
print(dict_play)
print(dict_play.get('name', 'Samson'))
print(dict_play.get('named', 'Samson'))
print(dict_play.pop('age'))
print(dict_play)
# print(dict_play.update('name', 'Tolani'))
print(dict_play.popitem())
print({}.fromkeys((1,2,3),(3,2,1)))


