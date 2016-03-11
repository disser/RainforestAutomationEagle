# RainforestAutomationEagle
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
print(eagle.get_device_list())
```
