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
    steps_to_complete = 500
    percent_steps_used = steps/steps_to_complete

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the agent is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward *= 1
    elif distance_from_center <= marker_2:
        reward *= 5
    elif distance_from_center <= marker_3:
        reward *= 1
    else:
        reward = 1e-3  # likely crashed/ close to off track
    # make the reward based on the ratio of track complete vs steps complete

    reward *= percent_track_complete/percent_steps_used

    # reward for being on the left side of the track

    if is_left:
        reward *= 8
    else:
        reward *= 2

    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 1

    # Penalize reward if the agent is steering too much
    if steering > ABS_STEERING_THRESHOLD:
        reward *= 0.7

    return float(reward)