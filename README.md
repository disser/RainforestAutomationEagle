# RainforestAutomationEagle
[unofficial] Rainforest Automation Eagle API Wrapper

## Usage:
```
from eagle import Eagle

eagle = Eagle(user="<cloud-ID>",
              password="<installation-code>",
              ipaddress="<eagle-IP-address>")

print(eagle.get_device_list())
```
