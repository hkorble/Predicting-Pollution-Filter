import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('LSTM predictions (GridSearch).csv')

# Compute the average of all entries for the specified columns
averaged_data = {
    'Average Future CO (mg/m^3)': [df['Future CO (mg/m^3)'].mean()],
    'Average Future NOx (ppb)': [df['Future NOx (ppb)'].mean()]
}

# Create a new DataFrame with the averaged data
averaged_df = pd.DataFrame(averaged_data)

# Export the new DataFrame to a CSV file
averaged_df.to_csv('average.csv', index=False)

# Display the new DataFrame
print(averaged_df)