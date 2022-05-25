import json
import os
from tkinter import messagebox as MessageBox

StopWord = "desea"
final_lexema = ""
Ind_StopWord = False
finalizar = "Si, muchas gracias"
menu = "Si"
adicion = "Si, Gracias"
table = "Respuestas.json"


def search_size_domain(word_pass):
    global table
    size = 0
    with open(table, "r") as j:
        try:
            mydata = json.load(j)
            for data in mydata[word_pass]:
                size = len(data)
        except:
            print("")
    if size > 0:
        return True


def search_data_domain(word):
    global table
    response = ""
    with open(table, "r") as j:
        try:
            mydata = json.load(j)
            for data in mydata[word]:
                response = response + data["total"]
        except:
            print("")
    return response


def create_table_response(symbols):
    ruta = os.path.abspath(os.getcwd())
    file = open(ruta + "\\" + "responsetable.txt", "w")
    file.write(symbols)
    file.close()


def response_generator(lexema, token2):
    global final_lexema, Ind_StopWord

    # Eliminacion StopWord
    if StopWord in lexema:
        final_lexema = lexema.replace(StopWord, "")
        Ind_StopWord = True

    # Generador de respuestas
    for x in final_lexema.split(" "):
        if search_size_domain(x):
            if x == "finalizar":
                MessageBox.showinfo("Alerta", finalizar)
                create_table_response(finalizar + "\n")
                break
            elif x == "menu":
                MessageBox.showinfo("Alerta",
                                    menu + "\n" + "______________ \n" + search_data_domain("menu").replace("|", "\n"))
                create_table_response(menu + "\n" + "______________ \n" + search_data_domain("menu").replace("|", "\n"))
                break
            elif x == "adicion":
                MessageBox.showinfo("Alerta",
                                    adicion + "\n" + "______________ \n" + search_data_domain("adicion").replace("|",
                                                                                                                 "\n"))
                create_table_response(adicion + "\n" + "______________ \n" + search_data_domain("adicion").replace("|",
                                                                                                                   "\n")
                                      )
                break

    # Impresion Token3
    final_string = token2.replace("V", StopWord, 1)
    return final_string.replace(" ", "\n")
