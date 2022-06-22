cmake_minimum_required(VERSION 3.0.2)
project(smart_python_ros_node)


find_package(catkin REQUIRED COMPONENTS
  dynamic_reconfigure
  message_generation
  rospy
  std_msgs
)

catkin_python_setup()

add_message_files(
  FILES
  smartCommonData.msg
)

generate_messages(
  DEPENDENCIES 
  std_msgs
)

generate_dynamic_reconfigure_options(
  cfg/smartCommon.cfg 
)

catkin_package(
  INCLUDE_DIRS
  LIBRARIES ${PROJECT_NAME}
  CATKIN_DEPENDS rospy std_msgs dynamic_reconfigure message_runtime 
  DEPENDS
)

###########
## Build ##
###########

include_directories(
  ${catkin_INCLUDE_DIRS}
)

#############
## Install ##
#############

# Install launch files
install(
  DIRECTORY launch cfg
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)