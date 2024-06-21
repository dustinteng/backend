#include "rclcpp/rclcpp.hpp"
#include "sensor_msgs/msg/image.hpp"
#include "cv_bridge/cv_bridge.h"
#include <opencv2/opencv.hpp>

class CameraNode : public rclcpp::Node {
public:
    CameraNode() : Node("camera_node") {
        // Initialize the camera using the Video for Linux 2 (V4L2) backend.
        if (!capture_.open(0, cv::CAP_V4L2)) {
            RCLCPP_FATAL(this->get_logger(), "Failed to open camera with V4L2 backend");
            rclcpp::shutdown();
        }
    }

    ~CameraNode() {
        capture_.release();  // Ensure capture device is closed properly
    }

    void publish_image() {
        cv::Mat frame;
        if (capture_.read(frame)) { // Check if frame is read correctly
            auto message = cv_bridge::CvImage(std_msgs::msg::Header(), "bgr8", frame).toImageMsg();
            RCLCPP_INFO(this->get_logger(), "Publishing image");
        } else {
            RCLCPP_WARN(this->get_logger(), "Failed to capture image");
        }
    }

private:
    cv::VideoCapture capture_;  // Declaration of the VideoCapture object
};

int main(int argc, char** argv) {
    rclcpp::init(argc, argv);
    auto node = std::make_shared<CameraNode>();
    rclcpp::Rate rate(10); // Set rate in Hz
    while (rclcpp::ok()) {
        node->publish_image();
        rclcpp::spin_some(node);
        rate.sleep();
    }
    rclcpp::shutdown();
    return 0;
}
