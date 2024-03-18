import pandas as pd

file = pd.read_csv("C:\\Users\\Lenovo\\Downloads\\result.csv")


sort_file = file.groupby("Rating")
# print(sort_file)

for x,y in sort_file:
    print(x)
    print(y)
    print()

n_file = pd.DataFrame(sort_file)
n_file.to_excel("new_data_file.xlsx")