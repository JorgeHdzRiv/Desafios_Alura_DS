import matplotlib.pyplot as plt
import seaborn as sns

def graficos_barras_top10(df, columna):
  # Grafico en general
  plt.figure(figsize=(12, 8))
  ax = sns.countplot(y=columna,
                     data=df,
                     hue=columna,
                     order=df[columna].value_counts().index[:10])
  # Etiquetas y titulos
  plt.xlabel("Frecuencia", fontsize=12)
  plt.ylabel(columna.title(), fontsize=12)
  plt.title(f"Top 10 {columna.title()} más frecuentes", fontsize=14, pad=20)

  # Anotaciones
  conteos = df[columna].value_counts()[:10]

  # Anotaciones en cada barra
  for i, v in enumerate(conteos):
    ax.text(v + 1, i, f"{v:,}",
            va="center",            # Alineación vertical al centro
            fontsize=10,            # Tamaño de fuente
            fontweight="bold")      # Negrita

  # Ajustar
  plt.tight_layout()

  # Cuadricula
  plt.grid(True, axis="x", linestyle="--", alpha=0.7)

  # Guardar el grafico
  plt.savefig(f"./results/eda/top10_{columna}.png")
  plt.close()

def graficos_barras(df, columna):
  # Grafico en general
  plt.figure(figsize=(12, 8))
  ax = sns.countplot(y=columna,
                     data=df,
                     hue=columna,
                     order=df[columna].value_counts().index)
  # Etiquetas y titulos
  plt.xlabel("Frecuencia", fontsize=12)
  plt.ylabel(columna.title(), fontsize=12)
  plt.title(f"{columna.title()} más frecuentes", fontsize=14, pad=20)

  # Anotaciones
  conteos = df[columna].value_counts()

  # Anotaciones en cada barra
  for i, v in enumerate(conteos):
    ax.text(v + 1, i, f"{v:,}",
            va="center",            # Alineación vertical al centro
            fontsize=10,            # Tamaño de fuente
            fontweight="bold")      # Negrita

  # Ajustar
  plt.tight_layout()

  # Cuadricula
  plt.grid(True, axis="x", linestyle="--", alpha=0.7)

  # Guardar el grafico
  plt.savefig(f"./results/eda/{columna}_frecuencias.png")
  plt.close()

def histogramas(df, columna):
  plt.figure(figsize=(12, 8))
  sns.histplot(df[columna], kde=True,color="blue",bins=20)
  plt.xlabel(columna.title(), fontsize=12)
  plt.ylabel("Frecuencia", fontsize=12)
  plt.title(f"Distribución de {columna.title()}", fontsize=14, pad=20)
  plt.grid(True, axis="x", linestyle="--", alpha=0.7)
  plt.savefig(f"./results/eda/{columna}_distribucion.png")
  plt.close()

def boxplots(df, columna1,columna2):
  plt.figure(figsize=(12, 8))
  sns.boxplot(x=columna1, y=columna2, data=df, palette="pastel",
              hue=columna1,legend=False)
  plt.xlabel(columna1.title(), fontsize=12)
  plt.ylabel(columna2.title(), fontsize=12)
  plt.title(f"{columna1.title()} vs {columna2.title()}", fontsize=14, pad=20)
  plt.grid(True, axis="y", linestyle="--", alpha=0.7)
  plt.xticks(rotation=45)
  plt.savefig(f"./results/eda/{columna1.title()}_vs_{columna2.title()}.png")
  plt.close()

def barras_categoricas(df, columna1, columna2):
  plt.figure(figsize=(14, 8))
  sns.barplot(x=columna1, y=columna2, data=df, palette="viridis",
              hue=columna1, legend=False,errorbar=None)
  plt.xlabel(columna1.title(), fontsize=12)
  plt.ylabel(columna2.title(), fontsize=12)
  plt.title(f"{columna1.title()} vs {columna2.title()}", fontsize=14, pad=20)
  plt.xticks(rotation=90)
  plt.grid(True, axis="y", linestyle="--", alpha=0.7)
  plt.savefig(f"./results/eda/{columna1.title()}_vs_{columna2.title()}.png")
  plt.close()

def scatterplots(df, columna1, columna2):
  plt.figure(figsize=(12, 8))
  sns.scatterplot(x=columna1, y=columna2, data=df, color="purple", alpha=0.7)
  plt.xlabel(columna1.title(), fontsize=12)
  plt.ylabel(columna2.title(), fontsize=12)
  plt.title(f"{columna1.title()} vs {columna2.title()}", fontsize=14, pad=20)
  plt.grid(True, axis="both", linestyle="--", alpha=0.5)
  plt.savefig(f"./results/eda/{columna1.title()}_vs_{columna2.title()}.png")
  plt.close()

def pastel(df, columna):
  plt.figure(figsize=(12, 8))
  df[columna].value_counts().plot.pie(autopct="%1.1f%%", colors=["lightblue", "orange"])
  plt.title(f"{columna.title()}", fontsize=14, pad=20)
  plt.ylabel("")
  plt.savefig(f"./results/eda/{columna}_pastel.png")
  plt.close()

# Graficos de clusterizacion
def scatter_clusters(df, x, y):
    plt.figure(figsize=(12, 8))
    sns.scatterplot(x=x, y=y, hue='cluster', data=df,palette='Set1')
    plt.xlabel(x.title(), fontsize=12)
    plt.ylabel(y.title(), fontsize=12)
    plt.title(f"Clusters en {x} vs {y}", fontsize=14, pad=20)
    plt.grid(True, axis="both", linestyle="--", alpha=0.5)
    plt.legend(title="Cluster")
    plt.savefig(f"./results/clustering/{x}_vs_{y}_clusters.png")
    plt.close()

def distribuciones_clusters(df,x):
  plt.figure(figsize=(16, 8))
  sns.countplot(x=x, hue='cluster', data=df, palette='Set1')
  plt.xlabel(x.title(), fontsize=12)
  plt.ylabel("Frecuencia", fontsize=12)
  plt.title(f"Distribución de {x} por Cluster", fontsize=14, pad=20)
  plt.xticks(rotation=90)
  plt.grid(True, axis="y", linestyle="--", alpha=0.7)
  plt.legend(title="Cluster")
  plt.savefig(f"./results/clustering/{x}_clusters.png")
  plt.close()