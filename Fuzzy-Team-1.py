def reward_function(params):
    '''
    Example of penalize steering, which helps mitigate zig-zag behaviors
    '''

    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    steering = abs(params['steering_angle'])  # Only need the absolute steering angle
    percent_track_complete = params['progress'] + 1
    steps = params['steps'] + 1

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the agent is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track

    if all_wheels_on_track:
        reward *= 1.3

    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 15

    # Penalize reward if the agent is steering too much
    if steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    # printout of standard values for the log
    print("the reward is {}".format(reward))

    print("The steering_angle is {} ".format(params['steering_angle']))
    print("The heading of the car is {} ".format(params['heading']))
    print("The percent_track_complete is {} ".format(params['progress'] + 1))
    print("The number of steps is {}".format(params['steps'] + 1))
    print("the current speed is {}".format(params['speed']))
    print("All Wheels are on the track ... {} ".format(params['all_wheels_on_track']))
    print("The car is_offtrack ... {} ".format(params['is_offtrack']))
    print("The X and Y coordinates of the car are {},{}".format(params['x'], params['y']))
    print("The closest waypoints are {} ".format(params['closest_waypoints']))
    print("The distance from center is  {} ".format(params['distance_from_center']))
    print("The car is_left_of_center {} ".format(params['is_left_of_center']))
    print("The is is reversed {} ".format(params['is_reversed']))
    print("The length of the track {} ".format(params['track_length']))
    print("The width of the track {} ".format(params['track_width']))
    print("Here is a list of all the waypoints  {} ".format(params['waypoints']))

    # # printout of custom values
    # print("The percent_steps_used is {}".format(percent_steps_used))
    # print("The completion bonus is {}".format(percent_track_complete / percent_steps_used))

    return float(reward)