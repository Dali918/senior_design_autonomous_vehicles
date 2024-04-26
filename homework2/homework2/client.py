import sys
import rclpy

from rclpy.node import Node
from std_srvs.srv import SetBool

class Client(Node):
    def __init__(self):
        super().__init__("client")
        self.cli = self.create_client(SetBool, "navigate")
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

        self.req = SetBool.Request()

    def send_request(self, bool):
        self.req.data = bool
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)

        try:
            response = self.future.result()
            if response.success:
                self.get_logger().info("Result: {}".format(response.message))
            else:
                self.get_logger().info("Service call failed %r" % (response.message,))
        except Exception as e:
            self.get_logger().info("Service call failed %r" % (e,))

    
    def callback(self, future):
        try:
            response = future.result()
            if response.success:
                self.get_logger().info("Result: {}".format(response.message))
            else:
                self.get_logger().info("Service call failed %r" % (response.message,))
        except Exception as e:
            self.get_logger().info("Service call failed %r" % (e,))


def main(args=None):
    rclpy.init(args=args)
    client = Client()
    client.get_logger().info("input 1 to turn on, 0 to turn off, q to quit")

    while True:
        user_input = input("Input 1 to turn on, 0 to turn off, q to quit: ")
        if user_input == 'q':
            break
        elif user_input in ['1', '0']:
            client.send_request(bool(int(user_input)))
        else:
            print("Invalid input. Please enter 1, 0, or q.")


    client.destroy_node()   
    rclpy.shutdown()

if __name__ == "__main__":
    main()

    