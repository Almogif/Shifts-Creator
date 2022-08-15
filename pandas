import pandas as pd

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html#pandas.DataFrame.join
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html

A = "Almog Alyona Alex Yossi"
A = A.split(" ")

ex = ["SaturDay", "FriDay"]
data = [[A[3], A[0]], [A[1],A[0]]]

df = pd.DataFrame(data, columns = ex)
df1 = pd.DataFrame(data, columns = ex)

df2 = df.join(df1, lsuffix='SaturDay', rsuffix='FriDay')


print(df2)

# # df.at[4, 'B'] = 10
# ex = ["SaturDay", "FriDay"]
# data = [[hello[2], hello[4]], [hello[6], hello[5]], [hello[8], hello[7]], [hello[9], ""]]
# df1 = pd.DataFrame(data, columns=ex)
#
# # pd.DataFrame.add([hello[2], hello[4]], [hello[6], hello[5]] , [hello[8], hello[7]], [hello[9], ""], axis=0, level=label, fill_value=None)
# # pd.concat([df1, df2])
# df1.to_excel('text.xlsx', index=False)
#
df2.to_excel('text.xlsx', index=False)
# print(df1, df2) 
