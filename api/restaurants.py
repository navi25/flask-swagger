from flask_injector import inject
from services.provider import RestaurantsProvider

@inject(data_provider = RestaurantsProvider)
def search(data_provider) -> list:
    return data_provider.get()
