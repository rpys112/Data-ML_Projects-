#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[3]:


ev_data = pd.read_csv("C:/Users/Rudra Singh/Downloads/Electric_Vehicle_Population_Data.csv")


# In[5]:


ev_data.head()


# In[6]:


ev_data.info()


# In[8]:


ev_data.isnull().sum()


# In[10]:


ev_data = ev_data.dropna()


# In[11]:


ev_data.info()


# In[16]:


ev_data.columns


# In[17]:


import matplotlib.pyplot as plt
import seaborn as sns 


# In[18]:


plt.figure(figsize=(12,10))


# In[22]:


ev_adoption_by_year = ev_data['Model Year'].value_counts().sort_index()
sns.barplot(x=ev_adoption_by_year.index, y=ev_adoption_by_year.values, palette="viridis")
plt.title('EV Adoption Over Time')
plt.xlabel('Model Year')
plt.ylabel('Number of Vehicles Registered')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[26]:


ev_county_distribution = ev_data['County'].value_counts()


# In[27]:


ev_county_distribution


# In[28]:


top_counties = ev_county_distribution.head(3).index


# In[31]:


top_counties


# In[32]:


top_counties_data = ev_data[ev_data['County'].isin(top_counties)]


# In[33]:


ev_city_distribution_top_counties = top_counties_data.groupby(['County', 'City']).size().sort_values(ascending=False).reset_index(name='Number of Vehicles')


# In[34]:


ev_city_distribution_top_counties


# In[36]:


top_cities = ev_city_distribution_top_counties.head(10)


# In[47]:


plt.figure(figsize=(12, 8))
sns.barplot(x='City', y='Number of Vehicles', hue='County', data=top_cities, palette="magma")
plt.title('Top Cities in Top Counties by EV Registrations')
plt.ylabel('Number of Vehicles Registered')
plt.xlabel('City')
plt.legend(title='County')
plt.tight_layout()
plt.show()


# In[42]:


ev_type_distribution = ev_data['Electric Vehicle Type'].value_counts()


# In[43]:


ev_type_distribution


# In[48]:


plt.figure(figsize=(12, 8))
sns.barplot(x=ev_type_distribution.index, y= ev_type_distribution.values, palette="rocket")
plt.title('Distribution of Electric Vehicle Types')
plt.ylabel('Number of Vehicles Registered')
plt.xlabel('Electric Vehicle Type')
plt.tight_layout()
plt.show()


# In[49]:


ev_make_distribution = ev_data['Make'].value_counts().head(10)


# In[50]:


ev_make_distribution


# In[55]:


plt.figure(figsize=(12, 8))
sns.barplot(y=ev_make_distribution.values, x=ev_make_distribution.index, palette="cubehelix")
plt.title('Top 10 Popular EV Makes')
plt.ylabel('Number of Vehicles Registered')
plt.xlabel('Make')
plt.tight_layout()
plt.show()


# In[56]:


top_3_makes = ev_make_distribution.head(3).index


# In[57]:


top_makes_data = ev_data[ev_data['Make'].isin(top_3_makes)]


# In[58]:


ev_model_distribution_top_makes = top_makes_data.groupby(['Make', 'Model']).size().sort_values(ascending=False).reset_index(name='Number of Vehicles')


# In[59]:


top_models = ev_model_distribution_top_makes.head(10)


# In[61]:


plt.figure(figsize=(10, 8))
sns.barplot(y='Number of Vehicles', x='Model', hue='Make', data=top_models, palette="viridis")
plt.title('Top Models in Top 3 Makes by EV Registrations')
plt.ylabel('Number of Vehicles Registered')
plt.xlabel('Model')
plt.legend(title='Make', loc='center right')
plt.tight_layout()
plt.show()


# In[62]:


ev_registration_counts = ev_data['Model Year'].value_counts().sort_index()
ev_registration_counts


# In[63]:


from scipy.optimize import curve_fit
import numpy as np


# In[64]:


filtered_years = ev_registration_counts[ev_registration_counts.index <= 2023]


# In[65]:


def exp_growth(x, a, b):
    return a * np.exp(b * x)


# In[66]:


x_data = filtered_years.index - filtered_years.index.min()
y_data = filtered_years.values


# In[67]:


params, covariance = curve_fit(exp_growth, x_data, y_data)


# In[68]:


forecast_years = np.arange(2024, 2024 + 6) - filtered_years.index.min()
forecasted_values = exp_growth(forecast_years, *params)


# In[69]:


forecasted_evs = dict(zip(forecast_years + filtered_years.index.min(), forecasted_values))


# In[70]:


forecasted_evs


# In[71]:


years = np.arange(filtered_years.index.min(), 2029 + 1)
actual_years = filtered_years.index
forecast_years_full = np.arange(2024, 2029 + 1)


# In[72]:


actual_values = filtered_years.values
forecasted_values_full = [forecasted_evs[year] for year in forecast_years_full]


# In[75]:


plt.figure(figsize=(12, 8))
plt.plot(actual_years, actual_values, 'bo-', label='Actual Registrations')
plt.plot(forecast_years_full, forecasted_values_full, 'ro--', label='Forecasted Registrations')
plt.title('Current & Estimated EV Market')
plt.xlabel('Year')
plt.ylabel('Number of EV Registrations')
plt.legend()
plt.grid(True)

plt.show()


# In[74]:





# In[ ]:




