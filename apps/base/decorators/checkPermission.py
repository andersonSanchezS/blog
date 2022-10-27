from apps.base.utils.index import decodeJWT, response


def checkPermission(permission):
    def decorator(fun):
        def wrapper(*args, **kwargs):
            try:
                authorized = False
                token = decodeJWT(args[1])
                superUser = token['is_superuser']
                # check if the role is in the token
                if permission:
                    for x in permission:
                        if x in token['permissions']:
                            authorized = True

                # check if the user is authorized
                if authorized or superUser:
                    return fun(*args, **kwargs)
                else:
                    return response({'error': True, 'message': 'no autorizado'}, 401)

            except Exception as e:
                if str(e) == "'is_superuser'":
                    return response({'error': True, 'message': 'token de acceso no proveído '}, 401)
                return response({'error': str(e)}, 500)
        return wrapper
    return decorator
