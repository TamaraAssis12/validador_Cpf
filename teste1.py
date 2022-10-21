cpf = str(input('Digite o seu CPF: '))

# Verifica se o CPF possui 11 números ou se todos são iguais:
if len(cpf) != 11 or len(set(cpf)) == 1:
    print('CPF inválido')
    
else:
    cpf = cpf[:9] #pega os 9 primeiros dígitos do cpf
    reverso = 10 #contador reverso
    total = 0 
    for index in range(19):#Para cada index em range(19)
        if index > 8: #Se o index for maior que 8
            index -= 9 #index = index - 9
        total += int(cpf[index]) * reverso  #total = total + int(cpf[index]) * reverso
        reverso -= 1 #reverso = reverso - 1
        if reverso < 2:    #Se reverso for menor que 2
            reverso = 11  #reverso = 11
            d = 11 - (total % 11) #d = 11 - (total % 11)
            if d > 9: #Se d for maior que 9
                d = 0 #d = 0
            total = 0 #total = 0
            cpf += str(d) #cpf = cpf + str(d)
    sequencia = cpf == str(cpf[0]) * len(cpf) #sequencia = cpf == str(cpf[0]) * len(cpf)
    if cpf == cpf and not sequencia:    #Se cpf == cpf e não sequencia
        print('CPF inválido') #Imprime CPF válido
    else: #Se não
        print('CPF Válido') #Imprime CPF inválido


        