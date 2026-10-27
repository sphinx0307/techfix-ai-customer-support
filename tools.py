class SupportTicketTool:

    def generate_ticket(self, issue):

        issue_lower = issue.lower()

        if any(word in issue_lower for word in ["battery", "charging"]):
            category = "Battery Issue"
            priority = "Medium"

        elif any(word in issue_lower for word in ["overheat", "heating"]):
            category = "Hardware Issue"
            priority = "High"

        elif any(word in issue_lower for word in ["wifi", "network", "internet"]):
            category = "Network Issue"
            priority = "Medium"

        elif any(word in issue_lower for word in ["screen", "display"]):
            category = "Display Issue"
            priority = "Medium"

        else:
            category = "General Support"
            priority = "Low"

        ticket = f"""
---------------- SUPPORT TICKET ----------------

Issue Category : {category}

Priority       : {priority}

Department     : Technical Support

Summary:
{issue}

Status:
Draft Generated

------------------------------------------------
"""

        return ticket