import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
def load_cleaned_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print(f"Cleaned data loaded successfully with shape {data.shape}")
        return data
    except Exception as e:
        print(f"Error loading cleaned data: {e}")
        return None

# Visualizations
def plot_bar(data, column):
    data[column].value_counts().plot(kind='bar')
    plt.title(f'{column} Bar Plot')
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.show()

# Main function
def main():
    file_path = '/mnt/data/processed/hospital_emergency_cleaned.csv'
    data = load_cleaned_data(file_path)
    if data is not None:
        plot_bar(data, 'ColumnName')  # Replace 'ColumnName' with the actual column name

if __name__ == "__main__":
    main()
