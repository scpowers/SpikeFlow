'''
run.py - file to be executed.
'''

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from data_handler import *
from vis_helpers import *
import h5py

# data parameters
train_data_filename = 'outdoor_day2_data.hdf5'
test_data_filename = 'indoor_flying2_data.hdf5'

train_data = data_handler(train_data_filename, 'train')

# test event visualization
#vis_events_timeslice(train_data, 0, 1000)

# test grayscale image visualization
vis_gs_image(train_data, 55)
