from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import filedialog
import json
from webbrowser import get

# Inicio logica

terminal = ["id", "+", "*", "(", ")", "$", "desea", "otro", "tipo", "de", "adicion", "el", "gustaria", "ordenar",
            "algo", "mas", "repetir", "menu", "ver", "las", "opciones", "recomendadas", "su", "pedido"]
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
    lb2['text'] = ""
    lb4['text'] = ""
    lb8['text'] = ""
    lb9['text'] = ""
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


def browseFiles():
    clean()
    MessageBox.showwarning("Alerta", "Cada cadena debe esta seperar por el simbolo |. Ejemplo Id|+|Id")
    rutfichero = filedialog.askopenfilename(initialdir="/",
                                            title="Select a File",
                                            filetypes=(("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
    lb2.configure(text=rutfichero)


def openfile():
    fichero = open(lb2.cget("text"))
    for i in fichero.readlines():
        return i


def remove_pila_terminal(x):
    for t in terminal:
        if x == t or x == "$":
            if x == t:
                return True
            return False


def error():
    MessageBox.showwarning("Alerta", "La pila esta vacia")


def search_token(token):
    sentece = token.split("|")
    senteceFinal = ""
    for i in sentece:
        senteceFinal = senteceFinal + i
    return senteceFinal


def search_Gramatic(x, ae):
    global table
    if (verify_table_select() == 1):
        table = "tablaIntroduccion.json"
    elif (verify_table_select() == 2):
        table = "tabla2.json"
    with open(table, "r") as j:
        mydata = json.load(j)
        for data in mydata[ae]:
            return data[x]


def search_Dataterminal(ae):
    global table
    if (verify_table_select() == 1):
        table = "tablaIntroduccion.json"
    elif (verify_table_select() == 2):
        table = "tabla2.json"
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
            final_exit = final_exit + "\n" + "\n" + x_original + "->" + exit_gramitc
        else:
            final_exit = final_exit + "\n" + "\n" + x + "->" + exit_gramitc
        if (x != "$"):
            not_terminal.remove(x)

        for z in reversed(gramatic_return.split("|")):  # Este for es para la pila
            if z != "e":
                not_terminal.append(z)
                printer_pila()
                x = z
            else:
                x = search_final_not_terminal()

        lb4.config(text=final_exit)
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


def printer_pila():
    global state_pila
    for i in not_terminal:
        if len(not_terminal) > 1:
            state_pila = state_pila + " " + i
    state_pila = state_pila + "\n"
    lb8.config(text=state_pila)


def printer_pila_entrada():
    global state_entrada
    for i in splitToken2:
        state_entrada = state_entrada + " " + i
    state_entrada = state_entrada + "\n" + "\n"
    lb9.config(text=state_entrada)


def verify_table_select():
    if (var1.get() == True and var2.get() == False):
        return 1
    elif (var1.get() == False and var2.get() == True):
        return 2
    else:
        return 0


def analizador():
    token = openfile()
    lb3['text'] = "Oracion ingresada: " + search_token(token)
    tokenFinal = token + "|$"
    splitToken = tokenFinal.split("|")
    global splitToken2
    splitToken2 = tokenFinal.split("|")
    state_not_terminal_select = False
    not_terminal.append("$")

    if (verify_table_select() == 1):
        not_terminal.append("E")
        not_terminal_select = "E"
    elif (verify_table_select() == 2):
        not_terminal.append("O")
        not_terminal_select = "O"
    else:
        MessageBox.showwarning("Alerta", "Ninguna entrega seleccionada")
        return 0

    printer_pila()
    printer_pila_entrada()
    for idx, x in enumerate(splitToken):
        terminal_select = x
        splitToken2.pop(0)
        printer_pila_entrada()
        if remove_pila_terminal(
                not_terminal_select) == True or not_terminal_select == "$" and state_not_terminal_select == False:
            if remove_pila_terminal(not_terminal_select) == True:
                printer_pila()
                not_terminal.remove(not_terminal_select)
                printer_pila()
                state_not_terminal_select = True
                not_terminal_select = search_final_not_terminal()
                if x != "$":
                    if state_not_terminal_select == True:  # Ejecucion de verificacion de gramaitca posterior a la eliminacion de un terminal de la pila
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


# Fin logica

# Inicio configuracion grafica
window = Tk()
window.title('Analizador sintactico')
window.geometry('700x650')
window['bg'] = "#D2D1D1"
lb1 = Label(window, text="Seleccione el archivo a leer")
lb1.grid(column=0, row=0)
lb1.place(x=104, y=35, anchor="center")
lb1['bg'] = "#D2D1D1"
lb2 = Label(window)  # Ruta del fichero de entrada
lb2.grid(column=1, row=1)
lb2.place(x=30, y=50)
lb2['bg'] = "#D2D1D1"
lb3 = Label(window)
lb3.place(x=30, y=75)
lb3['bg'] = "#D2D1D1"
lb4 = Label(window)
lb4.place(x=350, y=115)
lb4['bg'] = "#D2D1D1"
lb5 = Label(window, text="Salida")
lb5.place(x=350, y=110)
lb5['bg'] = "#D2D1D1"
lb6 = Label(window, text="Pila")
lb6.place(x=50, y=110)
lb6['bg'] = "#D2D1D1"
lb7 = Label(window, text="Entrada")
lb7.place(x=170, y=110)
lb7['bg'] = "#D2D1D1"
lb8 = Label(window)
lb8.place(x=30, y=147)
lb8['bg'] = "#D2D1D1"
lb9 = Label(window)
lb9.place(x=150, y=150)
lb9['bg'] = "#D2D1D1"
btnsearch = Button(window, text="Buscar", command=browseFiles)
btnsearch.grid(column=0, row=0)
btnsearch.place(x=500, y=48)
btnverify = Button(window, text="Verificar", command=analizador)
btnverify.grid(column=0, row=0)
btnverify.place(x=500, y=80)
var1 = BooleanVar()
var2 = BooleanVar()
check1 = Checkbutton(window, text="Primera Entrega", variable=var1)
check1.grid(column=0, row=0)
check1.place(x=499, y=120)
check1['bg'] = "#D2D1D1"
check2 = Checkbutton(window, text="Segunda Entrega", variable=var2)
check2.grid(column=0, row=0)
check2.place(x=499, y=155)
check2['bg'] = "#D2D1D1"


# Fin configuracion grafica

def run():
    window.mainloop()


if __name__ == '__main__':
    run()