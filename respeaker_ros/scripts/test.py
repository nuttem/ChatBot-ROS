#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from ros_speech_recognition import SpeechRecognitionClient

rospy.init_node('client')
pub = rospy.Publisher('/recognizer/output', String,queue_size=10)
r = rospy.Rate(1) # 10hz

def speaking():
	client = SpeechRecognitionClient()
	result = client.recognize()  # Please say 'Hello, world!' towards microphone
	a = str(result) #change data type
	word = a.split('[')[1].split(']')[0] #split word
	#print (word) #check
	pub.publish(word)
	rospy.sleep(2.) #3 second

if __name__ == '__main__':	
	while not rospy.is_shutdown():
		speaking()

