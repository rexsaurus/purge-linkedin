from linkedin_api import Linkedin

# Using this https://github.com/tomquirk/linkedin-api
# Replace USERNAME, PASSWORD with "" strings of your login info

# Authenticate using any Linkedin account credentials
api = Linkedin(USERNNAME, PASSWORD)

# fetch urn
def get_urn(member_profile):
    return member_profile["member_urn"][14:]

#remove all connections
def remove_all_connections(member_connections):
    for x in member_connections:
        urn = x["urn_id"]
        print("removing connection... " + urn)
        #api.remove_connection(urn)
        urn_prof = api.get_profile(urn)
        print(urn_prof)

#unfollow all entities
#def unfollow_all(follows)

# Search then purge
        
    
# GET your profile
profile = api.get_profile()
profile_urn = get_urn(profile)

# GET 1st degree connections of your given profile
connections = api.get_profile_connections(profile_urn)

remove_all_connections(connections)
