import numpy as np
import cv2
import os
import matplotlib.pyplot as plt
import time

# Calcul du nombre d'images par video
ski_nb_frames = os.listdir("/Users/yunji/PycharmProjects/INF8770 TP3/Images/Ski")
snow_nb_frames = os.listdir("/Users/yunji/PycharmProjects/INF8770 TP3/Images/Snow")
gym_nb_frames = os.listdir("/Users/yunji/PycharmProjects/INF8770 TP3/Images/Gym")

# Declaration des variables pour les images
list_ski_frames = []
conv_ski_frames = []
blur_ski_frames = []
edge_ski_frames = []
dila_ski_frames = []

edge_norm = []
dila_norm = []
dilate_rate = 3
safe_div = lambda x, y: 0 if y == 0 else x / y

length = len(ski_nb_frames)

# Lecture des images
for i in range(length - 1):
    name = '/Images/Ski/frame' + str(i + 1) + '.jpg'
    print('Reading...' + name)
    list_ski_frames.append(cv2.imread('/Users/yunji/PycharmProjects/INF8770 TP3' + name))

start_time = time.time()
# Operations sur les images
for i in range(length - 1):
    print('Creating.../Images/Ski/edge' + str(i))
    conv_ski_frames.append(cv2.cvtColor(list_ski_frames[i], cv2.COLOR_BGR2GRAY))
    blur_ski_frames.append(cv2.GaussianBlur(conv_ski_frames[i], (3, 3), 0))
    edge_ski_frames.append(cv2.Canny(blur_ski_frames[i], 100, 200))
    dila_ski_frames.append(cv2.dilate(edge_ski_frames[i], np.ones((dilate_rate, dilate_rate))))

for i in range(length - 1):
    edge_norm.append((edge_ski_frames[i].astype('float32') / 255).astype('uint8'))
    dila_norm.append((dila_ski_frames[i].astype('float32') / 255).astype('uint8'))

diff = []

for i in range(length - 2):
    pin = 1 - np.sum(cv2.bitwise_and(dila_norm[i], edge_norm[i + 1]))/np.sum(edge_norm[i + 1])
    pout = 1 - np.sum(cv2.bitwise_and(edge_norm[i], dila_norm[i + 1]))/np.sum(edge_norm[i])

    diff.append(max(pin, pout))

    print('Frame ' + str(i) + ' : ' + str(diff[i]))

end_time = time.time()

execution_time = end_time - start_time
print('Execution time : ' + str(execution_time))

# Creation des valeurs pour l'axe des x
x = list(range(len(diff)))

# Creation de l'histogramme
plt.bar(x, diff)
plt.title('Decomposition par aretes pour le video de Ski')
plt.xlabel('Trames')
plt.ylabel('Difference')
plt.show()


#print(coupure)

cv2.destroyAllWindows()
