uma_lista= ['a','b','c','d','e','f']
uma_lista[1:3]= 'x' 'y'

print(uma_lista)

#Utilizado para encaixar elementos em seus respectivos lugares.

uma_lista = ['a','d','f']
uma_lista[1:1]=['b','c']
print(uma_lista)
uma_lista[4:4]= ['e']
print(uma_lista)

uma_lista = [4,2,8,6,5]

#Remover 
a = ['um','dois','tres']
del a[1]
print(a)

lista = ['a','b','c','d','e','f']
del lista[1:5]
print(lista)

#Append
a = [81,82,83]
a.append(5)
print(a)

#sort
a = [88,81,82,83]
a.sort()
print(a)

#index
a = [1,2,3,4,5,6,7,8,9]
print(a.index(4))


#count
a = [88,81,82,83,88,85,88,86]
print(a)
print(a.count(88))

#extend
lista = [1,2,3]
lista.extend([4,5])
print(lista)