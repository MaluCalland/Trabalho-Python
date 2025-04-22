# Alunos:
# Bruna Brandão - 2314290051
# Malu Calland - 2314290066
# João Schettini - 
# Sarah Mahdavi - 

# TRABALHO EM GRUPO

valor_inicial = float(input('VALOR INICIAL A SER DEPOSITADO NA CAIXINHA SUPER COFRINHO: '))
dias_investimento = int(input('DIAS PARA SEU INVESTIMENTO: '))
print(f'\nValor inicial da aplicação: R${valor_inicial:.2f}')
print(f'Dias para investimento: {dias_investimento} dias')

def calcular_taxa_diaria(): 
    taxa_anual = 14.15
    taxa_diaria = ((1 + taxa_anual / 100) ** (1 / 365)) - 1
    return taxa_diaria

def calcular_rendimento_bruto(valor, dias, taxa_diaria):
    rendimento_bruto = valor * ((1 + taxa_diaria) ** dias - 1)
    return rendimento_bruto

def calcular_iof(dias, rendimento):
    if dias > 30:
        return 0.0
    percentual_iof = max(0, 96 - (dias - 1) * 3)
    valor_iof = rendimento * (percentual_iof / 100)
    return valor_iof
    
def calcular_ir(dias, rendimento_apos_iof):
    if dias <= 180:
        percentual_ir = 22.5
    elif dias <= 360:
        percentual_ir = 20.0
    elif dias <= 720:
        percentual_ir = 17.5
    else:
        percentual_ir = 15.0
    valor_ir = rendimento_apos_iof * (percentual_ir / 100)
    return valor_ir

taxa_diaria = calcular_taxa_diaria()
rendimento = calcular_rendimento_bruto(valor_inicial, dias_investimento, taxa_diaria)
valor_iof = calcular_iof(dias_investimento, rendimento)
rendimento_pos_iof = rendimento - valor_iof
valor_ir = calcular_ir(dias_investimento, rendimento_pos_iof)
rendimento_liquido = rendimento_pos_iof - valor_ir
valor_final = valor_inicial + rendimento_liquido

print(f'\nTaxa diária: {taxa_diaria:.10f}')
print(f'\nRendimento bruto após {dias_investimento} dias: R${rendimento:.5f}')
print(f'\nDesconto IOF: R$ {valor_iof:.5f}')
print(f'\nDesconto IR: R$ {valor_ir:.5f}')
print(f'\nRendimento líquido: R$ {rendimento_liquido:.5f}')
print(f'\nValor final da aplicação: R$ {valor_final:.2f}')