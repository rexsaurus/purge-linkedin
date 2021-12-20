# This is a GitPod to automate the process of automatically removing LinkedIn connections
# Using this https://github.com/tomquirk/linkedin-api
# This GitPod will streamline the setup process
from linkedin_api import Linkedin

# Replace USERNAME, PASSWORD with "" strings of your login info
USERNAME = "" # You Provide
PASSWORD = "" # You Provide

# Authenticate using any Linkedin account credentials
api = Linkedin(USERNAME, PASSWORD)

# fetch urn
def get_urn(member_profile):
    return member_profile["member_urn"][14:]

#remove all connections
def remove_all_connections(member_connections):
    for x in member_connections:
        urn = x["urn_id"]
        print("removing connection... " + urn)
        api.remove_connection(urn)

# GET your profile
profile = api.get_profile()
profile_urn = get_urn(profile)

# GET 1st degree connections of your given profile
connections = api.get_profile_connections(profile_urn)

# Begin the purge
remove_all_connections(connections)
