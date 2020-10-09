#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# In[2]:


# df = pd.read_csv("20201009_nakato_sampledata/E024-Input.jaccard.csv", sep='\t', index_col='Strand shift')

# 元データの６行目までがコメントなので、列数が合わないためエラーとなる。
# 6行目までを"skiprows=6" 指定で飛ばす。


# In[3]:


df = pd.read_csv("20201009_nakato_sampledata/E024-Input.jaccard.csv", sep='\t', skiprows=6, index_col='Strand shift') # 'Strand shift列をindexとして使用するの意味'
df


# In[4]:


# per control 列だけを抜き出す
pc = df.iloc[:,3] # ilocで列番号を指定できる
pc


# In[5]:


# 列名で指定してもよい
pc = df["per control"] # column nameでも指定できる。こちらの方がロバスト。
pc


# In[6]:


# 最もシンプルな可視化（x軸：index, y軸: per control）
plt.plot(pc)


# In[7]:


# これでも同じ
plt.plot(pc.index, pc)


# ## Strand shift 0~ 500 bpまでを可視化したい

# In[8]:


pc[500:1001]


# In[9]:


plt.plot(pc[500:1001])


# In[10]:


# pltオブジェクトで結果を操作
plt.figure(figsize=(4,4))
plt.plot(pc)
plt.xlim(0,500)


# In[11]:


# legendをつけてみる
plt.figure(figsize=(4,4))
plt.plot(pc, label="E024")
plt.xlim(0,500)
plt.legend(loc='upper right')


# In[12]:


# 線の色を変えてみる
plt.figure(figsize=(4,4))
plt.plot(pc, label="E024", color="red")
plt.xlim(0,500)
plt.legend(loc='upper right')


# In[13]:


# 3サンプルを重ねて可視化
df1 = pd.read_csv("20201009_nakato_sampledata/E024-Input.jaccard.csv", sep='\t', skiprows=6, index_col='Strand shift')
df2 = pd.read_csv("20201009_nakato_sampledata/E058-Input.jaccard.csv", sep='\t', skiprows=6, index_col='Strand shift')
df3 = pd.read_csv("20201009_nakato_sampledata/E096-Input.jaccard.csv", sep='\t', skiprows=6, index_col='Strand shift')


# In[14]:


plt.figure(figsize=(4,4))
plt.plot(df1["per control"], label="E024", color="red")
plt.plot(df2["per control"], label="E058", color="blue")
plt.plot(df3["per control"], label="E096", color="black")
plt.xlim(0,500)
plt.legend(loc='upper right')


# In[15]:


# 図をpdfにして保存
plt.figure(figsize=(4,4))
plt.plot(df1.iloc[:,3], label="E024", color="red")
plt.plot(df2.iloc[:,3], label="E058", color="blue")
plt.plot(df3.iloc[:,3], label="E096", color="black")
plt.xlim(0,500)
plt.legend(loc='upper right')
plt.savefig("Sample.Jaccard.0-500.pdf")


# ## お題

# In[22]:


# お題１：
# 上の３サンプルの図について、y軸のスケールを0から4にして表示する。

plt.figure(figsize=(4,4))
plt.plot(df1["per control"], label="E024", color="red")
plt.plot(df2["per control"], label="E058", color="blue")
plt.plot(df3["per control"], label="E096", color="black")
plt.xlim(0,500)
plt.ylim(0,4)
plt.legend(loc='upper right')


# In[23]:


# お題２：
# 上の３サンプルの図について、x軸を対数軸にし、0から1000000まで表示してみる。

plt.figure(figsize=(4,4))
plt.plot(df1["per control"], label="E024", color="red")
plt.plot(df2["per control"], label="E058", color="blue")
plt.plot(df3["per control"], label="E096", color="black")
plt.xscale("log")
plt.xlim(0,1000000)
plt.legend(loc='upper right')


# In[28]:


# お題３：
# 上の３サンプルの図について、３サンプルの「平均値」を持ったデータを作成し、上の図に追加で表示。（色は何色でもよい）

# それぞれ、per controlの列のみ抜き出す
df1_percontrol = df1["per control"] 
df2_percontrol = df2["per control"] 
df3_percontrol = df3["per control"] 
df1_percontrol


# In[36]:


# 抜き出したものをpd.concat(axis=1)で横に並べて結合する
df_concat_multi = pd.concat([df1_percontrol, df2_percontrol, df3_percontrol], axis=1)
df_concat_multi.columns = ['df1', 'df2', 'df3']
print(df_concat_multi)


# In[37]:


# 平均の値を求めて、df_meanに代入する
df_mean = df_concat_multi.mean(axis='columns')
df_mean


# In[38]:


# 図に示す

plt.figure(figsize=(4,4))
plt.plot(df1["per control"], label="E024", color="red")
plt.plot(df2["per control"], label="E058", color="blue")
plt.plot(df3["per control"], label="E096", color="black")
plt.plot(df_mean, label="mean", color="orange")
plt.xlim(0,500)
plt.legend(loc='upper right')


# In[39]:


# お題４：
# Jaccard index の列について、同じ３サンプルの図を作る。

plt.figure(figsize=(4,4))
plt.plot(df1["Jaccard index"], label="E024", color="red")
plt.plot(df2["Jaccard index"], label="E058", color="blue")
plt.plot(df3["Jaccard index"], label="E096", color="black")
plt.xlim(0,500)
plt.legend(loc='upper right')


# In[53]:


# 更に、「per control」の図と合わせて、「per control」「Jaccard index」の２つの図を横に並べて表示させる。
# その図を "rinkou_1009_<yourname>.pdf" という名前でローカルに保存する。

# figureを生成する
fig = plt.figure(figsize=(6, 8), dpi=100, facecolor='w', linewidth=0, edgecolor='w')
 
# 3x2の1番目
ax1 = fig.add_subplot(3, 2, 1)
ax1.set_title('E024_per control')  # グラフタイトル
ax1.plot(df1["per control"], label="E024", color="red")
ax1.set_xlim(0,500)
# 3x2の2番目
ax2 = fig.add_subplot(3, 2, 2)
ax2.set_title('E024_Jaccard index')  # グラフタイトル
ax2.plot(df1["Jaccard index"], label="E024", color="red")
ax2.set_xlim(0,500)
# 3x2の3番目
ax3 = fig.add_subplot(3, 2, 3)
ax3.set_title('E058_per control')  # グラフタイトル
ax3.plot(df2["per control"], label="E058", color="blue")
ax3.set_xlim(0,500)
# 3x2の4番目
ax4 = fig.add_subplot(3, 2, 4)
ax4.set_title('E058_Jaccard index')  # グラフタイトル
ax4.plot(df2["Jaccard index"], label="E058", color="blue")
ax4.set_xlim(0,500)
# 3x2の5番目
ax5 = fig.add_subplot(3, 2, 5)
ax5.set_title('E096_per control')  # グラフタイトル
ax5.plot(df3["per control"], label="E096", color="black")
ax5.set_xlim(0,500)
# 3x2の6番目
ax6 = fig.add_subplot(3, 2, 6)
ax6.set_title('E096_Jaccard index')  # グラフタイトル
ax6.plot(df3["Jaccard index"], label="E096", color="black")
ax6.set_xlim(0,500)
 
# 表示する
plt.tight_layout() # 文字の重なりを解消する呪文
plt.show()

# 保存する
fig.savefig("rinkou_1009_SAIJOU.pdf")


# In[20]:


# お題５：
# 任意の３つのサンプルを入力にとり、３サンプルを重ねた「per control」の図をpdfとして出力するPythonスクリプトを作成する。
# その際、前回用いたサンプルファイル、もしくは自分が作成したスクリプトを改良するかたちで行うこと。
# 出力例はtestdata ディレクトリに含まれるサンプルのうち３つを利用する。出力される図はlegendが適切に入るようにすること。


# In[21]:


# 発展課題（余裕があれば）
# testdata ディレクトリに含まれる全てのサンプルについて、１サンプルずつ per control(0~500 bp) のpdfを出力する
# Pythonスクリプト or シェルスクリプトを作成する。


# 今回のペア
# - 王　ー　堺谷（＆西條）
# - 仲嶋　ー　横田
# - 牧野　ー　大庭
# 
# 事前のディスカッションは特に必要ない。最低限pull request -> merge後のディスカッションのみでOK。（もちろん希望あれば多く議論することは良いこと）

# In[ ]:




