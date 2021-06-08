# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Check SPF records on a domain"


class Input:
    HOSTNAME = "hostname"
    

class Output:
    RESPONSE = "response"
    

class SpfInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "hostname": {
      "type": "string",
      "title": "Hostname",
      "description": "The hostname to look up",
      "order": 1
    }
  },
  "required": [
    "hostname"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SpfOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "response": {
      "$ref": "#/definitions/SPF_Output",
      "title": "Response",
      "description": "Response",
      "order": 1
    }
  },
  "required": [
    "response"
  ],
  "definitions": {
    "SPF_Information": {
      "type": "object",
      "title": "SPF_Information",
      "properties": {
        "Description": {
          "type": "string",
          "title": "Description",
          "order": 1
        },
        "Prefix": {
          "type": "string",
          "title": "Prefix",
          "order": 2
        },
        "PrefixDesc": {
          "type": "string",
          "title": "PrefixDesc",
          "order": 3
        },
        "Type": {
          "type": "string",
          "title": "Type",
          "order": 4
        },
        "Value": {
          "type": "string",
          "title": "Value",
          "order": 5
        }
      }
    },
    "SPF_Output": {
      "type": "object",
      "title": "SPF_Output",
      "properties": {
        "Command": {
          "type": "string",
          "title": "Command",
          "order": 20
        },
        "CommandArgument": {
          "type": "string",
          "title": "CommandArgument",
          "order": 1
        },
        "DnsServiceProvider": {
          "type": "string",
          "title": "DnsServiceProvider",
          "order": 8
        },
        "EmailServiceProvider": {
          "type": "string",
          "title": "EmailServiceProvider",
          "order": 22
        },
        "Errors": {
          "type": "array",
          "title": "Errors",
          "items": {
            "type": "object"
          },
          "order": 2
        },
        "Failed": {
          "type": "array",
          "title": "Failed",
          "items": {
            "type": "object"
          },
          "order": 6
        },
        "HasSubscriptions": {
          "type": "boolean",
          "title": "HasSubscriptions",
          "order": 14
        },
        "Information": {
          "type": "array",
          "title": "Information",
          "items": {
            "$ref": "#/definitions/SPF_Information"
          },
          "order": 3
        },
        "IsBruteForce": {
          "type": "boolean",
          "title": "IsBruteForce",
          "order": 18
        },
        "IsEndpoint": {
          "type": "boolean",
          "title": "IsEndpoint",
          "order": 21
        },
        "IsTransitioned": {
          "type": "boolean",
          "title": "IsTransitioned",
          "order": 13
        },
        "MultiInformation": {
          "type": "array",
          "title": "MultiInformation",
          "items": {
            "type": "object"
          },
          "order": 11
        },
        "MxRep": {
          "type": "integer",
          "title": "MxRep",
          "order": 23
        },
        "Passed": {
          "type": "array",
          "title": "Passed",
          "items": {
            "$ref": "#/definitions/SPF_Passed"
          },
          "order": 7
        },
        "RelatedIP": {
          "type": "string",
          "title": "RelatedIP",
          "order": 19
        },
        "RelatedLookups": {
          "type": "array",
          "title": "RelatedLookups",
          "items": {
            "$ref": "#/definitions/SPF_RelatedLookups"
          },
          "order": 4
        },
        "ReportingNameServer": {
          "type": "string",
          "title": "ReportingNameServer",
          "order": 15
        },
        "TimeRecorded": {
          "type": "string",
          "title": "TimeRecorded",
          "order": 5
        },
        "TimeToComplete": {
          "type": "string",
          "title": "TimeToComplete",
          "order": 17
        },
        "Timeouts": {
          "type": "array",
          "title": "Timeouts",
          "items": {
            "type": "object"
          },
          "order": 16
        },
        "Transcript": {
          "type": "array",
          "title": "Transcript",
          "items": {
            "$ref": "#/definitions/SPF_Transcript"
          },
          "order": 12
        },
        "UID": {
          "type": "string",
          "title": "UID",
          "order": 9
        },
        "Warnings": {
          "type": "array",
          "title": "Warnings",
          "items": {
            "type": "object"
          },
          "order": 10
        }
      },
      "definitions": {
        "SPF_Information": {
          "type": "object",
          "title": "SPF_Information",
          "properties": {
            "Description": {
              "type": "string",
              "title": "Description",
              "order": 1
            },
            "Prefix": {
              "type": "string",
              "title": "Prefix",
              "order": 2
            },
            "PrefixDesc": {
              "type": "string",
              "title": "PrefixDesc",
              "order": 3
            },
            "Type": {
              "type": "string",
              "title": "Type",
              "order": 4
            },
            "Value": {
              "type": "string",
              "title": "Value",
              "order": 5
            }
          }
        },
        "SPF_Passed": {
          "type": "object",
          "title": "SPF_Passed",
          "properties": {
            "ID": {
              "type": "integer",
              "title": "ID",
              "order": 1
            },
            "Info": {
              "type": "string",
              "title": "Info",
              "order": 2
            },
            "IsExcludedByUser": {
              "type": "boolean",
              "title": "IsExcludedByUser",
              "order": 3
            },
            "Name": {
              "type": "string",
              "title": "Name",
              "order": 4
            },
            "PublicDescription": {
              "type": "string",
              "title": "PublicDescription",
              "order": 5
            },
            "Url": {
              "type": "string",
              "title": "Url",
              "order": 6
            }
          }
        },
        "SPF_RelatedLookups": {
          "type": "object",
          "title": "SPF_RelatedLookups",
          "properties": {
            "Command": {
              "type": "string",
              "title": "Command",
              "order": 1
            },
            "CommandArgument": {
              "type": "string",
              "title": "CommandArgument",
              "order": 2
            },
            "Name": {
              "type": "string",
              "title": "Name",
              "order": 3
            },
            "URL": {
              "type": "string",
              "title": "URL",
              "order": 4
            }
          }
        },
        "SPF_Transcript": {
          "type": "object",
          "title": "SPF_Transcript",
          "properties": {
            "Answers": {
              "type": "string",
              "title": "Answers",
              "order": 1
            },
            "Authoritative": {
              "type": "string",
              "title": "Authoritative",
              "order": 2
            },
            "Depth": {
              "type": "string",
              "title": "Depth",
              "order": 3
            },
            "ElapsedTime": {
              "type": "string",
              "title": "ElapsedTime",
              "order": 4
            },
            "Question": {
              "type": "string",
              "title": "Question",
              "order": 5
            },
            "Result": {
              "type": "string",
              "title": "Result",
              "order": 6
            },
            "ServerIP": {
              "type": "string",
              "title": "ServerIP",
              "order": 7
            },
            "ServerName": {
              "type": "string",
              "title": "ServerName",
              "order": 8
            },
            "TimeStamp": {
              "type": "string",
              "title": "TimeStamp",
              "order": 9
            }
          }
        }
      }
    },
    "SPF_Passed": {
      "type": "object",
      "title": "SPF_Passed",
      "properties": {
        "ID": {
          "type": "integer",
          "title": "ID",
          "order": 1
        },
        "Info": {
          "type": "string",
          "title": "Info",
          "order": 2
        },
        "IsExcludedByUser": {
          "type": "boolean",
          "title": "IsExcludedByUser",
          "order": 3
        },
        "Name": {
          "type": "string",
          "title": "Name",
          "order": 4
        },
        "PublicDescription": {
          "type": "string",
          "title": "PublicDescription",
          "order": 5
        },
        "Url": {
          "type": "string",
          "title": "Url",
          "order": 6
        }
      }
    },
    "SPF_RelatedLookups": {
      "type": "object",
      "title": "SPF_RelatedLookups",
      "properties": {
        "Command": {
          "type": "string",
          "title": "Command",
          "order": 1
        },
        "CommandArgument": {
          "type": "string",
          "title": "CommandArgument",
          "order": 2
        },
        "Name": {
          "type": "string",
          "title": "Name",
          "order": 3
        },
        "URL": {
          "type": "string",
          "title": "URL",
          "order": 4
        }
      }
    },
    "SPF_Transcript": {
      "type": "object",
      "title": "SPF_Transcript",
      "properties": {
        "Answers": {
          "type": "string",
          "title": "Answers",
          "order": 1
        },
        "Authoritative": {
          "type": "string",
          "title": "Authoritative",
          "order": 2
        },
        "Depth": {
          "type": "string",
          "title": "Depth",
          "order": 3
        },
        "ElapsedTime": {
          "type": "string",
          "title": "ElapsedTime",
          "order": 4
        },
        "Question": {
          "type": "string",
          "title": "Question",
          "order": 5
        },
        "Result": {
          "type": "string",
          "title": "Result",
          "order": 6
        },
        "ServerIP": {
          "type": "string",
          "title": "ServerIP",
          "order": 7
        },
        "ServerName": {
          "type": "string",
          "title": "ServerName",
          "order": 8
        },
        "TimeStamp": {
          "type": "string",
          "title": "TimeStamp",
          "order": 9
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)