# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Retrieve a CI record from ServiceNow"


class Input:
    SYSTEM_ID = "system_id"
    TABLE = "table"


class Output:
    SERVICENOW_CI = "servicenow_ci"


class GetCiInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "system_id": {
      "type": "string",
      "title": "System ID",
      "description": "The system ID of the record to retrieve",
      "order": 2
    },
    "table": {
      "type": "string",
      "title": "Table",
      "description": "The ServiceNow table to retrieve the CI from",
      "order": 1
    }
  },
  "required": [
    "system_id",
    "table"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetCiOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "servicenow_ci": {
      "type": "object",
      "title": "ServiceNow CI",
      "description": "JSON object representing the CI record returned",
      "order": 1
    }
  },
  "required": [
    "servicenow_ci"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
