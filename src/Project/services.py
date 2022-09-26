from .models import Technologies, Programming_Language, Framework, Tool

class ProjectService:

    def __init__(self) -> None:
        pass

    def get_All_Technologies(self):
        techs = Technologies.objects.all()
        langs = list()
        frameworks = list()
        tools = list()

        for tech in techs:
            try:
                #Verify if the tech is a language
                lang = Programming_Language.objects.get(code=tech.code)
                langs.append(lang)
            except:
                try:
                    #Verify if it is a framework
                    framework = Framework.objects.get(code=tech.code)
                    frameworks.append(framework)
                except:
                    try:
                        #Verify if it is a framework
                        tool= Tool.objects.get(code=tech.code)
                        tools.append(tool)
                    except:
                        return None
        
        return langs, frameworks, tools