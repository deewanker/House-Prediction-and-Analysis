#!/usr/bin/env python
# coding: utf-8

# # Data Acquisition 

# In[12]:


#importing Libraries

import pandas as pd  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import seaborn as sns   # type: ignore


# In[4]:


#importing dataset

Housing = pd.read_csv("C:/Users/vipin/Downloads/housing_data.csv")


# In[5]:


#printing dataset
Housing


# In[6]:


#printing top 10 Entries

Housing.head(10)


# In[5]:


#printing last 10 Entries

Housing.tail(10)


# In[6]:


#Getting DataType Info

Housing.info()


# In[7]:


#Generate descriptive statistics

Housing.describe()


# In[8]:


#Finding Null Value

Housing.isnull()


# In[9]:


#Summing of Null Value

Housing.isnull().sum()


# In[10]:


# Drop Unnamed columns

columns_to_drop = ['Unnamed: 0']
Housing = Housing.drop(columns=columns_to_drop, axis=1)

Housing


# In[11]:


# Columns to display

Housing.columns


# In[12]:


#counting rows and columns

Housing.shape


# In[13]:


#Finding data types

Housing.dtypes


# # Data Wrangling

# In[10]:


#Finding mean


mean_values = Housing.mean(numeric_only=True)
print(mean_values)


# In[8]:


#Finding median

median_values = Housing.median(numeric_only=True)
print(median_values)


# In[16]:


# Handle missing values
Housing.fillna(Housing.mean(numeric_only=True), inplace=True)


# In[17]:


Housing


# In[18]:


# Handle missing values
Housing.fillna(Housing.median(numeric_only=True), inplace=True)


# In[19]:


Housing


# In[20]:


# Handle missing values
Housing.fillna(Housing.mode(numeric_only=True), inplace=True)


# In[21]:


Housing


# In[27]:


# Remove duplicates
Housing.drop_duplicates(inplace=True)


# In[28]:


Housing


# In[40]:


#Remove rows with negative prices

Housing= Housing[Housing['SalePrice'] > 0]


# In[41]:


Housing


# In[ ]:





# # Data Visualisation

# In[22]:


# Explore the distribution of house prices using a histogram  #Univariate Analysis
plt.figure(figsize=(10, 6))
sns.histplot(Housing['SalePrice'], bins=30, kde=True, color="Orange")
plt.title('Distribution of House Prices')
plt.xlabel('SalePrice')
plt.ylabel('Frequency')
plt.show()


# In[42]:


plt.figure(figsize=(10, 6))
sns.histplot(Housing['Price Per SqFt'], kde=True)
plt.title('Distribution of House Prices')
plt.xlabel('Price Per SqFt')
plt.ylabel('Frequency')
plt.show()


# In[49]:


# Explore the relationship between variables using a correlation matrix   #Multivariate
correlation_matrix = Housing.select_dtypes(include='number').corr()
plt.figure(figsize=(25, 25))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()


# In[ ]:





# In[13]:


# Explore relationships between various features and house prices
plt.figure(figsize=(18, 12))  # Increase the figure size for better visibility

plt.subplot(2, 3, 1)  # 2 rows, 3 columns, 1st subplot
sns.scatterplot(x='TotalBsmtSF', y='SalePrice', data=Housing)
plt.title('Total Basement SF vs. House Price')

plt.subplot(2, 3, 2)  # 2 rows, 3 columns, 2nd subplot
sns.scatterplot(x='BsmtFinSF1', y='SalePrice', data=Housing)
plt.title('Type 1 Finished SF vs. House Price')

plt.subplot(2, 3, 3)  # 2 rows, 3 columns, 3rd subplot
sns.scatterplot(x='BsmtFinSF2', y='SalePrice', data=Housing)
plt.title('Type 2 Finished SF vs. House Price')

plt.subplot(2, 3, 4)  # 2 rows, 3 columns, 4th subplot
sns.scatterplot(x='GrLivArea', y='SalePrice', data=Housing)
plt.title('Ground Living Area vs. House Price')

plt.subplot(2, 3, 5)  # 2 rows, 3 columns, 5th subplot
sns.scatterplot(x='1stFlrSF', y='SalePrice', data=Housing)
plt.title('First Floor SF vs. House Price')

plt.subplot(2, 3, 6)  # 2 rows, 3 columns, 6th subplot
sns.scatterplot(x='2ndFlrSF', y='SalePrice', data=Housing)
plt.title('Second Floor SF vs. House Price')

plt.tight_layout()
plt.show()


# In[ ]:





# In[96]:


# Explore relationships between key features and house prices

plt.figure(figsize=(18, 6))  # Increase the figure size for better visibility

plt.subplot(1, 4, 1)  # 1 row, 4 columns, 1st subplot
sns.scatterplot(x='BsmtFullBath', y='SalePrice', data=Housing)
plt.title('Basement full bathrooms vs. Sale Price')

plt.subplot(1, 4, 2)  # 1 row, 4 columns, 2nd subplot
sns.scatterplot(x='BsmtHalfBath', y='SalePrice', data=Housing)
plt.title('Basement Half bathrooms vs. Sale Price')


plt.subplot(1,4, 3)  # 1 row, 4 columns, 2nd subplot
sns.scatterplot(x='HalfBath', y='SalePrice', data=Housing)
plt.title('Half bathrooms vs. Sale Price')


plt.subplot(1,4, 4)  # 1 row, 4 columns, 2nd subplot
sns.scatterplot(x='FullBath', y='SalePrice', data=Housing)
plt.title('full bathrooms vs. Sale Price')



plt.tight_layout()
plt.show()


# In[100]:


# Explore relationships between key features and house prices

plt.figure(figsize=(12, 6))  # Increase the figure size for better visibility

plt.subplot(1, 3, 1)  # 1 row, 4 columns, 1st subplot
sns.scatterplot(x='BedroomAbvGr', y='SalePrice', data=Housing)
plt.title('Bedrooms above grade vs. Sale Price')

plt.subplot(1, 3, 2)  # 1 row, 4 columns, 2nd subplot
sns.scatterplot(x='KitchenAbvGr', y='SalePrice', data=Housing)
plt.title('Kitchens above grade vs. Sale Price')


plt.subplot(1,3, 3)  # 1 row, 4 columns, 2nd subplot
sns.scatterplot(x='TotRmsAbvGrd', y='SalePrice', data=Housing)
plt.title('Total rooms above grade vs. Sale Price')



plt.tight_layout()
plt.show()


# In[24]:


plt.figure(figsize=(10, 6))
sns.scatterplot(x='GrLivArea', y='SalePrice', data=Housing)
plt.title('House Price vs. Living Area (Square Feet)')
plt.xlabel('Living Area')
plt.ylabel('Price')
plt.show()


# In[108]:


# Explore relationships between key features and house prices

plt.figure(figsize=(12, 6))  # Increase the figure size for better visibility

plt.subplot(1, 1,1)  # 1 row, 4 columns, 1st subplot
sns.scatterplot(x='MiscVal', y='SalePrice', data=Housing)
plt.title('Miscellaneous feature vs. Sale Price')


plt.tight_layout()
plt.show()


# In[17]:


# Create a new feature for price per square foot
Housing['Price Per SqFt'] = Housing['SalePrice'] / Housing['LotArea']

# Create a new feature representing the property's age
current_year = 2024                                    # Assuming the current year is 2024
Housing['YrSold'] = current_year - Housing['YearBuilt']

print(Housing['YrSold'])


# In[15]:


# Converting 'YrSold' to datetime format
Housing['YrSold'] = pd.to_datetime(Housing['YrSold'], format='%Y')

# Setting 'YrSold' as an index
Housing.set_index('YrSold', inplace=True)

# Ploting historical house prices
plt.figure(figsize=(10, 6))
Housing['SalePrice'].resample('A').mean().plot()
plt.title('Historical House Prices')
plt.xlabel('Year Sold')
plt.ylabel('Average Sale Price')
plt.show()


# In[25]:


plt.figure(figsize=(10, 6))
sns.boxplot(x='PoolArea', y='SalePrice', data=Housing)
plt.title('Impact of Swimming Pool on House Prices')
plt.xlabel('Has Pool')
plt.ylabel('Price')
plt.show()


# In[26]:


plt.figure(figsize=(10, 6))
sns.boxplot(x='GarageCars', y='SalePrice', data=Housing)
plt.title('Garage on House vs  Prices')
plt.xlabel('Garage')
plt.ylabel('Price')
plt.show()


# In[27]:


plt.figure(figsize=(20, 20))
sns.boxplot(x='WoodDeckSF', y='SalePrice', data=Housing)
plt.title('Wood deck area vs  Prices')
plt.xlabel('WoodDeck')
plt.ylabel('Price')
plt.show()


# In[30]:


plt.figure(figsize=(25, 10))
sns.boxplot(x='OpenPorchSF', y='SalePrice', data=Housing)
plt.title('OpenPorchSF vs  Prices')
plt.xlabel('OpenPorch')
plt.ylabel('Price')
plt.show()


# In[29]:


plt.figure(figsize=(25, 10))
sns.boxplot(x='Fence', y='SalePrice', data=Housing)
plt.title('Fence vs  Prices')
plt.xlabel('Fence')
plt.ylabel('Price')
plt.show()


# # Conclusion

# In[21]:


# Summarized insights with bold headings

summary = """
\033[1mFeature Engineering\033[0m
Price Per Square Foot: Calculating Price Per SqFt helps normalize house prices relative to their lot area, providing a more standardized metric for price comparisons.
Years Since Built: The YrSold feature, representing the age of the house at the time of sale, captures the potential depreciation or appreciation due to age, helping in assessing its impact on sale prices.

\033[1mSize Impact on House Prices\033[0m
Basement Features: The scatter plots for TotalBsmtSF, BsmtFinSF1, and BsmtFinSF2 indicate that larger basement areas generally correlate with higher sale prices. This suggests that finished basements add significant value to houses.

\033[1mHistorical Pricing Trends\033[0m
Trend Over Time: The time-series plot of SalePrice resampled annually shows the average house prices over time. This helps identify market trends, such as periods of rapid price increase or decrease, and potential cyclical patterns in the housing market.

\033[1mCustomer Preferences and Amenities\033[0m
Impact of Amenities: Boxplots analyzing PoolArea, GarageCars, WoodDeckSF, OpenPorchSF, and Fence reveal that certain amenities significantly impact house prices:

    Pool Area: Homes with larger pool areas tend to have higher prices.
    Garage Capacity: An increase in garage car capacity correlates with higher house prices.
    Outdoor Spaces: Wood decks and open porches add value, indicating buyer preference for outdoor living spaces.
    Fence: The presence and quality of fencing also impact house prices.

Categorical Amenities: Boxplots for CentralAir, HeatingQC, and KitchenQual show:

    Central Air: Homes with central air conditioning are generally priced higher.
    Heating Quality: Higher heating quality is associated with increased house prices.
    Kitchen Quality: Better kitchen quality leads to higher house prices, highlighting its importance in buyer preferences.

\033[1mOverall Insights\033[0m
Feature Engineering: Derived features like Price Per SqFt and YrSold provide valuable insights into house pricing and age-related valuation.
Size Matters: Larger basement spaces and total square footage generally increase house prices, affirming the importance of living space.
Market Trends: Historical trends in house prices reveal overall market behavior and can help predict future market movements.
Amenities Influence: Both physical (pools, garages, decks) and categorical (central air, heating quality, kitchen quality) amenities significantly impact house prices, reflecting buyer preferences and the added value of these features.
"""

print(summary)


# In[ ]:





# In[ ]:




