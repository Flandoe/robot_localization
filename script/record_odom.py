#!/usr/bin/env python
#coding=utf-8

import numpy 
import rospy
from nav_msgs.msg import Odometry #使用时需要修改数据类型PoseWithCovarianceStamped

list_TF = []
def get_info (msg):
    trans = []
    trans.append(msg.pose.pose.position.x)
    trans.append(msg.pose.pose.position.y)
    trans.append(msg.pose.pose.position.z)
    rot = []
    rot.append(msg.pose.pose.orientation.x)
    rot.append(msg.pose.pose.orientation.y)
    rot.append(msg.pose.pose.orientation.z)
    rot.append(msg.pose.pose.orientation.w)
    TF = trans + rot
    list_TF.append(TF)
    numpy.savetxt('TF.txt',list_TF)
    print(TF)
 
rospy.init_node('record_odom')
list_log = []
list_log_yaw = []
sub = rospy.Subscriber ('/odometry/filtered', Odometry, get_info)
 
r = rospy.Rate(20)
while not rospy.is_shutdown():
    r.sleep()
