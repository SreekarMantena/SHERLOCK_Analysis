import tkinter as tk
from tkinter import filedialog
import pandas as pd
import statistics as stat
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue')
canvas1.pack()

def getExcel ():
    global df
    
    import_file_path = filedialog.askopenfilename()
    print("Importing Data From" + import_file_path)
    df = pd.read_excel (import_file_path, sheet_name='Sheet2')
    # names = pd.read_excel (import_file_path, sheet_name='Names')
    # print(names)
    # print(names.iloc[:,0])
    #df = pd.read_excel (import_file_path, sheet_name='Sheet1')
    print (df)
    root.destroy()
    
browseButton_Excel = tk.Button(text='Import Excel File Output from Plate Reader', command=getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(200, 200, window=browseButton_Excel)

root.mainloop()

data = []
ncrRNA = 27

iter = 0

print("crRNA Names:")
cNames = df.iloc[0:19,0].tolist()
print(cNames)

print("Target Names")
tNames = df.iloc[26,1:].tolist()
print(tNames)

# print(df.iloc[0,0])
# print(df.iloc[0,1])
# print(df.iloc[1,2])
# print(df.iloc[0,1:].tolist())

while (iter < len(cNames)):
    data.append(df.iloc[iter,1:].tolist())
    iter = iter + 1

#print(data)

#fig, ax = plt.subplots(figsize = (40, 200))
# im = ax.imshow(data[3:24])

data = np.around(data, decimals = 0)
ax = sns.heatmap(data, cbar = True, cbar_kws = {"shrink": 0.5}, square = True, linewidths = 0.005, annot=True)
# 
#, vmin = 39.12, vmax = 120

mask = []

# while (iter < len(cNames)):
#     while(iter)
#     if(data.[iter,1:].tolist())
#     iter = iter + 1


ax.set_xticks(np.arange(len(tNames)))
ax.set_yticks(np.arange(len(cNames)))
ax.set_xticklabels(tNames, rotation = "vertical", size = 14)
ax.set_yticklabels(cNames, size = 14)
ax.set_xlabel("Synthetic Viral Targets at Varying Concentrations", size = 15)
ax.set_ylabel("crRNA Detection Designs", size = 15)

# ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
# ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
# ax.set_xticklabels(tNames, minor = True, rotation = "vertical")

# for tick in ax.xaxis.get_minor_ticks():
#     tick.tick1line.set_markersize(0)
#     tick.tick2line.set_markersize(0)
#     tick.label1.set_horizontalalignment('center')

# # We want to show all ticks...
# ax.set_xticks(np.arange(len(tNames)))
# ax.set_yticks(np.arange(len(cNames)))
# # ... and label them with the respective list entries
#ax.set_xticklabels(tNames)
#plt.xticks(x, tNames, rotation = vertical)
#ax.set_yticklabels(cNames)

# # Rotate the tick labels and set their alignment.
#plt.setp(ax.get_xticklabels(), rotation="vertical")

#plt.setp(ax.get_yticklabels(), rotation="horizontal")

# # Loop over data dimensions and create text annotations.
# for i in range(len(tNames)):
#     for j in range(len(cNames)):
#         text = ax.text(j, i, 't', ha="center", va="center", color="w")


ax.set_title("Heatmap of Background-Subtracted Fluorescence", size = 20)
#fig.tight_layout()
#plt.colorbar(plt.pcolor(data))
#nnot_kws={"size": 5}, fmt = 'g'
for text in ax.texts:
    if float(text.get_text()) > 100:
        text.set_text("*")
        text.set_size(20)
        text.set_weight('bold')
        text.set_style('italic')
    else:
        text.set_text("")

plt.show()