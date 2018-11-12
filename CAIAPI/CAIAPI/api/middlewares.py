from flask import request


from CAIAPI.api.exceptions import APIInvalidRequest


class Middleware(object):
    def request_infos(self):
        return {}

    def intermediate_viewfunc(self):
        return None


class ArgumentMiddleware(Middleware):
    def __init__(self, arguments):
        self.arguments = arguments

    def request_infos(self):
        args = {}
        reqjson = request.json or {}

        for argument in self.arguments:
            argkey, required, _ = argument
            if argkey in reqjson:
                args[argkey] = reqjson[argkey]
            elif required:
                raise APIInvalidRequest('Argument "%s" is required' % argkey)

        return args
