#!/usr/bin/env python3
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, ThisLaunchFileDir

def generate_launch_description():
    lidar_dir = get_package_share_directory('sllidar_ros2')
    mycam2image_dir = get_package_share_directory('mycam2image')
    description_dir = get_package_share_directory('tracer_description')
    aruco_dir = get_package_share_directory('ros2_aruco')

    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    ld = LaunchDescription()

    declare_tracer = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([ThisLaunchFileDir(), '/tracer_base.launch.py'])
    )

    declare_description = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(description_dir, 'launch', 'tracer_state_publisher.launch.py'))
    )

    declare_lidar = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(lidar_dir, 'launch', 'sllidar_s2_launch.py'))
    )

    # declare_cam = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource(os.path.join(mycam2image_dir, 'launch', 'cam2image.launch.py'))
    # )
    declare_cam = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(get_package_share_directory('usb_cam'), 'launch', 'demo_launch.py'))
    )


    declare_aruco = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(aruco_dir, 'launch', 'aruco.launch.py'))
    )

    ld.add_action(declare_tracer)
    ld.add_action(declare_description)
    ld.add_action(declare_lidar)
    ld.add_action(declare_cam)
    # ld.add_action(declare_aruco)

    return ld
