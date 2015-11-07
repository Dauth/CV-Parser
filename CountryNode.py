__author__ = 'Owner'

class CountryNode(object):
    def __init__(self,json, country, city = None):
        self.country = country
        self.city = city
        self.json = json

    def getCity(self):
        return self.city
    def setCity(self, city):
        self.city = city

    def getCountry(self):
        return self.country
    def setCountry(self, country):
        self.country = country

    def getLocation(self):
        return self.json.get('location').lower()

    def getAddress(self):
        return self.json.get('address').lower()

    def getStreet(self):
        return self.json.get('street').lower()

    def getPostal(self):
        return self.json.get('postal').lower()
