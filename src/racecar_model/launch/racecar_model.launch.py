from distutils.cmd import Command
import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    
    path_to_launch_dir = os.path.dirname(os.path.realpath(__file__))
    path_to_ego = os.path.join(path_to_launch_dir, '../ego_racecar.xacro')
    path_to_opp = os.path.join(path_to_launch_dir, '../opp_racecar.xacro')

    return LaunchDescription([
        
        # Arguments for ego racecar
        DeclareLaunchArgument(
            'ego_racecar_xacro',
            default_value = path_to_ego,
            description = 'Path to the ego racecar xacro file'
        ),
        
        # Arguments for opponent racecar
        DeclareLaunchArgument(
            'opp_racecar_xacro',
            default_value = path_to_opp,
            description = 'Path to the opponent racecar xacro file'
        ),
        
        # Group for ego racecar
        GroupAction([
            Node(
                package='robot_state_publisher',
                executable='robot_state_publisher',
                namespace='ego_racecar',
                output='screen',
                parameters=[{
                    'tf_prefix': 'ego_racecar',
                    'robot_description': Command(['xacro ', LaunchConfiguration('ego_racecar_xacro')])
                }]
            )
        ]),
        
        # Group for opponent racecar
        GroupAction([
            Node(
                package='robot_state_publisher',
                executable='robot_state_publisher',
                namespace='opp_racecar',
                output='screen',
                parameters=[{
                    'tf_prefix': 'opp_racecar',
                    'robot_description': Command(['xacro ', LaunchConfiguration('opp_racecar_xacro')])
                }]
            )
        ]),
    ])
