import os
import random

print(len(os.listdir('/home/software/mehul/cartisan_ikea/lamp/train_data')))

while len(os.listdir('/home/software/mehul/cartisan_ikea/lamp/train_data')) > 500:
	os.remove('/home/software/mehul/cartisan_ikea/lamp/train_data/'+ os.listdir('/home/software/mehul/cartisan_ikea/lamp/train_data/')[random.randint(0,500)])
