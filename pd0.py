#Programe to create series with scalar value
import pandas as pd

D = [1, 2, 3, 4, 5, 7, 9, 44]
df = pd.Series(D)

Index = ["a", "b", "c", "d", "e", "f", "G", "h"]

si = pd.Series(D, Index)

print(df ,"\n\n")

print(si)