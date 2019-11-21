# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Suspend a User"


class Input:
    USER = "user"
    

class Output:
    USER = "user"
    

class SuspendUserInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "user": {
      "type": "string",
      "title": "User",
      "description": "The user's primary email address, unique ID, or alias email",
      "order": 1
    }
  },
  "required": [
    "user"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SuspendUserOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "user": {
      "$ref": "#/definitions/user",
      "title": "User",
      "description": "User Response Returned",
      "order": 1
    }
  },
  "definitions": {
    "email": {
      "type": "object",
      "title": "email",
      "properties": {
        "address": {
          "type": "string",
          "title": "Address",
          "description": "Email address",
          "order": 1
        },
        "primary": {
          "type": "boolean",
          "title": "Primary",
          "description": "True if primary email",
          "order": 2
        }
      }
    },
    "name": {
      "type": "object",
      "title": "name",
      "properties": {
        "familyName": {
          "type": "string",
          "title": "FamilyName",
          "description": "Family name",
          "order": 2
        },
        "fullName": {
          "type": "string",
          "title": "FullName",
          "description": "Full name",
          "order": 3
        },
        "givenName": {
          "type": "string",
          "title": "GivenName",
          "description": "Given name",
          "order": 1
        }
      }
    },
    "user": {
      "type": "object",
      "title": "user",
      "properties": {
        "agreedToTerms": {
          "type": "boolean",
          "title": "AgreedToTerms",
          "description": "True if agreed to TOS",
          "order": 12
        },
        "alias": {
          "type": "array",
          "title": "Alias",
          "description": "Aliases",
          "items": {
            "type": "string"
          },
          "order": 9
        },
        "changePasswordAtNextLogin": {
          "type": "boolean",
          "title": "ChangePasswordAtNextLogin",
          "description": "True if must change password at login",
          "order": 10
        },
        "creationTime": {
          "type": "string",
          "title": "CreationTime",
          "displayType": "date",
          "description": "Creation time",
          "format": "date-time",
          "order": 14
        },
        "customerId": {
          "type": "string",
          "title": "CustomerId",
          "order": 2
        },
        "emails": {
          "type": "array",
          "title": "Emails",
          "description": "Emails",
          "items": {
            "$ref": "#/definitions/email"
          },
          "order": 8
        },
        "id": {
          "type": "string",
          "title": "Id",
          "description": "User ID",
          "order": 1
        },
        "ipWhitelisted": {
          "type": "boolean",
          "title": "IpWhitelisted",
          "description": "True if ip whitelisted",
          "order": 11
        },
        "isAdmin": {
          "type": "boolean",
          "title": "IsAdmin",
          "description": "True if admin",
          "order": 4
        },
        "isDelegatedAdmin": {
          "type": "boolean",
          "title": "IsDelegatedAdmin",
          "description": "True if delegated admin",
          "order": 5
        },
        "lastLoginTime": {
          "type": "string",
          "title": "LastLoginTime",
          "displayType": "date",
          "description": "Last login time",
          "format": "date-time",
          "order": 13
        },
        "name": {
          "$ref": "#/definitions/name",
          "title": "Name",
          "description": "Name",
          "order": 3
        },
        "suspended": {
          "type": "boolean",
          "title": "Suspended",
          "description": "True if suspended",
          "order": 6
        },
        "suspensionReason": {
          "type": "string",
          "title": "SuspensionReason",
          "description": "Suspension Reason",
          "order": 7
        }
      },
      "definitions": {
        "email": {
          "type": "object",
          "title": "email",
          "properties": {
            "address": {
              "type": "string",
              "title": "Address",
              "description": "Email address",
              "order": 1
            },
            "primary": {
              "type": "boolean",
              "title": "Primary",
              "description": "True if primary email",
              "order": 2
            }
          }
        },
        "name": {
          "type": "object",
          "title": "name",
          "properties": {
            "familyName": {
              "type": "string",
              "title": "FamilyName",
              "description": "Family name",
              "order": 2
            },
            "fullName": {
              "type": "string",
              "title": "FullName",
              "description": "Full name",
              "order": 3
            },
            "givenName": {
              "type": "string",
              "title": "GivenName",
              "description": "Given name",
              "order": 1
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
