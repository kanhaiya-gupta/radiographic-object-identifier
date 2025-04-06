import csv
import numpy as np
import pandas as pd

def compute_uniqueness(config_QID, files, nos_samples):
    Uniqueness_result = pd.DataFrame(columns=files)
    
    input_path = f"{config_QID['Input_Path']}Processed_Data/Pores_{config_QID['No_of_pores']}/Similarity/{config_QID['Sample_name']}.csv"
    output_csv_path = f"{config_QID['Output_Path']}Pores_{config_QID['No_of_pores']}/CSV_data/{config_QID['Sample_name']}_similarity_result.csv"
    output_txt_path = f"{config_QID['Output_Path']}Pores_{config_QID['No_of_pores']}/Similarity_result/{config_QID['Sample_name']}_SIMILARITY.txt"
    
    with open(input_path) as mainfile:
        csvReader_main = csv.reader(mainfile, delimiter=',')
        next(csvReader_main)  # Skip header
        
        for row_main in csvReader_main:
            D, V1, V2 = map(float, row_main[2:5])
            uncertainty_dist = config_QID["Uncertainty_window"] * config_QID["Resolution_XCT"]
            
            r1 = np.round(((3 * V1) / (4 * np.pi)) ** (1 / 3))
            r2 = np.round(((3 * V2) / (4 * np.pi)) ** (1 / 3))
            diff_vol1_b = (4 / 3) * np.pi * (r1 + uncertainty_dist) ** 3
            diff_vol1_s = (4 / 3) * np.pi * (r1 - uncertainty_dist) ** 3
            diff_vol2_b = (4 / 3) * np.pi * (r2 + uncertainty_dist) ** 3
            diff_vol2_s = (4 / 3) * np.pi * (r2 - uncertainty_dist) ** 3
            
            Check_unique_point = []
            for k in range(nos_samples):
                test_result = []
                
                with open(f"{config_QID['Input_Path']}Processed_Data/Pores_{config_QID['No_of_pores']}/Similarity/{files[k]}") as otherfile:
                    csvReader_other = csv.reader(otherfile, delimiter=',')
                    next(csvReader_other)  # Skip header
                    
                    for row_other in csvReader_other:
                        D_t, V1_t, V2_t = map(float, row_other[2:5])
                        cond_D = np.abs(D - D_t) <= uncertainty_dist
                        
                        cond_V1 = (diff_vol1_s <= V1_t <= diff_vol1_b) or (diff_vol1_s <= V2_t <= diff_vol1_b)
                        cond_V2 = (diff_vol2_s <= V2_t <= diff_vol2_b)
                        
                        final_cond = cond_D and cond_V1 and cond_V2
                        test_result.append(final_cond)
                
                Check_unique_point.append(any(test_result))
            
            Uniqueness_result.loc[len(Uniqueness_result)] = Check_unique_point
    
    Uniqueness_result.index += 1  
    Uniqueness_result.to_csv(output_csv_path, index=False)
    
    with open(output_txt_path, "a") as file_old:
        for i in range(len(Uniqueness_result.columns)):
            false_count = Uniqueness_result[Uniqueness_result.columns[i]].value_counts().get(False, 0)
            truth_count = Uniqueness_result[Uniqueness_result.columns[i]].value_counts().get(True, 0)
            unique_percent = (truth_count * 100) / (truth_count + false_count) if (truth_count + false_count) > 0 else 0
            file_old.write(f"{Uniqueness_result.columns[i]}  {round(unique_percent, 2)}%\n")
    
    return Uniqueness_result
