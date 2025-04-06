#!/bin/bash
# Let's call this script script.sh
source $HOME/AppData/Local/miniconda3/Scripts/activate
cd $HOME/radiographic_identifier/Radiographic_identifier/
#conda activate env_doi
#pwd
python run.py
echo Outputs: 
echo Check the Output directory
#git status
