

import argparse
import redfish
import redfish_utilities
from newsensors import get_sensors,print_sensors,oem_sens


# Get the input arguments
argget = argparse.ArgumentParser( description = "A tool to walk a Redfish service and list sensor info" )
argget.add_argument( "--user", "-u", type = str, required = True, help = "The user name for authentication" )
argget.add_argument( "--password", "-p",  type = str, required = True, help = "The password for authentication" )
argget.add_argument( "--rhost", "-r", type = str, required = True, help = "The address of the Redfish service (with scheme)" )
args = argget.parse_args()

# Set up the Redfish object
redfish_obj = redfish.redfish_client( base_url = args.rhost, username = args.user, password = args.password )
redfish_obj.login( auth = "session" )

try:
    # Get and print the sensor info
    sensors = get_sensors( redfish_obj )
    print_sensors( sensors )
    oem_sens(redfish_obj)
finally:
    # Log out
    redfish_obj.logout()
