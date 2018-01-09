# Copyright (C) 2018 Google Inc.
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>

scope = "Audit"
description = """
  The permissions required by an auditor to access relevant resources for the
  program being audited.
  """
permissions = {
    "read": [
        "Audit",
        "Assessment",
        "Issue",
        "Snapshot",
        "ObjectPerson",
        "Relationship",
        "Document",
        "UserRole",
        "Comment",
        "Context",
    ],
    "create": [
        "Assessment",
        "Issue",
        "Comment",
    ],
    "view_object_page": [
        "__GGRC_ALL__"
    ],
    "update": [
        "Assessment",
        "Snapshot",  # Needed for mapping snapshots to Assessments/Issues
        "Issue",
    ],
    "delete": [
        "Assessment",
        "Issue"
    ],
}
