from textwrap import wrap
import tkinter as tk
from tkinter import *
from turtle import position

class validador_Cpf(tk.Frame):
    def __init__(self):
        self.root = tk.Tk()
        self.co0 = "#002468"  # cor azul
        self.co1 = "#feffff"  # Cor branco
        self.co2 = "#565656"  # cor cinza
        self.co3 = "#32CD32"   # cor verde
        self.root.title("Sistema para Validação de CPF")
        self.root.geometry("300x500")
        self.root.resizable(False, False)
        self.init_frame()

        """ Efetua a validação do CPF, tanto da quantidade de dígitos quanto de dígito verificadores.

        Parâmetros:
            cpf (str): CPF a ser validado

        Retorno:
            bool:
                - Falso, quando o CPF possuir o formato 999.999.999-99, só aceitará números;
                - Falso, quando o CPF não possuir 11 caracteres numéricos;
                - Falso, quando os dígitos verificadores forem inválidos;
                - Verdadeiro, caso contrário.

        Exemplos:

        >>> validar('529.982.247-25')
        False
        >>> validate('52998224725')
        True, se o CPF for válido
        >>> validate('111.111.111-11')
        False
        """


    def validar(self):
            cpf = self.entry.get()
            # Verifica se o CPF possui 11 números ou se todos são iguais:
            if len(cpf) != 11 or len(set(cpf)) == 1:
                self.label2["text"] = "CPF inválido! Tente novamente"
            else:
                sequencia_cpf_calculado = cpf[:9] #pega os 9 primeiros dígitos do cpf
                reverso = 10 #contador reverso
                total = 0 
                for index in range(19):#Para cada index em range(19)
                    if index > 8: #Se o index for maior que 8
                        index -= 9 #index = index - 9
                    total += int(sequencia_cpf_calculado[index]) * reverso  #total = total + int(cpf[index]) * reverso
                    reverso -= 1 #reverso = reverso - 1
                    if reverso < 2:    #Se reverso for menor que 2
                        reverso = 11  #reverso = 11
                        digito_esperado = 11 - (total % 11) #d = 11 - (total % 11)
                        if digito_esperado > 9: #Se d for maior que 9
                            digito_esperado = 0 #d = 0
                        total = 0 #total = 0
                        sequencia_cpf_calculado += str(digito_esperado) #sequencia_cpf_calculado = sequencia_cpf_calculado + str(digito_esperado)
                if cpf == sequencia_cpf_calculado:    #Se cpf == digito_esperado
                   self.label2["text"] = "CPF válido!" #Imprime CPF válido
                else: #Se não
                    self.label2["text"] = "CPF inválido! Tente novamente" #Imprime CPF inválido

    def init_frame(self): #Cria a janela
        self.frame_up = Frame(
            self.root, width=500, height=30, bg=self.co0, relief="flat"
        )
        self.frame_up.pack(expand=True, fill="both")    #Empacota a janela

        self.frame_down = Frame(
            self.root, width=500, height=230, bg="white", relief="flat"
        )  #Cria a 2ª   
        self.frame_down.pack(expand=True, fill="both") #Empacota a 2ª
        
        titulo_frameup = Label(
            self.frame_up,
            text="Validador de CPF",
            anchor=CENTER,
            font=("Poppins 18 bold"),
            bg=self.co0,
            fg=self.co1,
        )  #Cria o título
        titulo_frameup.place(x=45, y=35)   #Posiciona o título

        label = Label(self.frame_down,font="Poppins 11",
            bg=self.co1,
            text="Informe os números do  CPF: ") #Cria o label
        label.place(x=45, y=10) #Posiciona o label

        label = Label(self.frame_down,font="Poppins 8",
            bg=self.co1,
            fg=self.co2,
            text="Digite somente os números\n sem traço ou pontos\n Exemplo: 12345678910")
        label.place(x=70, y=34)
    

        self.entry = Entry(self.frame_down,
        width=25,
        bd=1,
        relief=RAISED,
        font=("arial 12")) #Cria a entrada de dados
        self.entry.place(x=40, y=100) #Posiciona a entrada de dados

        self.btn = Button(
            self.frame_down,
            text="VALIDAR",
            font="Poppins 11 bold",
            width=20,
            relief=RAISED,
            command=self.validar)   #Cria o botão
        self.btn.place(x=45, y=140) #Posiciona o botão

        self.label2 = Label(self.frame_down, 
            font="Poppins 11 bold",
            bg=self.co1,
            text="") #Cria o label
        self.label2.place(x=40, y=200) #Posiciona o label

    
        self.root.mainloop() #Inicia a janela

if __name__ == "__main__": #Inicia o programa
    validador_Cpf() #Chama a classe