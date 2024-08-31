# Pcd2Google-map
This repository is for utilities related to visualization for RTS-SLAM.
A utility for mapping SLAM-generated point clouds onto Google Maps using latitude and longitude information.

<div align="center">
<image src="assets/map.png" />
</div>
  
### Contact
If you have any questions, please let me know: 
- Shuang Song {songs@stu.xmu.edu.cn}

#### Requirements
This code has been tested on:
- Python 3.10.13, ROS melodic,folium 0.16.0,pyqt5 5.15.9,open3d 0.18.0,opencv-python  4.9.0.80

#### Datasets and Software
We implement rostopic in the gpsshowmap.py file to read IMU and RTK trajectories, mapping the trajectories to Google Maps. Then the point cloud is implemented on the open Google map for mapping.
For ease of use, we have integrated image reading, point cloud file reading and mapping into one software, the download link is below: 

Username: sam, Password:123
The rosbag for testing is available in the RTS-SLAM repository.
