# open
- TM
```
ros2 launch tm_driver tm5-900_bringup.launch.py
```
- realsense
```
ros2 launch realsense2_camera rs_launch.py
```
- apriltag_ros
```
ros2 launch apriltag_ros tag_realsense.launch.py
```
- easy handeye
```
ros2 launch easy_handeye2 calibrate.launch.py
```

# colcon build command
```
colcon build --allow-overriding cv_bridge image_geometry
```
why? because package cv_bridge and image_geometry in /opt/foxy is not good, need override