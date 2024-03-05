import cv2
import os
import matplotlib.pyplot as plt
import time
# Calcul du nombre d'images pour chaque video
ski_nb_frames = os.listdir("/Users/yunji/PycharmProjects/INF8770 TP3/Images/Ski")
snow_nb_frames = os.listdir("/Users/yunji/PycharmProjects/INF8770 TP3/Images/Snow")
gym_nb_frames = os.listdir("/Users/yunji/PycharmProjects/INF8770 TP3/Images/Gym")

# Declaration des variables pour les images
list_ski_frames = []
conv_ski_frames = []
hist_ski_frames = []
corr_ski_frames = []
eucl_ski_frames = []

length = len(ski_nb_frames)

start_time = time.time()
# Lecture et conversion des images
for i in range(length - 1):
    name = '/Images/SKi/frame' + str(i+1) + '.jpg'
    print('Reading...' + name)
    list_ski_frames.append(cv2.imread('/Users/yunji/PycharmProjects/INF8770 TP3' + name))
    conv_ski_frames.append(cv2.cvtColor(list_ski_frames[i], cv2.COLOR_BGR2GRAY))


# Creation des histogrammes
for i in range(length - 1):
    print('Creating.../Images/Ski/hist' + str(i))
    hist_ski_frames.append(cv2.calcHist([conv_ski_frames[i]], [0], None, [256], [0, 256]))
    #cv2.normalize(hist_ski_frames[i], hist_ski_frames[i], alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

# Convertion des histogrammes
for i in range(length - 2):
    corr_ski_frames.append(cv2.compareHist(hist_ski_frames[i], hist_ski_frames[i+1], cv2.HISTCMP_CORREL))
    eucl_ski_frames.append(cv2.norm(hist_ski_frames[i], hist_ski_frames[i+1], normType=cv2.NORM_L2))
end_time = time.time()
execution_time = end_time - start_time
print('Execution time : ' + str(execution_time))

# Creation des valeurs pour l'axe des x
x = list(range(len(eucl_ski_frames)))

# Creation de l'histogramme
plt.bar(x, eucl_ski_frames)
plt.ylim(0, 300000)
plt.title('Decomposition par histogramme pour le vidéo de Gym')
plt.xlabel('Trames')
plt.ylabel('Difference')
plt.show()



