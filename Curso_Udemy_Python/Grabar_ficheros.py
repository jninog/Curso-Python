#Grabar un fichero de texto

fichero = open('fichero_para_grabar.txt','wt')

print('Escriba lo que va a grabar en el archivo')
texto_fichero = input()
fichero.write(texto_fichero)

fichero.close()