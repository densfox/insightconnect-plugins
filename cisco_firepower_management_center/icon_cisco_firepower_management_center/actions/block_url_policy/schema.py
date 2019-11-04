# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Create a new block URL policy"


class Input:
    ACCESS_POLICY = "access_policy"
    RULE_NAME = "rule_name"
    URL_OBJECTS = "url_objects"
    

class Output:
    SUCCESS = "success"
    

class BlockUrlPolicyInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "access_policy": {
      "type": "string",
      "title": "Access Policy Name",
      "description": "Access Policy name",
      "order": 2
    },
    "rule_name": {
      "type": "string",
      "title": "Access Rule Name",
      "description": "Name for Access Rule to be created",
      "order": 3
    },
    "url_objects": {
      "type": "array",
      "title": "URL Objects",
      "description": "URL Objects to block",
      "items": {
        "$ref": "#/definitions/url_object"
      },
      "order": 1
    }
  },
  "required": [
    "access_policy",
    "rule_name",
    "url_objects"
  ],
  "definitions": {
    "url_object": {
      "type": "object",
      "title": "url_object",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of URL object",
          "order": 1
        },
        "url": {
          "type": "string",
          "title": "URL",
          "description": "URL to block (max 400 chars)",
          "order": 2
        }
      },
      "required": [
        "name",
        "url"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class BlockUrlPolicyOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Success",
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