from injector import inject , provider, Module

class RestaurantsProvider(Module):
    @inject
    def __init__(self, items: list=[]):
        self._items = items

    @provider
    def get(self, number_of_items: int=5) -> list:
        if not self._items:
            return []

        if number_of_items > len(self._items):
            number_of_items = len(self._items)

        return self._items

'''
class RestaurantModel(Module):
    def configure(self, binder):
        binder.bind(RestaurantsProvider)

class RestaurantModule(Module):
    def configure(self, binder):
       binder.bind(list, to= [{"Name":"F Restaurantsss"}])

    @provider
    def describe(self, item : list) -> list:
        return item
'''
