a={}
print(type(a))

b={
    1:'Python'
}
print(b[1])

b={
    1:'Python',
    2: 'Java',
    3: 'C'
}
print(b[3])

perfume = {
    'a': 'Axe',
    'f': 'fog',
    'v': 'vip 919'
}
print(perfume['v'])
print(perfume['f'])
print(perfume['h'])


perfume = {
    'a': 'Axe',
    'f': 'fog',
    '1': 'RB',
    'v': 'vip 919'
}
print(perfume.keys())
print(perfume.values())
perfume.clear()
print(perfume)


perfume = {
    'a': 'Axe',
    'f': 'fog',
     1: 'RB',
    'v': 'vip 919'
}
perfume.pop('f')
print(perfume)
perfume.popitem()
print(perfume)


a=[101,204,306,405,503]
print(dict.fromkeys(a,'Pass'))


perfume = {
    'a': 'Axe',
    'f': 'fog',
     1: 'RB',
    'v': 'vip 919'
}
perfume.update({'f':'fox'})
perfume.update({'m':'manoj'})
print(perfume)

perfume = {
    'a': 'Axe',
    'f': 'fog',
     1: 'RB',
    'v': 'vip 919'
}
perfume.setdefault('f','fox')
perfume.setdefault('m','manoj')
print(perfume)
print(perfume.items())

perfume = {
    'a': 'Axe',
    'f': 'fog',
     1: 'RB',
    'v': 'vip 919'
}
print(perfume.get(1))
print(perfume.get(2))
print(perfume[2])

print(dir(dict))