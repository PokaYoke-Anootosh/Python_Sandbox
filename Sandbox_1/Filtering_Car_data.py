import pandas as pd
import matplotlib.pyplot as plt

#Importing the .csv car dataset into a DataFrame 
# (Fetching Raw data from my Github repository): 
Raw_data_URL = "https://raw.githubusercontent.com/PokaYoke-Anootosh/poka_yoke_pyDojo/refs/heads/main/Cars_data_no_Index.csv"
Car_Inventory_DF = pd.read_csv(Raw_data_URL)

#Top 5 cars with highest prices: 
print(Car_Inventory_DF.sort_values(by="Price", ascending = False).head(5))


#Car with 4 or more doors: 
print(Car_Inventory_DF[Car_Inventory_DF["Doors"] >= 4]) 

# line-chart: The most expensive cars: 

# checking the data type of the price column - 
print(Car_Inventory_DF["Price"].dtype)

# Since the column data-type returned as Object/String, 
# Converting price column values datatype to numeric which can be plotted -
Car_Inventory_DF["Price"] = Car_Inventory_DF["Price"].str.replace(
    r'[\$,]', '', regex=True).astype(float)

# Plotting the price column on a line chart - 
print(Car_Inventory_DF["Price"].plot())



