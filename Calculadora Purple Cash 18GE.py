def calculate_price(item, weight):
    per_kg = {"Lacre": 4.00, "Oleo": 2.00, "Plastico": 1.00, "Pet": 3.80, "Latinha": 6.50}
    if item not in per_kg:
        return "Invalid item"
    price = (weight/1000) * per_kg[item] * 0.3
    return price

print("Olá! esse calculador automático foi criado pelo clã do 18GERJ para o projeto Purple Cash. Ele irá calcular 30% do valor em cima da quantidade de reciclável inserida.")
item = input("Para começar, por favor, digite o seu reciclável: (Lacre, Oleo, Plastico, Pet, Latinha): ")
weight = float(input("Por favor, digite a quantidade em gramas: "))
price = calculate_price(item, weight)
if price == "Inválido! Por favor, tente novamente":
    print(price)
else:
    print("Que ótimo! Você tem essa quantia em Purple Cash: ", price)
print("O Clã Yin Yang agradece a sua contribuição")
