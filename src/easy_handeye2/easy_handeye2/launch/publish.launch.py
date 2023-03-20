from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import Node
from launch.substitutions import TextSubstitution

def generate_launch_description():
    arg_name = DeclareLaunchArgument('name', default_value=TextSubstitution(text="TM"))

    handeye_publisher = Node(package='easy_handeye2', executable='handeye_publisher', name='handeye_publisher', parameters=[{
        'name': LaunchConfiguration('name'),
    }])

    return LaunchDescription([
        arg_name,
        handeye_publisher,
    ])
