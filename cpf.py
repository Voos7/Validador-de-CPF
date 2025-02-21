
cpf = input("Qual seu CPF? ")
cpf = cpf.replace(".","").replace("-","") # Remove pontos e tracos

if len(cpf) != 11 or len(set(cpf)) == 1:
    print("Não atende especificações")
    exit()

soma = 0
for i in range(9):
    soma += int(cpf[i]) * (10 - i)
resto = 11 - (soma % 11)
if resto == 10 or resto == 11:
    resto = 0
if resto != int(cpf[9]):
    print("falso")
    exit()

soma = 0
for i in range(10):
    soma += int(cpf[i]) * (11 - i)
resto = 11 - (soma % 11)
if resto == 10 or resto == 11:
    resto = 0
if resto != int(cpf[10]):
    print("False")
    exit()

print("CPF valido!")