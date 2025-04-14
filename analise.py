import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv("dados_clientes.csv")

# Verificar quantos clientes contrataram empréstimo
emprestimo_counts = df["contratou_emprestimo"].value_counts()

# Gráfico 1: Quantidade de clientes que contrataram empréstimo
plt.figure(figsize=(6,4))
emprestimo_counts.plot(kind="bar", color=["green", "red"])
plt.title("Clientes que contrataram empréstimo")
plt.xlabel("Contratou empréstimo")
plt.ylabel("Quantidade")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("grafico_emprestimo.png")
print("✅ Gráfico 1 salvo: grafico_emprestimo.png")

# Gráfico 2: Renda média por grupo
media_renda = df.groupby("contratou_emprestimo")["renda_mensal"].mean()

plt.figure(figsize=(6,4))
media_renda.plot(kind="bar", color=["orange", "blue"])
plt.title("Renda média por grupo de empréstimo")
plt.xlabel("Contratou empréstimo")
plt.ylabel("Renda Média")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("grafico_renda.png")
print("✅ Gráfico 2 salvo: grafico_renda.png")
