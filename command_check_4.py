# -*- coding: utf-8 -*-
"""
Created on Fri May 20 14:18:28 2022

@author: Alonso Moran
"""

#Import libraries 
import time 
import asyncio
import struct
import numpy as np
import pandas as pd
import array as arr
import math
import datetime as dt 
from bleak import BleakScanner 
from bleak import BleakClient
from bleak import BleakError
import nest_asyncio
nest_asyncio.apply()

#Identify LuDi devices around and print the address
async def main1():
    devices = await BleakScanner.discover()
    for d in devices:
        print(d)      
#asyncio.run(main1()) #set a break point here and read ludi address


data_array = []
final_data = []
#data_array_hex = []
#Function for data reading after connection //difficult to cast data that has different bytelengths
def notification_handler(sender, data):
    print(f"sender: {data}")
    data_2=list(data)
    print("data equals:", data_2)
    #data_3 = data_2[0:8]
    #data_bytes=bytes(data_3)
    #final = struct.unpack('Q', data_bytes)
    #data_hex=hex(data_2)
    data_array.append(data_2)
    print("array is:", data_array)
    #final_data.append(final)
    
    # for i in data_array:
    #     data_hex = hex(data_array[i])
    #     data_array_hex.append(data_hex)
Pressure_value_array = [] 
#final_pressure = [] #provisional and could delete 
# final_time=0
#Time_pressure_array = [[],[],[],[]]
#Time_pressure_array = [[]]*17
#Function for data reading for sensor commands 


#VERY EASY TO OPTIMIZE!!!
def notification_handler2(sender, data):
     print(f"{sender}: {data}")
     data_sensors = list(data)
     print("DATA: ", data_sensors)
     #Get the hexadecimal responses for each set 
     Time = data_sensors[0:4]
     mouthpiece = data_sensors[5:6]
     Co2 = data_sensors[7:11]
     Co2_1 = data_sensors[12:16]
     Co2_2 = data_sensors[17:21]
     Co2_3 = data_sensors[22:26]
     o2 = data_sensors[27:31]
     No2 = data_sensors[32:36]
     Pressure = data_sensors[37:41]
     Temp = data_sensors[42:46]
     Hum = data_sensors[47:51]
     Pressure_1 = data_sensors[52:56]
     Temp_1 = data_sensors[57:61]
     Hum_1 = data_sensors[62:66]
     Pressure_2 = data_sensors[67:71]
     Temp_2 = data_sensors[72:76]
     Hum_2 = data_sensors[77:81]
     bat = data_sensors[82:86]
     
     #Convert the hexadecimals to bytes
     Time_bytes = bytes(Time)
     print("time_bytes are:", Time_bytes)
     mouth_bytes = bytes(mouthpiece)
     Co2_bytes = bytes(Co2)
     Co2_1_bytes = bytes(Co2_1)
     Co2_2_bytes = bytes(Co2_2)
     Co2_3_bytes = bytes(Co2_3)
     o2_bytes = bytes(o2)
     No2_bytes = bytes(No2)
     Pressure_bytes = bytes(Pressure)
     Temp_bytes = bytes(Temp)
     Hum_bytes = bytes(Hum)
     Pressure_bytes_1 = bytes(Pressure_1)
     Temp_bytes_1 = bytes(Temp_1)
     Hum_bytes_1 = bytes(Hum_1)
     Pressure_bytes_2 = bytes(Pressure_2)
     Temp_bytes_2 = bytes(Temp_2)
     Hum_bytes_2 = bytes(Hum_2)
     bat_bytes = bytes(bat)
     
     #Conver the bytes to its corresponding, I unsigned int, B unsigned char, I int, f float 
     [final_time] = struct.unpack('I', Time_bytes)
     #print("final_time is:",final_time)
     [final_mouth] = struct.unpack('B',mouth_bytes)
     [final_Co2] = struct.unpack('i', Co2_bytes)
     [final_Co2_1] = struct.unpack('i', Co2_1_bytes)
     [final_Co2_2] = struct.unpack('i', Co2_2_bytes)
     [final_Co2_3] = struct.unpack('i', Co2_3_bytes)
     [final_o2] = struct.unpack('i', o2_bytes)
     [final_No2] = struct.unpack('i', No2_bytes)
     [final_pressure] = struct.unpack('f', Pressure_bytes)
     [final_temp] = struct.unpack('f', Temp_bytes)
     [final_hum] = struct.unpack('f', Hum_bytes)
     [final_pressure_1] = struct.unpack('f', Pressure_bytes_1)
     [final_temp_1] = struct.unpack('f', Temp_bytes_1)
     [final_hum_1] = struct.unpack('f', Hum_bytes_1)
     [final_pressure_2] = struct.unpack('f', Pressure_bytes_2)
     [final_temp_2] = struct.unpack('f', Temp_bytes_2)
     [final_hum_2] = struct.unpack('f', Hum_bytes_2)
     [final_bat] = struct.unpack('f', bat_bytes)
     
     
     #Append all  the values to its positon on the data array 
     Time_pressure_array[0].append(final_time)
     Time_pressure_array[1].append(final_mouth)
     Time_pressure_array[2].append(final_Co2)
     Time_pressure_array[3].append(final_Co2_1)
     Time_pressure_array[4].append(final_Co2_2)
     Time_pressure_array[5].append(final_Co2_3)
     Time_pressure_array[6].append(final_o2)
     Time_pressure_array[7].append(final_No2)
     Time_pressure_array[8].append(final_pressure)
     Time_pressure_array[9].append(final_temp)
     Time_pressure_array[10].append(final_hum)
     Time_pressure_array[11].append(final_pressure_1)
     Time_pressure_array[12].append(final_temp_1)
     Time_pressure_array[13].append(final_hum_1)
     Time_pressure_array[14].append(final_pressure_2)
     Time_pressure_array[15].append(final_temp_2)
     Time_pressure_array[16].append(final_hum_2) 
     Time_pressure_array[17].append(final_bat)
     
     
     # print("data equals to:",data_sensors)
     # print(Time_pressure_array)
     # Pressure_value_array.append(final_pressure)
     # data_array.append(data2)  
     

#Write command and convert to ascii
# Go through command list for all the support commands 
def prepare_command(command, command_list):
    for i in range(len(command)):
        output_list = bytearray.fromhex(command[i]).decode()
        output_list_split = output_list.split()
        command_final = bytearray(''.join(output_list_split), encoding = 'utf8')
        command_list.append(command_final)


#Make connection with device and send command
async def main2(addr):
    print("Connecting to device...")
    async with BleakClient(addr) as client:
        print("Connected")
        await client.start_notify(read_characteristic, notification_handler)#allow notification
        for i in range(len(command_list)):
            await client.write_gatt_char(write_characteristic, command_list[i])#write command
        # timeout_start = time.time()
        # while time.time() < timeout_start + timeout: #timer for taking data during x seconds  
        #   pass
            await client.read_gatt_char(read_characteristic)#read obatined data
        # await client.stop_notify(read_characteristic)#stop notification
        # await client.write_gatt_char(write_characteristic, inicio) #send stream stop command
        
#asyncio.run(main2(addr))

#Make connection with device and send sensor commands
async def main3(addr):
    print("Connecting to device...")
    async with BleakClient(addr) as client:
        print("Connected")
        await client.start_notify(read_characteristic, notification_handler2)#allow notification
        #for i in range(len(command_list)):
        await client.write_gatt_char(write_characteristic, command_list[0])#write command
        timeout_start = time.time()
        while time.time() < timeout_start + timeout: #timer for taking data during x seconds  
          pass
        await client.read_gatt_char(read_characteristic)#read obatined data
        await client.stop_notify(read_characteristic)#stop notification
        await client.write_gatt_char(write_characteristic, command_list[1]) #send stream stop command
        


#Evaluation of the support commands 
evaluation = []
def compare(data, comp_list):
      for i in range(len(data)):
          if data[i]==comp_list[i]:
              evaluation.append(1)
          else:
              evaluation.append(0)
      print("Evaluation matrix is:", evaluation)       
     

date = dt.datetime.now()
date_str = str(date)
def compare2(data, startend):
    #Open and write on a txt 
    file_eva = open ('evaluation.txt', 'a')
    #Store the device's address
    file_eva.write(addr)
    file_eva.write('\n')
    file_eva.write(date_str)
    file_eva.write('\n')
    #Go through each sensor's data
    for i in range(len(data)):
              #print (i) 
              row = data[i]
              start = startend[i][0] 
              end = startend[i][1]
              #If the first value is a 0, write the second value on its position, usually happens on the pressure
              if (row[0] == 0):
                  row[0] = row[1]
              else:
                  pass
             
              #Special if for the time, which is the first value 
              if (i==0):
                  for x in range(len(row)-1):
                    if(row[x]< row[x+1]):
                        test[i].append(1)
                    else: 
                        test[i].append(0)
              else:
                  pass
             
              #Write a 1 if value is within the given range 
              for x in range(1, len(row)):                      
                  if ((row[x] >= start) and (row[x] <= end)):
                      test[i].append(1)
                  else: 
                      test[i].append(0)
                     
              #All the elements are true/1, then print true, else print false 
              if all(test[i]): 
                sensor_matrix.append(True)
              else:
                sensor_matrix.append(False)
             
              #Write the results in a TXT file    
              #file_eva = open ('evaluation.txt', 'a') 
              lines = [index[i], ',', str(sensor_matrix[i]), '\n']
              for item in lines:
                  file_eva.write(item)
    #Line space and close txt              
    file_eva.write('\n')
    file_eva.close()
    
    
    

if  __name__ == "__main__":
    
#   for i in range(len(command_list)):
#       asyncio.run(main(addr, command_list[i]))
      #main(addr, command_list[i])
    #Identify Ludi devices around and print the address     
    asyncio.run(main1())  
    
    #Write device address
    #addr  = "EA:B8:AE:BB:7C:92" #ZWEI
    #addr  ="E9:9F:6E:84:46:19" #DREI
    #addr  ="F5:DE:09:9E:E2:C2" #FUENF
    addr  ="CF:34:4E:3D:D9:64" #EINS # add a breakpoint and add ludi address 
    read_characteristic = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"
    write_characteristic = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"
    
    
    #Support commands
    #Write command and convert it to ascii  
    #Support commands
    #command = ["3b30", "3c30"]
    #prepare_command(command, command_list)
    #Make connection with device and send command
    #Support commands
    #asyncio.run(main2(addr))
    #Compare results with comparison list
    #Compare support commands
    #compare_list = [[48, 46, 49, 46, 52, 10, 13, 165, 165, 165, 165],[0, 0, 0, 0, 0, 0, 0, 0, 165, 165, 165, 165]]
    #compare(data_array, compare_list)
    
    #Write command and convert it to ascii 
    #Sensor commands
    command = ["7230","7330"]
    timeout = 10
    
    #Declare array to store each sensor's values
    counter = 0
    Time_pressure_array = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    command_list = [] #??? put it up before the value, no need now
    #Convert command to ascii
    prepare_command(command, command_list)
    
    #Make connection with device and send command
    #Sensor commands
    asyncio.run(main3(addr))
    
    #Comparison matrix
    sensor_matrix = []
    index = ['time', 'mouthpiece','co2_0','co2_1','co2_2', 'co2_3','O2', 'NO2', 'pressure_0', 'temperature_0', 'humidity_0','pressure_1', 'temperature_1', 'humidity_1','pressure_2', 'temperature_2', 'humidity_2', 'battery']
    #ranges array, the CO2 values must always be within the adc readings, 
    #the same with the NO and the O but normally the values of these are lower, battery negative values because we have set the threshold higher so warns the user
    startend= [[0,math.inf],[0, 1.5], [-8388608, 8388608], [-8388608, 8388608], [-8388608, 8388608],[-8388608, 8388608],[5000000, 9000000 ],[-8388608, 8388608], [975,998], [0,60], [0,100], [975,998], [0,60], [0,100],[975,998], [0,60], [0,100],[-40,100]] #dont need to be accurate ranges, only make sense, i.e. 1080 for forced exhalation
    #startend= [[0,math.inf],[0, 1.5], [1000000, 1100000], [1000000, 1100000], [1000000, 1100000],[1000000, 1100000],[2, 3],[5,6], [980,995], [0,60], [0,100], [980,995], [0,60], [0,100],[980,995], [0,60], [0,100],[-40,100]] #dont need to be accurate ranges, only make sense, i.e. 1080 for forced exhalation
    #array to store results 
    test = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]    
    
    #compare2(Time_pressure_array, startend)
    
    