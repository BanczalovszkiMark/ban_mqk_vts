import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class WaterLevelNode(Node):

    def __init__(self):
        super().__init__('water_level_node')

        self.waterLevel = 50.0

        self.publisher = self.create_publisher(
            Float32,
            '/water_level',
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.update_water_level
        )

    def update_water_level(self):
        self.waterLevel -= 1.0

        if self.waterLevel < 0.0:
            self.waterLevel = 0.0

        msg = Float32()
        msg.data = self.waterLevel

        self.publisher.publish(msg)

        self.get_logger().info(
            f'Water level: {self.waterLevel:.1f}%'
        )


def main(args=None):
    rclpy.init(args=args)

    node = WaterLevelNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()