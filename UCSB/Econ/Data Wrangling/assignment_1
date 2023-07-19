#loading libraries
library(tidyverse)

library(readr)

library(janitor)

column_one <-
  c(8,10,4,1,30)
column_two <-
  c("hello","welcome","to","Econ","145")
column_three <-
  c(0,0,17,NA,15)
tibble_one <-
  tibble(column_one, column_two, column_three)
data_type_one<-typeof(column_one)
data_type_two<-typeof(column_two)
summary_stats_column_one <- 
  c(mean(column_one), 
    var(column_one), 
    sd(column_one))
summary_stats_column_three<-
  c(mean(column_three, na.rm = T), 
    var(column_three, na.rm = T), 
    sd(column_three, na.rm = T))
tidyverse_packages <- tidyverse_packages()
school_crime <- read_csv("assign_1.csv")
school_crime_colnames <- colnames(school_crime)
school_crime <- clean_names(school_crime)
na_location <- is.na(school_crime$location)
