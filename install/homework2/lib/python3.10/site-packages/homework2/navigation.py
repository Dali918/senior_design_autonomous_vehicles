import rclpy

from rclpy.node import Node
from std_srvs.srv import SetBool


class Navigation(Node):
    def __init__(self):
        super().__init__("navigation")
        self.srv = self.create_service(SetBool, "toggle_navigate", self.toggle_navigate)

    def toggle_navigate(self, request, response):
       if request.data:
        response.message = "Turning the navigation system on!"
        response.success = True
       else:
        response.message = "Turning the navigation system off!"
        response.success = True

       self.get_logger().info("Requested: {}".format(request.data))
       self.get_logger().info("Response: {}".format(response.message))

       return response

if __name__ == "__main__":
    rclpy.init()
    navigation = Navigation()
    rclpy.spin(navigation)
    navigation.destroy_node()
    rclpy.shutdown()