# Install jsonlite package
#install.packages("jsonlite")


#Simple Hello world
print("HelloWorld", quote=FALSE)

#Creating a VECTOR
v <- c(1,2,3,4,5)
print(v)
z <- c("A","B","C")
print(z)


#create a vector 
v1 <- c(1,2,3,4,5)
v2 <- c(6,7,8,9,10)
print(v1+v2)  #Element wise addition
print(v1*v2)  #Element wise multiplication
print(v2-v1)  #Element wise subtraction
print(v2/v1)  #Element wise division
print(v2^v1)  #Element wise power
print(v2%%v1) #Element wise modulus
print(v2%/%v1) #Element wise integer division
print(v1[1])  #Accessing first element of vector
print(v1[2])  #Accessing second element of vector
print(v1[1:3]) #Accessing first three elements of vector
print(v1[c(1,3,5)]) #Accessing first, third and fifth elements of vector
ls()          #List all variables
rm(list=ls()) #Remove all variables
ls()          #List all variables

#?matrix  #Help on matrix function
#Creating a MATRIX
m <- matrix(1:9, nrow=3, ncol=3, byrow=TRUE)
print(m)
m <- matrix(1:9, nrow=3, ncol=3, byrow=FALSE)
print(m)  
m <- matrix(data = c(1,2,5,8,1,4), nrow=2, ncol=3, byrow=TRUE)
print(m)
m <- matrix(m, nrow=3, ncol=2, byrow=FALSE)
print(m)

xR <- rnorm(50) #Generate 1000 random numbers from normal distribution
print(xR)

xR <- xR+ rnorm(50, mean=50, sd=0.1) #Generate 1000 random numbers from normal distribution with mean 100 and standard deviation 15
print(xR)