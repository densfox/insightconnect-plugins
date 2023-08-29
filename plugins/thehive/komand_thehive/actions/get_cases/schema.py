# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Retrieve list of cases"


class Input:
    pass


class Output:
    SUCCESS = "success"


class GetCasesInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetCasesOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "array",
      "title": "Success",
      "description": "List of cases",
      "items": {
        "$ref": "#/definitions/case"
      },
      "order": 1
    }
  },
  "definitions": {
    "case": {
      "type": "object",
      "title": "case",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "_id": {
          "type": "string",
          "title": "_ID",
          "description": "Alternative ID",
          "order": 2
        },
        "owner": {
          "type": "string",
          "title": "Owner",
          "description": "Case owner",
          "order": 3
        },
        "_routing": {
          "type": "string",
          "title": "Routing",
          "description": "Case routing",
          "order": 4
        },
        "_type": {
          "type": "string",
          "title": "Type",
          "description": "Case type",
          "order": 5
        },
        "caseId": {
          "type": "integer",
          "title": "Case ID",
          "description": "Case ID",
          "order": 6
        },
        "metrics": {
          "type": "object",
          "title": "Metrics",
          "description": "Case metrics",
          "order": 7
        },
        "_version": {
          "type": "integer",
          "title": "Version",
          "description": "Case version",
          "order": 8
        },
        "createdBy": {
          "type": "string",
          "title": "Created By",
          "description": "Who the case was created by",
          "order": 9
        },
        "_updatedBy": {
          "type": "string",
          "title": "Updated By",
          "description": "Who the case was updated by",
          "order": 10
        },
        "createdAt": {
          "type": "integer",
          "title": "Created At",
          "description": "Datetime in ms the case was created at",
          "order": 11
        },
        "title": {
          "type": "string",
          "title": "Case title",
          "description": "Title of the case",
          "order": 12
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "The description of the case",
          "order": 13
        },
        "severity": {
          "type": "integer",
          "title": "Severity",
          "description": "Severity of the case",
          "order": 14
        },
        "startDate": {
          "type": "integer",
          "title": "Start Date",
          "description": "Case start date (datetime in ms)",
          "order": 15
        },
        "tags": {
          "type": "array",
          "title": "Tags",
          "description": "Case tags",
          "items": {
            "type": "string"
          },
          "order": 16
        },
        "flag": {
          "type": "boolean",
          "title": "Flag",
          "description": "Something here",
          "order": 17
        },
        "tlp": {
          "type": "integer",
          "title": "TLP",
          "description": "Traffic Light Protocol level",
          "order": 18
        },
        "pap": {
          "type": "integer",
          "title": "PAP",
          "description": "Password Authenitcation Protocol",
          "order": 19
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Status of the case",
          "order": 20
        },
        "customFields": {
          "type": "object",
          "title": "Custom Fields",
          "description": "Case custom fields",
          "order": 21
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
