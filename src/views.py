from flask.ext import restful

from models import Resources
from errors import OutResourcesError, NotFoundError


class AllocateView (restful.Resource):
    def get(self, user):
        try:
            value = Resources().allocate(user)
        except OutResourcesError:
            return 'Out of resources.', 503
        else:
            return value, 201


class DeallocateView (restful.Resource):
    def get(self, resource):
        try:
            value = Resources().deallocate(resource)
        except NotFoundError:
            return 'Not allocated.', 404
        else:
            return value, 204


class ListView (restful.Resource):
    def get (self, user=None):
        return Resources().get_list(user)


class ResetView (restful.Resource):
    def get (self):
        return Resources().reset(), 204

