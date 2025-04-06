import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import qrcode
import yaml
from scipy.spatial.distance import pdist

# Load Configuration
def load_config(config_path):
    with open(config_path, "rb") as file:
        return yaml.safe_load(file)

# Extractor Class
class ETLExtractor:
    def __init__(self, config):
        self.config = config
    
    def load_data(self):
        file_path = os.path.join(self.config["Input_Path"], "Segmented_Data", "Porosity", f"{self.config['Sample_name']}.csv")
        return pd.read_csv(file_path)

# Transformer Class
class ETLTransformer:
    def __init__(self, data, config):
        self.data = data
        self.config = config
    
    def process_data(self):
        self.data = self.data.sort_values(by='Volume (µm³)', ascending=False)
        self.data.dropna(inplace=True)
        return self.data

    def filter_data(self):
        conditions = (self.data["Sphericity"] >= self.config["Sphericity"]) & (self.data["Voxel count"] >= self.config["Voxel_count"])
        return self.data[conditions]

# Loader Class
class ETLLoader:
    def __init__(self, data, config):
        self.data = data
        self.config = config
    
    def save_data(self):
        output_path = os.path.join(self.config["Output_Path"], "Processed_Data")
        os.makedirs(output_path, exist_ok=True)
        self.data.to_csv(os.path.join(output_path, f"{self.config['Sample_name']}_processed.csv"), index=False)
    
    def generate_qr_code(self):
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(self.data.to_string())
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save(os.path.join(self.config["Output_Path"], f"{self.config['Sample_name']}_QR.png"))

# Runner Class
class ETLRunner:
    def __init__(self, config_path):
        self.config = load_config(config_path)
    
    def run(self):
        extractor = ETLExtractor(self.config)
        data = extractor.load_data()
        
        transformer = ETLTransformer(data, self.config)
        processed_data = transformer.process_data()
        filtered_data = transformer.filter_data()
        
        loader = ETLLoader(filtered_data, self.config)
        loader.save_data()
        loader.generate_qr_code()
        print("ETL Pipeline Executed Successfully!")

# Run the ETL process
if __name__ == "__main__":
    etl = ETLRunner("config.yaml")
    etl.run()
