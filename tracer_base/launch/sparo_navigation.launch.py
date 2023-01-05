import os

from ament_index_python.packages import get_package_share_directory
import launch
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    
    tracer_base_dir = get_package_share_directory('tracer_base')
    tracer_navigation2_dir = get_package_share_directory('tracer_navigation2')

    declare_tracer = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(tracer_base_dir, 'launch', 'sparo.launch.py'))
    )

    declare_nav = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(tracer_navigation2_dir, 'launch', 'navigation2.launch.py'))
    )
    
    ld.add_action(declare_tracer)
    ld.add_action(declare_nav)

    return ld