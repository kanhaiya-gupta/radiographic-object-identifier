"""
File: module_list.py
Author: Kanhaiya Gupta
Date: 2023-08-29
Description: A Python script for importing all the required modules.

"""

# import the required modules

import os
import numpy as np                # module for math related work
import matplotlib.pyplot as plt   # module to plot figures
from scipy.linalg import eig, inv # modue to calculate eigen-values and eigen vectors
from scipy.stats import ks_2samp
from scipy.stats import norm
import progressbar
import time
from datetime import datetime

import csv                       # for csv related files
import pandas as pd              # pandas for data analysis
from pandas import DataFrame
import requests
import qrcode                    # to generate the QR codes


## modules for translating X, Y, Z of pores based on STL file

import logging
#import pyslm

# calclate the pair-wise distances
from scipy.spatial.distance import pdist

# Read the YAML file

import yaml  
from yaml.loader import FullLoader  
  

#open yaml file in read  

with open("../config/config.yaml", "rb") as file:  
    config_QID = yaml.load(file, Loader=FullLoader)  

