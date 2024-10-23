# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import zipfile
import os

# File paths (Update these paths based on where your files are)
zip_file_path = 'C:/Users/suppo/OneDrive/Desktop/Python_Project/venv/adult.zip'  # Path to your zip file
extracted_path = 'C:/Users/suppo/OneDrive/Desktop/Python'  # Path where you want to extract the files

# Step 1: Extract the zip file
# Create the directory if it doesn't exist
os.makedirs(extracted_path, exist_ok=True)  
# Extract all contents of the zip file to the specified directory
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_path)

# Step 2: Load the dataset
# Construct the path to the extracted dataset file
file_path = os.path.join(extracted_path, 'adult.data')  # Adjust based on the actual extracted filename
# Load the dataset into a pandas DataFrame
df = pd.read_csv(file_path, header=None)  # No header in the dataset, hence header=None

# Step 3: Assign column names
df.columns = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 
              'marital-status', 'occupation', 'relationship', 'race', 
              'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 
              'native-country', 'income']

# Step 4: Display basic info about the dataset
print("Summary of the Dataset:")
print(df.info())  # Displays information about the DataFrame structure
print("\nSummary Statistics:")
print(df.describe(include='all'))  # Displays summary statistics for all columns

# Step 5: Create a Histogram for Age Distribution
plt.figure(figsize=(10, 6))  # Set the figure size
# Create the histogram using seaborn
sns.histplot(df['age'], bins=30, kde=True)  # `kde=True` adds a Kernel Density Estimate curve
plt.title('Age Distribution of Individuals in the Census Income Dataset')  # Title of the histogram
plt.xlabel('Age')  # Label for the x-axis
plt.ylabel('Frequency')  # Label for the y-axis
plt.grid(axis='y', alpha=0.75)  # Add a grid for better readability
plt.show()  # Display the plot
