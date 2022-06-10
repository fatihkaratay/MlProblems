'''
given features
for each pid:
    compute distance(features, pid[features])
sort(distances)

return most frequent label(distance(1-k))
'''
import math

def predict_label(examples, features, k, label_key="is_intrusive"):
    knn = find_k_nearest_neighbors(examples, features, k)
    knn_labels = [examples[pid][label_key] for pid in knn]
    return round(sum(knn_labels) / k)

def find_k_nearest_neighbors(examples, features, k):
    distances = {}
    for pid, features_label_map in examples.items():
        distance = get_distance(features, features_label_map["features"])
        distances[pid] = distance
    return sorted(distances, key=distances.get)[:k]

def get_distance(features, other_features):
    squared_differences = []
    for i in range(len(features)):
        squared_differences.append((other_features[i] - features[i]) ** 2)
    return math.sqrt(sum(squared_differences))

