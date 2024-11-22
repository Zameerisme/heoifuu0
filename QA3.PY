import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# Load the dataset
df = pd.read_csv('smoker.csv')
# Display the first few rows of the dataframe
print(df.head())
# Plot histogram for 'age'
plt.figure(figsize=(10, 6))
plt.hist(df['age'], bins=20, edgecolor='black', alpha=0.7)
plt.title('Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
# Scatter plot for age vs. smoking_duration
plt.figure(figsize=(10, 6))
plt.scatter(df['age'], df['smoking_duration'], alpha=0.7,
c=df['smoking_status'].astype('category').cat.codes, cmap='viridis')
plt.title('Scatter Plot of Age vs. Smoking Duration')
plt.xlabel('Age')
plt.ylabel('Smoking Duration (years)')
plt.colorbar(label='Smoking Status')
plt.grid(True)
plt.show()
# Bar plot for smoking status distribution
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='smoking_status', palette='viridis')
plt.title('Frequency Distribution of Smoking Status')
plt.xlabel('Smoking Status')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
# Group by smoking status and calculate mean age
avg_age = df.groupby('smoking_status')['age'].mean().reset_index()
# Line plot for average age by smoking status
plt.figure(figsize=(10, 6))
plt.plot(avg_age['smoking_status'], avg_age['age'], marker='o', linestyle='-', color='b')
plt.title('Line Plot of Average Age by Smoking Status')
plt.xlabel('Smoking Status')
plt.ylabel('Average Age')
plt.grid(True)
plt.show()
