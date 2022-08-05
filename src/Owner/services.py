from .models import Certificate, Degree

class OwnerService:

    def getFilteredDegrees(self, degrees):
        """
          Returns only the degrees and removes the certifications
          from this response
        """
        filtered_Degrees = list() 
        for degree in degrees:
            try:
                #Verify if the degree is a certificate
                cert = Certificate.objects.get(code=degree.code)
            except:
                #In case the certificate is not found it is a degree and it is added to the list
                filtered_Degrees.append(degree)

        return filtered_Degrees