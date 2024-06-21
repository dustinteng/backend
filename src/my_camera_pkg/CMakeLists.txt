cmake_minimum_required(VERSION 3.5)
project(my_camera_pkg)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

# Find required packages
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(image_transport REQUIRED)
find_package(cv_bridge REQUIRED)
find_package(OpenCV REQUIRED)  # Add this line

# Declare a C++ executable
add_executable(camera_node src/camera_node.cpp)

# Specify libraries to link a library or executable target against
ament_target_dependencies(camera_node rclcpp sensor_msgs image_transport cv_bridge)
target_link_libraries(camera_node ${OpenCV_LIBS})  # Add this line

# Install targets
install(TARGETS
  camera_node
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
