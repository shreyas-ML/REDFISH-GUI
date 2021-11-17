def ui_mon(context):
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

                    Volt_Preset_Values = {

                        "volt_LTC" : voltage["LowerThresholdCritical"],
                        "volt_LTF" : voltage["LowerThresholdFatal"],
                        "volt_LTNC" : voltage["LowerThresholdNonCritical"],
                        "volt_UTC" : voltage["UpperThresholdCritical"],
                        "volt_UTF" : voltage["UpperThresholdFatal"],
                        "volt_UTNC" : voltage["UpperThresholdNonCritical"]             
                    }
                    
                    volt_reading = voltage["ReadingVolts"]
                    health = voltage["Status"]["Health"]
                    if(health != "OK" and health != "null"):
                        print("Health of ",volt_name ,"is", health)
                    if(volt_reading is not None):
                        check_value("volt",volt_name,volt_reading,Volt_Preset_Values)
                    else:
                        print("Reading of ",volt_name, "is", volt_reading)
       


                        


        if "Thermal" in chassis.dict:
            thermal = context.get( chassis.dict["Thermal"]["@odata.id"] )

            # Add information for each of the temperatures reported
            if "Temperatures" in thermal.dict:
                for temperature in thermal.dict["Temperatures"]:
                    #temperature_name = "Temperature " + str(temperature["MemberId"])
                    if "Name" in temperature:
                        temp_name = temperature["Name"]
                        #print(temp_name, "\n")
                        Temp_Preset_Values = {
                        
                            "temp_LTC" : temperature["LowerThresholdCritical"],
                            "temp_LTF" : temperature["LowerThresholdFatal"],
                            "temp_LTNC" : temperature["LowerThresholdNonCritical"],
                            "temp_UTC" : temperature["UpperThresholdCritical"],
                            "temp_UTF" : temperature["UpperThresholdFatal"],
                            "temp_UTNC" : temperature["UpperThresholdNonCritical"]
                        }
                        
                        temp_reading = temperature["ReadingCelsius"]
                        health = temperature["Status"]["Health"]
                        if(health != "OK" and health != "null"):
                            print("Health of ",temp_name ,"is", health)
                        if(temp_reading is not None):
                            check_value("temp",temp_name,temp_reading,Temp_Preset_Values)
                        else:
                            print("Reading of ",temp_name, "is", temp_reading)


                        




            # Add information for each of the fans reported
            if "Fans" in thermal.dict:
                for fan in thermal.dict["Fans"]:
                    #fan_name = "Fan " + fan["MemberId"]
                    if "Name" in fan:
                        fan_name = fan["Name"]

                        Fan_Preset_Values = {
                            "fan_LTC" : fan["LowerThresholdCritical"],
                            "fan_LTF" : fan["LowerThresholdFatal"],
                            "fan_LTNC" : fan["LowerThresholdNonCritical"],
                            "fan_UTC" : fan["UpperThresholdCritical"],
                            "fan_UTF" : fan["UpperThresholdFatal"],
                            "fan_UTNC" : fan["UpperThresholdNonCritical"]
                        }
                        fan_reading = fan["Reading"]
                        health = fan["Status"]["Health"]
                        if(health != "OK" and health != "null"):
                            print("Health of ",fan_name ,"is", health)
                        if(fan_reading is not None):
                            check_value("fan",fan_name,fan_reading,Fan_Preset_Values)
                        else:
                            print("Reading of ",fan_name, "is", fan_reading)





def check_value(type,name,reading,preset_value):
    #print(name)
    flag = 0
    
    
    if (preset_value["%s" %type + "_LTNC"] is not None):
        if(preset_value["%s" %type + "_LTNC"]>reading):
            flag = 1
            print("Warning!!!!",name,"reading is below Lower Threshold Non Critical")
            return


    if (preset_value["%s" %type + "_LTC"] is not None):
        if(preset_value["%s" %type + "_LTC"] > reading):
            flag = 1
            print("Warning!!!!",name,"reading is below Lower Threshold Critical")
            return
    if (preset_value["%s" %type + "_LTF"] is not None):
        if(preset_value["%s" %type + "_LTF"]>reading):
            print("Warning!!!!",name,"reading is below Lower Threshold Fatal")
            return

    if (preset_value["%s" %type + "_UTNC"] is not None):
        if(preset_value["%s" %type + "_UTNC"]<reading):
            flag = 1
            print("Warning!!!!",name,"reading is below Upper Threshold Non Critical")
            return

    if (preset_value["%s" %type + "_UTC"] is not None):
        if(preset_value["%s" %type + "_UTC"]<reading):
            flag = 1
            print("Warning!!!!",name,"reading is above Upper Threshold Critical")
            return
    if (preset_value["%s" %type + "_UTF"] is not None):
        if(preset_value["%s" %type + "_UTF"]<reading):
            flag = 1
            print("Warning!!!!",name,"reading is above Upper Threshold Fatal")
            return


    if (flag == 0):
        print(name, "condition is good \n")
        return
