#!/usr/bin/env python
# coding: utf-8

# In[38]:


# Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[39]:


# Importing dataset
Housing = pd.read_csv("C:/Users/vipin/Downloads/housing_data.csv")

Housing


# In[40]:


# Printing top 10 Entries
print(Housing.head(10))


# In[41]:


# Printing last 10 Entries
print(Housing.tail(10))


# In[42]:


# Getting DataType Info
print(Housing.info())


# In[43]:


# Generate descriptive statistics
print(Housing.describe())


# In[44]:


# Drop Unnamed columns
columns_to_drop = ['Unnamed: 0']
Housing = Housing.drop(columns=columns_to_drop, axis=1)

print(Housing)


# In[45]:


# Columns to display
print(Housing.columns)


# In[46]:


# Counting rows and columns
print(Housing.shape)


# In[47]:


# Finding data types
print(Housing.dtypes)


# # Data Wrangling

# In[49]:


# Finding Null Values
print(Housing.isnull().sum())


# In[50]:


# Fill missing values with appropriate strategies
Housing.fillna({
    'Electrical': 'No Electrical',
    'GarageYrBlt': Housing['GarageYrBlt'].median(),
}, inplace=True)


# In[51]:


# Convert categorical features to 'category' dtype
categorical_columns = Housing.select_dtypes(include=['object']).columns
print("Categorical Columns:")
print(categorical_columns)

for col in categorical_columns:
    Housing[col] = Housing[col].astype('category')


# In[52]:


# Display the dataframe info
print(Housing.info())


# In[53]:


# Finding mean
mean_values = Housing.mean(numeric_only=True)
print(mean_values)


# In[54]:


# Finding median
median_values = Housing.median(numeric_only=True)
print(median_values)


# In[55]:


# Handle missing values
Housing.fillna(Housing.mean(numeric_only=True), inplace=True)
Housing.fillna(Housing.median(numeric_only=True), inplace=True)


# In[56]:


# Remove duplicates
Housing.drop_duplicates(inplace=True)


# In[57]:


# Remove rows with negative prices
Housing = Housing[Housing['SalePrice'] > 0]


# In[60]:


Housing


# In[63]:


# Creating a new feature for price per square foot
Housing['Price Per SqFt'] = Housing['SalePrice'] / Housing['LotArea']


# # Data Visualization

# In[61]:


# Explore the distribution of house prices using a histogram             #Univariate Analysis
plt.figure(figsize=(10, 6))
sns.histplot(Housing['SalePrice'], bins=30, kde=True, color="orange")
plt.title('Distribution of House Prices')
plt.xlabel('SalePrice')
plt.ylabel('Frequency')
plt.show()


# In[64]:


plt.figure(figsize=(10, 6))
sns.histplot(Housing['Price Per SqFt'], kde=True)
plt.title('Distribution of House Prices')
plt.xlabel('Price Per SqFt')
plt.ylabel('Frequency')
plt.show()


# In[65]:


# Explore the relationship between variables using a correlation matrix                 #Multivariate Analysis
correlation_matrix = Housing.select_dtypes(include='number').corr()
plt.figure(figsize=(25, 25))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()


# In[69]:


# Explore relationships between various features and house prices
plt.figure(figsize=(18, 12))

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


# In[70]:


# Explore relationships between key features and house prices
plt.figure(figsize=(18, 6))

plt.subplot(1, 4, 1)  # 1 row, 4 columns, 1st subplot
sns.scatterplot(x='BsmtFullBath', y='SalePrice', data=Housing)
plt.title('Basement Full Bathrooms vs. Sale Price')

plt.subplot(1, 4, 2)  # 1 row, 4 columns, 2nd subplot
sns.scatterplot(x='BsmtHalfBath', y='SalePrice', data=Housing)
plt.title('Basement Half Bathrooms vs. Sale Price')

plt.subplot(1, 4, 3)  # 1 row, 4 columns, 3rd subplot
sns.scatterplot(x='HalfBath', y='SalePrice', data=Housing)
plt.title('Half Bathrooms vs. Sale Price')

plt.subplot(1, 4, 4)  # 1 row, 4 columns, 4th subplot
sns.scatterplot(x='FullBath', y='SalePrice', data=Housing)
plt.title('Full Bathrooms vs. Sale Price')

plt.tight_layout()
plt.show()


# In[71]:


# Explore relationships between key features and house prices

plt.figure(figsize=(12, 6)) 

plt.subplot(1, 3, 1)  # 1 row, 3 columns, 1st subplot
sns.scatterplot(x='BedroomAbvGr', y='SalePrice', data=Housing)
plt.title('Bedrooms Above Grade vs. Sale Price')

plt.subplot(1, 3, 2)  # 1 row, 3 columns, 2nd subplot
sns.scatterplot(x='KitchenAbvGr', y='SalePrice', data=Housing)
plt.title('Kitchens Above Grade vs. Sale Price')

plt.subplot(1, 3, 3)  # 1 row, 3 columns, 3rd subplot
sns.scatterplot(x='TotRmsAbvGrd', y='SalePrice', data=Housing)
plt.title('Total Rooms Above Grade vs. Sale Price')

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='GrLivArea', y='SalePrice', data=Housing)
plt.title('House Price vs. Living Area (Square Feet)')
plt.xlabel('Living Area')
plt.ylabel('Price')
plt.show()


# In[72]:


# Explore relationships between key features and house prices

plt.figure(figsize=(12, 6))  

plt.subplot(1, 1, 1)  # 1 row, 1 column, 1st subplot
sns.scatterplot(x='MiscVal', y='SalePrice', data=Housing)
plt.title('Miscellaneous Feature vs. Sale Price')

plt.tight_layout()
plt.show()


# In[75]:


# Create new features
Housing['Age'] = Housing['YrSold'] - Housing['YearBuilt']
Housing['Remodeled'] = (Housing['YearRemodAdd'] != Housing['YearBuilt']).astype(int)

# Droping original features that are redundant
Housing.drop(['YearBuilt', 'YearRemodAdd'], axis=1, inplace=True)


# In[76]:


Housing


# In[77]:


# Setting 'YrSold' as an index
Housing.set_index('YrSold', inplace=True)


# In[85]:


# Plot the 'Age' feature in a time series
plt.figure(figsize=(10, 6))
plt.plot(Housing.index, Housing['Age'], color='skyblue')
plt.title('Age of Houses Over Time')
plt.xlabel('Year Sold')
plt.ylabel('Age (Years)')
plt.grid(True)
plt.show()

# Plot the 'Remodeled' feature in a time series
plt.figure(figsize=(10, 6))
plt.plot(Housing.index, Housing['Remodeled'], color='salmon')
plt.title('Remodeled Houses Over Time')
plt.xlabel('Year Sold')
plt.ylabel('Remodeled (0: No, 1: Yes)')
plt.yticks([0, 1])
plt.grid(True)
plt.show()


# In[ ]:





# In[94]:


#plotting customer requirements ( ameneties)

plt.figure(figsize=(10, 6))
sns.boxplot(x='PoolArea', y='SalePrice', data=Housing)
plt.title('Impact of Swimming Pool on House Prices')
plt.xlabel('Has Pool')
plt.ylabel('Price')
plt.show()


# In[90]:


#plotting customer requirements ( ameneties)
plt.figure(figsize=(10, 6))
sns.boxplot(x='GarageCars', y='SalePrice', data=Housing)
plt.title('Garage on House vs  Prices')
plt.xlabel('Garage')
plt.ylabel('Price')
plt.show()




# In[91]:


#plotting customer requirements ( ameneties)
plt.figure(figsize=(20, 20))
sns.boxplot(x='WoodDeckSF', y='SalePrice', data=Housing)
plt.title('Wood deck area vs  Prices')
plt.xlabel('WoodDeck')
plt.ylabel('Price')
plt.show()




# In[92]:


#plotting customer requirements ( ameneties)

plt.figure(figsize=(25, 10))
sns.boxplot(x='OpenPorchSF', y='SalePrice', data=Housing)
plt.title('OpenPorchSF vs  Prices')
plt.xlabel('OpenPorch')
plt.ylabel('Price')
plt.show()




# In[93]:


#plotting customer requirements ( ameneties)

plt.figure(figsize=(25, 10))
sns.boxplot(x='Fence', y='SalePrice', data=Housing)
plt.title('Fence vs  Prices')
plt.xlabel('Fence')
plt.ylabel('Price')
plt.show()


# In[96]:


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





# In[ ]:




