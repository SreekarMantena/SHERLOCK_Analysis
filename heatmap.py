import tkinter as tk
from tkinter import filedialog
import pandas as pd
import statistics as stat
import numpy as np
import matplotlib.pyplot as plt

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
cNames = df.iloc[0:21,0].tolist()
print(cNames)

print("Target Names")
tNames = df.iloc[27,1:].tolist()
print(tNames)

print(df.iloc[0,0])
print(df.iloc[0,1])
print(df.iloc[1,2])
print(df.iloc[0,1:].tolist())

while (iter < len(cNames)):
    data.append(df.iloc[iter,1:].tolist())
    iter = iter + 1

#print(data)

vegetables = ["cucumber", "tomato", "lettuce", "asparagus",
              "potato", "wheat", "barley"]
farmers = ["Farmer Joe", "Upland Bros.", "Smith Gardening",
           "Agrifun", "Organiculture", "BioGoods Ltd.", "Cornylee Corp."]

harvest = np.array([[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
                    [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],
                    [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
                    [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
                    [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],
                    [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]])


fig, ax = plt.subplots()
im = ax.imshow(data)

# # We want to show all ticks...
ax.set_xticks(np.arange(len(tNames)))
ax.set_yticks(np.arange(len(cNames)))
# # ... and label them with the respective list entries
ax.set_xticklabels(tNames)
#plt.xticks(x, tNames, rotation = vertical)
ax.set_yticklabels(cNames)

# # Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation="vertical", ha="center")

plt.setp(ax.get_yticklabels(), rotation="horizontal", ha="right")

# # Loop over data dimensions and create text annotations.
# for i in range(len(tNames)):
#     for j in range(len(cNames)):
#         text = ax.text(j, i, data[i, j],
#                        ha="center", va="center", color="w")

ax.set_title("Background-Subtracted Fluorescence at 3 hours")
#fig.tight_layout()
plt.colorbar(plt.pcolor(data))
plt.show()