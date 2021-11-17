#! /usr/bin/python
# Copyright Notice:
# Copyright 2019-2020 DMTF. All rights reserved.
# License: BSD 3-Clause License. For full text see link: https://github.com/DMTF/Redfish-Tacklebox/blob/master/LICENSE.md

"""
Sensors Module
File : sensors.py
Brief : This file contains the definitions and functionalities for scanning a
        Redfish service's for PSU firmware versions
"""

def get_psu_fw_ver(context):
	service_root = context.get( "/redfish/v1/" )
	chassis_col = context.get( service_root.dict["Chassis"]["@odata.id"] )
	for chassis_member in chassis_col.dict["Members"]:
		chassis = context.get( chassis_member["@odata.id"] )

	if "Power" in chassis.dict:
		power = context.get( chassis.dict["Power"]["@odata.id"] )

	if "PowerSupplies" in power.dict:
		for power_supply in power.dict["PowerSupplies"]:
			psuv = power_supply["@odata.id"]
			v = psuv[-1]
			print("Firmware version of PSU",v," : " ,power_supply["FirmwareVersion"])
