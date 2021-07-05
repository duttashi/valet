# function to find duplicate values in a dataframe and return them
get_duplicates <- function(df){
  total_rows = dim(df)[1]
  unique_rows = dim(df %>% group_by_all %>% count)[1]
  n_duplicates = (total_rows - unique_rows)
  cat('n duplicates -> ', n_duplicates)
}
