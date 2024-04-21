from robomaster import robot


def sub_data_handler(sub_info):
    global distance
    distance = sub_info


if __name__ == "__main__":
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")

    ep_sensor = ep_robot.sensor
    ep_sensor.sub_distance(freq=5, callback=sub_data_handler)

    ep_chassis = ep_robot.chassis
    ep_chassis.drive_wheels(w1=20, w2=20, w3=20, w4=20)

    while True:
        if distance[0] < 150:
            ep_chassis.drive_wheels(w1=0, w2=0, w3=0, w4=0)
            break

    ep_sensor.unsub_distance()
    ep_robot.close()
