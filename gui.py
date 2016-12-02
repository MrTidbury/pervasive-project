#from tkinter import *
from tk import *
import python2-tk as tkinter
from time import sleep
import socket
import math
root = Tk()
root.title("AJ^2 Temeprature Monitor")
root.geometry('630x270')
root.configure(bg='#d3d3d3')

reading0=1
reading1=2
reading2=3
reading3=4
reading4=5
reading5=6

UDP_IP = "192.168.0.22"
UDP_PORT = 8888
MESSAGE = "req"

print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)
print ("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))

readings=[reading0, reading1, reading2, reading3, reading4, reading5]

def celsiusFahrenheit():
    display=celFah.get()
    if display=="C":
        temp0.set(reading0)
        temp1.set(reading1)
        temp2.set(reading2)
        temp3.set(reading3)
        temp4.set(reading4)
        temp5.set(reading5)
        rec.set(30)
    else:
        temp0.set(reading0*10)
        temp1.set(reading1*10)
        temp2.set(reading2*10)
        temp3.set(reading3*10)
        temp4.set(reading4*10)
        temp5.set(reading5*10)
        rec.set(60)

def average():
    av=(readings[0]+readings[1]+readings[2]+readings[3]+readings[4]+readings[5])/6
    ave.set(int(av))

Label(root, text="Welcome! \n Please select between celsius and fahrenheit\n", bg="#d3d3d3", fg="#000000").pack()

mainFrame=Frame(root, bg="#d3d3d3")
mainFrame.pack()

temp0=StringVar()
temp0.set(reading0)
Label(mainFrame, text="Temperature of Server Panel 1:   ", bg="#d3d3d3", fg="#000000").grid(row=0, column=0)
Label(mainFrame, textvariable=temp0, bg="#d3d3d3", fg="#000000").grid(row=0, column=1)
temp1=StringVar()
temp1.set(reading1)
Label(mainFrame, text="Temperature of Server Panel 2:   ", bg="#d3d3d3", fg="#000000").grid(row=1, column=0)
Label(mainFrame, textvariable=temp1, bg="#d3d3d3", fg="#000000").grid(row=1, column=1)
temp2=StringVar()
temp2.set(reading2)
Label(mainFrame, text="Temperature of Server Panel 3:   ", bg="#d3d3d3", fg="#000000").grid(row=2, column=0)
Label(mainFrame, textvariable=temp2, bg="#d3d3d3", fg="#000000").grid(row=2, column=1)
temp3=StringVar()
temp3.set(reading3)
Label(mainFrame, text="Temperature of Server Panel 4:   ", bg="#d3d3d3", fg="#000000").grid(row=3, column=0)
Label(mainFrame, textvariable=temp3, bg="#d3d3d3", fg="#000000").grid(row=3, column=1)
temp4=StringVar()
temp4.set(reading4)
Label(mainFrame, text="Temperature of Server Panel 5:   ", bg="#d3d3d3", fg="#000000").grid(row=4, column=0)
Label(mainFrame, textvariable=temp4, bg="#d3d3d3", fg="#000000").grid(row=4, column=1)
temp5=StringVar()
temp5.set(reading5)
Label(mainFrame, text="Temperature of Server Panel 6:   ", bg="#d3d3d3", fg="#000000").grid(row=5, column=0)
Label(mainFrame, textvariable=temp5, bg="#d3d3d3", fg="#000000").grid(row=5, column=1)

Label(mainFrame, text="\n", bg="#d3d3d3", fg="#000000").grid(row=6, column=0)

highTempC=StringVar()
highTempC.set(0)
Label(mainFrame, text="Highest Reading °C:", bg="#d3d3d3", fg="#000000").grid(row=7, column=0)
Label(mainFrame, textvariable=highTempC, bg="#d3d3d3", fg="#000000").grid(row=8, column=0)

highTempF=StringVar()
highTempF.set(0)
Label(mainFrame, text="Highest Reading °F:", bg="#d3d3d3", fg="#000000").grid(row=7, column=1)
Label(mainFrame, textvariable=highTempF, bg="#d3d3d3", fg="#000000").grid(row=8, column=1)

Label(mainFrame, text="            ", bg="#d3d3d3", fg="#000000").grid(row=2, column=2)

celFah=StringVar()
celFah.set(None)
Radiobutton(mainFrame, variable=celFah, value="C", text="Celsius", bg="#d3d3d3", fg="#000000").grid(row=1, column=3)
Radiobutton(mainFrame, variable=celFah, value="F", text="Fahrenheit", bg="#d3d3d3", fg="#000000").grid(row=1, column=4)

ave=StringVar()
ave.set(None)
Label(mainFrame, text="Average Temperature:   ", bg="#d3d3d3", fg="#000000").grid(row=3, column=3)
Label(mainFrame, textvariable=ave, bg="#d3d3d3", fg="#000000").grid(row=4, column=3)

rec=StringVar()
rec.set(None)
Label(mainFrame, text="Recommended Temperature:", bg="#d3d3d3", fg="#000000").grid(row=3, column=4)
Label(mainFrame, textvariable=rec, bg="#d3d3d3", fg="#000000").grid(row=4, column=4)

while (True):
    sleep(0.02)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))
    data, addr = sock.recvfrom(1024)
    decoded_data = data.decode()
    data_array = decoded_data.split(",")
    print (data_array)
    celsiusFahrenheit()
    cF=celFah.get()
    highestC=highTempC.get()
    highestF=highTempF.get()
    celsius=True
    if cF=="C":
        celsius=True
        readings=[int(data_array[0]), int(data_array[1]), int(data_array[2]), int(data_array[3]), int(data_array[4]), int(data_array[5])]
        temp0.set(int(readings[0]))
        temp1.set(int(readings[1]))
        temp2.set(int(readings[2]))
        temp3.set(int(readings[3]))
        temp4.set(int(readings[4]))
        temp5.set(int(readings[5]))
        average()
    else:
        celsius=False
        readings =[((int(data_array[0])*1.8)+32), ((int(data_array[1])*1.8)+32), ((int(data_array[2])*1.8)+32), ((int(data_array[3])*1.8)+32), ((int(data_array[4])*1.8)+32), ((int(data_array[5])*1.8)+32)]
        temp0.set(int(readings[0]))
        temp1.set(int(readings[1]))
        temp2.set(int(readings[2]))
        temp3.set(int(readings[3]))
        temp4.set(int(readings[4]))
        temp5.set(int(readings[5]))
        average()
    if celsius==True:
        for i in range(6):
            if readings[i]>float(highestC):
                highTempC.set(int(readings[i]))
    else:
        for i in range(6):
            if readings[i]>float(highestF):
                highTempF.set(int(readings[i]))
    root.update()
