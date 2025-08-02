Model: "vgg16"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
input_1 (InputLayer)         [(None, 150, 150, 3)]     0         
_________________________________________________________________
block1_conv1 (Conv2D)        (None, 150, 150, 64)      1792      
_________________________________________________________________
block1_conv2 (Conv2D)        (None, 150, 150, 64)      36928     
_________________________________________________________________
block1_pool (MaxPooling2D)   (None, 75, 75, 64)        0         
_________________________________________________________________
block2_conv1 (Conv2D)        (None, 75, 75, 128)       73856     
_________________________________________________________________
block2_conv2 (Conv2D)        (None, 75, 75, 128)       147584    
_________________________________________________________________
block2_pool (MaxPooling2D)   (None, 37, 37, 128)       0         
_________________________________________________________________
block3_conv1 (Conv2D)        (None, 37, 37, 256)       295168    
_________________________________________________________________
block3_conv2 (Conv2D)        (None, 37, 37, 256)       590080    
_________________________________________________________________
block3_conv3 (Conv2D)        (None, 37, 37, 256)       590080    
_________________________________________________________________
block3_pool (MaxPooling2D)   (None, 18, 18, 256)       0         
...
Total params: 14,714,688
Trainable params: 14,714,688
Non-trainable params: 0
_________________________________________________________________
Output is truncated. View as a scrollable element or open in a text editor. Adjust cell output settings...
/usr/local/lib/python3.6/dist-packages/ipykernel_launcher.py:3: FutureWarning: Passing a negative integer is deprecated in version 1.0 and will not be supported in future version. Instead, use None to not limit the column width.
  This is separate from the ipykernel package so we can avoid doing imports until
Layer Type	Layer Name	Layer Trainable
0	<tensorflow.python.keras.engine.input_layer.InputLayer object at 0x7f04bdef4550>	input_1	False
1	<tensorflow.python.keras.layers.convolutional.Conv2D object at 0x7f04bd61b710>	block1_conv1	False
2	<tensorflow.python.keras.layers.convolutional.Conv2D object at 0x7f04bd4244a8>	block1_conv2	False
3	<tensorflow.python.keras.layers.pooling.MaxPooling2D object at 0x7f04bd5dba90>	block1_pool	False
4	<tensorflow.python.keras.layers.convolutional.Conv2D object at 0x7f04bd5e0b38>	block2_conv1	False
5	<tensorflow.python.keras.layers.convolutional.Conv2D object at 0x7f04bd5dbc88>	block2_conv2	False
6	<tensorflow.python.keras.layers.pooling.MaxPooling2D object at 0x7f04bd5e7cc0>	block2_pool	False
7	<tensorflow.python.keras.layers.convolutional.Conv2D object at 0x7f04bd5eddd8>	block3_conv1	False
8	<tensorflow.python.keras.layers.convolutional.Conv2D object at 0x7f04bd5f9518>	block3_conv2	False
9	<tensorflow.python.keras.layers.convolutional.Conv2D object at 0x7f04bd5f96d8>	block3_conv3	False
10	<tensorflow.python.keras.layers.pooling.MaxPooling2D object at 0x7f04bd5ffeb8>	block3_pool	False
11	<tensorflow.python.keras.layers.convolutional.Conv2D object at 0x7f04bd609b70>	block4_conv1	False
12	<tensorflow.python.keras.layers.convolutional.Conv2D object at 0x7f04bd5ff1d0>	block4_conv2	False
13	<tensorflow.python.keras.layers.convolutional.Conv2D object at 0x7f04bd60ee48>	block4_conv3	False
14	<tensorflow.python.keras.layers.pooling.MaxPooling2D object at 0x7f04bd4a3550>	block4_pool	False
15	<tensorflow.python.keras.layers.convolutional.Conv2D object at 0x7f04bd4bd4a8>	block5_conv1	False
16	<tensorflow.python.keras.layers.convolutional.Conv2D object at 0x7f04bd4a3cc0>	block5_conv2	False
17	<tensorflow.python.keras.layers.convolutional.Conv2D object at 0x7f04bd4bdf28>	block5_conv3	False
18	<tensorflow.python.keras.layers.pooling.MaxPooling2D object at 0x7f04bd4c72e8>	block5_pool	False
Epoch 1/5
503/503 [==============================] - 47s 94ms/step - loss: 0.1576 - accuracy: 0.9613 - val_loss: 0.3448 - val_accuracy: 0.8846
Epoch 2/5
503/503 [==============================] - 48s 95ms/step - loss: 0.1565 - accuracy: 0.9607 - val_loss: 0.3418 - val_accuracy: 0.8870
Epoch 3/5
503/503 [==============================] - 47s 94ms/step - loss: 0.1553 - accuracy: 0.9615 - val_loss: 0.3430 - val_accuracy: 0.8851
Epoch 4/5
503/503 [==============================] - 48s 95ms/step - loss: 0.1540 - accuracy: 0.9608 - val_loss: 0.3433 - val_accuracy: 0.8876
Epoch 5/5
503/503 [==============================] - 48s 95ms/step - loss: 0.1533 - accuracy: 0.9623 - val_loss: 0.3419 - val_accuracy: 0.8859
<tensorflow.python.keras.callbacks.History at 0x7f016537b898>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
<Figure size 432x288 with 1 Axes>
