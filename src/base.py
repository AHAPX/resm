from flask import Flask
from flask.ext import restful

from models import Resources


class ResmApp (Flask):
    """ Flask application with initialization resources in run """

    def run(self, count, name, *args, **kwargs):
        Resources().init(count, name)
        return super(ResmApp, self).run(*args, **kwargs)
        

class ResmApi (restful.Api):
    """ Flask api with custom error handler """

    def handle_error(self, e):
        return self.make_response('Bad Request', 400)
