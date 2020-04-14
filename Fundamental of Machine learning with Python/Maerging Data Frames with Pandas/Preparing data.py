# Exercise
# Reading DataFrames from multiple files
# When data is spread among several files, you usually invoke pandas' read_csv() (or a similar data import function) multiple times to load the data into several DataFrames.

# The data files for this example have been derived from a list of Olympic medals awarded between 1896 & 2008 compiled by the Guardian.

# The column labels of each DataFrame are NOC, Country, & Total where NOC is a three-letter code for the name of the country and Total is the number of medals of that type won (bronze, silver, or gold).

# This course touches on a lot of concepts you may have forgotten, so if you ever need a quick refresher, download the Pandas Cheat Sheet and keep it handy!

# Instructions

# Import pandas as pd.
# Read the file 'Bronze.csv' into a DataFrame called bronze.
# Read the file 'Silver.csv' into a DataFrame called silver.
# Read the file 'Gold.csv' into a DataFrame called gold.
# Print the first 5 rows of the DataFrame gold. This has been done for you, so hit 'Submit Answer' to see the results.
# Import pandas

import pandas as pd

# Read 'Bronze.csv' into a DataFrame: bronze
bronze = pd.read_csv('Bronze.csv')

# Read 'Silver.csv' into a DataFrame: silver
silver = pd.read_csv('Silver.csv')

# Read 'Gold.csv' into a DataFrame: gold
gold = pd.read_csv('Gold.csv')

# Print the first five rows of gold
print(gold.head())

# Exercise
# Reading DataFrames from multiple files in a loop
# As you saw in the video, loading data from multiple files into DataFrames is more efficient in a loop or a list comprehension.

# Notice that this approach is not restricted to working with CSV files. That is, even if your data comes in other formats, as long as pandas has a suitable data import function, you can apply a loop or comprehension to generate a list of DataFrames imported from the source files.

# Here, you'll continue working with The Guardian's Olympic medal dataset.

# Instructions

# Create a list of file names called filenames with three strings 'Gold.csv', 'Silver.csv', & 'Bronze.csv'. This has been done for you.
# Use a for loop to create another list called dataframes containing the three DataFrames loaded from filenames:
# Iterate over filenames.
# Read each CSV file in filenames into a DataFrame and append it to dataframes by using pd.read_csv() inside a call to .append().
# Print the first 5 rows of the first DataFrame of the list dataframes. This has been done for you, so hit 'Submit Answer' to see the results.

# Import pandas
import pandas as pd

# Create the list of file names: filenames
filenames = ['Gold.csv', 'Silver.csv', 'Bronze.csv']

# Create the list of three DataFrames: dataframes
dataframes = []
for filename in filenames :
    dataframes.append(pd.read_csv(filename))

# Print top 5 rows of 1st DataFrame in dataframes
print(dataframes[0].head())

# Exercise
# Combining DataFrames from multiple data files
# In this exercise, you'll combine the three DataFrames from earlier exercises - gold, silver, & bronze - into a single DataFrame called medals. The approach you'll use here is clumsy. Later on in the course, you'll see various powerful methods that are frequently used in practice for concatenating or merging DataFrames.

# Remember, the column labels of each DataFrame are NOC, Country, and Total, where NOC is a three-letter code for the name of the country and Total is the number of medals of that type won.

# Instructions

# Construct a copy of the DataFrame gold called medals using the .copy() method.
# Create a list called new_labels with entries 'NOC', 'Country', & 'Gold'. This is the same as the column labels from gold with the column label 'Total' replaced by 'Gold'.
# Rename the columns of medals by assigning new_labels to medals.columns.
# Create new columns 'Silver' and 'Bronze' in medals using silver['Total'] & bronze['Total'].
# Print the top 5 rows of the final DataFrame medals. This has been done for you, so hit 'Submit Answer' to see the result!

# Import pandas
import pandas as pd

# Make a copy of gold: medals
medals = gold.copy()

# Create list of new column labels: new_labels
new_labels = ['NOC', 'Country', 'Gold']

# Rename the columns of medals using new_labels
medals.columns = new_labels

# Add columns 'Silver' & 'Bronze' to medals
medals['Silver'] = silver['Total']
medals['Bronze'] = bronze['Total']

# Print the head of medals
print(medals.head())

# Exercise
# Sorting DataFrame with the Index & columns
# It is often useful to rearrange the sequence of the rows of a DataFrame by sorting. You don't have to implement these yourself; the principal methods for doing this are .sort_index() and .sort_values().

# In this exercise, you'll use these methods with a DataFrame of temperature values indexed by month names. You'll sort the rows alphabetically using the Index and numerically using a column. Notice, for this data, the original ordering is probably most useful and intuitive: the purpose here is for you to understand what the sorting methods do.

# Instructions

# Read 'monthly_max_temp.csv' into a DataFrame called weather1 with 'Month' as the index.
# Sort the index of weather1 in alphabetical order using the .sort_index() method and store the result in weather2.
# Sort the index of weather1 in reverse alphabetical order by specifying the additional keyword argument ascending=False inside .sort_index().
# Use the .sort_values() method to sort weather1 in increasing numerical order according to the values of the column 'Max TemperatureF'.
# Import pandas
import pandas as pd

# Read 'monthly_max_temp.csv' into a DataFrame: weather1
weather1 = pd.read_csv('monthly_max_temp.csv', index_col='Month')

# Print the head of weather1
print(weather1.head())

# Sort the index of weather1 in alphabetical order: weather2
weather2 = weather1.sort_index()

# Print the head of weather2
print(weather2.head())

# Sort the index of weather1 in reverse alphabetical order: weather3
weather3 = weather1.sort_index(ascending=False)

# Print the head of weather3
print(weather3.head())

# Sort weather1 numerically using the values of 'Max TemperatureF': weather4
weather4 = weather1.sort_values('Max TemperatureF')

# Print the head of weather4
print(weather4.head())

# Exercise
# Reindexing DataFrame from a list
# Sorting methods are not the only way to change DataFrame Indexes. There is also the .reindex() method.

# In this exercise, you'll reindex a DataFrame of quarterly-sampled mean temperature values to contain monthly samples (this is an example of upsampling or increasing the rate of samples, which you may recall from the pandas Foundations course).

# The original data has the first month's abbreviation of the quarter (three-month interval) on the Index, namely Apr, Jan, Jul, and Oct. This data has been loaded into a DataFrame called weather1 and has been printed in its entirety in the IPython Shell. Notice it has only four rows (corresponding to the first month of each quarter) and that the rows are not sorted chronologically.

# You'll initially use a list of all twelve month abbreviations and subsequently apply the .ffill() method to forward-fill the null entries when upsampling. This list of month abbreviations has been pre-loaded as year.

# Instructions

# Reorder the rows of weather1 using the .reindex() method with the list year as the argument, which contains the abbreviations for each month.
# Reorder the rows of weather1 just as you did above, this time chaining the .ffill() method to replace the null values with the last preceding non-null value.
# Import pandas
import pandas as pd

# Reindex weather1 using the list year: weather2
weather2 = weather1.reindex(year)

# Print weather2
print(weather2)

# Reindex weather1 using the list year with forward-fill: weather3
weather3 =  weather1.reindex(year).ffill()

# Print weather3
print(weather3)

# Exercise
# Reindexing using another DataFrame Index
# Another common technique is to reindex a DataFrame using the Index of another DataFrame. The DataFrame .reindex() method can accept the Index of a DataFrame or Series as input. You can access the Index of a DataFrame with its .index attribute.

# The Baby Names Dataset from data.gov summarizes counts of names (with genders) from births registered in the US since 1881. In this exercise, you will start with two baby-names DataFrames names_1981 and names_1881 loaded for you.

# The DataFrames names_1981 and names_1881 both have a MultiIndex with levels name and gender giving unique labels to counts in each row. If you're interested in seeing how the MultiIndexes were set up, names_1981 and names_1881 were read in using the following commands:

# names_1981 = pd.read_csv('names1981.csv', header=None, names=['name','gender','count'], index_col=(0,1))
# names_1881 = pd.read_csv('names1881.csv', header=None, names=['name','gender','count'], index_col=(0,1))
# As you can see by looking at their shapes, which have been printed in the IPython Shell, the DataFrame corresponding to 1981 births is much larger, reflecting the greater diversity of names in 1981 as compared to 1881.

# Your job here is to use the DataFrame .reindex() and .dropna() methods to make a DataFrame common_names counting names from 1881 that were still popular in 1981.

# Instructions

# Create a new DataFrame common_names by reindexing names_1981 using the index attribute of the DataFrame names_1881 of older names.
# Print the shape of the new common_names DataFrame. This has been done for you. It should be the same as that of names_1881.
# Drop the rows of common_names that have null counts using the .dropna() method. These rows correspond to names that fell out of fashion between 1881 & 1981.
# Print the shape of the reassigned common_names DataFrame. This has been done for you, so hit 'Submit Answer' to see the result!
# Import pandas
import pandas as pd

# Reindex names_1981 with index of names_1881: common_names
common_names = names_1981.reindex(names_1881.index)

# Print shape of common_names
print(common_names.shape)

# Drop rows with null counts: common_names
common_names = common_names.dropna()

# Print shape of new common_names
print(common_names.shape)

# Exercise
# Broadcasting in arithmetic formulas
# In this exercise, you'll work with weather data pulled from wunderground.com. The DataFrame weather has been pre-loaded along with pandas as pd. It has 365 rows (observed each day of the year 2013 in Pittsburgh, PA) and 22 columns reflecting different weather measurements each day.

# You'll subset a collection of columns related to temperature measurements in degrees Fahrenheit, convert them to degrees Celsius, and relabel the columns of the new DataFrame to reflect the change of units.

# Remember, ordinary arithmetic operators (like +, -, *, and /) broadcast scalar values to conforming DataFrames when combining scalars & DataFrames in arithmetic expressions. Broadcasting also works with pandas Series and NumPy arrays.

# Instructions

# Create a new DataFrame temps_f by extracting the columns 'Min TemperatureF', 'Mean TemperatureF', & 'Max TemperatureF' from weather as a new DataFrame temps_f. To do this, pass the relevant columns as a list to weather[].
# Create a new DataFrame temps_c from temps_f using the formula (temps_f - 32) * 5/9.
# Rename the columns of temps_c to replace 'F' with 'C' using the .str.replace('F', 'C') method on temps_c.columns.
# Print the first 5 rows of DataFrame temps_c. This has been done for you, so hit 'Submit Answer' to see the result!

# Extract selected columns from weather as new DataFrame: temps_f
temps_f = weather[['Min TemperatureF','Mean TemperatureF','Max TemperatureF']]

# Convert temps_f to celsius: temps_c
temps_c = (temps_f - 32) * 5/9

# Rename 'F' in column names with 'C': temps_c.columns
temps_c.columns = temps_c.columns.str.replace('F', 'C')

# Print first 5 rows of temps_c
print(temps_c.head())

# Exercise
# Computing percentage growth of GDP
# Your job in this exercise is to compute the yearly percent-change of US GDP (Gross Domestic Product) since 2008.

# The data has been obtained from the Federal Reserve Bank of St. Louis and is available in the file GDP.csv, which contains quarterly data; you will resample it to annual sampling and then compute the annual growth of GDP. For a refresher on resampling, check out the relevant material from pandas Foundations.

# Instructions

# Read the file 'GDP.csv' into a DataFrame called gdp, using parse_dates=True and index_col='DATE'.
# Create a DataFrame post2008 by slicing gdp such that it comprises all rows from 2008 onward.
# Print the last 8 rows of the slice post2008. This has been done for you. This data has quarterly frequency so the indices are separated by three-month intervals.
# Create the DataFrame yearly by resampling the slice post2008 by year. Remember, you need to chain .resample() (using the alias 'A' for annual frequency) with some kind of aggregation; you will use the aggregation method .last() to select the last element when resampling.
# Compute the percentage growth of the resampled DataFrame yearly with .pct_change() * 100.
import pandas as pd

# Read 'GDP.csv' into a DataFrame: gdp
gdp = pd.read_csv('GDP.csv', index_col='DATE', parse_dates=True)

# Slice all the gdp data from 2008 onward: post2008
post2008 = gdp['2008':]

# Print the last 8 rows of post2008
print(post2008.tail(8))

# Resample post2008 by year, keeping last(): yearly
yearly = post2008.resample('A').last()

# Print yearly
print(yearly)

# Compute percentage growth of yearly: yearly['growth']
yearly['growth'] = yearly.pct_change() * 100

# Print yearly again
print(yearly)

# Exercise
# Converting currency of stocks
# In this exercise, stock prices in US Dollars for the S&P 500 in 2015 have been obtained from Yahoo Finance. The files sp500.csv for sp500 and exchange.csv for the exchange rates are both provided to you.

# Using the daily exchange rate to Pounds Sterling, your task is to convert both the Open and Close column prices.

# Instructions

# Read the DataFrames sp500 & exchange from the files 'sp500.csv' & 'exchange.csv' respectively..
# Use parse_dates=True and index_col='Date'.
# Extract the columns 'Open' & 'Close' from the DataFrame sp500 as a new DataFrame dollars and print the first 5 rows.
# Construct a new DataFrame pounds by converting US dollars to British pounds. You'll use the .multiply() method of dollars with exchange['GBP/USD'] and axis='rows'
# Print the first 5 rows of the new DataFrame pounds. This has been done for you, so hit 'Submit Answer' to see the results!.
# Import pandas
import pandas as pd

# Read 'sp500.csv' into a DataFrame: sp500
sp500 = pd.read_csv('sp500.csv',index_col='Date', parse_dates=True)

# Read 'exchange.csv' into a DataFrame: exchange
exchange = pd.read_csv('exchange.csv',index_col='Date', parse_dates=True)

# Subset 'Open' & 'Close' columns from sp500: dollars
dollars = sp500[['Open','Close']]

# Print the head of dollars
print(dollars.head())

# Convert dollars to pounds: pounds
pounds = dollars.multiply(exchange['GBP/USD'], axis='rows')

# Print the head of pounds
print(pounds.head())