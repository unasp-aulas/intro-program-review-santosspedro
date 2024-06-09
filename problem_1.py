def main():
    salario = int(input("Insira um salário: "))
    print(f"Seu salário é {salario} reais")
    
    cargo = input("Insira um cargo (Junior, Pleno, Senior, Outro): ")
    
    if cargo == "Junior":
        junior = salario * 1.15
        salario = junior
        print(f"Seu salário para Junior é {junior} reais")
    elif cargo == "Pleno":
        pleno = salario * 1.26
        salario = pleno
        print(f"Seu salário para Pleno é {pleno} reais")
    elif cargo == "Senior":
        senior = salario * 1.34
        salario = senior
        print(f"Seu salário para Senior é {senior} reais")
    else:
        outro = salario  # Aqui assumimos que "Outro" não muda o salário
        salario = outro
        print(f"Seu salário para Outro é {outro} reais")
    
    return salario

salario_final = main()
print(f"Salário final: {salario_final} reais")
