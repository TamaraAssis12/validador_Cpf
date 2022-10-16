import tkinter as tk
from tkinter import *

class validador_Cpf(tk.Frame):
    def __init__(self):
        self.root = tk.Tk()
        self.co0 = "#002468"  # cor azul
        self.co1 = "#feffff"  # Cor branco
        self.co2 = "#4F4F4F"  # cor cinza
        self.root.title("Sistema para Validação de CPF")
        self.root.geometry("300x500")
        self.root.resizable(False, False)
        self.init_frame()


    def validar(self):
            cpf = self.entry.get()
            # Verifica se o CPF possui 11 números ou se todos são iguais:
            if len(cpf) != 11 or len(set(cpf)) == 1:
                self.label2["text"] = "CPF inválido! Tente novamente"
            else:
                cpf = cpf[:9] #pega os 9 primeiros dígitos do cpf
                reverso = 10 #contador reverso
                total = 0 
                for index in range(19):
                    if index > 8: 
                        index -= 9 
                    total += int(cpf[index]) * reverso  
                    reverso -= 1 
                    if reverso < 2:    
                        reverso = 11  
                        d = 11 - (total % 11) 
                        if d > 9: 
                            d = 0 
                        total = 0 
                        cpf += str(d) 
                sequencia = cpf == str(cpf[0]) * len(cpf) 
                if cpf == cpf and not sequencia:    
                    self.label2["text"] = "CPF válido!"
                else:
                    self.label2["text"] = "CPF inválido! Tente novamente"

    def init_frame(self):
        self.frame_up = Frame(
            self.root, width=500, height=30, bg=self.co0, relief="flat"
        )
        self.frame_up.pack(expand=True, fill="both")

        self.frame_down = Frame(
            self.root, width=500, height=230, bg="white", relief="flat"
        )
        self.frame_down.pack(expand=True, fill="both")
        titulo_frameup = Label(
            self.frame_up,
            text="Validador de CPF",
            anchor=CENTER,
            font=("Poppins 18 bold"),
            bg=self.co0,
            fg=self.co1,
        )
        titulo_frameup.place(x=45, y=35)
        label = Label(self.frame_down,font="Poppins 11",
            bg=self.co1,
            text="Informe os números do  CPF: ")
        label.place(x=45, y=10)
        self.entry = Entry(self.frame_down,
        width=25,
        bd=1,
        relief=RAISED,
        font=("arial 12"))
        self.entry.place(x=40, y=60)
        self.btn = Button(
            self.frame_down,
            text="VALIDAR",
            font="Poppins 11 bold",
            width=20,
            relief=RAISED,
            command=self.validar)
        self.btn.place(x=45, y=100)
        self.label2 = Label(self.frame_down, 
            font="Poppins 11",
            bg=self.co1,
            text="")
        self.label2.place(x=45, y=160)

    
        self.root.mainloop()

if __name__ == "__main__":
    validador_Cpf()
