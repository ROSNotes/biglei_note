import rospy
from geometry_msgs.msg import Twist

pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10 )
rospy.init_node('xuehenxiaowugui')
xuegai_rate = rospy.Rate(5)

while not rospy.is_shutdown():

	xue_cmd = Twist()
	xue_cmd.linear.x = 0
	xue_cmd.angular.z = 0.1
	pub.publish(xue_cmd)

	xuegai_rate.sleep()
      
