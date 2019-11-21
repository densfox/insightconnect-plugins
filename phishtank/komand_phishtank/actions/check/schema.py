# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Submit URL to PhishTank"


class Input:
    URL = "url"
    

class Output:
    IN_DATABASE = "in_database"
    PHISH_DETAIL_URL = "phish_detail_url"
    PHISH_ID = "phish_id"
    SUBMITTED_AT = "submitted_at"
    URL = "url"
    VALID = "valid"
    VERIFIED = "verified"
    VERIFIED_AT = "verified_at"
    

class CheckInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "url": {
      "type": "string",
      "title": "URL",
      "description": "URL to Submit",
      "order": 1
    }
  },
  "required": [
    "url"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CheckOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "in_database": {
      "type": "boolean",
      "title": "In Database",
      "description": "If the URL is in the PhishTank database",
      "order": 2
    },
    "phish_detail_url": {
      "type": "string",
      "title": "Phish Detail URL",
      "description": "PhishTank detail URL for the phish, where you can view data about the phish, including a screenshot and the community votes",
      "order": 4
    },
    "phish_id": {
      "type": "string",
      "title": "Phish ID",
      "description": "The ID number by which PhishTank refers to a phish submission",
      "order": 3
    },
    "submitted_at": {
      "type": "string",
      "title": "Submitted At",
      "displayType": "date",
      "description": "The date and time at which this phish was reported to PhishTank",
      "format": "date-time",
      "order": 8
    },
    "url": {
      "type": "string",
      "title": "URL",
      "description": "Submitted URL",
      "order": 1
    },
    "valid": {
      "type": "boolean",
      "title": "Valid",
      "description": "Whether the phish is valid or not",
      "order": 7
    },
    "verified": {
      "type": "boolean",
      "title": "Verified",
      "description": "Whether or not this phish has been verified by the PhishTank community",
      "order": 5
    },
    "verified_at": {
      "type": "string",
      "title": "Verified At",
      "displayType": "date",
      "description": "The date and time at which the phish was verified as valid by the PhishTank community",
      "format": "date-time",
      "order": 6
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
