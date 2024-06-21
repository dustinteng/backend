import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

class PS5Controller(Node):
    def __init__(self):
        super().__init__('ps5_controller')
        self.subscription = self.create_subscription(
            Joy,
            '/joy',
            self.joy_callback,
            10)
        self.publisher_ = self.create_publisher(Twist, '/ps5_controller/cmd_vel', 10)

    def joy_callback(self, msg):
        twist = Twist()
        twist.linear.x = msg.axes[1]  # Assuming left stick's vertical axis for linear x
        twist.angular.z = msg.axes[0]  # Assuming left stick's horizontal axis for angular z
        self.publisher_.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    ps5_controller = PS5Controller()
    rclpy.spin(ps5_controller)
    ps5_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
