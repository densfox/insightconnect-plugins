# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Retrieve a list of available keyboard layouts for Windows analyzers"


class Input:
    pass

class Output:
    KEYBOARD_LAYOUTS = "keyboard_layouts"
    

class ListKeyboardLayoutsInput(komand.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListKeyboardLayoutsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "keyboard_layouts": {
      "type": "array",
      "title": "Keyboard Layouts",
      "description": "List of available keyboard layouts",
      "items": {
        "$ref": "#/definitions/keyboard_layout"
      },
      "order": 1
    }
  },
  "required": [
    "keyboard_layouts"
  ],
  "definitions": {
    "keyboard_layout": {
      "type": "object",
      "title": "keyboard_layout",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the keyboard layout language",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
