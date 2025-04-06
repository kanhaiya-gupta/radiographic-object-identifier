# analysis.py
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import yaml

class Analysis:
    def __init__(self, config):
        self.config = config
        self.sample_name = config["Sample_name"]
        self.input_path = config["Input_Path"]
        self.output_path = config["Output_Path"]
        self.no_of_pores = config["No_of_pores"]

    def load_data(self):
        file_path = f"{self.input_path}Segmented_Data/Porosity/{self.sample_name}.csv"
        self.df_pores = pd.read_csv(file_path)
        self.df_pores = self.df_pores.sort_values(by='Volume (µm³)', ascending=False)

    def visualize_data(self):
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.scatter3D(
            self.df_pores["Center Of Mass X (µm)"]/1000., 
            self.df_pores["Center Of Mass Y (µm)"]/1000., 
            self.df_pores["Center Of Mass Z (µm)"]/1000., 
            c=self.df_pores["Volume (µm³)"], cmap='hot'
        )
        ax.set_xlabel("X - axis (mm)")
        ax.set_ylabel("Y - axis (mm)")
        ax.set_zlabel("Z - axis (mm)")
        fig.savefig(f"{self.output_path}Pores_{self.no_of_pores}/Images/Reconstruction/{self.sample_name}_3d.png", dpi=400)
        plt.close(fig)

    def run(self):
        self.load_data()
        self.visualize_data()


# similarity.py
import os
import pandas as pd
from scipy.stats import ks_2samp

class Similarity:
    def __init__(self, config):
        self.config = config
        self.input_path = config["Input_Path"]
        self.sample_name = config["Sample_name"]
        self.no_of_pores = config["No_of_pores"]

    def compute_similarity(self):
        similarity_path = f"{self.input_path}Processed_Data/Pores_{self.no_of_pores}/Similarity/"
        main_sample = pd.read_csv(f"{similarity_path}{self.sample_name}.csv")
        
        for file in os.listdir(similarity_path):
            if file.endswith(".csv") and file != f"{self.sample_name}.csv":
                test_sample = pd.read_csv(f"{similarity_path}{file}")
                p_value = ks_2samp(main_sample["distance"], test_sample["distance"])[1]
                print(f"Similarity with {file}: p-value = {p_value}")

    def run(self):
        self.compute_similarity()


# run.py
import yaml
from analysis import Analysis
from similarity import Similarity

if __name__ == "__main__":
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)
    
    analysis = Analysis(config)
    analysis.run()
    
    similarity = Similarity(config)
    similarity.run()
