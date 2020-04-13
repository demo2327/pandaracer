def reward_function(params):
    # start the reward as a value
    reward = 1
    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    steering = abs(params['steering_angle']) # Only need the absolute steering angle
    is_left = params['is_left_of_center']
    percent_track_complete = params['progress']+1
    steps = params['steps']+1
    
    # create some parameters for us to use
    steps_to_complete = 300
    percent_steps_used = steps/steps_to_complete

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    center_of_lane = 0.25 * track_width
    wall = 0.5 * track_width

    # Give higher reward if the agent is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward *= 5
    elif distance_from_center <= center_of_lane:
        reward *= 3
    elif distance_from_center <= wall:
        reward *= 1
    else:
        reward = 1e-6  # likely crashed/ close to off track
    # make the reward based on the ratio of track complete vs steps complete

    reward *= percent_track_complete/percent_steps_used/50

    # reward for being on the left side of the track

    if is_left:
        reward *= 8
    else:
        reward *= 2

    
    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 1

    # Penalize reward if the agent is steering too much
    if steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8
    
    # print out some values so that we can see what they are

    print("The number of steps is {}".format(steps))
    print("The percent_steps_used is {}".format(percent_steps_used))
    print("The completion bonus is {}".format(percent_track_complete/percent_steps_used))
    print("the reward is {}".format(reward))
    print("the current speed is {}".format(params['speed']))
    print("the current progress is {}".format(params['progress']))
    
    

    return float(reward)