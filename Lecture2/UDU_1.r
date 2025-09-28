# Define a simple 2x2 matrix A
A <- matrix(c(4, 1,
              2, 3), nrow = 2, byrow = TRUE)

# Eigen decomposition
eig <- eigen(A)

# U is the matrix of eigenvectors
U <- eig$vectors

# D is the diagonal matrix of eigenvalues
D <- diag(eig$values)

# Reconstruct A: A = U * D * U^-1
A_reconstructed <- U %*% D %*% solve(U)

# Print original and reconstructed A
cat("Original A:\n")
print(A)

cat("\nReconstructed A (from eigen decomposition):\n")
print(A_reconstructed)

# Check if they are (approximately) equal
cat("\nDifference (A - A_reconstructed):\n")
print(A - A_reconstructed)