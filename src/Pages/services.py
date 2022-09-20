import requests
from django.http import Http404

class PageServices():

    BASE_URL = 'http://localhost:8080/back-api'

    def get_Owner_Info(self, objects:list) -> dict:
        response = dict()
        data_Format = 'json'

        for obj in objects:
            url = None
            if obj == 'owner':
                url = f"{self.BASE_URL}/{obj}/?owner_id=118200576&format={data_Format}"
            else:
                url = f"{self.BASE_URL}/{obj}/?format={data_Format}"
            
            #Call to the API
            apiResponse = requests.get(url)
            response[obj] = apiResponse.json()

            # if(apiResponse.status_code == '200'):
            #     response[obj] = apiResponse.json()
            # else:
            #     raise Http404

        return response