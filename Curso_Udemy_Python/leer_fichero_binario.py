# pickle 
import pickle

fichero = open("fichero_colores.pckl","rb")

lista_leida = pickle.load(fichero)

print(lista_leida)