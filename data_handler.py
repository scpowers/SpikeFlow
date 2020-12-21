'''
data_handler.py - handles data loading operations
'''

import h5py
import numpy as np
from os import path
from encoding import encode_inputs

class data_handler:

    # constructor
    def __init__(self, filename, N, data_dir=None):
        # setup
        if data_dir is None:
            data_dir = 'datasets/' + filename + '/' + filename

        # save for encode_inputs argument
        self.filename = filename

        # construct actual data path
        data_path = data_dir + '_data.hdf5' 

        # select data from the left DAVIS camera
        dset = h5py.File(data_path, 'r')['davis']['left']

        # events
        self.events = dset['events']
        # grasycale images
        self.images = dset['image_raw']
        # time stamps
        self.image_ts = dset['image_raw_ts']
        # shifted time stamps
        self.image_ts_norm = self.image_ts - self.image_ts[0]
        # indices for the nearest event to each DAVIS image in time
        self.image_raw_event_inds = dset['image_raw_event_inds']

        # clear out dset
        dset = None

        # print dataset info
        print('Info for dataset: ', filename)
        print('events shape: ', self.events.shape)
        print('images shape: ', self.images.shape)
        self.num_images = self.images.shape[0]
        self.im_width = self.images.shape[1]
        self.im_height = self.images.shape[2]
        print('images_ts shape: ', self.image_ts.shape)
        print('images_event_inds shape: ', self.image_raw_event_inds)
        print('\n\n')

        # check if the dataset has already been encoded
        encoding_path = data_dir + "_former_ON_frames.npy"
        if not path.exists(encoding_path):
            print('encoding dataset...')
            encode_inputs(self, N)



