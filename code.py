def getnumber(self):
	
    #This function will be used to get the number of goals we want to reach at the end
    
    rospy.init_node('listener', anonymous=True) #we create our code

    while self.number < 1:      #we don't want a number of goals less than 1 so we
                                #create a loop to obtain a positive integer
        try:
            self.number = int(raw_input('Enter the number of wanted waypoints: '))
                                #we check if the number is an integer

            if self.number < 1: #if the number is less than one
                rospy.loginfo("Not a positive number")   #we ask a positive number
        except ValueError:      #if the input is not an integer
            rospy.loginfo("Not a positive number")      #we ask a positive number

    rospy.loginfo("Now you can enter your different waypoints")  #we display that we can register our way points
    self.index = 0                        #we reset our index
    while self.index < self.number: we want to it until we got the good number of goals
       rospy.Subscriber('/move_base/goal', MoveBaseActionGoal, self.callback) #we subscribe to the goal node,
       rospy.spin()    #used to let only one instruction pass, this will wait another instruction

def callback(self, msg):   #this function will be used each time we create a new nav goal

    if self.over == 0:   #if we hadn't finish the program
        new_move = actionlib.SimpleActionClient("move_base", MoveBaseAction) #"new_move" will be a variable containting an action, here a MoveBaseAction to move the robot
        new_move.wait_for_server()   #we are waiting the robot server
        new_move.cancel_all_goals()  #we cancel every goals to avoid a movement of the robot

        self.goal = msg    #goal (a MoveBaseGoal) become the new goal we entered

        self.add_markers(self.goal) #with the goal we add a new markers on this position 

        if self,index == 0: #if this is the first move we allow it to 		not be compared


def callback(self,msg): #this function will be used each time we create a new nav goal

    if self.over == 0: #if we hadn't finished the program
        new_move = actionlib.SimpleActionClient("move_base", MoveBaseAction) #"new_move" will be variable containing an action, here a MoveBaseAction to move the robot
        new_move.wait_for_server()   #we are waiting the robot server
        new_move.cancel_all_goals() #We cancel every goals to avoid a movement of the robot

        self.goal = msg     #goal (a MoveBaseGoal) become the new goal we entered

        self.add_markers(self.goal)  #with the goal we add a new markers on this position 

        if self.index == 0:  #if this is the first move we allow it not be compared
            self.WaypointsLists = self.WayPointsLists.append(self.goal)
                 #We add the new goal to the goals list
            self.index = self.index +1
                 #we increment the index
        
        if self.WayPointLists[self.index-1] !=self.goal:
                #we compare the new goal to the last one to avoid some useless move
            self.WaypointsLists = self.WayPointsLists.append(self.goal)
                #We add the new goal to the goals list
            self.index = self.index +1
                 #we increment the index

        if self.index >= self.number and not rospy.is_shutdown():
                #if the index is equal or greater than the number of goals
           rospy.loginfo("Procurement finished")   #we entered all the goals
           self.over = 1
           self.recurrence() #we call the function to reach goals
