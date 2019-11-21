# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Provides the ownership record for a domain name or IP address with basic registration details"


class Input:
    QUERY = "query"
    

class Output:
    RESPONSE = "response"
    

class WhoisInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "query": {
      "type": "string",
      "title": "Query",
      "description": "Domain name or an IP address to perform a whois lookup",
      "order": 1
    }
  },
  "required": [
    "query"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class WhoisOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "response": {
      "$ref": "#/definitions/whois_response",
      "title": "Response",
      "description": "Response",
      "order": 1
    }
  },
  "definitions": {
    "registration": {
      "type": "object",
      "title": "registration",
      "properties": {
        "created": {
          "type": "string",
          "title": "Created",
          "order": 1
        },
        "expires": {
          "type": "string",
          "title": "Expires",
          "order": 2
        },
        "registrar": {
          "type": "string",
          "title": "Registrar",
          "order": 3
        },
        "statuses": {
          "type": "array",
          "title": "Statuses",
          "items": {
            "type": "string"
          },
          "order": 4
        },
        "updated": {
          "type": "string",
          "title": "Updated",
          "order": 5
        }
      }
    },
    "whois_response": {
      "type": "object",
      "title": "whois_response",
      "properties": {
        "name_servers": {
          "type": "array",
          "title": "Name Servers",
          "items": {
            "type": "string"
          },
          "order": 1
        },
        "record_source": {
          "type": "string",
          "title": "Record Source",
          "order": 2
        },
        "registrant": {
          "type": "string",
          "title": "Registrant",
          "order": 3
        },
        "registration": {
          "$ref": "#/definitions/registration",
          "title": "Registration",
          "order": 4
        },
        "whois": {
          "$ref": "#/definitions/whois_whois",
          "title": "Whois",
          "order": 5
        }
      },
      "definitions": {
        "registration": {
          "type": "object",
          "title": "registration",
          "properties": {
            "created": {
              "type": "string",
              "title": "Created",
              "order": 1
            },
            "expires": {
              "type": "string",
              "title": "Expires",
              "order": 2
            },
            "registrar": {
              "type": "string",
              "title": "Registrar",
              "order": 3
            },
            "statuses": {
              "type": "array",
              "title": "Statuses",
              "items": {
                "type": "string"
              },
              "order": 4
            },
            "updated": {
              "type": "string",
              "title": "Updated",
              "order": 5
            }
          }
        },
        "whois_whois": {
          "type": "object",
          "title": "whois_whois",
          "properties": {
            "date": {
              "type": "string",
              "title": "Date",
              "order": 1
            },
            "record": {
              "type": "string",
              "title": "Record",
              "order": 2
            }
          }
        }
      }
    },
    "whois_whois": {
      "type": "object",
      "title": "whois_whois",
      "properties": {
        "date": {
          "type": "string",
          "title": "Date",
          "order": 1
        },
        "record": {
          "type": "string",
          "title": "Record",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
