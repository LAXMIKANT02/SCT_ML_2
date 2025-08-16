import matplotlib
matplotlib.use('Agg')

from django.shortcuts import render
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def home(request):
    return render(request, 'clustering/home.html')

def cluster(request):
    df = pd.read_csv('clustering/Mall_Customers.csv')
    X = df[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]

    kmeans = KMeans(n_clusters=4)
    kmeans.fit(X)

    df['Cluster'] = kmeans.labels_
    centroids = kmeans.cluster_centers_

    # Count how many in each cluster
    counts = df['Cluster'].value_counts().sort_index().tolist()

    # Plot
    plt.figure()
    plt.scatter(X['Annual Income (k$)'], X['Spending Score (1-100)'], c=df['Cluster'])
    plt.scatter(centroids[:, 1], centroids[:, 2], marker='X', s=200)
    plt.xlabel('Annual Income')
    plt.ylabel('Spending Score')
    plt.title('K-Means Clusters')
    plt.savefig('clustering/static/plot.png')
    plt.close()

    # Pie Chart of cluster sizes
    plt.figure()
    labels = [f'Cluster {i+1}' for i in range(len(counts))]
    plt.pie(counts, labels=labels, autopct='%1.1f%%')
    plt.title('Cluster Distribution')
    plt.savefig('clustering/static/piechart.png')
    plt.close()

    return render(request, 'clustering/result.html', {
        'centroids': centroids,
        'counts': counts,
        'plot_url': 'plot.png',
        'piechart_url': 'piechart.png'
    })
