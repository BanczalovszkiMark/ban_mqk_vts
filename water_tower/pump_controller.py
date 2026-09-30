import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from std_msgs.msg import Bool


class PumpController(Node):

    def __init__(self):
        super().__init__('pump_controller')

        self.pumpOn = False

        self.publisher = self.create_publisher(
            Bool,
            '/pump_command',
            10
        )

        self.subscription = self.create_subscription(
            Float32,
            '/water_level',
            self.water_level_callback,
            10
        )

    def water_level_callback(self, msg):

        waterLevel = msg.data

        if waterLevel < 30.0:
            self.pumpOn = True

        elif waterLevel > 80.0:
            self.pumpOn = False

        pumpMsg = Bool()
        pumpMsg.data = self.pumpOn

        self.publisher.publish(pumpMsg)

        self.get_logger().info(
            f'Water level: {waterLevel:.1f}% '
            f'Pump: {"ON" if self.pumpOn else "OFF"}'
        )


def main(args=None):
    rclpy.init(args=args)

    node = PumpController()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()