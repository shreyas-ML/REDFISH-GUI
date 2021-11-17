def get_lan_config( context ):

    service_root = context.get( "/redfish/v1/" )
    manager_col = context.get( service_root.dict["Managers"]["@odata.id"] )
    for manager_member in manager_col.dict["Members"]:
        manager = context.get( manager_member["@odata.id"] )

    ethnet = context.get(manager.dict["EthernetInterfaces"]["@odata.id"])
    manager_col = context.get(ethnet.dict["Members"][0]["@odata.id"])
    print ("lan info:")
    print ("\t extern link info:")
    """ 
    link_status = {
    health : manager_col.dict["Status"]["Health"],
    stat : manager_col.dict["Status"]["State"]
    }
    """
    print ("\t\t link status :")
    print("\t\t\t Health = ",manager_col.dict["Status"]["Health"])
    print("\t\t\t State = ",manager_col.dict["Status"]["State"])
    print("\t\t link speed : ", manager_col.dict["SpeedMbps"])
    print("\t\t Mac Addr : ", manager_col.dict["PermanentMACAddress"])

    print("\t ipv4 :")
    try:
        if(manager_col.dict["IPv4Addresses"]):
            print("\t\t enable : true")
    except:
        print("\t\t enable : false")

    ipv4 = manager_col.dict["IPv4Addresses"]
    print("\t\t", "ip_addr : ",ipv4[0]["Address"])
    if(ipv4[0]["AddressOrigin"]=="DHCP"):
        print("\t\t", "ip_dhcp : true")
    else:
        print("\t\t", "ip_dhcp : false")
    print("\t\t", "ip_mask : ",ipv4[0]["SubnetMask"])
    print("\t\t", "ip_gw : ",ipv4[0]["Address"])

    print("\t ipv6 :")
    try:
        if(manager_col.dict["IPv6Addresses"]):
            print("\t\t enable : true")
    except:
        print("\t\t enable : false")

    ipv6 = manager_col.dict["IPv6Addresses"]
    try:
        if(ipv6[0]["RouterAdvertisementEnabled"] == "true"):
            print("\t\t ra_enable : true")
    except:
        print("\t\t ra_enable : false")

    for i in range(len(ipv6)):
        ipv6detail = ipv6[i]
        print("\t\tDeatil ",ipv6detail["AddressOrigin"] , ":")
        for key,value in ipv6detail.items():
            print("\t\t\t", key, " : ", value)
