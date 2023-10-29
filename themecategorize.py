# Define sub-theme keywords for each main theme
sub_theme_keywords = {
    "Networking": {
        "Connection": ["connect", "dns", "proxy", "url"],
        "Protocol": ["http", "https"],
        "Port": ["port"]
    },
    "Testing": {
        "UnitTest": ["test", "assert", "unit"],
        "Mocking": ["mock"],
        "Verification": ["verify"]
    },
    "GUI": {
        "Design": ["design", "layout"],
        "Functionality": ["button", "screen"],
        "Issues": ["error", "issue", "problem"]
    },
    "Update and Installation": {
        "Docker": ["docker", "compose"],
        "Installation": ["install", "setup"],
        "Versioning": ["update", "version"]
    },
    "Performance": {
        "Optimization": ["optimize", "speed", "fast"],
        "Issues": ["slow", "lag", "delay"]
    },
    "CI/CD": {
        "Pipeline": ["pipeline", "jenkins", "travis", "github action"],
        "Deployment": ["deploy", "release"]
    },
    "Security": {
        "Authentication": ["auth", "token", "login"],
        "Encryption": ["encrypt", "ssl", "tls"],
        "Permissions": ["permission", "access"]
    }
}

# Helper function to categorize issues into sub-themes
def categorize_sub_theme(main_theme, issue_title, issue_details):
    if main_theme in sub_theme_keywords:
        for sub_theme, keywords in sub_theme_keywords[main_theme].items():
            for keyword in keywords:
                if re.search(keyword, issue_title, re.I) or re.search(keyword, issue_details, re.I):
                    return sub_theme
    return "Other"

# Categorize issues based on sub-theme keywords
issues_df["Sub Theme"] = issues_df.apply(lambda row: categorize_sub_theme(row["Main Theme"], row["Issue Title"], row["Issue Details"]), axis=1)

# Display the first few rows with the new "Sub Theme" column
issues_df.head()
