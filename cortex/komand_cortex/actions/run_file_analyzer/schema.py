# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Run analyzers on a file"


class Input:
    ANALYZER_ID = "analyzer_id"
    ATTRIBUTES = "attributes"
    FILE = "file"
    

class Output:
    ANALYZERID = "analyzerId"
    ARTIFACT = "artifact"
    DATE = "date"
    ID = "id"
    STATUS = "status"
    

class RunFileAnalyzerInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "analyzer_id": {
      "type": "string",
      "title": "Analyzer ID",
      "description": "Analyzer ID e.g. File_Info_2_0",
      "order": 1
    },
    "attributes": {
      "$ref": "#/definitions/input_file_attributes",
      "title": "Attributes",
      "description": "Attributes",
      "order": 3
    },
    "file": {
      "type": "string",
      "title": "File",
      "displayType": "bytes",
      "description": "A file to analyze",
      "format": "bytes",
      "order": 2
    }
  },
  "required": [
    "analyzer_id",
    "attributes",
    "file"
  ],
  "definitions": {
    "input_file_attributes": {
      "type": "object",
      "title": "input_file_attributes",
      "properties": {
        "filename": {
          "type": "string",
          "title": "File Name",
          "description": "File name",
          "order": 2
        },
        "tlp": {
          "type": "integer",
          "title": "TLP",
          "description": "Traffic Light Protocol level e.g. 1",
          "order": 1
        }
      },
      "required": [
        "tlp"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RunFileAnalyzerOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "analyzerId": {
      "type": "string",
      "title": "AnalyzerId",
      "description": "The analyzer's ID",
      "order": 4
    },
    "artifact": {
      "$ref": "#/definitions/file_artifact",
      "title": "Artifact",
      "description": "The observable details",
      "order": 5
    },
    "date": {
      "type": "integer",
      "title": "Date",
      "description": "A timestamp which represents the job's start date",
      "order": 2
    },
    "id": {
      "type": "string",
      "title": "ID",
      "description": "The job's ID",
      "order": 3
    },
    "status": {
      "type": "string",
      "title": "Status",
      "description": "The job's status: Success, InProgress or Failure",
      "order": 1
    }
  },
  "required": [
    "analyzerId",
    "artifact",
    "date",
    "id",
    "status"
  ],
  "definitions": {
    "file_artifact": {
      "type": "object",
      "title": "file_artifact",
      "properties": {
        "attributes": {
          "$ref": "#/definitions/file_attributes",
          "title": "Attributes",
          "order": 1
        }
      },
      "definitions": {
        "file_attributes": {
          "type": "object",
          "title": "file_attributes",
          "properties": {
            "content-type": {
              "type": "string",
              "title": "Content Type",
              "description": "The files mime type",
              "order": 3
            },
            "dataType": {
              "type": "string",
              "title": "Data Type",
              "description": "Data type e.g. domain, ip, file",
              "order": 1
            },
            "filename": {
              "type": "string",
              "title": "File Name",
              "description": "File name",
              "order": 4
            },
            "tlp": {
              "type": "integer",
              "title": "TLP",
              "description": "Traffic Light Protocol level e.g. 1",
              "order": 2
            }
          }
        }
      }
    },
    "file_attributes": {
      "type": "object",
      "title": "file_attributes",
      "properties": {
        "content-type": {
          "type": "string",
          "title": "Content Type",
          "description": "The files mime type",
          "order": 3
        },
        "dataType": {
          "type": "string",
          "title": "Data Type",
          "description": "Data type e.g. domain, ip, file",
          "order": 1
        },
        "filename": {
          "type": "string",
          "title": "File Name",
          "description": "File name",
          "order": 4
        },
        "tlp": {
          "type": "integer",
          "title": "TLP",
          "description": "Traffic Light Protocol level e.g. 1",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
