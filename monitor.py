from Monitoring import monitoring


def mon(context):
    service_root = context.get( "/redfish/v1/" )

    #if "Chassis" not in service_root.dict:
        # No Chassis Collection
        #return sensor_list
       
    #Preset_Values = {}
    Volt_Preset_Values = {}
    Fan_Preset_Values = {}
    Temp_Preset_Values ={}
    


    # Get the Chassis Collection and iterate through its collection
    chassis_col = context.get( service_root.dict["Chassis"]["@odata.id"] )
    for chassis_member in chassis_col.dict["Members"]:
        chassis = context.get( chassis_member["@odata.id"] )

        #print(chassis)

        if "Power" in chassis.dict:
            power = context.get( chassis.dict["Power"]["@odata.id"] )
            #if "PowerSupplies" in power.dict:
                #for power_supply in power.dict["PowerSupplies"]:
                   # if "Name" in power_supply:
                        #power_supply_name = power_supply["Name"] 
                        

        if "Voltages" in power.dict:
            for voltage in power.dict["Voltages"]:
                #voltage_name = "Voltage " + str(voltage["MemberId"])
                if "Name" in voltage:

                    volt_name = voltage["Name"]

                    Volt_Preset_Values["%s" %volt_name] = {

                        "volt_LTC" : voltage["LowerThresholdCritical"],
                        "volt_LTF" : voltage["LowerThresholdFatal"],
                        "volt_LTNC" : voltage["LowerThresholdNonCritical"],
                        "volt_UTC" : voltage["UpperThresholdCritical"],
                        "volt_UTF" : voltage["UpperThresholdFatal"],
                        "volt_UTNC" : voltage["UpperThresholdNonCritical"]             
                    }
                        


        if "Thermal" in chassis.dict:
            thermal = context.get( chassis.dict["Thermal"]["@odata.id"] )

            # Add information for each of the temperatures reported
            if "Temperatures" in thermal.dict:
                for temperature in thermal.dict["Temperatures"]:
                    #temperature_name = "Temperature " + str(temperature["MemberId"])
                    if "Name" in temperature:
                        temp_name = temperature["Name"]
                        #print(temp_name, "\n")
                        Temp_Preset_Values["%s" %temp_name] = {
                        #a_dictionary["key%s" %number]
                        "temp_LTC" : temperature["LowerThresholdCritical"],
                        "temp_LTF" : temperature["LowerThresholdFatal"],
                        "temp_LTNC" : temperature["LowerThresholdNonCritical"],                    
                        "temp_UTC" : temperature["UpperThresholdCritical"],
                        "temp_UTF" : temperature["UpperThresholdFatal"],
                        "temp_UTNC" : temperature["UpperThresholdNonCritical"]
                        }


                        




            # Add information for each of the fans reported
            if "Fans" in thermal.dict:
                for fan in thermal.dict["Fans"]:
                    #fan_name = "Fan " + fan["MemberId"]
                    if "Name" in fan:
                        fan_name = fan["Name"]

                        Fan_Preset_Values["%s" %fan_name] = {
                        "fan_LTC" : fan["LowerThresholdCritical"],
                        "fan_LTF" : fan["LowerThresholdFatal"],
                        "fan_LTNC" : fan["LowerThresholdNonCritical"],
                        "fan_UTC" : fan["UpperThresholdCritical"],
                        "fan_UTF" : fan["UpperThresholdFatal"],
                        "fan_UTNC" : fan["UpperThresholdNonCritical"]
                        }


    Preset_Values = {
        "Volt_Preset_Values" : Volt_Preset_Values,
        "Temp_Preset_Values" : Temp_Preset_Values,
        "Fan_Preset_Values" : Fan_Preset_Values
    }
    
    print("Monitoring has started ")
    print("To terminate monitoring Press Ctrl-C")
    i = 1
    try:
        while (True):
            print(i)
            i = i+1
            monitoring(context,Preset_Values)

    except:
        pass
    
    


