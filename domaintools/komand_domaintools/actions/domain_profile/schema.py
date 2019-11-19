# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Provides basic domain name registration details and a preview of additional data"


class Input:
    DOMAIN = "domain"
    

class Output:
    RESPONSE = "response"
    

class DomainProfileInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "domain": {
      "type": "string",
      "title": "Domain",
      "description": "Domain name you wish to query",
      "order": 1
    }
  },
  "required": [
    "domain"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DomainProfileOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "response": {
      "$ref": "#/definitions/domain_profile_response",
      "title": "Response",
      "description": "Response",
      "order": 1
    }
  },
  "definitions": {
    "domain_profile_history": {
      "type": "object",
      "title": "domain_profile_history",
      "properties": {
        "ip_address": {
          "$ref": "#/definitions/ip_address",
          "title": "IP Address",
          "order": 1
        },
        "name_server": {
          "$ref": "#/definitions/ip_address",
          "title": "Name Server",
          "order": 2
        },
        "registrar": {
          "$ref": "#/definitions/registrar",
          "title": "Registrar",
          "order": 3
        },
        "whois": {
          "$ref": "#/definitions/whois",
          "title": "Whois",
          "order": 4
        }
      },
      "definitions": {
        "ip_address": {
          "type": "object",
          "title": "ip_address",
          "properties": {
            "events": {
              "type": "integer",
              "title": "Events",
              "order": 1
            },
            "product_url": {
              "type": "string",
              "title": "Product Url",
              "order": 2
            },
            "timespan_in_years": {
              "type": "integer",
              "title": "Timespan In Years",
              "order": 3
            }
          }
        },
        "registrar": {
          "type": "object",
          "title": "registrar",
          "properties": {
            "abuse_contact_email": {
              "type": "string",
              "title": "Abuse Contact Email",
              "order": 1
            },
            "abuse_contact_phone": {
              "type": "string",
              "title": "Abuse Contact Phone",
              "order": 2
            },
            "iana_id": {
              "type": "string",
              "title": "Iana Id",
              "order": 3
            },
            "name": {
              "type": "string",
              "title": "Name",
              "order": 4
            },
            "url": {
              "type": "string",
              "title": "Url",
              "order": 5
            },
            "whois_server": {
              "type": "string",
              "title": "Whois Server",
              "order": 6
            }
          }
        },
        "whois": {
          "type": "object",
          "title": "whois",
          "properties": {
            "earliest_event": {
              "type": "string",
              "title": "Earliest Event",
              "order": 1
            },
            "product_url": {
              "type": "string",
              "title": "Product Url",
              "order": 2
            },
            "records": {
              "type": "integer",
              "title": "Records",
              "order": 3
            }
          }
        }
      }
    },
    "domain_profile_response": {
      "type": "object",
      "title": "domain_profile_response",
      "properties": {
        "history": {
          "$ref": "#/definitions/domain_profile_history",
          "title": "History",
          "order": 1
        },
        "name_servers": {
          "type": "array",
          "title": "Name Servers",
          "items": {
            "$ref": "#/definitions/name_servers"
          },
          "order": 2
        },
        "registrant": {
          "$ref": "#/definitions/registrant",
          "title": "Registrant",
          "order": 3
        },
        "registration": {
          "$ref": "#/definitions/registration",
          "title": "Registration",
          "order": 4
        },
        "seo": {
          "$ref": "#/definitions/seo",
          "title": "Seo",
          "order": 5
        },
        "server": {
          "$ref": "#/definitions/server",
          "title": "Server",
          "order": 6
        },
        "website_data": {
          "$ref": "#/definitions/website_data",
          "title": "Website Data",
          "order": 7
        }
      },
      "definitions": {
        "domain_profile_history": {
          "type": "object",
          "title": "domain_profile_history",
          "properties": {
            "ip_address": {
              "$ref": "#/definitions/ip_address",
              "title": "IP Address",
              "order": 1
            },
            "name_server": {
              "$ref": "#/definitions/ip_address",
              "title": "Name Server",
              "order": 2
            },
            "registrar": {
              "$ref": "#/definitions/registrar",
              "title": "Registrar",
              "order": 3
            },
            "whois": {
              "$ref": "#/definitions/whois",
              "title": "Whois",
              "order": 4
            }
          },
          "definitions": {
            "ip_address": {
              "type": "object",
              "title": "ip_address",
              "properties": {
                "events": {
                  "type": "integer",
                  "title": "Events",
                  "order": 1
                },
                "product_url": {
                  "type": "string",
                  "title": "Product Url",
                  "order": 2
                },
                "timespan_in_years": {
                  "type": "integer",
                  "title": "Timespan In Years",
                  "order": 3
                }
              }
            },
            "registrar": {
              "type": "object",
              "title": "registrar",
              "properties": {
                "abuse_contact_email": {
                  "type": "string",
                  "title": "Abuse Contact Email",
                  "order": 1
                },
                "abuse_contact_phone": {
                  "type": "string",
                  "title": "Abuse Contact Phone",
                  "order": 2
                },
                "iana_id": {
                  "type": "string",
                  "title": "Iana Id",
                  "order": 3
                },
                "name": {
                  "type": "string",
                  "title": "Name",
                  "order": 4
                },
                "url": {
                  "type": "string",
                  "title": "Url",
                  "order": 5
                },
                "whois_server": {
                  "type": "string",
                  "title": "Whois Server",
                  "order": 6
                }
              }
            },
            "whois": {
              "type": "object",
              "title": "whois",
              "properties": {
                "earliest_event": {
                  "type": "string",
                  "title": "Earliest Event",
                  "order": 1
                },
                "product_url": {
                  "type": "string",
                  "title": "Product Url",
                  "order": 2
                },
                "records": {
                  "type": "integer",
                  "title": "Records",
                  "order": 3
                }
              }
            }
          }
        },
        "ip_address": {
          "type": "object",
          "title": "ip_address",
          "properties": {
            "events": {
              "type": "integer",
              "title": "Events",
              "order": 1
            },
            "product_url": {
              "type": "string",
              "title": "Product Url",
              "order": 2
            },
            "timespan_in_years": {
              "type": "integer",
              "title": "Timespan In Years",
              "order": 3
            }
          }
        },
        "meta": {
          "type": "object",
          "title": "meta",
          "properties": {
            "description": {
              "type": "string",
              "title": "Description",
              "order": 1
            }
          }
        },
        "name_servers": {
          "type": "object",
          "title": "name_servers",
          "properties": {
            "product_url": {
              "type": "string",
              "title": "Product Url",
              "order": 1
            },
            "server": {
              "type": "string",
              "title": "Server",
              "order": 2
            }
          }
        },
        "registrant": {
          "type": "object",
          "title": "registrant",
          "properties": {
            "domains": {
              "type": "integer",
              "title": "Domains",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "order": 2
            },
            "product_url": {
              "type": "string",
              "title": "Product Url",
              "order": 3
            }
          }
        },
        "registrar": {
          "type": "object",
          "title": "registrar",
          "properties": {
            "abuse_contact_email": {
              "type": "string",
              "title": "Abuse Contact Email",
              "order": 1
            },
            "abuse_contact_phone": {
              "type": "string",
              "title": "Abuse Contact Phone",
              "order": 2
            },
            "iana_id": {
              "type": "string",
              "title": "Iana Id",
              "order": 3
            },
            "name": {
              "type": "string",
              "title": "Name",
              "order": 4
            },
            "url": {
              "type": "string",
              "title": "Url",
              "order": 5
            },
            "whois_server": {
              "type": "string",
              "title": "Whois Server",
              "order": 6
            }
          }
        },
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
        "seo": {
          "type": "object",
          "title": "seo",
          "properties": {
            "product_url": {
              "type": "string",
              "title": "Product Url",
              "order": 1
            },
            "score": {
              "type": "integer",
              "title": "Score",
              "order": 2
            }
          }
        },
        "server": {
          "type": "object",
          "title": "server",
          "properties": {
            "ip_address": {
              "type": "string",
              "title": "IP Address",
              "order": 1
            },
            "other_domains": {
              "type": "integer",
              "title": "Other Domains",
              "order": 2
            },
            "product_url": {
              "type": "string",
              "title": "Product Url",
              "order": 3
            }
          }
        },
        "website_data": {
          "type": "object",
          "title": "website_data",
          "properties": {
            "meta": {
              "$ref": "#/definitions/meta",
              "title": "Meta",
              "order": 1
            },
            "product_url": {
              "type": "string",
              "title": "Product Url",
              "order": 2
            },
            "response_code": {
              "type": "integer",
              "title": "Response Code",
              "order": 3
            },
            "server": {
              "type": "string",
              "title": "Server",
              "order": 4
            },
            "title": {
              "type": "string",
              "title": "Title",
              "order": 5
            }
          },
          "definitions": {
            "meta": {
              "type": "object",
              "title": "meta",
              "properties": {
                "description": {
                  "type": "string",
                  "title": "Description",
                  "order": 1
                }
              }
            }
          }
        },
        "whois": {
          "type": "object",
          "title": "whois",
          "properties": {
            "earliest_event": {
              "type": "string",
              "title": "Earliest Event",
              "order": 1
            },
            "product_url": {
              "type": "string",
              "title": "Product Url",
              "order": 2
            },
            "records": {
              "type": "integer",
              "title": "Records",
              "order": 3
            }
          }
        }
      }
    },
    "ip_address": {
      "type": "object",
      "title": "ip_address",
      "properties": {
        "events": {
          "type": "integer",
          "title": "Events",
          "order": 1
        },
        "product_url": {
          "type": "string",
          "title": "Product Url",
          "order": 2
        },
        "timespan_in_years": {
          "type": "integer",
          "title": "Timespan In Years",
          "order": 3
        }
      }
    },
    "meta": {
      "type": "object",
      "title": "meta",
      "properties": {
        "description": {
          "type": "string",
          "title": "Description",
          "order": 1
        }
      }
    },
    "name_servers": {
      "type": "object",
      "title": "name_servers",
      "properties": {
        "product_url": {
          "type": "string",
          "title": "Product Url",
          "order": 1
        },
        "server": {
          "type": "string",
          "title": "Server",
          "order": 2
        }
      }
    },
    "registrant": {
      "type": "object",
      "title": "registrant",
      "properties": {
        "domains": {
          "type": "integer",
          "title": "Domains",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "order": 2
        },
        "product_url": {
          "type": "string",
          "title": "Product Url",
          "order": 3
        }
      }
    },
    "registrar": {
      "type": "object",
      "title": "registrar",
      "properties": {
        "abuse_contact_email": {
          "type": "string",
          "title": "Abuse Contact Email",
          "order": 1
        },
        "abuse_contact_phone": {
          "type": "string",
          "title": "Abuse Contact Phone",
          "order": 2
        },
        "iana_id": {
          "type": "string",
          "title": "Iana Id",
          "order": 3
        },
        "name": {
          "type": "string",
          "title": "Name",
          "order": 4
        },
        "url": {
          "type": "string",
          "title": "Url",
          "order": 5
        },
        "whois_server": {
          "type": "string",
          "title": "Whois Server",
          "order": 6
        }
      }
    },
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
    "seo": {
      "type": "object",
      "title": "seo",
      "properties": {
        "product_url": {
          "type": "string",
          "title": "Product Url",
          "order": 1
        },
        "score": {
          "type": "integer",
          "title": "Score",
          "order": 2
        }
      }
    },
    "server": {
      "type": "object",
      "title": "server",
      "properties": {
        "ip_address": {
          "type": "string",
          "title": "IP Address",
          "order": 1
        },
        "other_domains": {
          "type": "integer",
          "title": "Other Domains",
          "order": 2
        },
        "product_url": {
          "type": "string",
          "title": "Product Url",
          "order": 3
        }
      }
    },
    "website_data": {
      "type": "object",
      "title": "website_data",
      "properties": {
        "meta": {
          "$ref": "#/definitions/meta",
          "title": "Meta",
          "order": 1
        },
        "product_url": {
          "type": "string",
          "title": "Product Url",
          "order": 2
        },
        "response_code": {
          "type": "integer",
          "title": "Response Code",
          "order": 3
        },
        "server": {
          "type": "string",
          "title": "Server",
          "order": 4
        },
        "title": {
          "type": "string",
          "title": "Title",
          "order": 5
        }
      },
      "definitions": {
        "meta": {
          "type": "object",
          "title": "meta",
          "properties": {
            "description": {
              "type": "string",
              "title": "Description",
              "order": 1
            }
          }
        }
      }
    },
    "whois": {
      "type": "object",
      "title": "whois",
      "properties": {
        "earliest_event": {
          "type": "string",
          "title": "Earliest Event",
          "order": 1
        },
        "product_url": {
          "type": "string",
          "title": "Product Url",
          "order": 2
        },
        "records": {
          "type": "integer",
          "title": "Records",
          "order": 3
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
