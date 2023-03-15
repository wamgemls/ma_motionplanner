import matplotlib.pyplot as plt
import csv
import numpy as np

csv_filepath = 'log_temp/dummy.csv'

timestamp_l = []
ego_x_l = []
ego_y_l = []
ego_vx_l = []
ego_ax_l = []
ego_yaw_l = []
ego_curvature_l = []
prekingpin_x_l = []
prekingpin_y_l = []
prekingpin_yaw_l = []
kingpin_x_l = []
kingpin_y_l = []
kingpin_yaw_l = []
dis_error_trajectory_l = []
yaw_error_trajectory_l = []
dis_error_trajectory_goal_l = []
yaw_error_trajectory_goal_l = []
dis_error_prekingpin_l = []
yaw_error_prekingpin_l = []
dis_error_kingpin_l = []
yaw_error_kingpin_l = []

trajectory_t = []
trajectory_s = []
trajectory_x = []
trajectory_y = []
trajectory_vx = []
trajectory_ax = []
trajectory_yaw = []
trajectory_curvature = []

trajectory23_t = []
trajectory23_s = []
trajectory23_x = []
trajectory23_y = []
trajectory23_vx = []
trajectory23_ax = []
trajectory23_yaw = []
trajectory23_curvature = []

timestamps = []
x_values = []



# Read in the CSV file and extract the timestamp and x value from each row
with open(csv_filepath, mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    
    trajectory_delimiter=[]

    for j,row in enumerate(reader):
        timestamp,ego_x,ego_y,ego_vx,ego_yaw,ego_curvature,prekingpin_x,prekingpin_y,prekingpin_yaw,kingpin_x,kingpin_y,kingpin_yaw,dis_error_trajectory,yaw_error_trajectory,dis_error_trajectory_goal, yaw_error_trajectory_goal,dis_error_prekingpin, yaw_error_prekingpin,dis_error_kingpin,yaw_error_kingpin = row[:20]

        timestamp_l.append(float(timestamp))
        ego_x_l.append(float(ego_x))
        ego_y_l.append(float(ego_y))
        ego_yaw_l.append(float(ego_yaw))
        ego_vx_l.append(float(ego_vx))
        ego_curvature_l.append(float(ego_curvature))
        prekingpin_x_l.append(float(prekingpin_x))
        prekingpin_y_l.append(float(prekingpin_y))
        prekingpin_yaw_l.append(float(prekingpin_yaw))
        kingpin_x_l.append(float(kingpin_x))
        kingpin_y_l.append(float(kingpin_y))
        kingpin_yaw_l.append(float(kingpin_yaw))
        dis_error_trajectory_l.append(float(dis_error_trajectory))
        yaw_error_trajectory_l.append(float(yaw_error_trajectory))
        dis_error_trajectory_goal_l.append(float(dis_error_trajectory_goal))
        yaw_error_trajectory_goal_l.append(float(yaw_error_trajectory_goal))
        dis_error_prekingpin_l.append(float(dis_error_prekingpin))
        yaw_error_prekingpin_l.append(float(yaw_error_prekingpin))
        dis_error_kingpin_l.append(float(dis_error_kingpin))
        yaw_error_kingpin_l.append(float(yaw_error_kingpin))

        if j==100:

            for i,col in enumerate(row):
                if col == "|":
                    trajectory_delimiter.append(i+1)
            
            trajectory_h_l = row[trajectory_delimiter[0]:trajectory_delimiter[1]]
            trajectory23_h_l = row[trajectory_delimiter[1]:len(row)]

            for i in np.arange(0,len(trajectory_h_l)-1,8):
                trajectory_t.append(i)
                trajectory_s.append(i+1)
                trajectory_x.append(i+2)
                trajectory_y.append(i+3)
                trajectory_vx.append(i+4)
                trajectory_ax.append(i+5)
                trajectory_yaw.append(i+6)
                trajectory_curvature.append(i+7)
        
        
            

bird_figure, bird_axis = plt.subplots()
bird_axis.grid()
bird_axis.plot(trajectory_s, trajectory_vx)
#bird_axis.set_aspect('equal','datalim')

plt.show()



