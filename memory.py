def get_memory_details(context):

    service_root = context.get( "/redfish/v1/" )
    if "Systems" not in service_root.dict:
        return 1

    
    system_col = context.get(service_root.dict["Systems"]["@odata.id"])
    for system_member in system_col.dict["Members"]:
        system = context.get(system_member["@odata.id"])

        if "Memory" not in system.dict:
            return 1
        
        memory_col = context.get(system.dict["Memory"]["@odata.id"])

        #memory_count = memory_col.dict["Members@odata.count"]
        #print(memory_count)

        mem_line_format = "  {:10s} | {:15s} | {:15s} | {:15s} | {:15s} | {:8s} | {:8s} | {:10s}  "

        print(mem_line_format.format("Name","Description","Capacity in MiB","Device Locator","Device Type","State","Health","Operation Speed in MHZ"))

        for memory_member in memory_col.dict["Members"]:
            memory = context.get(memory_member["@odata.id"])

            name = str(memory.dict["Name"])
            desc = str(memory.dict["Description"])
            cap = str(memory.dict["CapacityMiB"])
            devloc = str(memory.dict["DeviceLocator"])
            devtype = str(memory.dict["MemoryDeviceType"])
            state = str(memory.dict["Status"]["State"])
            if state != "Enabled":
                health = "NA"
            else:
                health = str(memory.dict["Status"]["Health"])

            op_speed = str(memory.dict["OperatingSpeedMhz"])

            print(mem_line_format.format(name,desc,cap,devloc,devtype,state,health,op_speed))
