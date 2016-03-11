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

### get_device_list
```py
response = eagle.get_device_list()

response.num_devices
response.device_model_id  # list of model IDs
response.device_mac_id    # list of MAC-addresses
```

### get_network_info
```py
response = eagle.get_network_info(MacId="0xd8d5b90000000000")

response.network_status
response.network_ext_pan_id
response.network_short_addr
response.network_channel
response.network_meter_mac_id
response.network_link_strength
response.network_timestamp
```

### get_device_info
```py
response = eagle.get_device_info(MacId="0xd8d5b90000000000")

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

### get_price
```py
response = eagle.get_price(MacId="0xd8d5b90000000000")

response.price_units
response.price
response.price_timestamp
response.price_label
```

### get_message
```py
response = eagle.get_message(MacId="0xd8d5b90000000000")

response.message_queue
response.meter_status
response.message_confirm_required
response.message_confirmed
response.message_read
response.message_timestamp
response.message_id)
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
historical_data = eagle.get_historical_data(Type="demand", Period="Hour", MacId="0xd8d5b90000000000")
```

Note that the function name `get_historical_data` corresponds to the XML `Name` field. All other fields correspond to the keyword arguments of the function. Knowing this you can now call any `get_` Eagle API function. The `eagle` object will generically generate the XML.

Unfortunately the **Eagle API does not return error codes** for maleformed API-calls. The only way to know that something is wrong is when you receive an empty response object.
