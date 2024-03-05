import cv2
import os

ski_cap = cv2.VideoCapture("/Users/yunji/PycharmProjects/INF8770 TP3/Videos/ski_cross.mp4")
snow_cap = cv2.VideoCapture("/Users/yunji/PycharmProjects/INF8770 TP3/Videos/slopestyle.mp4")
gym_cap = cv2.VideoCapture("/Users/yunji/PycharmProjects/INF8770 TP3/Videos/gymnastique.mp4")

try:
    if not os.path.exists('Images/Ski'):
        os.makedirs('Images/Ski')
    if not os.path.exists('Images/Snow'):
        os.makedirs('Images/Snow')
    if not os.path.exists('Images/Gym'):
        os.makedirs('Images/Gym')

except OSError:
    print('Error : Creating directory for Images')

currentframe = 1

print('------------------- Creating frames for Gym -------------------\n')
while True:
    ret, frame = gym_cap.read()

    if ret:
        name = './Images/Gym/frame' + str(currentframe) + '.jpg'
        print('Creating...' + name)

        cv2.imwrite(name, frame)
        currentframe += 1
    else:
        break

currentframe = 1

print('------------------- Creating frames for Ski -------------------\n')
while True:
    ret, frame = ski_cap.read()

    if ret:
        name = './Images/Ski/frame' + str(currentframe) + '.jpg'
        print('Creating...' + name)

        cv2.imwrite(name, frame)
        currentframe += 1
    else:
        break

currentframe = 1

print('------------------- Creating frames for Snow ------------------\n')
while True:
    ret, frame = snow_cap.read()

    if ret:
        name = './Images/Snow/frame' + str(currentframe) + '.jpg'
        print('Creating...' + name)

        cv2.imwrite(name, frame)
        currentframe += 1
    else:
        break

ski_cap.release()
cv2.destroyAllWindows()
