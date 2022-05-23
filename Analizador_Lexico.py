posLectura = []
lexema = ""
estadoAcepta = False;
estado = 0
estadoError = 0

verbos = ["desea", "gustaria", "ordenar", "repetir", "ver"]
nucleo = ["tipo", "adicion", "menu", "opciones", "recomendadas", "pedido"]
adj = ["algo", "mas"]
det = ["el", "de", "las"]
pro = ["su", "otro", "le"]


def algoritmoInt(entrada):
    global posLectura, lexema, estadoAcepta, estado, estadoError
    posLectura = [1];
    lexema = entrada;
    estadoAcepta = False;
    estado = 0;
    estadoError = 0;
    posLectura[0] = 0;
    return procesoInt()


def procesoInt():
    valido = True
    valido = automataInt()
    return valido


def automataInt():
    global posLectura, lexema, estadoAcepta, estado, estadoError
    caracter = ""
    for x, char in enumerate(lexema):
        caracter = char
        if caracter.isdigit() == True or caracter == '-' and estado == 0:
            estado = 1
            estadoAcepta = True
        else:
            if caracter.isdigit() == True and estado == 1:
                estado = 1
                estadoAcepta = True
            else:
                estadoAcepta = False
                posLectura[0] = x
                break

    return estadoAcepta


def algoritmoId(entrada):
    global posLectura, lexema, estadoAcepta, estado, estadoError
    posLectura = [1];
    lexema = entrada;
    estadoAcepta = False;
    estado = 0;
    estadoError = 0;
    posLectura[0] = 0;
    return procesoId()


def procesoId():
    valido = True
    valido = automataId()
    return valido


def automataId():
    global posLectura, lexema, estadoAcepta, estado, estadoError
    caracter = ""
    for x, char in enumerate(lexema):
        caracter = char
        if caracter.isalpha() == True and estado == 0:
            estado = 1
            estadoAcepta = True
        else:
            if caracter.isalpha() == True and estado == 1:
                estado = 1
                estadoAcepta = True
            else:
                estadoAcepta = False
                posLectura[0] = x
                break

    return estadoAcepta


def fallo():
    global lexema
    return str(lexema[posLectura[0]])


def tokenizador(word):
    for i in verbos:
        if word == i:
            return "V"

    for x in nucleo:
        if word == x:
            return "N"

    for y in adj:
        if word == y:
            return "ADV"

    for z in det:
        if word == z:
            return "DET"

    for j in pro:
        if word == j:
            return "PRO"

    return ""
