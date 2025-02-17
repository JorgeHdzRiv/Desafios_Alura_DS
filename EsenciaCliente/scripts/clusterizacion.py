import pandas as pd
import os
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score
os.environ["LOKY_MAX_CPU_COUNT"] = "4"  # O el número de núcleos físicos que desees usar

def comprobacion_clusters(X_std):
    # Crear carpeta si no existe
    os.makedirs("./results/clustering", exist_ok=True)

    # Aplicar PCA para reducir la dimensionalidad antes de KMeans
    pca_kmeans = PCA(n_components=2)
    X_pca_kmeans = pca_kmeans.fit_transform(X_std)  # X_std ya está estandarizado

    # Método del Codo (Elbow Method) y Silhouette Score
    inercia_pca = []
    scores_silhouette_pca = []

    comparison_results = {
        "Número de Clusters": [],
        "Silhouette Score": [],
        "Davies-Bouldin Score": [],
        "Calinski-Harabasz Score": []
    }

    # Calcular métricas para cada número de clusters en el rango
    for k in range(3, 11):
        kmeans_pca = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans_pca.fit(X_pca_kmeans)

        labels = kmeans_pca.labels_

        inercia_pca.append(kmeans_pca.inertia_)  # Inercia
        silhouette = silhouette_score(X_pca_kmeans, labels)  # Silhouette Score
        scores_silhouette_pca.append(silhouette)  # 🔹 Se agrega correctamente a la lista
        davies_bouldin = davies_bouldin_score(X_pca_kmeans, labels)
        calinski_harabasz = calinski_harabasz_score(X_pca_kmeans, labels)

        # Guardar métricas en el diccionario
        comparison_results["Número de Clusters"].append(k)
        comparison_results["Silhouette Score"].append(silhouette)
        comparison_results["Davies-Bouldin Score"].append(davies_bouldin)
        comparison_results["Calinski-Harabasz Score"].append(calinski_harabasz)

    # Graficar resultados
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(range(3, 11), inercia_pca, marker='o', linestyle='-', color='b')
    plt.xlabel('Número de Clusters')
    plt.ylabel('Inercia (Suma de Cuadrados Intra-cluster)')
    plt.title('Método del Codo con PCA')

    plt.subplot(1, 2, 2)
    plt.plot(range(3, 11), scores_silhouette_pca, marker='o', linestyle='-', color='g')
    plt.xlabel('Número de Clusters')
    plt.ylabel('Coeficiente de Silueta')
    plt.title('Silhouette Score con PCA')

    # Ajustar el diseño de la gráfica y guardar
    plt.tight_layout()
    plt.savefig("./results/clustering/elbow_silhouette_pca.png")

    # Guardar las métricas en CSV
    df_comparison = pd.DataFrame(comparison_results)
    df_comparison.to_csv("./results/clustering/comparison_results.csv", index=False)

    print("Análisis de clusters completado.")

def instanciar_kmeans(df, X_std):
    variables_elegidas = [
        "categoria_alimento",
        "departamento",
        "tipo",
        "ventas_tienda(en millones)",
        "costo_tienda(en millones)",
        "pais",
        "estado_civil",
        "genero",
        "escolaridad",
        "miembro",
        "ocupacion",
        "ingreso_anual",
        "numero_hijos",
        "pies_cuadrados_tienda",
        "costo"
    ]

    # Crear una copia explícita para evitar advertencias
    df_clusters = df[variables_elegidas].copy()

    # Aplicar PCA para reducir la dimensionalidad antes de la clusterización con KMeans
    pca_kmeans = PCA(n_components=2)  # Reducimos a 2 dimensiones
    X_pca_kmeans = pca_kmeans.fit_transform(X_std)  # Se definió X_std anteriormente

    # Instanciar KMeans con 5 clusters
    kmeans_final = KMeans(n_clusters=5, random_state=42, n_init=50, max_iter=500, init='k-means++')

    # Ajustar el modelo con el conjunto de datos X_pca_kmeans
    kmeans_final.fit(X_pca_kmeans)

    # Asignar los clusters al DataFrame copiado sin advertencias
    df_clusters.loc[:, 'cluster'] = kmeans_final.labels_

    # Guardar el DataFrame con los clusters en un archivo CSV
    df_clusters.to_csv("./results/clustering/datos_clusterizados.csv", index=False)

    print("\nClusterización completada.")

    return df_clusters