import tensorflow as tf

print("CPU's:", tf.config.list_physical_devices('CPU'))
print("GPU's:", tf.config.list_physical_devices('GPU'))
print("GPU Available:", tf.test.is_gpu_available())
print("GPU Support:", tf.test.is_built_with_gpu_support())
print("CUDA Support:", tf.test.is_built_with_cuda())
