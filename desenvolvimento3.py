print("Laço WHILE")

andar = 20
while andar >= 1:
    if andar != 13:
        print(f"{andar}º andar")
    andar -= 1  

print("\nLaço DO-WHILE")

andar = 20
while True:
    if andar != 13:
        print(f"{andar}º andar")
    
    andar -= 1
    
    if andar < 1:
        break