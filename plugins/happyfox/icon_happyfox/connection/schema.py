# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    APIKEY = "apiKey"
    AUTHCODE = "authCode"
    SUBDOMAIN = "subdomain"
    

class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "apiKey": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "API Key",
      "description": "HappyFox API key",
      "order": 1
    },
    "authCode": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "Auth Code",
      "description": "HappyFox auth code",
      "order": 2
    },
    "subdomain": {
      "type": "string",
      "title": "Subdomain",
      "description": "Subdomain from your HappyFox URL, for example \\"example-company\\" from \\"https://example-company.happyfox.com\\"",
      "order": 3
    }
  },
  "required": [
    "apiKey",
    "authCode",
    "subdomain"
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
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)