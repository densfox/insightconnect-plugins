# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Fires when a new alert is found"


class Input:
    pass
    

class Output:
    
    ALERT = "alert"
    

class NewAlertInput(komand.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class NewAlertOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "alert": {
      "$ref": "#/definitions/alert",
      "title": "Alert",
      "description": "Carbon Black alert",
      "order": 1
    }
  },
  "definitions": {
    "alert": {
      "type": "object",
      "title": "alert",
      "properties": {
        "alert_severity": {
          "type": "number",
          "title": "Severity",
          "order": 1
        },
        "alert_type": {
          "type": "string",
          "title": "Type",
          "order": 16
        },
        "created_time": {
          "type": "string",
          "title": "Created Time",
          "displayType": "date",
          "format": "date-time",
          "order": 6
        },
        "feed_id": {
          "type": "integer",
          "title": "Feed ID",
          "order": 13
        },
        "feed_name": {
          "type": "string",
          "title": "Feed Name",
          "order": 5
        },
        "feed_rating": {
          "type": "number",
          "title": "Feed Rating",
          "order": 8
        },
        "hostname": {
          "type": "string",
          "title": "Hostname",
          "order": 3
        },
        "ioc_attr": {
          "type": "string",
          "title": "IOC Attributes",
          "order": 14
        },
        "ioc_confidence": {
          "type": "number",
          "title": "IOC Confidence",
          "order": 9
        },
        "md5": {
          "type": "string",
          "title": "MD5",
          "order": 11
        },
        "os_type": {
          "type": "string",
          "title": "OS Type",
          "order": 7
        },
        "report_score": {
          "type": "integer",
          "title": "Report Score",
          "order": 4
        },
        "sensor_criticality": {
          "type": "number",
          "title": "Sensor Criticality",
          "order": 2
        },
        "sensor_id": {
          "type": "integer",
          "title": "Sensor ID",
          "order": 12
        },
        "status": {
          "type": "string",
          "title": "Status",
          "order": 15
        },
        "unique_id": {
          "type": "string",
          "title": "Unique ID",
          "order": 10
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
