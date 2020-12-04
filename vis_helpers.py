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
            ax.scatter(t,x,y,color='red')

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
