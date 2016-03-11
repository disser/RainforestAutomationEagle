# Rainforest Automation - Eagle API Wrapper
[unofficial] Rainforest Automation Eagle API Wrapper

## Dependencies:
* [requests](http://docs.python-requests.org/)

## Usage:
```py
# import eagle
from RainforestAutomationEagle.eagle import Eagle

# initialize eagle object
eagle = Eagle(user="<cloud-ID>",
              password="<installation-code>",
              ipaddress="<eagle-IP-address>")

# make API request
device_list = eagle.get_device_list()
```

## Available API calls

### 
```py
response = eagle.get_device_list()

response.num_devices
response.device_model_id # list of model IDs
response.device_mac_id # list of MAC-addresses
```

### get_device_info
```py
response = eagle.get_device_info(MacId=mac_id)

response.device_date_code
response.device_install_code
response.device_hw_version
reponse.device_zb_version
reponse.device_link_key_lo
response.device_timestamp
response.device_mac_id
response.device_fw_version
response.device_manufacturer
response.device_model_id
response.device_link_key_hi
```

## Making a generic API call

The Rainforest Automation Eagle API receives its commands via an XML structure. Here is an example:
```xml
<Command>
  <Name>get_historical_data</Name>
  <Type>demand</Type>
  <Period>Hour</Period>
  <MacId>0xd8d5b90000000000</MacId>
</Command>
```

This command is created when you run:
```py
historical_data = eagle.get_historical_data(Type="demand", Period="Hour", MacId=mac_id)
```

Note that the function name `get_historical_data` corresponds to the XML `Name` field. All other fields correspond to the keyword arguments of the function.
