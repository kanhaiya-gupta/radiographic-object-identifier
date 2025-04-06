"""
File: similarity.py
Author: Kanhaiya Gupta
Date: 2023-08-29
Description: A Python script applying the authentication concept.

"""

from module_list import *
from functions import *

if not config_QID["Similarity_study"]:
    exit()

# assign path
path, dirs, files = next(os.walk(config_QID["Input_Path"] + "Processed_Data" + "/" + "Pores_" + str(config_QID["No_of_pores"]) + "/"  + "Similarity/"))
files.remove(config_QID["Sample_name"] + ".csv")

#print(files)
nos_samples = len(files)  # file count

if nos_samples < 1:
    print("There is only one sample and nothing to test")
    exit()

# KS-test 

# create empty list
dataframes_list = []

main_sample = pd.read_csv(config_QID["Input_Path"] + "Processed_Data" + "/" + "Pores_" + str(config_QID["No_of_pores"]) + "/" + "Similarity/" + config_QID["Sample_name"] + ".csv")

for i in range(nos_samples):
    temp_df = pd.read_csv(config_QID["Input_Path"] + "Processed_Data" + "/" + "Pores_" + str(config_QID["No_of_pores"]) + "/"  + "Similarity/" + files[i])
    dataframes_list.append(temp_df)
     

# for t, dataset in enumerate(dataframes_list):

#     # plot the each dataframe

#     df_others = pd.DataFrame(dataset)

#     ks_test = ks_2samp(main_sample["distance"], df_others["distance"])
#     p_value_ks = ks_test[1]*100.

#     main_sample_name = config_QID["Sample_name"]
#     others_samples = files
#     other_sample_names = (others_samples[i]).replace(".csv", "")

#     fig = plt.figure()
#     ax = plt.axes()
#     ax.hist(main_sample["distance"], bins=config_QID["No_of_bins"], density=False, histtype='stepfilled',color='orange', alpha=0.7, label = main_sample_name)
#     ax.hist(df_others["distance"], bins=config_QID["No_of_bins"], density=False, histtype='stepfilled',color='blue', alpha=0.7, label = other_sample_names)
#     xmin, xmax = ax.get_xlim()
#     ymin, ymax = ax.get_ylim()
#     dx_alongX = xmax - xmin 
#     dx_alongY = ymax - ymin 
#     #ax.set_title("Distance of the pores from centre of laser path")
#     ax.set_xlabel("Combination of distances of succussive volumes of pores  ($\mu m$)")
#     ax.set_ylabel("Number of events")
#     ax.text(xmin + 0.5*dx_alongX,ymax - 0.33*dx_alongY, r"KS-test: p value = %.2f"%p_value_ks+"%")
#     #ax.text(xmin + 0.5*dx_alongX,ymax - 0.38*dx_alongY, r"No. of Bins = %0.0f"% config_QID["No_of_bins"])
#     ax.grid()
#     ax.legend()
#     fig.savefig(config_QID["Output_Path"] + "Pores_" + str(config_QID["No_of_pores"]) + "/" + "Images/" + "Distance_comparison/" + config_QID["Sample_name"] +"_vs_"+other_sample_names+".png",  bbox_inches='tight', dpi=400)
     
# append datasets to the list

Uniqueness_result = DataFrame(columns = files)
# Load the main segmented CT data
 
with open(config_QID["Input_Path"] + "Processed_Data" + "/" + "Pores_" + str(config_QID["No_of_pores"]) + "/" + "Similarity/" + config_QID["Sample_name"] + ".csv") as mainfile:
    csvReader_main = csv.reader(mainfile, delimiter=',')
    for i, row_main in enumerate(csvReader_main):
        if i == 0:
            continue
        #print(row_main)

        D = float(row_main[2])
        V1 = float(row_main[3])
        V2 = float(row_main[4])

        uncertainty_dist = config_QID["Uncertainty_window"]*(config_QID["Resolution_XCT"]) 

        r1 = np.round(((3*V1)/(4*np.pi))**(1/3))
        r2 = np.round(((3*V2)/(4*np.pi))**(1/3))
        diff_vol1_b = 4/3*np.pi*(r1 + uncertainty_dist)**3 
        diff_vol1_s = 4/3*np.pi*(r1 - uncertainty_dist)**3
        diff_vol2_b = 4/3*np.pi*(r2 + uncertainty_dist)**3 
        diff_vol2_s = 4/3*np.pi*(r2 - uncertainty_dist)**3
        
        Sample_unique = True
        Check_unique_point = []
        for k in range(nos_samples):
            Test_result = []

            with open(config_QID["Input_Path"] + "Processed_Data" + "/" + "Pores_" + str(config_QID["No_of_pores"]) + "/"  + "Similarity/" + files[k]) as otherfiles:
                csvReader_other = csv.reader(otherfiles, delimiter=',')
                for j, row_other in enumerate(csvReader_other):
                    if j == 0:
                        continue
                    #print(row_other)

                    D_t = float(row_other[2])
                    V1_t = float(row_other[3])
                    V2_t = float(row_other[4])
                    

                    cond_D = False
                    cond_V1 = False
                    cond_V2 = False

                    cond_D = np.abs(D - D_t) <= uncertainty_dist
                
                    if ((V1_t >= diff_vol1_s) & (V1_t <= diff_vol1_b)):
                        cond_V1 = True
                        if ((V2_t >= diff_vol2_s) & (V2_t <= diff_vol2_b)):
                            cond_V2 = True
                    elif ((V2_t >= diff_vol1_s) & (V2_t <= diff_vol1_b)):
                        cond_V1 = True
                        if ((V2_t >= diff_vol2_s) & (V2_t <= diff_vol2_b)):
                            cond_V2 = True

                    final_cond = cond_D & cond_V1 & cond_V2
                    

                    if final_cond:
                        Test_result.append(True)
                    else:
                        Test_result.append(False)

            Check_unique_point.append(any(Test_result)) 

        Uniqueness_result.loc[len(Uniqueness_result)] = Check_unique_point
        #Sample_unique = Sample_unique * Check_unique_point[0]
        #print("The test result is: ", Check_unique_point[0])

Uniqueness_result.index += 1  
Uniqueness_result.to_csv(config_QID["Output_Path"] + "Pores_" + str(config_QID["No_of_pores"]) + "/" + "CSV_data/"+ config_QID["Sample_name"] + "_similarity_result.csv", index=False)

no_of_cols = len(Uniqueness_result.axes[1])

file_old = open(config_QID["Output_Path"] + "Pores_" + str(config_QID["No_of_pores"]) + "/" + "Similarity_result/" + config_QID["Sample_name"] + "_SIMILARITY.txt","a")


for i in range(no_of_cols):
    false_count = 0
    truth_count = 0
    false_count = (Uniqueness_result[Uniqueness_result.columns[i]]).value_counts()[False]
    if (false_count != len(Uniqueness_result)):
        truth_count = (Uniqueness_result[Uniqueness_result.columns[i]]).value_counts()[True]
    unique_percent = (truth_count * 100)/(truth_count + false_count)
    file_old.write(Uniqueness_result.columns[i] + "  ")
    file_old.write(str(round(unique_percent, 2)) +  "%" + "\n")

file_old.close()



file_read = open(config_QID["Output_Path"] + "Pores_" + str(config_QID["No_of_pores"]) + "/" + "Similarity_result/" + config_QID["Sample_name"] + "_SIMILARITY.txt","r")
lines = file_read.readlines()
#print(lines)
lines_set = set(lines)
file_read.close()
#print(lines_set)

out = open(config_QID["Output_Path"] + "Pores_" + str(config_QID["No_of_pores"]) + "/" + "Similarity_result/" + config_QID["Sample_name"] + "_SIMILARITY.txt","w")

for line in lines_set:
    out.write(line)
    #print(line)
    
out.close()

