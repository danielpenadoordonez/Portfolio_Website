#Code to get data that will be passed to the base HTML template
import requests

def tech_Types(request) -> dict:
    #Call the API with the technologies
    tech = {
        "tech_Types" : {
            
        }
    }

    api_Response = requests.get("http://localhost:8080/back-api/technologies/?format=json").json()
    tech["tech_Types"]["languages"] = api_Response.get("langs")
    tech["tech_Types"]["frameworks"] = api_Response.get("frameworks")
    tech["tech_Types"]["tools"] = api_Response.get("tools")
    return tech