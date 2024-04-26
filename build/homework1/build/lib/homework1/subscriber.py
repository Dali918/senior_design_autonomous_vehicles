import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class Subscriber(Node):
    def __init__(self):
        super().__init__("subscriber")
        self.subscription = self.create_subscription(
            Int32, 
            "publisher_topic", 
            self.subscription_callback, 
            10
        )

    def subscription_callback(self, msg):
        heard = msg.data
        found = heard * 2
        self.get_logger().info("I heard: {} and found: {}".format(heard,found))

def main(args=None):
    rclpy.init(args=args)
    subscriber = Subscriber()
    rclpy.spin(subscriber)
    subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()