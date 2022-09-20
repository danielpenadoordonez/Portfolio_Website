#Code to get data that will be passed to the base HTML template

def tech_Types(request) -> dict:
    #Call the API with the technologies
    tech = {
        "tech_Types" : {
            
        }
    }
    # tech["tech_Types"]["languages"] = ["Python", "Java"]
    # tech["tech_Types"]["frameworks"] = ["Django", ".NET"]
    # tech["tech_Types"]["tools"] = ["Docker", "Linux"]
    return tech