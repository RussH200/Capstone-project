# read in byarea table to create a dataframe w 14 variables by 10 rows : byarea
byarea10 <- read.table("BYAREA.TXT",sep="|",nrows=10)
# print out byarea to check format
byarea10
# Separate incidence from mortality in Event_Type col 6
# Is this data the same for the other files - this may be all you need
# Read in byage.txt to create dataframe
byage10 <- read.table("BYAGE.TXT",sep="|",nrows = 10)
#print out byage10 first 10 rows
byage10
# readin in byesite table to create dataframe
bysite10 <- read.table("BYSITE.TXT",sep="|",nrows = 10)
# print out bysite
bysite10



