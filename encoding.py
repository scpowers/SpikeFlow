'''
encoding.py - tools for encoding the event information
from the DAVIS camera into the discretized input
representation detailed in Lee et al.
'''
import numpy as np
import h5py

# data is a data_loader object, N is 
# number of event frames per group
def encode_inputs(data, N):

    # initialize arrays to be saved later
    # note: assuming that polarities are not summed
    # in each of the on/off frames...still binary.
    # also, one fewer than num_images because frames only created between
    # pairs of images...one fewer gap than the number of images
    '''
    former_ON = np.zeros((data.num_images - 1, N, data.im_width, 
        data.im_height))
    former_OFF = np.zeros((data.num_images - 1, N, data.im_width, 
        data.im_height))
    latter_ON = np.zeros((data.num_images - 1, N, data.im_width, 
        data.im_height))
    latter_OFF = np.zeros((data.num_images - 1, N, data.im_width, 
        data.im_height))
    '''
    former_ON = np.zeros((1, N, data.im_width, data.im_height))
    former_OFF = np.zeros((1, N, data.im_width, data.im_height))
    latter_ON = np.zeros((1, N, data.im_width, data.im_height))
    latter_OFF = np.zeros((1, N, data.im_width, data.im_height))
    # holds event frame times for each image
    frame_times = np.zeros((1, 2*N)) 

    # splits are largely governed by number of GS images
    #for i in range(data.num_images-1):
    for i in range(1): # only encode first 6 images
        # if first image, no corresponding nearest event
        if i == 0:
            event_i_start = 0
        else:
            event_i_start = data.image_raw_event_inds[i]

        event_i_end = data.image_raw_event_inds[i+1]
        #print('event_i_start: ', event_i_start)
        #print('event_i_end: ', event_i_end)

        # now have slice of events to consider
        events = data.events[event_i_start:event_i_end+1, :]
        print('len of events: ', len(events))
        #t_start = data.events[event_i_start, 2]
        t_start = data.image_ts[i]
        #print('t_start: ', t_start)
        #t_end = data.events[event_i_end, 2]
        t_end = data.image_ts[i+1]

        # determine midpoint in time between the two gs images
        t_mid = t_start + (t_end - t_start)/2
        #print('t_mid: ', t_mid)
        
        # determine time interval between event frames
        dt = (t_end - t_start) / (2*N)

        frame_times[i,:] = np.arange(t_start+dt, t_end+dt, dt)
        print('frame times: ', frame_times[i,:])
        print('array start time: ', frame_times[i,0])
        print('start time: ', t_start)
        print('array end time: ', frame_times[i,-1])
        print('end time: ', t_end)
        print('dt: ', dt)

        num_grouped = 0

        for n in range(N):
            for e in events:
                y = int(e[0])
                x = int(e[1])
                t = e[2]
                p = e[3]

                # former event frames
                if t >= t_start + (n*dt) and t < t_start + ((n+1)*dt):
                    num_grouped += 1
                    # if you find an ON event
                    if p == 1:
                        # only update event frame if an event wasn't already here
                        if former_ON[i,n,x,y] != 1:
                            former_ON[i,n,x,y] = 1
                    # must be an OFF event then
                    else:
                        # still only update if an event wasn't already here
                        if former_OFF[i,n,x,y] != 1:
                            former_OFF[i,n,x,y] = 1

                # latter event frames
                if e[2] >= t_mid + (n*dt) and e[2] < t_mid + ((n+1)*dt):
                    num_grouped += 1
                    # if you find an ON event
                    if p == 1:
                        # only update event frame if an event wasn't already here
                        if latter_ON[i,n,x,y] != 1:
                            latter_ON[i,n,x,y] = 1
                    # must be an OFF event then
                    else:
                        # still only update if an event wasn't already here
                        if latter_OFF[i,n,x,y] != 1:
                            latter_OFF[i,n,x,y] = 1
        print('% grouped: ', num_grouped/len(events) * 100)


    # now save arrays containing event frames
    np.save(data.filename + '_former_ON.npy', former_ON)
    np.save(data.filename + '_former_OFF.npy', former_OFF)
    np.save(data.filename + '_latter_ON.npy', latter_ON)
    np.save(data.filename + '_latter_OFF.npy', latter_OFF)

    output = np.zeros((4,5, N, data.im_width, data.im_height))
    output[0,:,:,:,:] = former_ON
    output[1,:,:,:,:] = former_OFF
    output[2,:,:,:,:] = latter_ON
    output[3,:,:,:,:] = latter_OFF
    np.save(data.filename + '_network_input.npy', output)
    np.save(data.filename + '_frame_times.npy', frame_times)


        






