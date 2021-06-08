# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Convert HTML to Markdown"


class Input:
    DOC = "doc"
    

class Output:
    MARKDOWN_CONTENTS = "markdown_contents"
    MARKDOWN_FILE = "markdown_file"
    

class MarkdownInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "doc": {
      "type": "string",
      "title": "Document",
      "description": "Document to transform",
      "order": 1
    }
  },
  "required": [
    "doc"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class MarkdownOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "markdown_contents": {
      "type": "string",
      "title": "Contents",
      "description": "Markdown Contents",
      "order": 1
    },
    "markdown_file": {
      "type": "string",
      "title": "File",
      "displayType": "bytes",
      "description": "Markdown File",
      "format": "bytes",
      "order": 2
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)