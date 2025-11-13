import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# 1. Vendas por Região
# dados = {
#     "Região": ["Sul", "Sudeste", "Centro-Oeste", "Nordeste", "Norte"],
#     "Vendas": [35000, 52000, 27000, 31000, 18000]
# }
# df = pd.DataFrame(dados)
# plt.figure(figsize=(8, 5))
# sns.barplot(x="Região", y="Vendas", data=df, palette="viridis")
# plt.title("Vendas por Região")  
# plt.xlabel("Região")
# plt.ylabel("Vendas (R$)")
# plt.grid(axis='y')
# plt.show()

# 2. Satisfação do Cliente
# dados = {
#     "Cliente": ["Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Felipe", "Gabriela", "Heitor"],
#     "Satisfação": [8.5, 6.0, 9.0, 7.5, 8.0, 5.5, 9.5, 7.0],
#     "Categoria": ["Premium", "Básico", "Premium", "Básico", "Premium", "Básico", "Premium", "Básico"]
# }
# df = pd.DataFrame(dados)
# plt.figure(figsize=(10, 6))
# sns.boxplot(x="Categoria", y="Satisfação", data=df)
# plt.title("Satisfação do Cliente por Categoria")
# plt.xlabel("Categoria")
# plt.ylabel("Nível de Satisfação")
# plt.show()

# 3. Produtividade da Equipe
# dados = {
#     "Funcionário": ["Alice", "Bruno", "Carlos", "Diana", "Eduardo", "Fernanda", "Gustavo", "Helena"],
#     "Produtividade": [82, 74, 90, 65, 77, 88, 93, 70],
#     "Horas_Semanais": [40, 36, 42, 30, 38, 44, 45, 35]
# }
# df = pd.DataFrame(dados)
# plt.figure(figsize=(10, 6))
# sns.scatterplot(x ="Horas_Semanais", y="Produtividade", data=df)
# plt.title("Produtividade da Equipe")
# plt.xlabel("Horas Trabalhadas por Semana")
# plt.ylabel("Produtividade (%)")
# plt.show()

# 4. Lucro Mensal
# dados = {
#     "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"],
#     "Lucro": [12000, 15000, 17000, 14000, 16000, 18000, 22000, 21000, 19000, 23000, 25000, 24000]
# }
# df = pd.DataFrame(dados)
# plt.figure(figsize=(10, 6))
# sns.lineplot(x="Mês", y="Lucro", data=df)
# plt.title("Lucro da empresa ao Longo dos Meses")
# plt.xlabel("Mês")
# plt.ylabel("Lucro (R$)")
# plt.show()

# 5. Uso de Aplicativo
# dados = {
#     "Aplicativo": ["Instagram", "TikTok", "WhatsApp", "YouTube", "X (Twitter)"],
#     "Minutos por dia": [95, 110, 80, 120, 60]
# }
# df = pd.DataFrame(dados)
# plt.figure(figsize=(8, 5))
# sns.barplot(x="Aplicativo", y="Minutos por dia", data=df)
# plt.title("Uso de Aplicativos ")
# plt.xlabel("Aplicativo")
# plt.ylabel("Tempo por dia")
# plt.show()

# 6. Idade dos funcionários por setor
# dados = {
#     "Setor": ["Financeiro", "Comercial", "TI", "RH", "Marketing", "Comercial", "TI", "Financeiro", "Marketing", "RH"],
#     "Idade": [34, 29, 25, 41, 28, 33, 26, 38, 31, 45]
# }
# df = pd.DataFrame(dados)
# plt.figure(figsize=(10, 6))
# sns.boxplot(x="Setor", y="Idade", data=df)
# plt.title("Idade dos Funcionários por Setor ")
# plt.xlabel("Setor")
# plt.ylabel("Idade")
# plt.show()

# 7. Análise de custos e receitas
dados = {
    "Produto": ["Notebook", "Celular", "Tablet", "Fone", "Monitor"],
    "Custo": [2500, 1800, 1200, 200, 900],
    "Receita": [3200, 2300, 1700, 350, 1200]
}
df = pd.DataFrame(dados)
plt.figure(figsize=(10, 6))
sns.barplot(x="Produto", y="value", hue="variable", data=pd.melt(df, ["Produto"]))
plt.title("Análise de Custos e Receitas por Produto")
plt.xlabel("Produto")
plt.ylabel("Valor (R$)")
plt.show()