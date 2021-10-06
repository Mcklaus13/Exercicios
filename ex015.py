preco = float(input('Digite o valor do produto: R$ '))
print(f'Se o pagamento for à vista você tem 10% de desconto e o valor fica R${preco-(preco * 10 / 100):.2f}\n'
      f'Se for parcelado tem um acréscimo de 8% e o valor fica de R${preco + (preco * 8 /100):.2f}')
