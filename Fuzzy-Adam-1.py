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

    #   weighting
    centerline_weighting = 0.8
    all_wheels_on_track_weighting = 0.5
    zigzag_weighting = 0.6
    percent_track_complete_weighting = 0.5
    fewer_steps_weighting = 0.4

    # Start with a base reward value

    reward = 10

    #############################################################################
    #                  BEGIN - sample code for time trials                      #
    #############################################################################

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the agent is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward *= 1 * centerline_weighting
    elif distance_from_center <= marker_2:
        reward *= 0.5 * centerline_weighting
    elif distance_from_center <= marker_3:
        reward *= 0.1 * centerline_weighting
    else:
        reward = 1e-3  # likely crashed/ close to off track

    if all_wheels_on_track:
        reward *= all_wheels_on_track_weighting

    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 15

    # Penalize reward if the agent is steering too much
    if steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8 * zigzag_weighting
    else:
        reward *= zigzag_weighting
    #############################################################################
    #                    END - sample code for time trials                      #
    #############################################################################

    #############################################################################
    #                    BEGIN - Percent Complete                               #
    #############################################################################

    # track completion creates a number going from 1 at the begining of the race
    # to 2 for completion. This is then multiplied by the weighting. so a weighting
    # of 7 would multiple reward by 7 at beginning fo race and 14 at completion

    reward *= (1 + (percent_track_complete / 100)) * percent_track_complete_weighting

    #############################################################################
    #                    END - Percent Complete                                 #
    #############################################################################


    #############################################################################
    #                    BEGIN - Fewer Steps to Complete                        #
    #############################################################################

    # want to reward for not taking too many steps to complete
    # the fewer steps_to_complete the steeper the reward function
    steps_to_complete = 400
    percent_steps_used = steps / steps_to_complete

    reward *= (1 + (percent_steps_used)) * fewer_steps_weighting


    #############################################################################
    #                    END - Fewer Steps to Complete                          #
    #############################################################################


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