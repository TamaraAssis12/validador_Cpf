class validador_Cpf():
    def __init__(self, cpf):
        self.cpf = cpf

    """ Efetua a validação do CPF, tanto formatação quando dígito verificadores.

    Parâmetros:
        cpf (str): CPF a ser validado

    Retorno:
        bool:
            - Falso, quando o CPF não possuir o formato 999.999.999-99;
            - Falso, quando o CPF não possuir 11 caracteres numéricos;
            - Falso, quando os dígitos verificadores forem inválidos;
            - Verdadeiro, caso contrário.

    Exemplos:

    >>> validate('529.982.247-25')
    True
    >>> validate('52998224725')
    False
    >>> validate('111.111.111-11')
    False
    """

    def valida_tamanho_cpf(self): 
        # Verifica se o CPF possui 11 números ou se todos são iguais:
        if len(self.cpf) != 11 or len(set(self.cpf)) == 1:
            return False
        else:
            cpf = self.cpf
            novo_cpf = cpf[:9] #pega os 9 primeiros dígitos do cpf
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
                    novo_cpf += str(d)
            sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)
            if cpf == novo_cpf and not sequencia:
                return True
            else:
                return False

    def formata_cpf(self):
        mascara = MaskedText(self.cpf, mask='###.###.###-##')
        return mascara

    def __str__(self):
        return self.formata_cpf()