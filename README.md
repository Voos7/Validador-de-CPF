Oi!

Criei um verificador de cpf!!

Primeiro você insere o CPF desejado e ele vai passar por um processo de filtragem, que retira os pontos e traços.

Depois vai verificar se ele tem 11 digitos e se não são numeros repetidos, ex: 0000000000

Depois ele vai fazer o calculo do primeiro digito verificador, multiplica todos os primeiros 9 numeros começando com 10 e indo até 2,
armazena na variavel soma e calcula o resto, que é o resultado da soma dos números dividido por 11.

Verifica se o resto é 10 ou 11 (norma pra verificação de CPF) e define para 0.

Se o resto (0) for diferente do decimo numero do cpf digitado ele retorna falso.

A segunda parte vai ser a mesma coisa, mudando apenas a posição do digito e o numero do "for" 



Esse foi meu primeiro projeto mais elaborado, se tiver alguma sugestão, fico feliz de ouvir!
