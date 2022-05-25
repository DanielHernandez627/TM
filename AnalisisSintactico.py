from tkinter import messagebox as MessageBox
import json

# Inicio logica

terminal = ["id", "+", "*", "(", ")", "$", "desea", "otro", "tipo", "de", "adicion", "el", "gustaria", "ordenar",
            "algo", "mas", "repetir", "menu", "ver", "las", "opciones", "recomendadas", "su", "pedido"]
verbos = ["desea", "gustaria", "ordenar", "repetir", "ver"]
nucleo = ["tipo", "adicion", "menu", "opciones", "recomendadas", "pedido"]
adj = ["algo", "mas"]
det = ["el", "de", "las"]
pro = ["su", "otro", "le"]
terminal_select = ""
splitToken = []
splitToken2 = []
not_terminal = []
not_terminal_select = ""
final_exit = ""
fina_pila_exit = []
state_pila = ""
state_entrada = ""
table = ""


def clean():
    global terminal_select
    terminal_select = ""
    global splitToken
    splitToken = []
    global splitToken2
    splitToken2 = []
    global not_terminal
    not_terminal = []
    global not_terminal_select
    not_terminal_select = ""
    global final_exit
    final_exit = ""
    global fina_pila_exit
    fina_pila_exit = []
    global state_pila
    state_pila = ""
    global state_entrada
    state_entrada = ""


def search_words(word):
    for i in verbos:
        if word == i:
            return "V"

    for x in nucleo:
        if word == x:
            return "N"

    for y in adj:
        if word == y:
            return "ADJ"

    for z in det:
        if word == z:
            return "DET"

    for j in pro:
        if word == j:
            return "PRO"

    return ""


def remove_pila_terminal(x):
    for t in terminal:
        if x == t or x == "$":
            if x == t:
                return True
            return False


def error():
    MessageBox.showwarning("Alerta", "La pila esta vacia")


def search_token(token):
    sentece = token.split(" ")
    senteceFinal = ""
    for i in sentece:
        senteceFinal = senteceFinal + i + "|"
    return senteceFinal


def search_Gramatic(x, ae):
    global table
    table = "nuevaTabla.json"
    with open(table, "r") as j:
        mydata = json.load(j)
        for data in mydata[ae]:
            return data[x]


def search_Dataterminal(ae):
    global table
    table = "nuevaTabla.json"
    with open(table, "r") as j:
        mydata = json.load(j)
        for data in mydata[ae]:
            return len(data)


def verify_Gramatic(size_terminal, x, ae):
    i = 0
    exit_gramitc = ""
    global final_exit
    x_original = x
    while i < size_terminal:
        gramatic_return = search_Gramatic(x, ae)
        for zx in gramatic_return.split("|"):  # Este for es para la generacion de salidas
            exit_gramitc = exit_gramitc + zx
        if i == 0:
            verify_word = search_words(exit_gramitc)
            if verify_word != "":
                final_exit = final_exit + "\n" + "\n" + x_original + "->" + verify_word
            else:
                final_exit = final_exit + "\n" + "\n" + x_original + "->" + exit_gramitc
        else:
            final_exit = final_exit + "\n" + "\n" + x + "->" + exit_gramitc
        if x != "$":
            not_terminal.remove(x)
        for z in reversed(gramatic_return.split("|")):  # Este for es para la pila
            if z != "e":
                not_terminal.append(z)
                x = z
            else:
                x = search_final_not_terminal()

        exit_gramitc = ""
        i = i + 1
        if ae == x:
            not_terminal_select = x
            break
        else:
            not_terminal_select = x
    return not_terminal_select


def search_final_not_terminal():
    not_terminal_final = not_terminal[-1]
    return not_terminal_final


def analizador(tokenizacion):
    token = search_token(tokenizacion)
    tokenFinal = token + "$"
    splitToken = tokenFinal.split("|")
    global splitToken2
    splitToken2 = tokenFinal.split("|")
    state_not_terminal_select = False
    not_terminal.append("$")
    not_terminal.append("O")
    not_terminal_select = "O"

    for idx, x in enumerate(splitToken):
        terminal_select = x
        splitToken2.pop(0)
        if remove_pila_terminal(
                not_terminal_select) == True or not_terminal_select == "$" and state_not_terminal_select == False:
            if remove_pila_terminal(not_terminal_select):
                not_terminal.remove(not_terminal_select)
                state_not_terminal_select = True
                not_terminal_select = search_final_not_terminal()
                if x != "$":
                    if state_not_terminal_select:  # Ejecucion de verificacion de gramaitca posterior a la
                        # eliminacion de un terminal de la pila
                        not_terminal_select = verify_Gramatic(search_Dataterminal(terminal_select), not_terminal_select,
                                                              terminal_select)
                        state_not_terminal_select = False
                else:
                    break
            else:
                error()
                break
        else:
            not_terminal_select = verify_Gramatic(search_Dataterminal(terminal_select), not_terminal_select,
                                                  terminal_select)
            state_not_terminal_select = False
    return True
# Fin logica
