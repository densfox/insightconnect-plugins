# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Get a page of scans, based on supplied pagination parameters"


class Input:
    INDEX = "index"
    SIZE = "size"
    SORT = "sort"
    

class Output:
    SCANS = "scans"
    

class GetScansInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "index": {
      "type": "integer",
      "title": "Index",
      "description": "The page index to start form. If blank, index will be 0",
      "order": 1
    },
    "size": {
      "type": "integer",
      "title": "Size",
      "description": "The number of entries on each page. If blank, size will be 50",
      "order": 2
    },
    "sort": {
      "type": "string",
      "title": "Sort",
      "description": "How to sort the scans. If blank, sort will be alphabetical by scan name",
      "order": 3
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetScansOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "scans": {
      "type": "array",
      "title": "Scans",
      "description": "A list of scans",
      "items": {
        "$ref": "#/definitions/scan"
      },
      "order": 1
    }
  },
  "definitions": {
    "link": {
      "type": "object",
      "title": "link",
      "properties": {
        "href": {
          "type": "string",
          "title": "Href",
          "description": "Href",
          "order": 1
        },
        "rel": {
          "type": "string",
          "title": "Rel",
          "description": "rel",
          "order": 2
        }
      }
    },
    "scan": {
      "type": "object",
      "title": "scan",
      "properties": {
        "app_id": {
          "type": "string",
          "title": "App ID",
          "description": "App UUID",
          "order": 2
        },
        "completion_time": {
          "type": "string",
          "title": "Completion Time",
          "displayType": "date",
          "description": "The time the scan was completed",
          "format": "date-time",
          "order": 6
        },
        "failure_reason": {
          "type": "string",
          "title": "Failure Reason",
          "description": "The reason the scan may have failed",
          "order": 8
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Scan UUID",
          "order": 1
        },
        "links": {
          "type": "array",
          "title": "Links",
          "description": "A list of links",
          "items": {
            "$ref": "#/definitions/link"
          },
          "order": 9
        },
        "scan_config_id": {
          "type": "string",
          "title": "Scan Config ID",
          "description": "Scan configs UUID",
          "order": 3
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "The status of the scan",
          "order": 7
        },
        "submit_time": {
          "type": "string",
          "title": "Submit Time",
          "displayType": "date",
          "description": "The time the scan was submitted",
          "format": "date-time",
          "order": 5
        },
        "submitter": {
          "$ref": "#/definitions/submitter",
          "title": "Submitter",
          "description": "The submitter of the scan",
          "order": 4
        }
      },
      "definitions": {
        "link": {
          "type": "object",
          "title": "link",
          "properties": {
            "href": {
              "type": "string",
              "title": "Href",
              "description": "Href",
              "order": 1
            },
            "rel": {
              "type": "string",
              "title": "Rel",
              "description": "rel",
              "order": 2
            }
          }
        },
        "submitter": {
          "type": "object",
          "title": "submitter",
          "properties": {
            "id": {
              "type": "string",
              "title": "ID",
              "description": "The submitters UUID",
              "order": 2
            },
            "submitter_type": {
              "type": "string",
              "title": "Type",
              "description": "The type of the submitter e.g. USER",
              "order": 1
            }
          }
        }
      }
    },
    "submitter": {
      "type": "object",
      "title": "submitter",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The submitters UUID",
          "order": 2
        },
        "submitter_type": {
          "type": "string",
          "title": "Type",
          "description": "The type of the submitter e.g. USER",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
