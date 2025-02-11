import pandas as pd
cars = pd.read_csv('cars.csv') #read the csv file

print(cars.head()) #print the first 5 rows of the dataframe
print(cars.info()) #print the info of the dataframe
print(cars.describe()) #print the description of the dataframe

#Data cleaning: Find all the null value in the dataset. If there is any null value, fill it with the mean of the column.
# Print null values before cleaning
print("\nNull values before cleaning:")
print(cars.isnull().sum())

# Fill numeric columns with mean and categorical columns with mode
numeric_columns = cars.select_dtypes(include=['int64', 'float64']).columns
categorical_columns = cars.select_dtypes(include=['object']).columns

# Fill numeric columns with mean
cars[numeric_columns] = cars[numeric_columns].fillna(cars[numeric_columns].mean())

# Fill categorical columns with mode
for col in categorical_columns:
    cars[col] = cars[col].fillna(cars[col].mode()[0])

# Print null values after cleaning
print("\nNull values after cleaning:")
print(cars.isnull().sum())


#Check the different types of Make in the dataset. Return the count of each make in the dataset.
print(cars['Make'].value_counts())

#Check the different types of Model in the dataset. Return the count of each model in the dataset.
print(cars['Model'].value_counts())

#Show all the records where Origin is Asia or Europe.
print(cars[cars['Origin'].isin(['Asia', 'Europe'])])

#Remove all records where Weight is greater than 4000 pounds.
cars = cars[~(cars['Weight'] > 4000)]
print(cars)

#Increase all the values of MPG_City by 3.
cars['MPG_City'] = cars['MPG_City'].apply(lambda x: x + 3)
print(cars)



