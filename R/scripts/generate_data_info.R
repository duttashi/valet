# function that provides all the required information about the data
# function naming convention follows Hadlye's book Advanced R
# Variable and function names should be lowercase. Use an underscore (_) to separate words within a name. Generally, variable names should be nouns and function names should be verbs. Strive for names that are concise and meaningful (this is not easy!).
# Reference: http://adv-r.had.co.nz/Style.html#:~:text=Variable%20and%20function%20names%20should,this%20is%20not%20easy!).

generate_data_info<- function(df){
  NAvalues <- list(); NAclass <- list(); UniqueVals <- list(); ColName <- names(df); Index <- c(1:dim(df)[2])
  for(i in 1:dim(df)[2]) {
    NAvalues[i] <- sum(is.na(df[,i]))
    NAclass[i] <- class(df[,i])
    if(class(df[,i])=="numeric" | class(df[,i])=="integer") {
      UniqueVals[i] <- 'Not Applicable'
    }
    else{
      UniqueVals[i] <- length(unique(df[,i]))
    }
  }
  NAlist <- cbind(Index,ColName,NAvalues,NAclass,UniqueVals) 
}

# check the function
data(mtcars)
data_info <- generate_data_info(mtcars)
data_info
