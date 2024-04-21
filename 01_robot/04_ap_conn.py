# -*-coding:utf-8-*-
# Copyright (c) 2020 DJI.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import robomaster
from robomaster import robot


if __name__ == "__main__":
    # If the local IP is automatically obtained incorrectly, manually specify the local IP address.
    # robomaster.config.LOCAL_IP_STR = "192.168.2.20"
    ep_robot = robot.Robot()

    # Specify the connection method as AP direct connection mode
    ep_robot.initialize(conn_type="ap")

    version = ep_robot.get_version()
    print("Robot version: {0}".format(version))
    ep_robot.close()
