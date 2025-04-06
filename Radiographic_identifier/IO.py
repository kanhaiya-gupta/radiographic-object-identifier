"""
File: IO.py
Author: Kanhaiya Gupta
Date: 2024-11-05
Description: A Python script defining the paths for Inputs and Outputs.

"""

from module_list import *

####################################################################################

# Create the Data directory
 
Input_path = config_QID["Input_Path"] 
os.makedirs(Input_path, exist_ok=True)

Segmented_directory = os.path.join(Input_path, r'Segmented_Data')
os.makedirs(Segmented_directory, exist_ok=True)
Porosity_directory = os.path.join(Segmented_directory, r'Porosity')
os.makedirs(Porosity_directory, exist_ok=True)

Processed_data_directory = os.path.join(Input_path, r'Processed_Data')
os.makedirs(Processed_data_directory, exist_ok=True)
Pores_data_directory = Path_processed_data = Processed_data_directory + "/" + "Pores_" + str(config_QID["No_of_pores"]) + "/"
os.makedirs(Pores_data_directory, exist_ok=True)
Similarity_directory = os.path.join(Pores_data_directory, r'Similarity')
os.makedirs(Similarity_directory, exist_ok=True)



########################################################################################

# Create the output directory
Output_path = config_QID["Output_Path"]
isExist_OP = os.path.exists(Output_path)

if not isExist_OP:
    os.makedirs(Output_path, exist_ok=True)

Path_pores = config_QID["Output_Path"] + "Pores_" + str(config_QID["No_of_pores"])

isExist = os.path.exists(Path_pores)
if not isExist:
    os.makedirs(Path_pores, exist_ok=True)
    #print(Path_pores)
    CSV_directory = os.path.join(Path_pores, r'CSV_data')
    os.makedirs(CSV_directory, exist_ok=True)
    Similarity_directory = os.path.join(Path_pores, r'Similarity_result')
    os.makedirs(Similarity_directory, exist_ok=True)
    UID_directory = os.path.join(Path_pores, r'UID')
    os.makedirs(UID_directory, exist_ok=True)
    Images_directory = os.path.join(Path_pores, r'Images')
    os.makedirs(Images_directory, exist_ok=True)
    # Create inside image directory
    Distance_directory = os.path.join(Images_directory, r'Distances')
    os.makedirs(Distance_directory, exist_ok=True)
    QRcode_directory = os.path.join(Images_directory, r'QR-codes')
    os.makedirs(QRcode_directory, exist_ok=True)
    Reconstruction_directory = os.path.join(Images_directory, r'Reconstruction')
    os.makedirs(Reconstruction_directory, exist_ok=True)
    Distance_comp_directory = os.path.join(Images_directory, r'Distance_comparison')
    os.makedirs(Distance_comp_directory, exist_ok=True)

# Create the meta-data

# datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

updict = {"Date_and_time" : dt_string, "Topic" : "Microstructural_fingerprinting"}
with open(Path_pores + '/' + 'Meta-data.yaml', 'w') as yaml_file:
    # ** operator for packing and unpacking items in order
    config_QID_update = {**updict, **config_QID}
    yaml.dump(config_QID_update, yaml_file, default_flow_style=False, sort_keys=False)