# Redefining themes with subthemes
subthemes = {
    "Networking": {
        "DNS/HTTP": ["dns", "http"],
        "TCP/UDP/IP": ["tcp", "udp", "ip "],
        "Security": ["ssl", "tls"]
    },
    "Testing": {
        "Unit Testing": ["unit test", "unittest"],
        "Integration Testing": ["integration test"],
        "Test Automation": ["automated test", "automation"]
    },
    "GUI": {
        "User Experience": ["ux", "user experience"],
        "Interface Design": ["ui", "interface", "design"],
        "Graphic Elements": ["graphic", "visual"]
    },
    "Update and Installation": {
        "Installation Issues": ["install", "setup"],
        "Update Problems": ["update", "upgrade"],
        "Configuration": ["configure", "configuration"]
    },
    "Performance": {
        "Speed/Optimization": ["performance", "speed", "optimize"],
        "Latency Issues": ["latency"],
        "Resource Usage": ["resource", "memory", "cpu"]
    },
    "CI/CD": {
        "Integration Tools": ["jenkins", "travis", "ci/cd"],
        "Deployment Processes": ["deployment", "deploy"],
        "Pipeline Configuration": ["pipeline"]
    },
    "Security": {
        "Authentication": ["auth", "authentication"],
        "Encryption": ["encrypt"],
        "Vulnerabilities": ["vulnerability", "security"]
    },
    "Database": {
        "SQL/NoSQL": ["sql", "nosql"],
        "Performance": ["database performance", "db performance"],
        "Configuration": ["database config", "db config"]
    },
    "API": {
        "REST/Web Services": ["api", "rest", "web service"],
        "JSON/XML": ["json", "xml"],
        "Endpoint Issues": ["endpoint"]
    },
    "Error Handling": {
        "Exceptions": ["exception"],
        "Crashes": ["crash", "fail"],
        "Bugs": ["bug", "error", "fault"]
    },
    "Cloud Services": {
        "AWS/Azure/GCP": ["aws", "azure", "gcp", "cloud"],
        "Serverless Architecture": ["serverless", "lambda"],
        "Storage Services": ["s3", "storage"]
    },
    "Other": {}
}

# Function to categorize issues based on title and description with subthemes
def categorize_issue_with_subthemes(title, description):
    text = f"{title} {description}".lower()

    # Find the themes and subthemes that match
    for main_theme, subthemes_dict in subthemes.items():
        for sub_theme, keywords in subthemes_dict.items():
            for keyword in keywords:
                if re.search(r"\b" + re.escape(keyword) + r"\b", text):
                    return main_theme, sub_theme

    # Default to "Other" if no match is found
    return "Other", "None"

# Apply the new categorization to each issue
issues_df["Main Theme"], issues_df["Sub Theme"] = zip(*issues_df.apply(lambda row: categorize_issue_with_subthemes(row["Issue Title"], row["Issue Details"]), axis=1))

# Count of issues per main theme and sub theme
theme_subtheme_counts = issues_df.groupby(["Main Theme", "Sub Theme"]).size().reset_index(name="Count")

theme_subtheme_counts.head()  # Display the first few rows for review
