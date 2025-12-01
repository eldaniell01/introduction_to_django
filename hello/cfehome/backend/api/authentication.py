from rest_framework.authentication import TokenAuthentication as Bt

class TokenAuthentication(Bt):
    keyword = 'Bearer'