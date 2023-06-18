idadeh1 = int(input("Informe a idade do primeiro homem: "))
idadeh2 = int(input("Informe a idade do segundo homem: "))

idadem1 = int(input("Informe a idade da primeira mulher: "))
idadem2 = int(input("Informe a idade da segunda mulher: "))
if idadeh1 > idadeh2:
  if idadem1 > idadem2:
    soma = (idadeh1 + idadem2)
    produto = (idadeh2 * idadem1)
    print(f'A soma da idade do homem mais velho com a da mulher mais nova {soma}')
    print(f'O produto da idade do homem mais novo com a mulher mais velha {produto}')
  