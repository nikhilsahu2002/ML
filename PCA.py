import numpy as np
import matplotlib.pyplot as plt

x = np.array([4, 8, 13, 7])
y = np.array([11, 4, 5, 14])

x_mean = np.mean(x)
y_mean = np.mean(y)
x_centered = x - x_mean
y_centered = y - y_mean

data_matrix = np.column_stack((x_centered, y_centered))

cov_matrix = np.cov(data_matrix, rowvar=False)

eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

eigenvalue_order = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[eigenvalue_order]
eigenvectors = eigenvectors[:, eigenvalue_order]

explained_variance = eigenvalues / np.sum(eigenvalues)


transformed_data = np.dot(data_matrix, eigenvectors)

plt.scatter(x, y, label="Original Data", color='blue')

for i, eigenvector in enumerate(eigenvectors.T):
    plt.quiver(x_mean, y_mean, eigenvector[0], eigenvector[1], angles='xy', scale_units='xy', scale=1, color='red', label=f"Principal Component {i+1}")

plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid()
plt.show()

print("Principal Components (Eigenvectors):")
print(eigenvectors)
print("\nExplained Variance:")
print(explained_variance)
