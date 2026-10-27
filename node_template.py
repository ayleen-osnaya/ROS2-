import rclpy
from rclpy.node import Node

class Generic(Node): # <--- replace with your desired class name
    def __init__(self):
        super().__init__('node_name') # <--- replace with your desired node name
        self.get_logger().info('Node has been started.')


def main(args=None):
    rclpy.init(args=args) # <--- initialize ROS 2 communication
    generic_node = Generic() # <--- replace with your desired class name
    rclpy.spin(generic_node) # <--- keep the node running until interrupted
    generic_node.destroy_node() # <--- clean up and destroy the node
    rclpy.shutdown() # <--- shut down ROS 2 communication

if __name__ == '__main__':
    main()