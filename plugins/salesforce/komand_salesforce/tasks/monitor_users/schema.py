# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get information about users, their login history and changes made to user data"


class Input:
    pass

class State:
    pass

class Output:
    USERS = "users"
    

class MonitorUsersInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class MonitorUsersState(insightconnect_plugin_runtime.State):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class MonitorUsersOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
  {
     "type": "array",
     "title": "Users",
     "description": "Information about users, their login history and changes made to user data",
     "items": {
     "$ref": "#/definitions/userData"
  },
  "definitions": {
    "userData": {
      "type": "object",
      "title": "userData",
      "properties": {
        "alias": {
          "type": "string",
          "title": "Alias",
          "description": "The user’s alias",
          "order": 6
        },
        "application": {
          "type": "string",
          "title": "Application",
          "description": "The application used to access the organization",
          "order": 14
        },
        "browser": {
          "type": "string",
          "title": "Browser",
          "description": "The current browser version",
          "order": 15
        },
        "dataType": {
          "type": "string",
          "title": "Data Type",
          "description": "Type of the data",
          "order": 1
        },
        "email": {
          "type": "string",
          "title": "Email",
          "description": "The user’s email address",
          "order": 5
        },
        "firstName": {
          "type": "string",
          "title": "First Name",
          "description": "The user’s first name",
          "order": 3
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The ID of the user",
          "order": 2
        },
        "isActive": {
          "type": "boolean",
          "title": "Is Active",
          "description": "Indicates whether the user has access to log in (true) or not (false)",
          "order": 7
        },
        "lastName": {
          "type": "string",
          "title": "Last Name",
          "description": "The user’s last name",
          "order": 4
        },
        "loginTime": {
          "type": "string",
          "title": "Login Time",
          "description": "The time of user login. Time zone is based on GMT",
          "order": 8
        },
        "loginType": {
          "type": "string",
          "title": "Login Type",
          "description": "The type of login used to access the session",
          "order": 10
        },
        "loginUrl": {
          "type": "string",
          "title": "Login URL",
          "description": "URL from which the login request is coming",
          "order": 11
        },
        "sourceIp": {
          "type": "string",
          "title": "Source IP",
          "description": "IP address of the machine from which the login request is coming. The address can be an IPv4 or IPv6 address",
          "order": 12
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Displays the status of the attempted login. Status is either success or a reason for failure",
          "order": 13
        },
        "userId": {
          "type": "string",
          "title": "User ID",
          "description": "ID of the user logging in",
          "order": 9
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)