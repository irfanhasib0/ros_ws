# CMake generated Testfile for 
# Source directory: /home/irfan/Desktop/ros_ws/src/unique_identifier/unique_id/tests
# Build directory: /home/irfan/Desktop/ros_ws/build/unique_identifier/unique_id/tests
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_unique_id_gtest_test_unique_id "/home/irfan/Desktop/ros_ws/build/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/irfan/Desktop/ros_ws/build/test_results/unique_id/gtest-test_unique_id.xml" "--return-code" "/home/irfan/Desktop/ros_ws/devel/lib/unique_id/test_unique_id --gtest_output=xml:/home/irfan/Desktop/ros_ws/build/test_results/unique_id/gtest-test_unique_id.xml")
add_test(_ctest_unique_id_nosetests_test_unique_id.py "/home/irfan/Desktop/ros_ws/build/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/irfan/Desktop/ros_ws/build/test_results/unique_id/nosetests-test_unique_id.py.xml" "--return-code" "\"/usr/bin/cmake\" -E make_directory /home/irfan/Desktop/ros_ws/build/test_results/unique_id" "/usr/bin/nosetests-2.7 -P --process-timeout=60 /home/irfan/Desktop/ros_ws/src/unique_identifier/unique_id/tests/test_unique_id.py --with-xunit --xunit-file=/home/irfan/Desktop/ros_ws/build/test_results/unique_id/nosetests-test_unique_id.py.xml")
