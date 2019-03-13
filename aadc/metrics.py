import numpy as np
from scipy.spatial import distance


# def compute_score(min_distances_a, min_distances_b, img_size):
#     scores = []
#     for key, value in min_distances_a.items():
#         scores.append(len(set(value[:img_size]).intersection(set(min_distances_b[key][:img_size]))) / img_size)
#
#     print('Score for size of ', img_size, ' ', np.average(scores))


def compute_estimators(origin, encoded):
    """gets origin and encoded distances and returns mean and std"""
    estimators = dict()
    for name, samples in {'origin': origin, 'encoded': encoded}.items():
        for dist_type, dist_vector in samples.items():
            estimators[name + '_' + dist_type + '_avg'] = np.average(dist_vector)
            estimators[name + '_' + dist_type + '_std'] = np.std(dist_vector)

    return estimators


def compute_score(origin, encoded, n=1):
    scores = {}
    for name, samples in {'origin': origin, 'encoded': encoded}.items():
        for dist_type, dist_vector in samples.items():
            dist_matrix =  distance.squareform(dist_vector)
            np.fill_diagonal(dist_matrix, np.inf)
            sorted_indices_matrix = np.argpartition(dist_matrix, list(range(dist_matrix.shape[0])), axis=1)
            trunc_sorted_indices_matrix = sorted_indices_matrix[:, :-n]
            trunc_sorted_indices_matrix

    # TODO: check the intersection between origin/encoded in trunc_sorted_indices_matrix (must change n to be > 1)
    pass

