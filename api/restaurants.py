from flask_injector import inject
from services.provider import RestaurantsProvider

@inject
def search(data_provider = RestaurantsProvider) -> list:
    return data_provider
