import json
import requests
import xml.etree.ElementTree as ET

from collections import namedtuple, defaultdict
from functools import partial


class EagleException(Exception):
    """Just so you can catch our own exceptions if needed."""
    pass


class Eagle(object):
    """
    as per: http://rainforestautomation.com/wp-content/uploads/2015/07/EAGLE_REST_API-1.1.pdf
    """

    def __init__(self, user, password, ipaddress):
        """Store mandatory data"""
        self._user = user
        self._password = password
        self._ipaddress = ipaddress
        self._base_url = "http://{ip}/cgi-bin/cgi_manager".format(ip=ipaddress)


    def __getattribute__(self, name):
        try:
            # always check the object's real attributes first
            return object.__getattribute__(self, name)
        except AttributeError:
            # Trust the developer to send the correct function name
            # pre-fill function with name of command
            return partial(self._execute_command, command=name)


    def _execute_command(self, command, **options):
        """Return response data for command."""
        # build xml request
        xml_command = self._build_command(command, **options)
        # send xml request
        response = self._send_request(xml_command)
        # parse resonse
        data = self._parse_response(response.text, command)
        return data


    def _build_command(self, command_name, **options):
        """Return XML command string for eagle device."""
        command = ET.Element('Command')
        options.update({"Name":command_name})

        for key, value in options.iteritems():
            option = ET.SubElement(command, key)
            option.text = value

        return ET.tostring(command)


    def _send_request(self, xml_command):
        """Return parsed JSON as dictionary for given XML command."""
        print(xml_command)
        response = requests.post(self._base_url,
                                 auth=(self._user, self._password),
                                 data=xml_command)
        return response


    def _parse_response(self, response_data, command):
        # parse JSON
        try:
            raw_data = json.loads(response_data)
        except ValueError:
            msg = "invalid query parameters for '%s'. (Probably you are " +\
                  "missing a parameter like 'MacId')."
            msg = msg % command
            raise EagleException(msg)

        # parse list responses, as the eagle's response is pretty useless
        parsed_data = defaultdict(list)
        keys_to_sort = set()
        for key, value in raw_data.iteritems():
            if "[" in key:
                real_key, index = key.split("[")
                index = int(index.replace("]", ""))
                parsed_data[real_key].append([index, value])
                keys_to_sort.add(real_key)
            else:
                parsed_data[key] = value

        # sort lists
        for key in keys_to_sort:
            sorted_values = sorted(parsed_data[key], key=lambda x: x[0])
            sorted_values = [sv[1] for sv in sorted_values]
            parsed_data[key] = sorted_values

        # package data into named tuple for easier consumption
        Response = namedtuple("Response", parsed_data.keys())
        data = Response(**parsed_data)
        return data

