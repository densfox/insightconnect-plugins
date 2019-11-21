# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    API_KEY = "api_key"
    API_TOKEN = "api_token"
    VERSION = "version"
    

class ConnectionSchema(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "api_key": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "API Key",
      "description": "API key",
      "order": 3
    },
    "api_token": {
      "$ref": "#/definitions/credential_token",
      "title": "API Token",
      "description": "API Token",
      "order": 2
    },
    "version": {
      "type": "integer",
      "title": "Version",
      "description": "Version",
      "default": 1,
      "order": 1
    }
  },
  "required": [
    "api_key",
    "api_token",
    "version"
  ],
  "definitions": {
    "credential_secret_key": {
      "id": "credential_secret_key",
      "type": "object",
      "title": "Credential: Secret Key",
      "description": "A shared secret key",
      "properties": {
        "secretKey": {
          "type": "string",
          "title": "Secret Key",
          "displayType": "password",
          "description": "The shared secret key",
          "format": "password"
        }
      },
      "required": [
        "secretKey"
      ]
    },
    "credential_token": {
      "id": "credential_token",
      "type": "object",
      "title": "Credential: Token",
      "description": "A pair of a token, and an optional domain",
      "properties": {
        "domain": {
          "type": "string",
          "title": "Domain",
          "description": "The domain for the token"
        },
        "token": {
          "type": "string",
          "title": "Token",
          "displayType": "password",
          "description": "The shared token",
          "format": "password"
        }
      },
      "required": [
        "token"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
