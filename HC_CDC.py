# Import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt


# Assign filename to BYAREA text file
filename = "byarea_10k.csv"

# Read in CDC Wonder text file BYAREA and put in a dataframe df
#df = pd.read_table(filename,sep='|')
df = pd.read_csv(filename,sep=',')

# Write out Dataframe as a CSV file byarea.csv
#df.to_csv("byarea.csv")
#df.to_csv('byarea_10k.csv')

# print out the columns names
df.columns

# print out the shape rows by columns
df.shape

# print out the data types for the columns can also use df.dtypes
df.info

# print out numeric data which is only the first(index[0] - unamed) column and the population column
df.describe()
# check for frequency counts in categorical data also checking for NA's by dropna=FALSE
print(df['EVENT_TYPE'].value_counts(dropna=False))
print(df.EVENT_TYPE.all)

# Convert 'YEAR','COUNT','POPULATION' to a numeric dtypes
df.YEAR = pd.to_numeric(df.YEAR, errors='coerce')
df.COUNT = pd.to_numeric(df['COUNT'], errors='coerce')
df.POPULATION = pd.to_numeric(df['POPULATION'], errors='coerce')

# convert null datatypes to category to save memory usage 103MB down to 44MB - 58% savings
df.AREA = df.AREA.astype('category')
df.RACE = df.RACE.astype('category')
df.SEX = df.SEX.astype('category')
df.AGE_ADJUSTED_CI_LOWER = df.AGE_ADJUSTED_CI_LOWER.astype('category')
df.AGE_ADJUSTED_CI_UPPER = df.AGE_ADJUSTED_CI_UPPER.astype('category')
df.AGE_ADJUSTED_RATE = df.AGE_ADJUSTED_RATE.astype('category')
df.CRUDE_CI_LOWER = df.CRUDE_CI_LOWER.astype('category')
df.CRUDE_CI_UPPER = df.CRUDE_CI_UPPER.astype('category')
df.CRUDE_RATE = df.CRUDE_RATE.astype('category')
df.SITE = df.SITE.astype('category')
df.EVENT_TYPE = df.EVENT_TYPE.astype('category')

# write out a new CSV file to save on disk space
# df.to_csv("byarea_new.csv")

# Notice that Incidence and Mortality are in the same column EVENT_TYPE. These need to be in separate
# columns. Using Pivot table create 2 new variables, (Incidence, Mortality). Keeping Area, year, race and sex fixed.
# Use popolation as values argument as this will be the data that is in the incidence and mortality columns now
df_pivot_1 = df.pivot_table(index=['SEX'], columns='EVENT_TYPE', values='POPULATION')
df_pivot_2 = df.pivot_table(index=['AREA'],columns='EVENT_TYPE', values='POPULATION')
df_pivot_3 = df.pivot_table(index=['AGE_ADJUSTED_RATE'],columns='EVENT_TYPE',values="POPULATION")
df_pivot_4 = df.pivot_table(index=['COUNT'],columns='EVENT_TYPE',values='POPULATION')

#print out df_pivot to check on reporting format
df_pivot_1

# Plot some views of Incidence and Mortality based upon Population, AREA
# Plotting as a bar chart
plot1 = df_pivot_1.plot(kind='bar')
plot1.legend(loc='upper right',title='Incidence and Mortality by SEX')
# plot1.set_ylabel('Incidence')
# plot1.set_xlabel('Mortality')
plt.show()

plot2 = df_pivot_2.plot(kind='bar')
plot2.legend(loc='upper right',title='Incidence and Mortality by AREA')
plt.show()

plot3 = df_pivot_3.plot(kind='bar')
plot3.legend(loc='upper right',title='Incidence and mortality by AGE')
plt.show()

plot4 = df_pivot_4.plot(kind='bar')
plot4.legend(loc='upper right',title='Incidence and mortality by COUNT')
plt.show()

# Filter EVENT_TYPE to create slices of Incidence and Mortality as their own dataframe
#df_incidence = df[df.EVENT_TYPE == "Incidence"]
#df_mortality = df[df.EVENT_TYPE == "Mortality"]

#df.incidence = df_incidence.rename(columns={'EVENT_TYPE': 'Incidence'})
#df.mortality = df_mortality.rename(columns={'EVENT_TYPE': 'Mortality'})

#df_incidence = df_incidence.reset_index
#df_mortality = df_mortality.reset_index
# merge the dataframes back together by merging them horizontally
#df_merge = pd.merge(df_incidence,df_mortality,left_on=['AREA','YEAR','RACE','SEX'],right_on=['POPULATION'])
# creates columns incidence and mortality
#df_merge = pd.merge(df_incidence,df_mortality,left_on="AREA",right_on='CRUDE_RATE')
