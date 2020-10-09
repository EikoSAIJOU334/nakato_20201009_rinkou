import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

file1 = input("please enter your file_path_1: ")
file2 = input("please enter your file_path_2: ")
file3 = input("please enter your file_path_3: ")

prefix1 = os.path.splitext(os.path.splitext(os.path.basename(file1))[0])[0]
prefix2 = os.path.splitext(os.path.splitext(os.path.basename(file2))[0])[0]
prefix3 = os.path.splitext(os.path.splitext(os.path.basename(file3))[0])[0]

# 3サンプルを重ねて可視化
df1 = pd.read_csv(file1, sep='\t', skiprows=6, index_col='Strand shift')
df2 = pd.read_csv(file2, sep='\t', skiprows=6, index_col='Strand shift')
df3 = pd.read_csv(file3, sep='\t', skiprows=6, index_col='Strand shift')


plt.figure(figsize=(4,4))
plt.plot(df1["per control"], label=prefix1, color="red")
plt.plot(df2["per control"], label=prefix2, color="blue")
plt.plot(df3["per control"], label=prefix3, color="black")
plt.xlim(0,500)
plt.legend(loc='lower right')
plt.title('"per control"')
# 図をpdfにして保存
plt.savefig("{0}_{1}_{2}.per_control.0-500.pdf".format(prefix1, prefix2, prefix3))

print("your pdf file is saved as: " + "{0}_{1}_{2}.per_control.0-500.pdf".format(prefix1, prefix2, prefix3))
