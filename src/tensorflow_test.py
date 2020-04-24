import tensorflow as tf
from time import sleep
from datetime import datetime

import os

force_cpu = False

if force_cpu:
    os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

print("CPU's:", tf.config.list_physical_devices('CPU'))
print("GPU's:", tf.config.list_physical_devices('GPU'))
print("GPU Available:", tf.test.is_gpu_available())
print("GPU Support:", tf.test.is_built_with_gpu_support())
print("CUDA Support:", tf.test.is_built_with_cuda())

import sound_predictor


usl = "../resources/UrbanSound8K/"
filename = usl + 'audio/fold5/100852-0-0-0.wav'

sound_predictor.load_sound_model('sound_category_model.h5')
start = datetime.now()
for i in range(0, 100):
    sound_predictor.prediction(filename, True)
duration = datetime.now() - start
print("Test 100: ", duration)

sleep(5)
