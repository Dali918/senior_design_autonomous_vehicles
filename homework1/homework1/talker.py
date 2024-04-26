import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter

from std_msgs.msg import String


class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.line_generator = self.read_lines_from_file()

    def read_lines_from_file(self):
        with open(self.file_path, 'r') as file:
            for line in file:
                yield line.strip()

    def get_next_line(self):
        try:
            return next(self.line_generator)
        except StopIteration:
            return "end of file!"

class MinimalPublisher(Node):
    def __init__(self, file_path):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String,'topic',10)
        timer_period = 0.5  # seconds
        self.file_reader = FileReader(file_path)
        self.timer = self.create_timer(timer_period, self.callback)
        self.t=0


    def callback(self):
        msg = String()
        msg.data = self.file_reader.get_next_line()
        self.publisher_.publish(msg)
        self.get_logger().info('Published: "%s"' % msg.data)
        self.t +=1

def main(args=None):
    rclpy.init(args=args)
    file_path = '/home/dalitso//ros2_edu/src/homework1/homework1/succession_script.txt'
    minimal_publisher = MinimalPublisher(file_path)

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()



