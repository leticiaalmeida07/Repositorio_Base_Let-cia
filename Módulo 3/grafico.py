import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Criando dados
dados = {
    "Ingles":[6,5,7,6,7],
    "Comunicação":[9,10,9,10,9],
    "Trabalho em Equipe":[8,7,9,8,9],
    "Habilidade":[7,8,6,7,8],
    "Proatividade":[8,9,7,8,9]
}
df = pd.DataFrame(dados)
plt.figure(figsize=(10, 6))
sns.histplot(data=df)
plt.title("Habilidades Profissionais da Letícia")
plt.xlabel("Habilidades")
plt.ylabel("Nível de Proficiência")
plt.show()

    

