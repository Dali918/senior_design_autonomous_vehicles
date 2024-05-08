import os 
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import Command
from launch_ros.actions import Node

def generate_launch_description():
    use_sim_time = True
    package_directory = get_package_share_directory('homework3')
    # path of urdf file
    robot_description_path = os.path.join(package_directory, 'urdf', 'robot.urdf')
    
    #Run robot state publisher
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        emulate_tty=True,
        parameters=[{'use_sim_time': use_sim_time, 'robot_description': Command(['xacro ', robot_description_path])}]
    )

    # Run joint state publisher
    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        output='screen',
        emulate_tty=True,
        name= 'joint_state_publisher'
    )

    # Run Rviz2
    rviz2_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2_node',
        output='screen',
        emulate_tty=True,
        parameters=[{
            'use_sim_time': use_sim_time,
            }]
    )

    return LaunchDescription(
        [
        robot_state_publisher_node,
        joint_state_publisher_node,
        rviz2_node
        ]
    )




