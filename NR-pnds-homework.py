import panda as pd

iris = pd.read_csv("data/iris_modified.csv", sep=";")
iris.head()

df = iris.to_excel("iris.xlsx", sheet_name="iris")

writer = pd.ExcelWriter("iris2.xlsx", engine='xlsxwriter')
for typ in df["variety"].unique:
    newdf = df[df["variety"] == typ]
    newdf.to_excel(writer, sheet_name=typ)

writer.save()

