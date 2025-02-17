import pandas as pd
from graficos_funciones import (
    graficos_barras_top10,
    graficos_barras,
    histogramas,
    boxplots,
    barras_categoricas,
    scatterplots,
    pastel,
    scatter_clusters,
    distribuciones_clusters
)

def generar_graficos_eda(df):
    """Genera todos los gráficos de exploración de datos."""
    
    # Categorias
    graficos_barras_top10(df, "categoria_alimento")
    graficos_barras_top10(df, "departamento")
    graficos_barras(df, "tipo")
    graficos_barras(df, "escolaridad")
    graficos_barras_top10(df, "ocupacion")

    # Histogramas
    histogramas(df, "ventas_tienda(en millones)")
    histogramas(df, "ingreso_anual")

    # Diagramas de caja o Boxplots
    boxplots(df, "estado_civil", "ingreso_anual")
    boxplots(df, "genero", "ventas_tienda(en millones)")
    boxplots(df, "escolaridad", "ingreso_anual")

    # Barras categoricas
    barras_categoricas(df, "categoria_alimento", "ventas_tienda(en millones)")
    barras_categoricas(df, "departamento", "ventas_tienda(en millones)")
    barras_categoricas(df, "tipo", "ventas_tienda(en millones)")

    # Scatterplots
    scatterplots(df, "ingreso_anual", "numero_hijos")

    # Gráfico de pastel
    pastel(df, "miembro")

    print("\nExploración de datos finalizada")

def generar_graficos_clustering(df_clusters):
    """Genera todos los gráficos de clusterización."""
    scatter_clusters(df_clusters, "ventas_tienda(en millones)", "costo_tienda(en millones)")
    scatter_clusters(df_clusters, "ingreso_anual", "numero_hijos")
    distribuciones_clusters(df_clusters, "categoria_alimento")
    distribuciones_clusters(df_clusters, "departamento")
    distribuciones_clusters(df_clusters, "estado_civil")
    distribuciones_clusters(df_clusters, "escolaridad")
    distribuciones_clusters(df_clusters, "miembro")
    distribuciones_clusters(df_clusters,"ocupacion")

    print("\nGráficos de clusterización finalizados")
