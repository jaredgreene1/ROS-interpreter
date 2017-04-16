#!/usr/bin/env python

import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal



class MoveBaseClient(object):
    def __init__(self):
        self.client = actionlib.SimpleActionClient("move_base", MoveBaseAction)
        rospy.loginfo("waiting for movebase client")
        self.client.wait_for_server()

    def goto(self, x, y, theta, frame="map"):
         move_goal = MoveBaseGoal()
         move_goal.target_pose.pose.position.x = x
         move_goal.target_pose.pose.position.y = y
         move_goal.target_pose.pose.orientation.z = sin(theta/2.0)
         move_goal.target_pose.pose.orientation.w = cos(theta/2.0)
         move_goal.target_pose.header.frame_id = frame
         move_goal.target_pose.header.stamp = rospy.Time.now()

	self.client.send_goal(move_goal)
	self.client.wait_for_result()

if __name__ == "__main__":
     # Create a node
     rospy.init_node("landmarks")

     # Make sure sim time is working
     while not rospy.Time.now():
         pass

     # Setup client
     move_base = MoveBaseClient()

     move_base.goto(5.0, 2.1, 0.0)
     move_base.goto(0.0, 5.0, 0.5)
