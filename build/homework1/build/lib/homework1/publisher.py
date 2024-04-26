import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class Publisher(Node):
    def __init__(self):
        super().__init__("publisher")
        self.publisher = self.create_publisher(Int32,'publisher_topic',10)
        timer_period = 0.5#seconds
        self.timer = self.create_timer(timer_period, self.callback)
        self.count = 0

    def callback(self):
        msg = Int32()
        msg.data = self.count
        self.publisher.publish(msg)
        self.get_logger().info('Published: {}'.format(msg.data))
        self.count += 1

def main(args=None):
    rclpy.init(args=args)
    publisher = Publisher()
    rclpy.spin(publisher)
    publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()