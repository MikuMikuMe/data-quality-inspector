Certainly! Below is a complete Python program for a simple data quality inspector that can be used to automate data quality checks for consistency and accuracy in datasets. The program includes comments and error handling to guide you through its functionalities.

```python
import pandas as pd
import numpy as np

class DataQualityInspector:
    def __init__(self, dataframe):
        """Initialize with a pandas dataframe."""
        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError("Input must be a pandas DataFrame.")
        self.df = dataframe

    def check_missing_values(self):
        """Checks for missing values in the DataFrame."""
        missing_values = self.df.isnull().sum()
        print("Missing Values in each column:\n", missing_values)
        return missing_values

    def check_duplicates(self):
        """Checks for duplicate rows in the DataFrame."""
        duplicate_rows = self.df.duplicated().sum()
        print(f"Number of duplicate rows: {duplicate_rows}")
        return duplicate_rows

    def check_data_types(self):
        """Checks and prints data types for each column."""
        data_types = self.df.dtypes
        print("Data types of each column:\n", data_types)
        return data_types

    def check_outliers(self, column_name):
        """Detects outliers in a specified column using the IQR method."""
        if column_name not in self.df.columns:
            raise ValueError(f"{column_name} not found in DataFrame columns.")

        if not pd.api.types.is_numeric_dtype(self.df[column_name]):
            raise TypeError("Outlier detection requires a numeric column.")

        Q1 = self.df[column_name].quantile(0.25)
        Q3 = self.df[column_name].quantile(0.75)
        IQR = Q3 - Q1
        
        outliers = self.df[(self.df[column_name] < (Q1 - 1.5 * IQR)) | (self.df[column_name] > (Q3 + 1.5 * IQR))]
        print(f"Outliers in column {column_name}:\n", outliers)
        return outliers

    def summary(self):
        """Provides a complete summary of data quality checks."""
        print("Performing data quality checks...")
        self.check_missing_values()
        self.check_duplicates()
        self.check_data_types()
        print("Data quality checks completed.")

def main():
    # Sample data
    data = {
        'name': ['Alice', 'Bob', 'Charlie', 'David', np.nan],
        'age': [25, 30, 35, 40, 25],
        'salary': [50000, 60000, 70000, 80000, 50000],
        'department': ['HR', 'Finance', 'IT', 'Marketing', 'HR']
    }

    df = pd.DataFrame(data)

    try:
        inspector = DataQualityInspector(df)
        inspector.summary()
        inspector.check_outliers('salary')
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

### Explanation of the Code:

- **DataQualityInspector Class**: This class handles the inspection of a DataFrame.
  - `__init__`: Initializes with a DataFrame and checks if the argument is of the correct type.
  - `check_missing_values`: Calculates and prints missing values per column.
  - `check_duplicates`: Prints the number of duplicate rows.
  - `check_data_types`: Prints the data types of each column in the DataFrame.
  - `check_outliers`: Detects data outliers in a specified column using the IQR method.
  - `summary`: Calls the core data quality check functions.

- **Main Function**: 
  - Creates a sample DataFrame.
  - Instantiates the `DataQualityInspector` class.
  - Executes the data quality checks and handles exceptions gracefully.

This code provides a foundational mechanism for checking data quality. Depending on the requirements, you can expand it with more specific checks or processing routines.