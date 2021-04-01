# R 
This will be a basic overview of the `R` language. 


# Basics

Quickstart Syntax:
* R starts at 1 (not 0)
* `dataframe$column` 
* `v <- c(1,2,3,4)`


Dot notation is not the default in R, however it can be helpful as an alternative to camelcase. Given that we can just use *tab*.

animal.mammal.bear <- "Grizzly"
animal.mammal.rat <- "Common black"

## Variable Types
`class()` is used to determine the type.


R by default uses numeric, rather than  int, float, double, etc.


`NA` - "NULL"/etc.

`NaN` - not a number



as.integer(4.1)

as.numeric(4.1)

as.character(4.1)

as.logical(4.1)

## Data Structures
* *vectors* - 1D, one data type
* *matrix* - 2D, one data type
* *array* - more than 2D, one data type
* *dataframe* - 2D, many data types
* *list* - any size, many data types

### Vector

v <- c(1, 245, 35)

v

### Matrix

# matrix
m <- matrix(1:25, 5, 5)
m

### Array

a <- array(1:50, c(5, 5, 2))
print(a[,,1])
print(a[,,2])

### Dataframe

# dataframe
col1 <- rep("Yes", 5)
col2 <- 1:5
col3 <- TRUE 

df <- data.frame(col1, col2, col3)
names(df) <- c("Question", "id", "Bool")


df

Note the *broadcasting* with the use of `TRUE`

df$id

df[,1]

df[1,3] <- FALSE
df

### Lists

species <- c("grizzly", "panda", "black")
weight <- c(900, 600, 300)
df <- data.frame(c(1,2,3), c(FALSE, TRUE, TRUE))


l <- list(species = species, weight = weight, data=df)

l

l[[1]]

## Interacting with the system

* `getwd()`
* `setwd()`
* `read.table()`
* `write.table()`
* `read.csv()`
* `write.csv()`
* `read.delim()`
* `write.delim()`

## Control flow

`break` and `next` can be used

if(1 < 10){
    print("1 is less than 10")
}else{
    print("no.")
}

i = 0

while(i < 5){
    print(i)
    i = i + 1
}

for(n in 1:5){
    print(n)
}

### Functions


additionFunc <- function(x, y){
    return (x + y)
}



additionFunc(1, 2)

## Vectorisation

Applying an operation/function across a vector, matrix, etc. rather than iterating through each element.

Create a function that *sums every element in the matrix* (without using `sum`)

m <- matrix(runif(1000000),1000,1000)

# bad method

badMatrixSum <- function(matrixIn){
    counterTotal <- 0

    row_m <- dim(matrixIn)[1]
    col_m <- dim(matrixIn)[2]

    for(x in 1:row_m){
        for(y in 1:col_m){
            counterTotal <- counterTotal + matrixIn[x, y]
        }
    }

    return(counterTotal)
    
}



# better method
betterMatrixSum <- function(matrixIn){
    rowTotal <- 0
    counterTotal <- 0
    

    row_m <- dim(matrixIn)[1]
    
    for(x in 1:row_m){

            rowTotal <- rowTotal + matrixIn[x, ]
    }
    

    for(n in 1:length(rowTotal)){
        counterTotal <- rowTotal[n] + counterTotal
    }
    
    return(counterTotal)
    
}


print("bad method")
system.time(badMatrixSum(m))
print("better method")
system.time(betterMatrixSum(m))
print("sum")
system.time(sum(m))

### Apply family

* `apply` - godfather of the applys 
* `lapply` - takes and returns lists
* `sapply` - "simplify", wrapper for lapply

there are many other types, `tapply`, `mapply`, etc. 

m <- matrix(rnorm(100), 10, 10)

apply(m, 1, sum) # sum of each row

lapply(1:3, function(x) x^2)

sapply(1:3, function(x) x^2)