# Linear Algebra
#### Simple objective principle component analysis
- Eigne values 
- Eigne vector
~ Google uses eigne valuesin page rank algorithm ~

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

Any Square matrix A can be represented as 

### A = U x P x U<sup>-1</sup>
- P is the Eigen value matrix of A

## there are 2 problem 
- Inverse of all matrix can not always exist
- Not all matrix will always be square 

<span style="color:red">_Singular Value decomposition_ </span>
### A = U x S x V<sup>T</sup>
- S is the singular value of matrix

1. Find A x A<sup>T</sup>
2. Find Eigne **vector** of A x A<sup>T</sup> **_This is U_** 
3. Find A<sup>T</sup> x A
4. Find Eigen **vector** of A<sup>T</sup> x A **_This is V_**
5. Find Eigen **value** of A x A<sup>T</sup> **_This is S_** 