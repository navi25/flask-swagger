from flask_injector import inject
from services.provider import RestaurantsProvider


#Connexion's RestyResolver looks for search() function for get operations
@inject
def search(data_provider : RestaurantsProvider.RestaurantsProvider) -> list:
    return data_provider.get()


#Connexion's RestyResolver looks for post() function for post operations
@inject
def post(data_provider : RestaurantsProvider.RestaurantsProvider):
    x=3
