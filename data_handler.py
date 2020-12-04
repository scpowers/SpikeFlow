'''
data_handler.py - handles data loading operations
'''

import h5py
import numpy as np

class data_handler:

    # constructor
    def __init__(self, filename, usage, data_path=None):
        # setup
        if data_path is None:
            data_path = 'datasets/'

        # construct path
        data_path += filename 

        # select data from the left DAVIS camera
        dset = h5py.File(data_path, 'r')['davis']['left']

        # events
        self.events = dset['events']
        # grasycale images
        self.images = dset['image_raw']
        # time stamps
        self.image_ts = dset['image_raw_ts']
        # event indices for each DAVIS image in time
        self.image_raw_event_inds = dset['image_raw_event_inds']

        # clear out dset
        dset = None

        print('events shape: ', self.events.shape)
        print('images shape: ', self.images.shape)
        print('images_ts shape: ', self.image_ts.shape)
        print('images_event_inds shape: ', self.image_raw_event_inds)

        print('sample raw image: \n', self.images[32,:,:])



