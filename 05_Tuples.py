### tuplas##

my_tuple = tuple()
my_new_tuple = ()

my_tuple = (36,1.77,'brais','moure','brais')
my_new_tuple = (35,60)
print(my_tuple)


print(my_tuple[0])
print(my_tuple[-1])
##print(my_tuple[-6]) error
##print(my_tuple[-1]) error

print(my_tuple.count('brais'))
print(my_tuple.index('moure'))
print(my_tuple.index('brais'))

##my_tuple[1] = 1.80  ERROR
##print(my_tuple)  ERROR

print(my_tuple+my_new_tuple)
my_sum_tuple = my_tuple+my_new_tuple

print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = 'Niño'
my_tuple.insert(1,'Azul')
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

del my_tuple
#print(my_tuple) no esta definida es un error
