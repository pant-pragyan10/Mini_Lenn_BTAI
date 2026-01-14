import numpy as np
from sklearn.cluster import KMeans

# Train once (simulated behavior data)
behavior_data = np.array([
    [0.9, 0.2],
    [0.85, 0.3],
    [0.2, 0.8],
    [0.3, 0.7],
    [0.8, 0.4],
    [0.25, 0.75]
])

kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(behavior_data)

def classify_behavior(impulse_score: float, saving_score: float):
    cluster = kmeans.predict([[impulse_score, saving_score]])[0]

    # Interpret clusters manually (important!)
    centers = kmeans.cluster_centers_

    impulsive_cluster = np.argmax(centers[:, 0])  # higher impulse

    if cluster == impulsive_cluster:
        return "Impulsive Spender"
    else:
        return "Disciplined Saver"
