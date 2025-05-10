#Data Exploration

#import packages
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway

#Read in data file
df = pd.read_csv("Crop_recommendation.csv")
print(df.head())

print(df.info())

print(df.select_dtypes(include=['int64', 'float64']).describe())

#Data Visualization 
# Setting the aesthetic style of the plots
sns.set(style="whitegrid")

# Creating visualizations for Temperature, Humidity, and Rainfall
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Temperature Distribution
sns.histplot(df['temperature'], kde=True, color="skyblue", ax=axes[0])
axes[0].set_title('Temperature Distribution')

# Humidity Distribution
sns.histplot(df['humidity'], kde=True, color="olive", ax=axes[1])
axes[1].set_title('Humidity Distribution')

# Rainfall Distribution
sns.histplot(df['rainfall'], kde=True, color="gold", ax=axes[2])
axes[2].set_title('Rainfall Distribution')

plt.tight_layout()
plt.show()

#ANOVA Analysis for Humidity

# Define crop_types based on your DataFrame 'df'
crop_types = df['label'].unique()

# Preparing a list of humidity values for each crop type
humidity_lists = [df[df['label'] == crop]['humidity'] for crop in crop_types]

# Performing the ANOVA test for humidity
anova_result_humidity = f_oneway(*humidity_lists)

anova_result_humidity

#  ANOVA Analysis for Rainfall

# Define crop_types based on your DataFrame 'df' if not already defined
crop_types = df['label'].unique()

# Preparing a list of rainfall values for each crop type
rainfall_lists = [df[df['label'] == crop]['rainfall'] for crop in crop_types]

# Performing the ANOVA test for rainfall
anova_result_rainfall = f_oneway(*rainfall_lists)

anova_result_rainfall

# Anova Analysis for Temperature

# Ensure crop_types is defined from your DataFrame 'df'
crop_types = df['label'].unique()

# Preparing a list of temperature values for each crop type
temperature_lists = [df[df['label'] == crop]['temperature'] for crop in crop_types]

# Performing the ANOVA test for temperature
anova_result_temperature = f_oneway(*temperature_lists)

print(anova_result_temperature)

'''
 Final Insights
As we conclude our analysis, we've gathered important insights that can inform precision agriculture practices.

Actionable Insights

Humidity, Rainfall, and Temperature: The ANOVA tests demonstrate that these environmental factors significantly influence crop selection. Understanding how they impact different crops is key to optimizing choices for specific environmental conditions.
Statistical Significance

The low p-values from our ANOVA tests offer high confidence in the statistical significance of our findings. This emphasizes the critical role of these environmental factors in crop cultivation decisions.
Recommendations

It is recommended that precision agriculture practices heavily consider these environmental factors when advising on crop selection.
Future Research

Further studies could explore the interaction effects between these factors, leading to more nuanced and precise recommendations.

This comprehensive analysis not only facilitates improved crop selection strategies but also makes a significant contribution to the broader field of agricultural data science.
'''