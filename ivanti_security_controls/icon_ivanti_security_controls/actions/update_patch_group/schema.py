# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Add CVEs or Patches to an existing patch group"


class Input:
    PATCH_GROUP = "patch_group"
    VULNERABILITY_IDENTIFIER = "vulnerability_identifier"
    

class Output:
    SUCCESS = "success"
    

class UpdatePatchGroupInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "patch_group": {
      "type": "string",
      "title": "Patch Group",
      "description": "Name or ID of an existing patch group",
      "order": 1
    },
    "vulnerability_identifier": {
      "type": "array",
      "title": "Vulnerability Identifier",
      "description": "List of patch IDs or CVEs to add to an existing patch group",
      "items": {
        "type": "string"
      },
      "order": 2
    }
  },
  "required": [
    "patch_group",
    "vulnerability_identifier"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UpdatePatchGroupOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Was operation successful",
      "order": 1
    }
  },
  "required": [
    "success"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)