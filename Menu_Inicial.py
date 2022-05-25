from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import filedialog
import os
import Analizador_Lexico as Al
import AnalisisSintactico as As
import Procesador as Ps
from os import remove

TokenInit = ""
LexemaInit = ""
SymbolTable = ""
SymbolTableS = ""
TokenSn = ""
Word_Error = ""
Ind_fase2 = False
Ind_fase1 = False


def clean():
    global TokenInit, LexemaInit, SymbolTable, TokenSn
    TokenInit = ""
    LexemaInit = ""
    SymbolTable = ""
    TokenSn = ""
    lb3.config(text="")
    lb5.config(text="")
    lb6.config(text="")
    lb9.config(text="")
    remove("symboltable.txt")
    remove("responsetable.txt")


def create_table_simbol(symbols):
    ruta = os.path.abspath(os.getcwd())
    file = open(ruta + "\\" + "symboltable.txt", "w")
    file.write(symbols)
    file.close()


def search_gramatic(entrada):
    global Word_Error
    if entrada != '':
        for ch in entrada.split(" "):
            if Al.tokenizador(ch) == "":
                Word_Error = ch
                return False
            else:
                return True


def exe_fase1():  # Fase 1 pertenece a el analisis lexico de la frase y su respectiva tokenizacion
    global TokenInit, LexemaInit, SymbolTable, TokenSn, SymbolTableS, Ind_fase1
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
                        if Al.tokenizador(ch) == "":
                            TokenSn = "Error"
                        else:
                            TokenSn = Al.tokenizador(ch)
                    else:
                        LexemaInit = LexemaInit + "\n" + ch

                        if Al.tokenizador(ch) == "":
                            TokenSn = "Error"
                        else:
                            TokenSn = TokenSn + " " + Al.tokenizador(ch)

                    SymbolTable = SymbolTable + ch + "," + "int" + "\r"
                    SymbolTableS = SymbolTableS + ch + "," + "int" + "," + Al.tokenizador(ch) + "\r"
                elif Al.algoritmoId(ch):

                    TokenInit = TokenInit + "id" + "\n"

                    if LexemaInit == "":
                        if Al.tokenizador(ch) == "":
                            TokenSn = "Error"
                        else:
                            TokenSn = Al.tokenizador(ch)
                        LexemaInit = ch
                    else:
                        if Al.tokenizador(ch) == "":
                            TokenSn = "Error"
                        else:
                            TokenSn = TokenSn + " " + Al.tokenizador(ch)
                        LexemaInit = LexemaInit + "\n" + ch

                    SymbolTable = SymbolTable + ch + "," + "id"  + "\r"
                    SymbolTableS = SymbolTableS + ch + "," + "id" + "," + Al.tokenizador(ch) + "\r"

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
                SymbolTable = SymbolTable + ch + "," + "?" + "," + "?" + "\r"
            i = i + 1
        if state:
            create_table_simbol(SymbolTable)
            MessageBox.showinfo("Alerta", "Oracion correcta. " + str(i) + " Palabras analizadas")
            lb3.config(text=LexemaInit)
            lb5.config(text=TokenInit)
            Ind_fase1 = True

    else:
        MessageBox.showinfo("Alerta", "No se aceptan cadenas vacias")


def exe_fase2():
    global TokenSn, Word_Error, SymbolTableS, Ind_fase2
    ind_Exe = False
    if Ind_fase1:
        lb6.config(text=TokenSn.replace(" ", "\n"))
        for i in input1.get().split(" "):
            if i != "?":
                if search_gramatic(i):
                    ind_Exe = True
                    remove("symboltable.txt")
                    create_table_simbol(SymbolTableS)
                else:
                    ind_Exe = False
                    break
        Ind_fase2 = ind_Exe
        if ind_Exe:
            if As.analizador(TokenSn):
                lb6.config(text=TokenSn.replace(" ", "\n"))
                MessageBox.showinfo("Alerta", "Oracion correcta sintacticamente")
        else:
            MessageBox.showinfo("Alerta", "Palabra no pertenece a la gramatica " + Word_Error)
    else:
        MessageBox.showinfo("Alerta", "Fase 1 sin ejecutar")


def exe_fase3():
    global TokenSn
    lexema = input1.get()
    if Ind_fase2:
        lb9.config(text=Ps.response_generator(lexema, TokenSn))
    else:
        MessageBox.showinfo("Alerta", "Fase 2 sin ejecutar")


# Inicio configuracion grafica
window = Tk()
window.title('Maquina Turing')
window.geometry('700x350')
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
lb6 = Label(window)
lb6.place(x=220, y=135)
lb6['bg'] = "#D2D1D1"
lb7 = Label(window, text="Token Sintactico")
lb7.place(x=190, y=110)
lb7['bg'] = "#D2D1D1"
lb8 = Label(window, text="Token Respuesta")
lb8.place(x=325, y=110)
lb8['bg'] = "#D2D1D1"
lb9 = Label(window)
lb9.place(x=350, y=135)
lb9['bg'] = "#D2D1D1"
input1 = Entry(window, width=40)
input1.grid(column=0, row=0)
input1.place(x=130, y=60, anchor="center")
btnfase1 = Button(window, text="Fase 1", command=exe_fase1)
btnfase1.grid(column=0, row=0)
btnfase1.place(x=600, y=45)
btnfase2 = Button(window, text="Fase 2", command=exe_fase2)
btnfase2.grid(column=0, row=0)
btnfase2.place(x=600, y=85)
btnfase3 = Button(window, text="Fase 3",command=exe_fase3)
btnfase3.grid(column=0, row=0)
btnfase3.place(x=600, y=125)
btnclean = Button(window, text="Limpiar", command=clean)
btnclean.grid(column=0, row=0)
btnclean.place(x=600, y=165)


# Fin configuracion grafica

def run():
    window.mainloop()


if __name__ == '__main__':
    run()
