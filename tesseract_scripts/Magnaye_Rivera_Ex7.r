# Magnaye_Ex7.R

x <- c(1995,2000,2005,2010,2015)
y <- c(68349452,75505061,82079348,87940171,93440274)

sortLag <- function(x, y){
  
  # sorts data in terms of X
  
  o <- order(x)
  x <- x[o]
  y <- y[o]
  
  return(list(x=x, y=y))
}

sortNev <- function(gx, x, y){
  
  # sorts data in terms of x distance to gx
  
  s <- sortLag(x,y)
  
  x <- s$x
  y <- s$y

  x_abs = abs(x-gx)
  o = order(x_abs)
  x = x[o]
  y = y[o]
  
  return(list(x=x, y=y, xabs=x_abs))
}

lix <- function(n, i, x, y){
  
  # returns the L[i](x) of the function given the i and the n
  
  finalString <- ""
  
  c <- 1
  for(j in (1:n)){
    if(j != i){
      finalString <- paste(finalString,"((x - ", as.character(x[j]),") / (",as.character(x[i])," - ",as.character(x[j]),"))",sep="")
      if(j != n && c < n-1){
        finalString <- paste(finalString," * ", sep = "") 
        c <- c + 1
      }
    }
  }
  
  return(finalString)
  
}

Lagrange <- function(x, y){
  
  # returns function that intetpolates xy
  
  n <- length(x)
  
  s <- sortLag(x,y)
  x <- s$x
  y <- s$y
  
  finalString <- "f <- function(x) "
  
  for(i in (1:n)){
    finalString <- paste(finalString, y[i], " * ", lix(n, i, x, y), sep="") # adds the function the f(x[i]) and l[i](x)
    if(i != n)finalString <- paste(finalString," + ",sep="")
  }
  
  return(list(f=eval(parse(text = finalString))))
}

print(ret <- Lagrange(x,y))


Neville <- function(x, y, gx){
  
  # returns the matrix of the neville method and the value of the interpolation function given gx
  
  n <- length(x)
  
  s <- sortNev(gx,x,y)
  x <- s$x
  y <- s$y
  a <- s$xabs
  
  ddMatrix <- matrix(data = 0, nrow = n, ncol = n+3, byrow = TRUE)
  ddMatrix[,1] <- c(1:n)
  ddMatrix[,2] <- x
  ddMatrix[,3] <- a
  ddMatrix[,4] <- y
  
  for(j in (5:ncol(ddMatrix))){
    for(i in (1:nrow(ddMatrix))){
      if(i <= ncol(ddMatrix) - j+1){
        ddMatrix[i,j] <- (((gx - x[i]) * ddMatrix[i+1, j-1]) + ((x[i+j-4] - gx) * ddMatrix[i, j-1])) / (x[i+j-4] - x[i]) 
      }
    }
  }
  
  return((list(mat=ddMatrix, value=ddMatrix[1,ncol(ddMatrix)])))
}

print(ret2 <- Neville(x,y,2004))