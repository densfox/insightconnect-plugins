# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Add IP addresses to the existing blacklist within the blocked IP address configuration"


class Input:
    APP_ID = "app_id"
    IPS = "ips"
    

class Output:
    ID = "id"
    MESSAGE = "message"
    

class AddIpsToBlacklistInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "app_id": {
      "type": "string",
      "title": "App ID",
      "description": "App ID",
      "order": 1
    },
    "ips": {
      "type": "array",
      "title": "IPs",
      "description": "List of IP addresses",
      "items": {
        "type": "string"
      },
      "order": 2
    }
  },
  "required": [
    "app_id",
    "ips"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddIpsToBlacklistOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "integer",
      "title": "ID",
      "description": "ID of a new, updated configuration",
      "order": 1
    },
    "message": {
      "type": "string",
      "title": "Message",
      "description": "'Nothing to update' in case the configuration was not changed",
      "order": 2
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
