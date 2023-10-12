import numpy as np
import matplotlib.pyplot as plt

# Define your data points
x = np.array([4, 8, 13, 7])
y = np.array([11, 4, 5, 14])

# Center the data (subtract the mean)
x_mean = np.mean(x)
y_mean = np.mean(y)
x_centered = x - x_mean
y_centered = y - y_mean

# Create the data matrix
data_matrix = np.column_stack((x_centered, y_centered))

# Calculate the covariance matrix
cov_matrix = np.cov(data_matrix, rowvar=False)

# Calculate eigenvalues and eigenvectors of the covariance matrix
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# Sort eigenvalues and eigenvectors in descending order
eigenvalue_order = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[eigenvalue_order]
eigenvectors = eigenvectors[:, eigenvalue_order]

# Calculate the explained variance
explained_variance = eigenvalues / np.sum(eigenvalues)

# Calculate the transformed data
transformed_data = np.dot(data_matrix, eigenvectors)

# Plot the original data
plt.scatter(x, y, label="Original Data", color='blue')

# Plot the principal components
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
