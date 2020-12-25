'''
vis_helpers.py - tools to help with visualization
'''
import h5py
import numpy as np
import matplotlib.pyplot as plt

'''
visualize events over time in (t,x,y) colored by polarity
ON events (positive change in intensity) are blue
OFF events (negative change in intensity) are red
data is a data_handler object
'''
def vis_events_timeslice(data, start_ind, end_ind):
    # for normalizing the time axis
    t_start = data.events[0,2]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_box_aspect((5, 1, 1))
    for i in range(start_ind, end_ind + 1):
        [x,y,t,p] = data.events[i,:]
        t -= t_start
        if p == 1:
            ax.scatter3D(t,x,y,color='blue')
        else:
            ax.scatter3D(t,x,y,color='red')

    ax.set_xlabel('time')
    ax.set_ylabel('x')
    ax.set_zlabel('y')
    plt.show()
    #plt.savefig('event_vis.png')

'''
displays a single grayscale image
data is a data_handler object
'''
def vis_gs_image(data, ind):
    plt.figure()
    plt.imshow(data.images[ind,:], cmap='gray', vmin=0, vmax=255)
    plt.show()

'''
visualize event frames between one pair of gs images.
start_ind is the index of first of the two gs images
'''
def vis_event_frames(network_input, frame_times, start_ind):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_box_aspect((5, 1, 1))
    for i in range(4): # loop over the four channels
        if i % 2 == 0:
            color = 'red'
        else:
            color = 'blue'

        data = network_input[i,start_ind,:,:,:]
        N = data.shape[0]
        for j in range(N): # loop over the N event frames per group
            if i<2:
                tmp = 0
            else:
                tmp = 1
            time = frame_times[start_ind,tmp*N + j]
            for x in range(data.shape[1]):
                for y in range(data.shape[2]):
                    if data[j,x,y] == 1:
                        ax.scatter3D(time,x,y,color=color)

    ax.set_xlabel('time')
    ax.set_ylabel('x')
    ax.set_zlabel('y')
    plt.show()

