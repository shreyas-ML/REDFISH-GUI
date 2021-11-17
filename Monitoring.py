import subprocess
import smtplib


def monitoring(context,Present_Values):
    #print(context)
    #print(Present_Values)
    #send_mail()
    service_root = context.get( "/redfish/v1/" )
    chassis_col = context.get( service_root.dict["Chassis"]["@odata.id"] )
    for chassis_member in chassis_col.dict["Members"]:
        chassis = context.get( chassis_member["@odata.id"] )

        #print(chassis)

        if "Power" in chassis.dict:
            power = context.get( chassis.dict["Power"]["@odata.id"] )

        
        if "Voltages" in power.dict:
            for voltage in power.dict["Voltages"]:
                if "Name" in voltage:
                    volt_name = voltage["Name"]
                    volt_reading = voltage["ReadingVolts"]                    
                    volt_preset_value = Present_Values["Volt_Preset_Values"][volt_name]
                    health = voltage["Status"]["Health"]
                    #print(health)                    
                    if(health != "OK"):
                        print("Health of ",volt_name ,"is not \"OK\"")
                    if( volt_reading is not None):
                        check_value("volt",volt_name,volt_reading,volt_preset_value)
                    else:
                        print("Reading of ",volt_name, "is", volt_reading)


        if "Thermal" in chassis.dict:
            thermal = context.get( chassis.dict["Thermal"]["@odata.id"] )

            
            if "Temperatures" in thermal.dict:
                for temperature in thermal.dict["Temperatures"]:
                    if "Name" in temperature:
                        temp_name = temperature["Name"]
                        #print(temp_name)
                        temp_reading = temperature["ReadingCelsius"]                  
                        temp_preset_value = Present_Values["Temp_Preset_Values"][temp_name]
                        #print(temp_name, temp_preset_value,"\n")
                        health = temperature["Status"]["Health"]
                        #print(health)                    
                        if(health != "OK" and health != None):
                            print("Health of ",temp_name ,"is", health)
                        if(temp_reading is not None):
                            check_value("temp",temp_name,temp_reading,temp_preset_value)
                        else:
                            print("Reading of ",temp_name, "is", temp_reading)


            if "Fans" in thermal.dict:
                for fan in thermal.dict["Fans"]:
                    #fan_name = "Fan " + fan["MemberId"]
                    if "Name" in fan:
                        fan_name = fan["Name"]
                        fan_reading = fan["Reading"]
                        fan_preset_value = Present_Values["Fan_Preset_Values"][fan_name]
                        health = fan["Status"]["Health"]
                        if(health != "OK" and health != "null"):
                            print("Health of ",fan_name ,"is", health)
                        if(fan_reading is not None):
                            check_value("fan",fan_name,fan_reading,fan_preset_value)
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
        #print(preset_value["%s" %type + "_LTC"])
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

def send_mail():
    msg = "TEST"
    sender = 'redfish.hw.notification@gmail.com'
    receivers = ['redfish.hw.notification@gmail.com']

    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receivers, msg)         
        print ("Successfully sent email")
    except:
        print ("Error: unable to send email")

    




