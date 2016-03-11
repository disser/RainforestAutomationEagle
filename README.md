# RainforestAutomationEagle
[unofficial] Rainforest Automation Eagle API Wrapper

## Requirements:
* [requests](http://docs.python-requests.org/)

## Usage:
```py
# import eagle
from RainforestAutomationEagle.eagle import Eagle

# 
eagle = Eagle(user="<cloud-ID>",
              password="<installation-code>",
              ipaddress="<eagle-IP-address>")

print(eagle.get_device_list())
```
