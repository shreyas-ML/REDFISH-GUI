#! /usr/bin/python
# Copyright Notice:
# Copyright 2019-2020 DMTF. All rights reserved.
# License: BSD 3-Clause License. For full text see link: https://github.com/DMTF/Redfish-Tacklebox/blob/master/LICENSE.md

"""
Sensors Module
File : sensors.py
Brief : This file contains the definitions and functionalities for scanning a
        Redfish service's for bmc info
"""

def get_bmc_info(context):
	service_root = context.get( "/redfish/v1/" )
	manager_col = context.get( service_root.dict["Managers"]["@odata.id"] )
	for manager_member in manager_col.dict["Members"]:
		manager = context.get( manager_member["@odata.id"] )
	print("BMC Firmwareversion :",manager.dict["FirmwareVersion"])