nome = input("Digite seu nome completo: ")

while True:
    try:
        ano_nascimento = int(input("Digite seu ano de nascimento (1922-2021): "))
        if 1922 <= ano_nascimento <= 2021:
            break
        else:
            print("Erro: O ano deve estar entre 1922 e 2021.")
    except ValueError:
        print("Erro: Digite um número válido.")

idade = 2022 - ano_nascimento

print(f"Nome: {nome}")
print(f"Idade completada (ou a completar) em 2022: {idade} anos")