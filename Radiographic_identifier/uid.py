"""
File: uid.py
Author: Kanhaiya Gupta
Date: 2023-11-29
Description: A Python script for developing the URL Key.

"""

from module_list import *
from functions import *

if not config_QID["Develop_URL_key"]:
    exit()

# Use the absolute coordinates coordinates to construct the Identifier

QR_data_absolute = pd.read_csv(config_QID["Input_Path"] + "Processed_Data" + "/" + "Pores_" + str(config_QID["No_of_pores"]) + "/"  + config_QID["Sample_name"] + "_QR-code_data.csv", usecols = ["Center Of Mass X (µm)", "Center Of Mass Y (µm)", "Center Of Mass Z (µm)"])

QR_data_absolute  = QR_data_absolute.head(config_QID["No_of_pores"])

pair_dist = QR_data_absolute.to_numpy()

pair_distance = roundPartial(pdist(pair_dist), config_QID["Resolution_XCT"])   



distance_matrix = np.zeros((config_QID["No_of_pores"]-1,config_QID["No_of_pores"]-1))

Split_initialise = (np.arange(1,config_QID["No_of_pores"]))[::-1]

splitted_distance = np.split(pair_distance, np.cumsum(Split_initialise))

for i in range(config_QID["No_of_pores"]-1):
    distance_matrix[i] = np.concatenate([splitted_distance[i], np.zeros(i)])

eigen_values, eigen_vectors = eig(distance_matrix) 
eigen_values_absolute = np.absolute(eigen_values)
#print("The eigen values are : ", eigen_values_absolute)
eigen_values_absolute_3digit = eigen_values_absolute*1000.
eigen_values_array = [str(int(element)).zfill(5)  for element in eigen_values_absolute_3digit]

eigen_values_str = ''.join(map(str, eigen_values_array))


UID = decimalToBase57decimal(int(eigen_values_str))

print("The UID of "+ config_QID["Sample_name"] + " is ", UID)


file_old = open(config_QID["Output_Path"] + "Pores_" + str(config_QID["No_of_pores"]) + "/" + "UID/" + "UID.txt","a")
file_old.write(config_QID["Sample_name"] + "  ")
file_old.write(str(UID) + "\n")
file_old.close()


file_read = open(config_QID["Output_Path"] + "Pores_" + str(config_QID["No_of_pores"]) + "/" + "UID/" + "UID.txt","r")
lines = file_read.readlines()
lines_set = set(lines)

out = open(config_QID["Output_Path"] + "Pores_" + str(config_QID["No_of_pores"]) + "/" + "UID/" + "UID.txt","w")

for line in lines_set:
    out.write(line)
    
file_read.close()
out.close()