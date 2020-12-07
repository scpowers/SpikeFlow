#!/usr/bin/env python3
'''
run.py - file to be executed.
'''
import tensorflow as tf
from tensorflow import keras
from data_handler import *
from vis_helpers import *

print('\n\n\n')
################ Parameters  ################
# data sources
train_data_filename = 'outdoor_day2_data.hdf5'
test_data_filename = 'indoor_flying2_data.hdf5'

# encoding parameters
N = 5 # number of event frames per before/after group

# training parameters
dt = 1 # time window length, in # of gs images apart
lam = 10 # weight factor for smoothness loss
numEpochs = 100 # number of training epochs
batchSize = 8 # mini-batch size

# photometric loss parameters
r = 0.45
eta = 0.001

# SNN parameters
V_t = 0.75 # IF neuron threshold voltage

################ Implementation  ################
train_data = data_handler(train_data_filename, 'train')

# test event visualization
#vis_events_timeslice(train_data, 0, 1000)

# test grayscale image visualization
#vis_gs_image(train_data, 55)
