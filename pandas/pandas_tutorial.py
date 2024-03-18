import pandas as pd

a = [1,2,3,45,5]
b = [5,6,7,8,9]
df = pd.DataFrame({"a":a ,"b":b})
# print(df)

df["c"]= df["a"]+df["b"]
# print(df)


df['d']= df["c"]>=10
print(df)

# print(df.loc[[1,2],"a"])
# print(df)
# b =

# Get a particular item using iloc function it

print(df.iloc[0,3])