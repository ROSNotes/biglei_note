import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def callback (xue):
	if (xue.linear.x>0 ):
		rospy.loginfo(" wu qian jin ")
	
	rospy.loginfo(xue,linear.x)

def listener():

	rospy.init_node('listener',anonymous=True)
	rospy.Subscriber('chatter',Twist,callback)
	rospy.spin()
if __name__ == '__main__':
	listener()
