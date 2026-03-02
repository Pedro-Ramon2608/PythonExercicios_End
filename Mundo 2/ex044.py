preco = float(input('Preço das compras: R$'))
print('''Escolha uma forma de pagamento: 
[ 1 ] à vista dinheiro (10% de desconto)
[ 2 ] à vista no cartão (5% de desconto)
[ 3 ] 2x no cartão (valor total a ser pago dividido em 2x)
[ 4 ] 3x ou mais no cartão (20% de juros)''')
opcao = int(input('Qual será a forma de pagamento? '))
if opcao == 1:
    novo = preco - (preco * 10 / 100)
    print('A opção selecionada foi DINHEIRO. \nO valor total era de R${:.2f}, e o valor com desconto é de R${:.2f}'.format(preco, novo))
elif opcao == 2:
    novo = preco - (preco * 5 / 100)
    print('A opção selecionada foi CARTÃO À VISTA. \nO valor total era de R${:.2f}, e o valor com desconto é de R${:.2f}'.format(preco, novo))
elif opcao == 3:
    novo = preco / 2
    print('A opção selecionada foi 2x no CARTÃO. \nVocê terá 2 parcelas de R${:.2f}'.format(novo))
elif opcao == 4:
    novo = preco + (preco * 20 / 100)
    parcela = int(input('Quantas parcelas? '))
    valor = novo / parcela
    print('A opção selecionada foi 3x ou mais no CARTÃO. \nO valor total era de R${:.2f}, e o valor a ser pago com JUROS será de R${:.2f} \nA compra foi dividida em {}x de R${:.2f}'.format(preco, novo, parcela, valor))
