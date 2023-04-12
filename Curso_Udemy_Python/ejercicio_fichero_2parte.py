import pickle

frutas = open("fichero.pckl","rb")

fichero_leido_frutas = pickle.load(frutas)

print(fichero_leido_frutas)
print(type(fichero_leido_frutas))
print(fichero_leido_frutas.values())