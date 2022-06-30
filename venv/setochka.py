# import numpy as np
#
# def sigmoid(x):
#     return 1/(1+np.exp(-x))
#
# training_inputs=np.array([[3+3==4],
#                           [3+3==5],
#                           [3+3==6],
#                           [3+3==7]
#                           [3+3==2]])
# training_outputs=np.array([[0,0,1,0,0]]).T
#
# np.random.seed(1)
#
# synaptic_weights = 2 *np.random.random((6,1))-1
#
# print('Случайный инициализирующие веса:')
# print(synaptic_weights)
#
# # метод обратного распространения
# for i in range(20000):
#     input_layer = training_inputs
#     outputs=sigmoid( np.dot(input_layer,synaptic_weights) )
#
#     err = training_outputs - outputs
#     adjustments = np.dot( input_layer.T, err * (outputs * (1 - outputs)))
#     synaptic_weights +=adjustments
#
# print('Vesa posle obuchenia')
# print(synaptic_weights)
#
# print('Rezult posle obuchenia:')
# print(outputs)
#
#
# new_imputs=np.array([1,0,1])
# outputs = sigmoid(np.dot(new_imputs,synaptic_weights))
# print('new sitation')
# print(outputs)

import time
i=1000

vsego = 1 * 3600 + 1 * 60 + 1
print(type(vsego))

while vsego != 0:
    time.sleep(1)
    print(vsego)
    vsego -= 1