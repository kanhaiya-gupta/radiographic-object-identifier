# Radiographic digital Identifier

## Download the directory
* git clone https://git.bam.de/kgupta/radiographic_identifier.git
* cd radiographic_identifier

## Install the required modules
* pip install -r requirements.txt

## Config file
* Edit the config file stored in 
    * config/config.yaml

## Input 
* The output from the image analysis software such as Dragonfly or VG-Studio are stored in Data/Segmented_Data directory.
    * STL file to make the relative position of pores
    * The csv file includes all the variables information.


## Analysis
* Run the analysis
    * cd Radiographic_identifier
    * python run.py or ./script.sh

## Output
* The output of the analysis is stored in Images directory
   * QR codes
   * Variables plot