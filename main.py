#1.	Agora que seus conhecimentos de programação aumentaram, você decidiu refazer o programa que recebe notas dos alunos da sua vizinha. Na nova versão, o programa recebe um número indeterminado de notas (do tipo real) que estão vinculadas ao nome de cada aluno. Lembre-se de testar se há nomes iguais no dicionário antes de fazer a inserção. Se houver, não permita que a nota seja inserida e avise a usuária. Após a inserção de todas as notas, ofereça à usuária a opção de alterar ou excluir uma nota.


notas = {"laisa": 0}
print(notas)

for j in range(5):
  nome = input("insira o nome do aluno: ")
  def questao():
    p = "s"
    while p == "s":
      nts = float(input("insira as notas: "))
      p = input("quer continuar inserindo notas?: ")

    if nome in notas.keys():
      notas[nome]=nts
      print(nts)

    else:
      print("sua alteração foi salva com sucesso! ")
      print(nts)
  questao()

nome = input("deseja excluir algum aluno?")
if nome in notas.keys():
  notas.pop(nome)
  print(notas)
else:
  print("aluno inexistente!")
  print(notas)

nome = input("deseja excluir alguma nota do aluno?")
if nome in notas.keys():
  nts=float(input("insira as notas: "))
  notas[nome] = nts
  print(notas)
else:
  print("notas inexistentes")
  print(notas)
  