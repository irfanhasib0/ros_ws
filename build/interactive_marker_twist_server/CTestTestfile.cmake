# CMake generated Testfile for 
# Source directory: /home/irfan/Desktop/ros_ws/src/interactive_marker_twist_server
# Build directory: /home/irfan/Desktop/ros_ws/build/interactive_marker_twist_server
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_interactive_marker_twist_server_roslaunch-check_launch_interactive_markers.launch "/home/irfan/Desktop/ros_ws/build/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/irfan/Desktop/ros_ws/build/test_results/interactive_marker_twist_server/roslaunch-check_launch_interactive_markers.launch.xml" "--return-code" "/usr/bin/cmake -E make_directory /home/irfan/Desktop/ros_ws/build/test_results/interactive_marker_twist_server" "/opt/ros/melodic/share/roslaunch/cmake/../scripts/roslaunch-check -o '/home/irfan/Desktop/ros_ws/build/test_results/interactive_marker_twist_server/roslaunch-check_launch_interactive_markers.launch.xml' '/home/irfan/Desktop/ros_ws/src/interactive_marker_twist_server/launch/interactive_markers.launch' ")
add_test(_ctest_interactive_marker_twist_server_roslint_package "/home/irfan/Desktop/ros_ws/build/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/irfan/Desktop/ros_ws/build/test_results/interactive_marker_twist_server/roslint-interactive_marker_twist_server.xml" "--working-dir" "/home/irfan/Desktop/ros_ws/build/interactive_marker_twist_server" "--return-code" "/opt/ros/melodic/share/roslint/cmake/../../../lib/roslint/test_wrapper /home/irfan/Desktop/ros_ws/build/test_results/interactive_marker_twist_server/roslint-interactive_marker_twist_server.xml make roslint_interactive_marker_twist_server")