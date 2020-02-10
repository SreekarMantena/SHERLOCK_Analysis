import tkinter as tk
from tkinter import filedialog
import pandas as pd
import statistics as stat
import numpy as np
import matplotlib.pyplot as plt

backgroundx = 57
backgroundx = backgroundx -2
numTimes = 28
samplex = 57 + 20*numTimes
samplex = samplex - 2
techReps = 4
numViruses = 7
virusNames = []

#test
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue')
canvas1.pack()

def getExcel ():
    global df
    
    import_file_path = filedialog.askopenfilename()
    print("Importing Data From" + import_file_path)
    df = pd.read_excel (import_file_path, sheet_name='Plate 1 - Sheet1')
    # names = pd.read_excel (import_file_path, sheet_name='Names')
    # print(names)
    # print(names.iloc[:,0])
    #df = pd.read_excel (import_file_path, sheet_name='Sheet1')
    print (df)
    root.destroy()
    
browseButton_Excel = tk.Button(text='Import Excel File Output from Plate Reader', command=getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(200, 200, window=browseButton_Excel)

root.mainloop()

virusNames = df.Names[0:numViruses]
print("Virus Names:")
print(virusNames)

# def fetchData():

#     return [e4, e3, e2, e1, NTC]

def getInfo(v):
    y=3
    SArr = [getArray(samplex + v,y), getArray(samplex + v, y+2), getArray(samplex + v, y+4), getArray(samplex + v, y+6)]
    BArr =[getArray(backgroundx + v,y), getArray(backgroundx + v, y+2), getArray(backgroundx + v, y+4), getArray(backgroundx + v, y+6)]
    SNTC = [getNTC(samplex + v, y+8)]
    ANTC = [getNTC(backgroundx + v, y+8)]
    BSFArr=  np.subtract(SArr, BArr)
    NTCB = np.subtract(SNTC, ANTC)
    e4A = stat.mean(BSFArr[0])
    e4S = stat.stdev(BSFArr[0])
    e3A = stat.mean(BSFArr[1])
    e3S = stat.stdev(BSFArr[1])
    e2A = stat.mean(BSFArr[2])
    e2S = stat.stdev(BSFArr[2])
    e1A = stat.mean(BSFArr[3])
    e1S = stat.stdev(BSFArr[3])
    NTCA = stat.mean(NTCB[0])
    NTCS = stat.stdev(NTCB[0])
    Avg = [e4A, e3A, e2A, e1A, NTCA]
    STD = [e4S, e3S, e2S, e1S, NTCS]
    print(Avg)
    print(BSFArr)
    return [Avg, STD, BSFArr.tolist()]

def getArray(x,y):
    if(techReps ==4):
        return [df.iloc[x,y], df.iloc[x+1,y], df.iloc[x, y+1], df.iloc[x+1,y+1]]
    else:
        return [df.iloc[x,y], df.iloc[x+1,y], df.iloc[x, y+1]]

def getNTC(x,y):
    if(techReps==4):
        return [df.iloc[x,y], df.iloc[x+1,y], df.iloc[x, y+1], df.iloc[x,y+2], df.iloc[x+1,y+2], df.iloc[x, y+3], df.iloc[x+1,y+1], df.iloc[x+1, y+3]]
    else:
        return  [df.iloc[x,y], df.iloc[x+1,y], df.iloc[x, y+1], df.iloc[x,y+2], df.iloc[x+1,y+2], df.iloc[x, y+3]]

#print(getInfo(0))

#getInfo(0)


x = 0
virusTD = []

while(x < numViruses*2):  
    virusTD.append(getInfo(x))
    x = x+2

print("\n\nVirus All Information:")
print(virusTD)

e4 = []
e3 = []
e2 = []
e1 = []
NTC = []
e4E = []
e3E = []
e2E = []
e1E = []
NTCE = []
for virus in virusTD:
    e4.append(virus[0][0])
    e3.append(virus[0][1])
    e2.append(virus[0][2])
    e1.append(virus[0][3])
    NTC.append(virus[0][4])

    e4E.append(virus[1][0])
    e3E.append(virus[1][1])
    e2E.append(virus[1][2])
    e1E.append(virus[1][3])
    NTCE.append(virus[1][4]*3)


# data to plot
n_groups = 8

# create plot
fig, ax = plt.subplots()
index = np.arange(numViruses)
bar_width = 0.15
opacity = 0.8


#print(e4)

rects1 = plt.bar(index, e4, bar_width,
alpha=opacity,
color='y',
label='e4', yerr = e4E, capsize = 5)

rects2 = plt.bar(index + bar_width, e3, bar_width,
alpha=opacity,
color='r',
label='e3', yerr = e3E, capsize = 5)
# ax.plot(1, 1000 , 'bo')
# ax.plot(1.5, 1000 , 'go')
#ax.plot(1.4, 1000 , 'yo')

rects3 = plt.bar(index + 2*bar_width, e2, bar_width,
alpha=opacity,
color='g',
label='e2', yerr = e2E, capsize = 5)

rects4 = plt.bar(index + 3*bar_width, e1, bar_width,
alpha=opacity,
color='b',
label='e1', yerr = e1E, capsize = 5)

rects5 = plt.bar(index + 4*bar_width, NTC, bar_width,
alpha=opacity,
color='c',
label='NTC', yerr = NTCE, capsize = 5)

plt.xlabel('Virus Name')
plt.ylabel('Background Subtracted Flourescence')
plt.title('Background Subtracted Flourescence for Virus at 2 hours')
plt.xticks(index + bar_width, virusNames)
plt.legend()
plt.tight_layout()
plt.show()


def getTime(v):
    y=3
    SArr = [] 
    iter = 0
    iter2 = 0

    le4 = []
    le3 = []
    le2 = []
    le1 = []
    lNTC = []
    while(iter < numTimes):
        #while(iter2 < numViruses):
            le4.append(getArray(iter*20 + backgroundx + 2*v,y))
            le3.append(getArray(iter*20 + backgroundx + 2*v, y+2))
            le2.append(getArray(iter*20 + backgroundx + 2*v, y+4))
            le1.append(getArray(iter*20 + backgroundx + 2*v, y+6))
            lNTC.append(getNTC(iter*20 + backgroundx + 2*v, y+8))
          #  iter2 = iter2 + 1

            iter = iter + 1
    
    #print(le4)

    
    # for (i4, i3, i2, i1, iN) in (le4, le3, le2, le1, lNTC):
    #     i4 = stat.mean(i4)
    
    pe4 = []
    pe3 = []
    pe2 = []
    pe1 = []
    pNTC = []
    for item in le4:
        pe4.append(stat.mean(item))
    
    for item in le3:
        pe3.append(stat.mean(item))

    for item in le2:
        pe2.append(stat.mean(item))
    
    for item in le1:
        pe1.append(stat.mean(item))
    
    for item in lNTC:
        pNTC.append(stat.mean(item))

    return [pe4, pe3, pe2, pe1, pNTC]
     

#print(result)

plt.figure(2)
 # List to hold x values.
time = np.arange(numTimes) * 5

virusPlot = 1
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=.25, hspace=.7)
while(virusPlot < numViruses+1):
    result = getTime(virusPlot-1)
    # List to hold y values.
    e4P = result[0]
    e3P = result[1]
    e2P = result[2]
    e1P = result[3]
        # Plot the number in the list and set the line thickness.
    plt.subplot(4,2,virusPlot)
    plt.plot(time, e4P[0:numTimes],  'y', marker = '.', linewidth=3, label = 'e4')
    plt.plot(time, e3P[0:numTimes],  'r', marker = '.', linewidth=3, label = 'e3')
    plt.plot(time, e2P[0:numTimes],  'g', marker = '.', linewidth=3, label = 'e2')
    plt.plot(time, e1P[0:numTimes],  'b', marker = '.', linewidth=3, label = 'e1')
    plt.plot(time, result[4],  'c', marker = '.', linewidth=3)

    # Set the line chart title and the text font size.
    plt.title("Flourescence Over Time for " + virusNames[virusPlot-1], fontsize=12)

        # Set x axes label.
    plt.xlabel("Time (5 minutes)", fontsize=8)
    plt.ylabel("Flourescence Value", fontsize=8)

        # Set the x, y axis tick marks text size.
    plt.tick_params(axis='both', labelsize=9)

    virusPlot = virusPlot + 1

#plt.legend(bbox_to_anchor=(0, 0))
plt.show()
