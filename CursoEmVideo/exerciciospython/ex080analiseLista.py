print("""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre: 
A) Quantos números foram digitados;
B) A lista de valores ordenada de forma decrescente;
C) Se o valor 5 foi digitado e está ou não na lista.
""")

programa = True
valores = []
while programa == True:
    valor = int(input("Digite um número: "))
    valores.append(valor)
    while True:
        resp = input("Quer continuar? [S/N]").strip().upper()[0]
        if resp == "N":
            print("Programa encerrado!")
            programa = False
            break
        elif resp == "S":
            break
        else:
            print("Opção inválida, tente novamente!", end=" ")
valores.sort(reverse=True)
print(f"Você digitou {len(valores)} valores")
print(f"Os valores em ordem decrescente são {valores}")
if 5 in valores:
    print("O valor 5 faz parte da lista")
else:
    print("O valor 5 NÃO faz parte da lista")
