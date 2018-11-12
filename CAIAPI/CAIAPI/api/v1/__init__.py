from CAIAPI.api import API

api = API(1)

@api
@api.register('', 'GET')
@api.return_code(200, "Hello")
@api.no_client_auth
@api.no_user_auth
def index():
    return {"message": "Greetings"}

@api
@api.register('', 'POST')
@api.return_code(200, "Hello")
@api.argument('name', True, 'User name to say hello to')
@api.no_client_auth
@api.no_user_auth
def index(name):
    return {"message": "Greetings, %s. CAIAPI says hi!" % name}
