import pandas as pd

file = pd.read_excel("C:\\Users\\Lenovo\\Desktop\\Selenium\\pythonProject\\scraping\\Full_reviews.xlsx")
# Drop the column named "Unnamed:"
file.drop(columns=["Unnamed: 0"], inplace=True)

# Print the DataFrame after removing the column
print(file)
sorting = file.sort_values(by="Rating",ascending=True,ignore_index=True)


print(file)

sorting.to_excel("C:\\Users\\Lenovo\\Desktop\\Selenium\\pythonProject\\scraping\\Full_reviews.xlsx")
