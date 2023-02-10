#!/usr/bin/env python
import rospy, rosbag
from tf.transformations import quaternion_matrix
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-b", "--bag_file", help = "Give the bag file path")
args = parser.parse_args()

#Take the bagfile path
input_bagfile = args.bag_file

#Store the bias, features, translation and time 
accbias = []
gyrobias = []
features = []
translation = []
z_translation = []

#Read the param values from the bag file
with rosbag.Bag(input_bagfile, 'r') as bagfile:
	for topic, msg, t in bagfile:
		if topic == "/vins_estimator/acc_bias":
			accbias.append([msg.data, t])
		if topic == "/vins_estimator/gyro_bias":
			gyrobias.append([msg.data, t])
		if topic == "/vins_estimator/translation":
			translation.append([msg.data, t])
		if topic == "/vins_estimator/z_translation":
			z_translation.append([msg.data, t])
		if topic == "/vins_estimator/features_detected":
			features.append([msg.data, t])


#Statistics of the params 
print("Len of accbias ", len(accbias))
print("Len of gyrobias", len(gyrobias))
print("Len of features", len(features))
print("Len of translation", len(translation))
print("Len of z_translation", len(z_translation))


#Acceleration bias 
acc = []
t_acc = []

#Convert the ROS time to seconds 
for i in accbias:
	acc.append(i[0])
	t_acc.append(i[1].to_sec())

acc_start_time = t_acc[0]

for i in range(len(t_acc)):
	t_acc[i] = t_acc[i] - acc_start_time


plt.plot(t_acc, acc)
plt.title("Acceleration bias vs Time")
plt.xlabel("Time in sec")
plt.ylabel("Acceleration bias")
plt.show()

#Acceleration bias 
gyro = []
t_gyro = []

#Convert the ROS time to seconds 
for i in gyrobias:
	gyro.append(i[0])
	t_gyro.append(i[1].to_sec())

gyro_start_time = t_gyro[0]

for i in range(len(t_gyro)):
	t_gyro[i] = t_gyro[i] - gyro_start_time

plt.plot(t_gyro, gyro)
plt.title("Gyro bias vs Time")
plt.xlabel("Time in sec")
plt.ylabel("Gyro bias")
plt.show()

#Translation
tran = []
t_tran = []

#Convert the ROS time to seconds 
for i in translation:
	tran.append(i[0])
	t_tran.append(i[1].to_sec())

translation_start_time = t_tran[0]

for i in range(len(t_tran)):
	t_tran[i] = t_tran[i] - translation_start_time

plt.plot(t_tran, tran)
plt.title("Translation vs Time")
plt.xlabel("Time in sec")
plt.ylabel("Translation")
plt.show()

#Z Translation
ztran = []
t_ztran = []

#Convert the ROS time to seconds 
for i in z_translation:
	ztran.append(i[0])
	t_ztran.append(i[1].to_sec())

z_translation_start_time = t_ztran[0]

for i in range(len(t_ztran)):
	t_ztran[i] = t_ztran[i] - z_translation_start_time

plt.plot(t_ztran, ztran)
plt.title("Z_Translation vs Time")
plt.xlabel("Time in sec")
plt.ylabel("Z_Translation")
plt.show()


#Features 
feat = []
t_feat= []

#Convert the ROS time to seconds 
for i in features:
	feat.append(i[0])
	t_feat.append(i[1].to_sec())

features_start_time = t_feat[0]

for i in range(len(t_feat)):
	t_feat[i] = t_feat[i] - features_start_time

plt.plot(t_feat, feat)
plt.title("Features vs Time")
plt.xlabel("Time in sec")
plt.ylabel("Features Detected")
plt.show()