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
    centerline_weighting = 1.2
    all_wheels_on_track_weighting = 1.2
    zigzag_weighting = 1.6
    percent_track_complete_weighting = 2.5
    fewer_steps_bonus = 2.0

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
        centerline = 1.5 * centerline_weighting
        reward *= centerline
    elif distance_from_center <= marker_2:
        centerline = 1.2 * centerline_weighting
        reward *= centerline
    elif distance_from_center <= marker_3:
        centerline = 1 * centerline_weighting
        reward *= centerline
    else:
        centerline = 999999999
        reward = 1e-3  # likely crashed/ close to off track
    
    ontrack = 1

    if all_wheels_on_track:
        ontrack = all_wheels_on_track_weighting
        reward *= all_wheels_on_track_weighting

    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 15

    # Penalize reward if the agent is steering too much
    
    zigzag = 1

    if steering > ABS_STEERING_THRESHOLD:
        zigzag == 0.8 * zigzag_weighting
        reward *= 0.8 * zigzag_weighting
    else:
        zigzag = zigzag_weighting
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

    percent_complete_reward = (1 + (percent_track_complete / 100)) * percent_track_complete_weighting
    reward *= percent_complete_reward

    #############################################################################
    #                    END - Percent Complete                                 #
    #############################################################################


    #############################################################################
    #                    BEGIN - Fewer Steps to Complete                        #
    #############################################################################

    # want to reward for not taking too many steps to complete
    # the fewer steps_to_complete the steeper the reward function
    steps_to_complete = 300
    percent_steps_used = steps / steps_to_complete

    if percent_steps_used <= (params['progress']+1)/101:
        reward *= fewer_steps_bonus
        fewer_steps_bonus_recieved = fewer_steps_bonus
    else:
        fewer_steps_bonus_recieved = 1
    


    #############################################################################
    #                    END - Fewer Steps to Complete                          #
    #############################################################################


    # printout of standard values for the log
    print(" _  the reward is {}".format(reward))

    print(" __  The steering_angle is {} ".format(params['steering_angle']))
    print(" ___  The heading of the car is {} ".format(params['heading']))
    print(" ____  The percent_track_complete is {} ".format(params['progress'] + 1))
    print(" _____  The number of steps is {}".format(params['steps'] + 1))
    print(" ______  the current speed is {}".format(params['speed']))
    print(" _______  All Wheels are on the track ... {} ".format(params['all_wheels_on_track']))
    print(" ________  The car is_offtrack ... {} ".format(params['is_offtrack']))
    print(" _________  The X and Y coordinates of the car are {},{}".format(params['x'], params['y']))
    print(" __________  The closest waypoints are {} ".format(params['closest_waypoints']))
    print(" ___________  The distance from center is  {} ".format(params['distance_from_center']))
    print(" ____________  The car is_left_of_center {} ".format(params['is_left_of_center']))
    print(" _____________  The is is reversed {} ".format(params['is_reversed']))
    print(" ______________  The length of the track {} ".format(params['track_length']))
    print(" _______________  The width of the track {} ".format(params['track_width']))
    print(" ________________  Here is a list of all the waypoints  {} ".format(params['waypoints']))

    # # printout of custom values
    print(" ________________________  The percent_steps_used is {}".format(percent_steps_used))
    print(" ________________________  The completion bonus is {}".format((params['progress']+1)/101))
    print("Step:{}__Reward:{}__CL:{}__OT:{}__ZZ:{}__%C:{}/__FS:{}".format(params['steps'] , round(reward , 2) , round(centerline , 2) , ontrack , zigzag , round(percent_complete_reward , 2), fewer_steps_bonus_recieved ))
    print(" ________________________ ")
    print(" ________________________ ")
    
    return float(reward)