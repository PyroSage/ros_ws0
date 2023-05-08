#!/usr/bin/env python3
import rospy as rp
from std_msgs.msg import String

def callback(msg):
    rp.loginfo("I heard %s", msg.data)

if __name__ == '__main__':
    rp.init_node('sub', anonymous=True)
    rp.Subscriber("/Published_topic", String, callback)
    rp.spin()