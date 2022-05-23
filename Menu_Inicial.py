from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import filedialog
import json
import os
import Analizador_Lexico as Al

TokenInit = ""
LexemaInit = ""
SymbolTable = ""
TokenSn = ""

def clean():
    global TokenInit, LexemaInit, SymbolTable, TokenSn
    TokenInit = ""
    LexemaInit = ""
    SymbolTable = ""
    TokenSn = ""

def create_table_simbol(symbols):
    ruta = os.path.abspath(os.getcwd())
    file = open(ruta + "\\" + "symboltable.txt", "w")
    file.write(symbols)
    file.close()


def exe_fase1():  # Fase 1 pertenece a el analisis lexico de la frase y su respectiva tokenizacion
    global TokenInit, LexemaInit, SymbolTable,TokenSn
    entrada = input1.get()
    i = 0
    state = True
    if entrada != '':
        for ch in entrada.split(" "):
            if ch.find("?") > 0 or ch.find("?") == -1:
                if Al.algoritmoInt(ch):
                    TokenInit = TokenInit + "int" + "\n"
                    if LexemaInit == "":
                        LexemaInit = ch
                        TokenSn = Al.tokenizador(ch) + "\n"
                    else:
                        LexemaInit = LexemaInit + "\n" + ch
                        TokenSn = TokenSn + " " + Al.tokenizador(ch)
                    SymbolTable = SymbolTable + ch + "," + "int" + "\r"
                elif Al.algoritmoId(ch):
                    TokenInit = TokenInit + "id" + "\n"
                    if LexemaInit == "":
                        TokenSn = Al.tokenizador(ch)
                        LexemaInit = ch
                    else:
                        TokenSn = TokenSn + " " + Al.tokenizador(ch)
                        LexemaInit = LexemaInit + "\n" + ch
                    SymbolTable = SymbolTable + ch + "," + "id" + "\r"
                else:
                    MessageBox.showinfo("Alerta",
                                        "Error Lexico en " + ch + " por el simbolo " + Al.fallo())
                    state = False
            else:
                TokenInit = TokenInit + "?" + "\n"
                if LexemaInit == "":
                    LexemaInit = ch
                else:
                    LexemaInit = LexemaInit + "\n" + ch
                SymbolTable = SymbolTable + ch + "," + "?" + "\r"
            i = i + 1
        if state:
            create_table_simbol(SymbolTable)
            MessageBox.showinfo("Alerta", "Oracion correcta. " + str(i) + " Palabras analizadas")
            lb3.config(text=LexemaInit)
            lb5.config(text=TokenInit)
            lb6.config(text="Token Sintactico "+TokenSn)
    else:
        MessageBox.showinfo("Alerta", "No se aceptan cadenas vacias")


def exe_fase2():
    print("prueba")


# Inicio configuracion grafica
window = Tk()
window.title('Maquina Turing')
window.geometry('700x650')
window['bg'] = "#D2D1D1"
lb1 = Label(window, text="Ingrese la frase a analizar")
lb1.grid(column=0, row=0)
lb1.place(x=5, y=28)
lb1['bg'] = "#D2D1D1"
lb2 = Label(window, text="Lexema")
lb2.place(x=15, y=110)
lb2['bg'] = "#D2D1D1"
lb3 = Label(window)
lb3.place(x=25, y=135)
lb3['bg'] = "#D2D1D1"
lb4 = Label(window, text="Token")
lb4.place(x=100, y=110)
lb4['bg'] = "#D2D1D1"
lb5 = Label(window)
lb5.place(x=105, y=135)
lb5['bg'] = "#D2D1D1"
lb6 = Label(window, text="")
lb6.grid(column=0, row=0)
lb6.place(x=300, y=48)
lb6['bg'] = "#D2D1D1"
input1 = Entry(window, width=40)
input1.grid(column=0, row=0)
input1.place(x=130, y=60, anchor="center")
btnfase1 = Button(window, text="Fase 1", command=exe_fase1)
btnfase1.grid(column=0, row=0)
btnfase1.place(x=600, y=45)
btnfase2 = Button(window, text="Fase 2", command=exe_fase2)
btnfase2.grid(column=0, row=0)
btnfase2.place(x=600, y=85)


# Fin configuracion grafica

def run():
    window.mainloop()


if __name__ == '__main__':
    run()
