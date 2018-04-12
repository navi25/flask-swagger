from connexion.resolver import RestyResolver
import connexion
from injector import Binder, CallableProvider
from flask_injector import FlaskInjector
from services.provider import RestaurantsProvider

def configure(binder: Binder) -> Binder:
    binder.bind(
        interface=RestaurantsProvider.RestaurantsProvider,
        to=RestaurantsProvider.RestaurantsProvider(items = [{"Name":"Fgh"}])
    );


if __name__ == '__main__':
    app = connexion.App(__name__, port=2508, specification_dir='swagger/')
    app.add_api('restaurants.yaml', resolver=RestyResolver('api'))
    # app.run(ssl_context=('cert.pem','key.pem'))
    FlaskInjector(app=app.app, modules=[configure])
    app.run()
