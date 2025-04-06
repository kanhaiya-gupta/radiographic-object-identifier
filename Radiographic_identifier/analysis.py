"""
File: analysis.py
Author: Kanhaiya Gupta
Date: 2023-08-29
Description: A Python script for applying the methodology.

"""

from module_list import *
from functions import *


print("Sample:", config_QID["Sample_name"])
print("Number of features:", config_QID["No_of_pores"])

## Load the segmented CT data

data_pores = pd.read_csv(config_QID["Input_Path"] + "Segmented_Data" + "/" + "Porosity" + "/"  + config_QID["Sample_name"] +".csv")


df_pores = pd.DataFrame(data_pores)

# Sort based on the decreasing Equivalent Spherical Diameter
df_pores = df_pores.sort_values(by='Volume (µm³)', ascending=False)

# Drop not a number values
#df_pores = data_pores.drop("Name (NA)",axis=1) 


# Data for three-dimensional scattered points
# Visualize the data
fig = plt.figure()
ax = plt.axes(projection='3d')

plot_abs = ax.scatter3D(df_pores["Center Of Mass X (µm)"]/1000., df_pores["Center Of Mass Y (µm)"]/1000., df_pores["Center Of Mass Z (µm)"]/1000., c= df_pores["Volume (µm³)"], cmap='hot')
#ax.set_title("Colorbar represent ")
ax.set_xlabel("X - axis (mm)")
ax.set_ylabel("Y - axis (mm)")
ax.set_zlabel("Z - axis (mm)")
fig.colorbar(plot_abs, ax=ax, shrink=0.90, pad=0.1, label='Volume of the pore')
fig.savefig(config_QID["Output_Path"] + "Pores_" + str(config_QID["No_of_pores"]) + "/" + "Images/" + "Reconstruction/" + config_QID["Sample_name"] +"_3d.png",  bbox_inches='tight', dpi=400)

if config_QID["Volume_of_pore_"]:
    fig = plt.figure()
    ax = plt.axes()
    ax.hist(df_pores["Volume (µm³)"], bins=config_QID["No_of_bins"], density=False, histtype='stepfilled', alpha=1.0, label = config_QID["Sample_name"])
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    dx_alongX = xmax - xmin 
    dx_alongY = ymax - ymin 
    #ax.set_title("Distance of the pores from centre of laser path")
    ax.set_xlabel(r"Volumes of pores  ($\mu m^{3}$)")
    ax.set_ylabel(r"Number of events")
    #ax.text(xmin + 0.5*dx_alongX,ymax - 0.33*dx_alongY, r"KS-test: p value = %.2f"%p_value_ks+"%")
    #ax.text(xmin + 0.5*dx_alongX,ymax - 0.38*dx_alongY, r"No. of Bins = %0.0f"% config_QID["No_of_bins"])
    ax.grid()
    ax.legend()
    fig.savefig(config_QID["Output_Path"] + "Pores_" + str(config_QID["No_of_pores"]) + "/" + "Images/" + "Reconstruction/" + config_QID["Sample_name"] +"_Volume.png",  bbox_inches='tight', dpi=400)

if config_QID["Voxel_count_"]:
    fig = plt.figure()
    ax = plt.axes()
    ax.hist(df_pores["Voxel count"], bins=config_QID["No_of_bins"], density=False, histtype='stepfilled', alpha=1.0, label = config_QID["Sample_name"])
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    dx_alongX = xmax - xmin 
    dx_alongY = ymax - ymin 
    #ax.set_title("Distance of the pores from centre of laser path")
    ax.set_xlabel(r"Voxel counts")
    ax.set_ylabel(r"Number of events")
    #ax.text(xmin + 0.5*dx_alongX,ymax - 0.33*dx_alongY, r"KS-test: p value = %.2f"%p_value_ks+"%")
    #ax.text(xmin + 0.5*dx_alongX,ymax - 0.38*dx_alongY, r"No. of Bins = %0.0f"% config_QID["No_of_bins"])
    ax.grid()
    ax.legend()
    fig.savefig(config_QID["Output_Path"] + "Pores_" + str(config_QID["No_of_pores"]) + "/" + "Images/" + "Reconstruction/" + config_QID["Sample_name"] +"_Voxel.png",  bbox_inches='tight', dpi=400)

if config_QID["Sphericity_"]:
    fig = plt.figure()
    ax = plt.axes()
    ax.hist(df_pores["Sphericity"], bins=config_QID["No_of_bins"], density=False, histtype='stepfilled', alpha=1.0, label = config_QID["Sample_name"])
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    dx_alongX = xmax - xmin 
    dx_alongY = ymax - ymin 
    #ax.set_title("Distance of the pores from centre of laser path")
    ax.set_xlabel(r"Sphericity")
    ax.set_ylabel(r"Number of events")
    #ax.text(xmin + 0.5*dx_alongX,ymax - 0.33*dx_alongY, r"KS-test: p value = %.2f"%p_value_ks+"%")
    #ax.text(xmin + 0.5*dx_alongX,ymax - 0.38*dx_alongY, r"No. of Bins = %0.0f"% config_QID["No_of_bins"])
    ax.grid()
    ax.legend()
    fig.savefig(config_QID["Output_Path"] + "Pores_" + str(config_QID["No_of_pores"]) + "/" + "Images/" + "Reconstruction/" + config_QID["Sample_name"] +"_Sphericity.png",  bbox_inches='tight', dpi=400)

if config_QID["Equivalent_Spherical_Diameter_"]:
    fig = plt.figure()
    ax = plt.axes()
    ax.hist(df_pores["Equivalent Spherical Diameter (µm)"], bins=config_QID["No_of_bins"], density=False, histtype='stepfilled', alpha=1.0, label = config_QID["Sample_name"])
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    dx_alongX = xmax - xmin 
    dx_alongY = ymax - ymin 
    #ax.set_title("Distance of the pores from centre of laser path")
    ax.set_xlabel(r"Equivalent Spherical Diameter ($\mu m$)")
    ax.set_ylabel(r"Number of events")
    #ax.text(xmin + 0.5*dx_alongX,ymax - 0.33*dx_alongY, r"KS-test: p value = %.2f"%p_value_ks+"%")
    #ax.text(xmin + 0.5*dx_alongX,ymax - 0.38*dx_alongY, r"No. of Bins = %0.0f"% config_QID["No_of_bins"])
    ax.grid()
    ax.legend()
    fig.savefig(config_QID["Output_Path"] + "Pores_" + str(config_QID["No_of_pores"]) + "/" + "Images/" + "Reconstruction/" + config_QID["Sample_name"] +"_diameter.png",  bbox_inches='tight', dpi=400)


if config_QID["Equivalent_Spherical_Diameter_"] and config_QID["Sphericity_"]:
    fig = plt.figure()
    ax = plt.axes()
    ax.scatter(df_pores["Equivalent Spherical Diameter (µm)"], df_pores["Sphericity"],color="black", marker= "+", s=50,  alpha = 1.0, label = config_QID["Sample_name"])
    ax.set_xlabel(r"Equivalent spherical diameter ($d_{equ}$) [$\mu m$]", fontsize=12,  color='black', rotation=0)
    ax.set_ylabel(r"Sphericity ($\Phi$)", fontsize=12,  color='black', rotation=90)
    #ax.set_xlim(0, 210)
    #ax.set_ylim(0.3, 1.08)
    ax.legend(fontsize = 12)
    ax.grid()
    fig.savefig(config_QID["Output_Path"] + "Pores_" + str(config_QID["No_of_pores"]) + "/" + "Images/" + "Reconstruction/" + config_QID["Sample_name"] +"_diameter_sphericity.png",  bbox_inches='tight', dpi=400)


##  Write the preprocessed data

df_pores.to_csv(config_QID["Input_Path"] + "Processed_Data" + "/" + "Pores_" + str(config_QID["No_of_pores"]) + "/" + config_QID["Sample_name"] + "_absolute.csv", index=False)


#  Load the segmented CT data after round off for further processing

pores_absolute = pd.read_csv(config_QID["Input_Path"] + "Processed_Data" + "/"  + "Pores_" + str(config_QID["No_of_pores"]) + "/" + config_QID["Sample_name"] + "_absolute.csv")


## Apply the selection cuts

#  Conditions

## For the translated coordinates
# if config_QID["Equivalent_Spherical_Diameter_max"] != -999.:
#     cond_diameter = (pores_absolute["Equivalent Spherical Diameter (µm)"] < config_QID["Equivalent_Spherical_Diameter_max"]) & (pores_absolute["Equivalent Spherical Diameter (µm)"] > config_QID["Equivalent_Spherical_Diameter_min"])
# else:
#     cond_diameter =  pores_absolute["Equivalent Spherical Diameter (µm)"] > config_QID["Equivalent_Spherical_Diameter_min"]

#print("Sphericity values:", type(config_QID["Sphericity"]))

if config_QID["Sphericity"] != -999.:
    cond_sphericity = df_pores["Sphericity"] >= config_QID["Sphericity"]

# else:
#     cond_sphericity = True

if config_QID["Voxel_count"] != -999.:
    cond_voxel = df_pores["Voxel count"] >= config_QID["Voxel_count"]

# else:
#     cond_voxel = True

#cond_distance = pores_translated["radius_pores"]

#condition = cond_diameter & cond_sphericity & cond_voxel
condition = cond_sphericity & cond_voxel


pores_absolute = df_pores[condition]

#print(len(pores_absolute))

# Sort based on the decreasing Equivalent Spherical Diameter
pores_absolute = pores_absolute.sort_values(by='Volume (µm³)', ascending=False)

if config_QID["No_of_pores"] != -999.:
    pores_absolute  = pores_absolute.head(config_QID["No_of_pores"])

#print(len(pores_absolute))
## Pores used for making the selection cuts
fig = plt.figure()
ax = plt.axes(projection='3d')
# Data for three-dimensional scattered points

plot_ = ax.scatter3D(pores_absolute["Center Of Mass X (µm)"]/1000., pores_absolute["Center Of Mass Y (µm)"]/1000., pores_absolute["Center Of Mass Z (µm)"]/1000., c= pores_absolute["Volume (µm³)"], cmap='hot')
#ax.set_title("Colorbar represent ")
ax.set_xlabel("X - axis (mm)")
ax.set_ylabel("Y - axis (mm)")
ax.set_zlabel("Z - axis (mm)")
fig.colorbar(plot_, ax=ax, shrink=0.90, pad=0.1, label='Volume of the pore')
fig.savefig(config_QID["Output_Path"] + "Pores_" + str(config_QID["No_of_pores"]) + "/" + "Images/" + "Reconstruction/" + config_QID["Sample_name"] +"_3d_selection.png",  bbox_inches='tight', dpi=400)


## Make the QR Code as Digital Identifier
# Create the data with required variables for QR-code

column_list_absolute=[]

if config_QID["Position_X"]:
    column_list_absolute.append("Center Of Mass X (µm)")

if config_QID["Position_Y"]:
    column_list_absolute.append("Center Of Mass Y (µm)")

if config_QID["Position_Z"]:
    column_list_absolute.append("Center Of Mass Z (µm)")

if config_QID["Volume_of_pore_"]:
    column_list_absolute.append("Volume (µm³)")

if config_QID["Sphericity_"]:
    column_list_absolute.append("Sphericity")

if config_QID["Voxel_count_"]:
    column_list_absolute.append("Voxel count")

if config_QID["Aspect_Ratio_"]:
    column_list_absolute.append("Aspect Ratio")

QR_code_data_absolute = DataFrame(columns = column_list_absolute)


if config_QID["Position_X"]:
    QR_code_data_absolute["Center Of Mass X (µm)"] = pores_absolute["Center Of Mass X (µm)"] 

if config_QID["Position_Y"]:
    QR_code_data_absolute["Center Of Mass Y (µm)"] = pores_absolute["Center Of Mass Y (µm)"]

if config_QID["Position_Z"]:
    QR_code_data_absolute["Center Of Mass Z (µm)"] = pores_absolute["Center Of Mass Z (µm)"]

if config_QID["Volume_of_pore_"]:
    QR_code_data_absolute["Volume (µm³)"] = pores_absolute["Volume (µm³)"]

if config_QID["Equivalent_Spherical_Diameter_"]:
    QR_code_data_absolute["Equivalent Spherical Diameter (µm)"] = pores_absolute["Equivalent Spherical Diameter (µm)"]

if config_QID["Sphericity_"]:
    QR_code_data_absolute["Sphericity"] = pores_absolute["Sphericity"]
    #QR_code_data_absolute["Sphericity"] = round(QR_code_data_absolute["Sphericity"], 3)

if config_QID["Voxel_count_"]:
    QR_code_data_absolute["Voxel count"] = pores_absolute["Voxel count"]
    #QR_code_data_absolute["Voxel count"] = round(QR_code_data_absolute["Voxel count"], 0)

if config_QID["Aspect_Ratio_"]:
    QR_code_data_absolute["Aspect Ratio"] = pores_absolute["Aspect Ratio"]
    #QR_code_data_absolute["Aspect Ratio"] = round(QR_code_data_absolute["Aspect Ratio"], 3)

QR_code_data_absolute.to_csv(config_QID["Input_Path"] + "Processed_Data" + "/" + "Pores_" + str(config_QID["No_of_pores"]) + "/" + config_QID["Sample_name"] + "_QR-code_data.csv", index=False)

# Use the absolute coordinates coordinates to construct the Identifier

QR_data_absolute = pd.read_csv(config_QID["Input_Path"] + "Processed_Data" + "/" + "Pores_" + str(config_QID["No_of_pores"]) + "/" + config_QID["Sample_name"] + "_QR-code_data.csv", usecols = ["Center Of Mass X (µm)", "Center Of Mass Y (µm)", "Center Of Mass Z (µm)"])

pair_dist = QR_data_absolute.to_numpy()

pair_distance = pdist(pair_dist)

#pair_distance = roundPartial(pdist(pair_dist), config_QID["Resolution_XCT"])   

matrix_dist_vol = np.zeros(6*len(pair_distance))

#print(len(matrix_dist_vol))

Volume_pores = np.array(QR_code_data_absolute["Volume (µm³)"])

#print(Volume_pores)

matrix_dist_vol = matrix_dist_vol.reshape(-1, 6)

pores_array = np.arange(0,config_QID["No_of_pores"])

#print(pores_array)

list_1 = pores_array
list_2 = pores_array
 
unique_combinations = []
 
for i in range(len(list_1)):
    for j in range(len(list_2)):
        if i >= j:
            continue
        unique_combinations.append([0., 0., 0., 0., list_1[i], list_2[j]])

unique_combinations = np.array(unique_combinations)

#print("3d array: ", unique_combinations)

for i, dist_value in enumerate(pair_distance):
    index_volume_1 = unique_combinations[i][4] 
    index_volume_2 = unique_combinations[i][5]
    #print(index_volume_1)
    #print(Volume_pores[index_volume_2])
    matrix_dist_vol[i][0] = index_volume_1 + 1
    matrix_dist_vol[i][1] = index_volume_2 + 1
    matrix_dist_vol[i][2] = pair_distance[i]
    #print(Volume_pores[int(index_volume_1)])
    matrix_dist_vol[i][3] = Volume_pores[int(index_volume_1)]
    matrix_dist_vol[i][4] = Volume_pores[int(index_volume_2)]

matrix_dist_vol[:,5] = matrix_dist_vol[:,3] + matrix_dist_vol[:,4]

#print("Matrix ", matrix_dist_vol)
# export as csv file
dist_vol_data = {'index_1':matrix_dist_vol[:,0], 'index_2':matrix_dist_vol[:,1],'distance':matrix_dist_vol[:,2], 'volume_1':matrix_dist_vol[:,3], 'volume_2':matrix_dist_vol[:,4], 'pair-wise_volume':matrix_dist_vol[:,5]}
df_pair_distance = pd.DataFrame(dist_vol_data)

# sort according to pair-wise volume
#df_pair_distance = df_pair_distance.sort_values(by=["pair-wise_volume"], ascending=False)

## Plot the histogram of distances
fig = plt.figure()
ax = plt.axes()

ax.hist(df_pair_distance["distance"], bins=config_QID["No_of_bins"], density=False, histtype='stepfilled',color='blue', alpha=1.0)
xmin, xmax = ax.get_xlim()
ymin, ymax = ax.get_ylim()
dx_alongX = xmax - xmin 
dx_alongY = ymax - ymin 
#ax.set_title("Distance of the pores from centre of laser path")
ax.set_xlabel(r"Combination of distances of succussive volumes of pores  ($\mu$ m)")
ax.set_ylabel("Number of events")
ax.text(xmin + 0.05*dx_alongX,ymax - 0.1*dx_alongY, r"No. of Bins = %0.0f"% config_QID["No_of_bins"])
ax.grid()
fig.savefig(config_QID["Output_Path"] + "Pores_" + str(config_QID["No_of_pores"]) + "/" + "Images/" + "Distances/" + config_QID["Sample_name"] +".png",  bbox_inches='tight', dpi=400)
    

# Developing QR code

if config_QID["Develop_identifier"]:
    # sort according to pair-wise volume
    df_pair_distance = df_pair_distance.sort_values(by=["pair-wise_volume"], ascending=False)
    # create the string of distances
    pair_distances = [str(element) for element in np.array(df_pair_distance["distance"])]
    dist_string = "|" + '|'.join(pair_distances) + "|"

    ## Plot the QR code
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5, border=2,
        )
    # The version parameter is an integer from 1 to 40 that controls the size of the QR Code
    #(the smallest, version 1, is a 21x21 matrix). Set to None and use the fit parameter 
    # when making the code to determine this automatically.

    # boz_size changes the size of QR code
    # border chnges the spaces between the QR code and the border of the image
    qr.add_data(dist_string)
    qr.make(fit=True)
    img = qr.make_image(fill_color="white", back_color="black")
    img.save(config_QID["Output_Path"] + "Pores_" + str(config_QID["No_of_pores"]) + "/" + "Images/" +  "QR-codes/" + config_QID["Sample_name"] +".png")


# create csv file
df_pair_distance.to_csv(config_QID["Input_Path"] + "Processed_Data" + "/" + "Pores_" + str(config_QID["No_of_pores"]) + "/"  + "Similarity/" + config_QID["Sample_name"] + ".csv", index=False)
