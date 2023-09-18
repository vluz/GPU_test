import tensorflow as tf


tf.get_logger().setLevel('ERROR')
print("GPU is available  : ",tf.test.is_gpu_available())
print("Device info       : ",tf.config.list_physical_devices('GPU'))