import sys
import rclpy

from rclpy.node import Node
from std_srvs.srv import SetBool

class Client(Node):
    def __init__(self):
        super().__init__("client")
        self.client = self.create_client(SetBool, "navigate")
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

        self.req = SetBool.Request()

    def send_request(self, bool):
        self.req.data = bool
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()
    
def main():
    rclpy.init()
    client = Client()
    client.get_logger().info("input 1 to turn on, 0 to turn off, q to quit")

    while sys.argv[1]!='q':
        if sys.argv[1]=='1':
            response = client.send_request(True)
        else:
            response = Client.send_request(False)
        client.get_logger().info("sent:{} \t result:{}".format(sys.argv[1], response.message))
    
    client.destroy_node()   
    rclpy.shutdown()

if __name__ == "__main__":
    main()

    