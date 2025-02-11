import pandas as pd

def display_menu():
    print("\n=== Car Database Analysis Menu ===")
    print("1. Display entire database")
    print("2. Show first 5 rows")
    print("3. Show database info")
    print("4. Show statistical description")
    print("5. Check and clean null values")
    print("6. Show car makes count")
    print("7. Show car models count")
    print("8. Show Asian and European cars")
    print("9. Remove cars over 4000 pounds")
    print("10. Increase city MPG by 3")
    print("0. Exit")
    print("===============================")

def main():
    global cars  # Make cars accessible for modifications
    cars = pd.read_csv('cars.csv')
    
    while True:
        display_menu()
        choice = input("Enter your choice (0-10): ")
        
        if choice == '0':
            print("Exiting program. Goodbye!")
            break
            
        elif choice == '1':
            print("\nComplete Database:")
            print(cars)
            
        elif choice == '2':
            print("\nFirst 5 rows:")
            print(cars.head())
            
        elif choice == '3':
            print("\nDatabase Info:")
            print(cars.info())
            
        elif choice == '4':
            print("\nStatistical Description:")
            print(cars.describe())
            
        elif choice == '5':
            print("\nNull values before cleaning:")
            print(cars.isnull().sum())
            
            numeric_columns = cars.select_dtypes(include=['int64', 'float64']).columns
            categorical_columns = cars.select_dtypes(include=['object']).columns
            
            cars[numeric_columns] = cars[numeric_columns].fillna(cars[numeric_columns].mean())
            for col in categorical_columns:
                cars[col] = cars[col].fillna(cars[col].mode()[0])
                
            print("\nNull values after cleaning:")
            print(cars.isnull().sum())
            
        elif choice == '6':
            print("\nCar Makes Count:")
            print(cars['Make'].value_counts())
            
        elif choice == '7':
            print("\nCar Models Count:")
            print(cars['Model'].value_counts())
            
        elif choice == '8':
            print("\nAsian and European Cars:")
            print(cars[cars['Origin'].isin(['Asia', 'Europe'])])
            
        elif choice == '9':
            cars = cars[~(cars['Weight'] > 4000)]
            print("\nCars over 4000 pounds removed.")
            print("Remaining records:", len(cars))
            
        elif choice == '10':
            cars['MPG_City'] = cars['MPG_City'].apply(lambda x: x + 3)
            print("\nCity MPG increased by 3.")
            
        else:
            print("\nInvalid choice! Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()



