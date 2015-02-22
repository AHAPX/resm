from base import ResmApp, ResmApi
from views import AllocateView, DeallocateView, ResetView, ListView
from models import Resources


app = ResmApp(__name__)
api = ResmApi(app, catch_all_404s=True)


api.add_resource(AllocateView, '/allocate/<string:user>')
api.add_resource(DeallocateView, '/deallocate/<string:resource>')
api.add_resource(ResetView, '/reset')
api.add_resource(ListView, '/list', '/list/<string:user>')
