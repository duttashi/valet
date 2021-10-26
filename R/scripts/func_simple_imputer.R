# Missing value treatment
# impute missing values with median or mode

impute_by_median_mode<- function(x)
  {
  if(is.numeric(x))
    ifelse(is.na(x),median(x,na.rm=T),x) 
  else x
} # end function
