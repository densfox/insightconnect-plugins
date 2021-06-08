# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Export all events in XML format"


class Input:
    ENCODE_ATTACHMENTS = "encode_attachments"
    EVENT_ID = "event_id"
    FROM = "from"
    LAST = "last"
    TAGS = "tags"
    TO = "to"
    

class Output:
    EVENTS = "events"
    

class ExportEventsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "encode_attachments": {
      "type": "boolean",
      "title": "Encode Attachments",
      "description": "Encode attachments in export",
      "default": true,
      "order": 2
    },
    "event_id": {
      "type": "string",
      "title": "Event ID",
      "description": "Specify single event to export",
      "order": 1
    },
    "from": {
      "type": "string",
      "title": "From Date",
      "description": "From date E.g. 2015-02-15",
      "order": 4
    },
    "last": {
      "type": "string",
      "title": "Last Events",
      "description": "Events within x amount of time E.g. 5d",
      "order": 6
    },
    "tags": {
      "type": "array",
      "title": "Tags",
      "description": "Array of tags to include in results",
      "items": {
        "type": "string"
      },
      "order": 3
    },
    "to": {
      "type": "string",
      "title": "To Date",
      "description": "To date E.g. 2015-02-17",
      "order": 5
    }
  },
  "required": [
    "encode_attachments"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ExportEventsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "events": {
      "type": "string",
      "title": "Event Output",
      "displayType": "bytes",
      "description": "Event output",
      "format": "bytes",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)