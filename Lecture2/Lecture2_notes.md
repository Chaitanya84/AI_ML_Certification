# Linear Algebra
#### Simple objective principle component analysis
- Eigne values 
- Eigne vector
~ Google uses eigne values in page rank algorithm ~

### The key Idea

#### 1. If you have square matrix then you can easily find eigen value 
#### 2. If A is Square matrix of NxN then there will be N _Eigen_ values

- Determinant of matrix
- Transpose of the matrix
- Decomposition

_Exercise_: You have a black and white image of 256 x 256 pixel. If you want to store this iimage it will require 65535 bytes (vector i.e. matrix of single column) of data but can you find a way to store this image in a vector of 1000 element. Write a program to do it. 

1. How to find principle component ?
Principle component is the vector of 1000 pixel data in the above image. 

- Eigen value decomposition
-------------------------------
Concept :

 Matrix Similarity: \( A = U P U^{-1} \)

#### Question 1: What do A, U, and P represent in the equation \( A = U P U^{-1} \)?

This equation represents a **similarity transformation** of a matrix. It expresses a square matrix \( A \) as being similar to a (usually simpler) matrix \( P \), via a change of basis matrix \( U \).

### Definitions:

- **\( A \)**: The original square matrix (\( n \times n \)) we want to analyze.
- **\( U \)**: An invertible matrix whose columns are the (generalized) eigenvectors of \( A \).
- **\( P \)**: A simpler matrix similar to \( A \), usually in:
  - **Diagonal form** (if \( A \) is diagonalizable), or
  - **Jordan form** (if \( A \) is not diagonalizable).

### Scenarios:

#### 1. Diagonalizable Case:
If \( A \) has \( n \) linearly independent eigenvectors, then:

\[
A = U D U^{-1}
\]

- \( D \) is a diagonal matrix with eigenvalues of \( A \) on its diagonal.
- \( U \) contains the corresponding eigenvectors.

#### 2. Non-Diagonalizable Case (Jordan Form):
If \( A \) does **not** have enough independent eigenvectors, we use:

\[
A = U J U^{-1}
\]

- \( J \) is the **Jordan matrix**, which is almost diagonal but includes \( 1 \)'s just above the diagonal in some blocks.

---

#### Question 2: Sample R Code to Demonstrate \( A = U D U^{-1} \)

Below is an R example that performs eigen decomposition of a diagonalizable matrix:

```r
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
```
-----

