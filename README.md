# CSV-Cleaner

CSV Cleaner 🧹

A mini project to practice data preprocessing with Python and Pandas.
This tool reads messy Excel/CSV files and applies cleaning steps such as handling null values, fixing inconsistent types, and standardizing values before exporting a cleaned dataset.


Features ✨

Load messy Excel/CSV files into a Pandas DataFrame

Handle missing values:

Fill missing names with known replacements

Fill missing ages with corrected values

Fix invalid data:

Replace negative ages with valid numbers

Type conversions:

Convert age from float to int

Ensure consistent types for columns

Standardize categorical values:

Fix inconsistent department names (Marketng to Marketing)

Normalize boolean-like columns (yes/no/TRUE/FALSE to True/False)

Save cleaned results to a new Excel file (renameDF.xlsx)

Generate summary statistics: null value counts, column dtypes, etc.
