# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Get a Docker network by ID"


class Input:
    ID = "id"
    

class Output:
    NETWORK = "network"
    

class NetworkGetInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "string",
      "title": "ID",
      "description": "Network ID",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class NetworkGetOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "network": {
      "$ref": "#/definitions/network",
      "title": "Network",
      "description": "Network",
      "order": 1
    }
  },
  "definitions": {
    "container": {
      "type": "object",
      "title": "container",
      "properties": {
        "created_at": {
          "type": "string",
          "title": "Created At",
          "displayType": "date",
          "format": "date-time",
          "order": 4
        },
        "id": {
          "type": "string",
          "title": "Id",
          "order": 1
        },
        "image": {
          "$ref": "#/definitions/image",
          "title": "Image",
          "order": 3
        },
        "labels": {
          "type": "object",
          "title": "Labels",
          "order": 6
        },
        "name": {
          "type": "string",
          "title": "Name",
          "order": 2
        },
        "size_rootfs": {
          "type": "integer",
          "title": "Size Rootfs",
          "order": 8
        },
        "size_rw": {
          "type": "integer",
          "title": "Size Rw",
          "order": 7
        },
        "status": {
          "type": "string",
          "title": "Status",
          "order": 5
        }
      },
      "definitions": {
        "image": {
          "type": "object",
          "title": "image",
          "properties": {
            "containers": {
              "type": "integer",
              "title": "Containers",
              "order": 6
            },
            "created_at": {
              "type": "string",
              "title": "Created At",
              "displayType": "date",
              "format": "date-time",
              "order": 3
            },
            "id": {
              "type": "string",
              "title": "Id",
              "order": 1
            },
            "labels": {
              "type": "object",
              "title": "Labels",
              "order": 4
            },
            "parent_id": {
              "type": "string",
              "title": "Parent Id",
              "order": 2
            },
            "repo_digests": {
              "type": "array",
              "title": "Repo Digests",
              "items": {
                "type": "string"
              },
              "order": 10
            },
            "repo_tags": {
              "type": "array",
              "title": "Repo Tags",
              "items": {
                "type": "string"
              },
              "order": 9
            },
            "shared_size": {
              "type": "integer",
              "title": "Shared Size",
              "order": 7
            },
            "size": {
              "type": "integer",
              "title": "Size",
              "order": 5
            },
            "virtual_size": {
              "type": "integer",
              "title": "Virtual Size",
              "order": 8
            }
          }
        }
      }
    },
    "image": {
      "type": "object",
      "title": "image",
      "properties": {
        "containers": {
          "type": "integer",
          "title": "Containers",
          "order": 6
        },
        "created_at": {
          "type": "string",
          "title": "Created At",
          "displayType": "date",
          "format": "date-time",
          "order": 3
        },
        "id": {
          "type": "string",
          "title": "Id",
          "order": 1
        },
        "labels": {
          "type": "object",
          "title": "Labels",
          "order": 4
        },
        "parent_id": {
          "type": "string",
          "title": "Parent Id",
          "order": 2
        },
        "repo_digests": {
          "type": "array",
          "title": "Repo Digests",
          "items": {
            "type": "string"
          },
          "order": 10
        },
        "repo_tags": {
          "type": "array",
          "title": "Repo Tags",
          "items": {
            "type": "string"
          },
          "order": 9
        },
        "shared_size": {
          "type": "integer",
          "title": "Shared Size",
          "order": 7
        },
        "size": {
          "type": "integer",
          "title": "Size",
          "order": 5
        },
        "virtual_size": {
          "type": "integer",
          "title": "Virtual Size",
          "order": 8
        }
      }
    },
    "network": {
      "type": "object",
      "title": "network",
      "properties": {
        "containers": {
          "type": "array",
          "title": "Containers",
          "items": {
            "$ref": "#/definitions/container"
          },
          "order": 4
        },
        "id": {
          "type": "string",
          "title": "Id",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "order": 3
        },
        "short_id": {
          "type": "string",
          "title": "Short Id",
          "order": 2
        }
      },
      "definitions": {
        "container": {
          "type": "object",
          "title": "container",
          "properties": {
            "created_at": {
              "type": "string",
              "title": "Created At",
              "displayType": "date",
              "format": "date-time",
              "order": 4
            },
            "id": {
              "type": "string",
              "title": "Id",
              "order": 1
            },
            "image": {
              "$ref": "#/definitions/image",
              "title": "Image",
              "order": 3
            },
            "labels": {
              "type": "object",
              "title": "Labels",
              "order": 6
            },
            "name": {
              "type": "string",
              "title": "Name",
              "order": 2
            },
            "size_rootfs": {
              "type": "integer",
              "title": "Size Rootfs",
              "order": 8
            },
            "size_rw": {
              "type": "integer",
              "title": "Size Rw",
              "order": 7
            },
            "status": {
              "type": "string",
              "title": "Status",
              "order": 5
            }
          },
          "definitions": {
            "image": {
              "type": "object",
              "title": "image",
              "properties": {
                "containers": {
                  "type": "integer",
                  "title": "Containers",
                  "order": 6
                },
                "created_at": {
                  "type": "string",
                  "title": "Created At",
                  "displayType": "date",
                  "format": "date-time",
                  "order": 3
                },
                "id": {
                  "type": "string",
                  "title": "Id",
                  "order": 1
                },
                "labels": {
                  "type": "object",
                  "title": "Labels",
                  "order": 4
                },
                "parent_id": {
                  "type": "string",
                  "title": "Parent Id",
                  "order": 2
                },
                "repo_digests": {
                  "type": "array",
                  "title": "Repo Digests",
                  "items": {
                    "type": "string"
                  },
                  "order": 10
                },
                "repo_tags": {
                  "type": "array",
                  "title": "Repo Tags",
                  "items": {
                    "type": "string"
                  },
                  "order": 9
                },
                "shared_size": {
                  "type": "integer",
                  "title": "Shared Size",
                  "order": 7
                },
                "size": {
                  "type": "integer",
                  "title": "Size",
                  "order": 5
                },
                "virtual_size": {
                  "type": "integer",
                  "title": "Virtual Size",
                  "order": 8
                }
              }
            }
          }
        },
        "image": {
          "type": "object",
          "title": "image",
          "properties": {
            "containers": {
              "type": "integer",
              "title": "Containers",
              "order": 6
            },
            "created_at": {
              "type": "string",
              "title": "Created At",
              "displayType": "date",
              "format": "date-time",
              "order": 3
            },
            "id": {
              "type": "string",
              "title": "Id",
              "order": 1
            },
            "labels": {
              "type": "object",
              "title": "Labels",
              "order": 4
            },
            "parent_id": {
              "type": "string",
              "title": "Parent Id",
              "order": 2
            },
            "repo_digests": {
              "type": "array",
              "title": "Repo Digests",
              "items": {
                "type": "string"
              },
              "order": 10
            },
            "repo_tags": {
              "type": "array",
              "title": "Repo Tags",
              "items": {
                "type": "string"
              },
              "order": 9
            },
            "shared_size": {
              "type": "integer",
              "title": "Shared Size",
              "order": 7
            },
            "size": {
              "type": "integer",
              "title": "Size",
              "order": 5
            },
            "virtual_size": {
              "type": "integer",
              "title": "Virtual Size",
              "order": 8
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
