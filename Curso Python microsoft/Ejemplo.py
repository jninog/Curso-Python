participantes = ['aaa','bbb','ccc','ddd','eee','fff']

def sorteo(participantes):
    if(len(participantes) %2 !=0):
        participantes.append("Descansa")

    fixture = []
    rivales = len(participantes)-1
    partidos = len(participantes) //2

    for r in range(rivales):
        count = rivales
    
        for p in range(partidos):
                       fixture.extend([participantes[p]])
        fixture.extend([participantes[count]])
        count -=1
    
        participantes.insert(1,participantes[-1])
        participantes.pop()
        fixture.extend(["### jornada",r+1])
    
    return fixture


print(sorteo(participantes))