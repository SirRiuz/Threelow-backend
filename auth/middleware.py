

# Rest_framework
from django.http.response import JsonResponse




# Auth
from .auth import AuthToken


# gAAAAABhXfvQ_FwzZGje7gAMRgTZoTwNh_UVAXK2HysvHx_7X7o9TqHM7G0eUYq2UtswtUHb5STBMl2tKrYgl6eNy9TNMZweD2ac8khVMoo_ZCr4133PyULbRkTxboDLi6nJcEszao0W33Pm7OotPljJyTicmvpaMtSn9zgGyJbV2X9HcBUmbeGmNNvn7DZ0frxzwwi14IGRmzdA5F_i-GUwB1U2aeDGI-FGU5B2LuvtIf20H1jN_GRfsBjppVqBy9tnLvy3yC7vV9cOa2gjUbs2nCBx4h0Gxg81gShKrVMV8mSfihMIerHPAWhQidQ9Ff9zYIvQmSTgOpuTMldcv8RG3atWageqxXaPiwtqhjxUCAUun-WX_ckM27ujom0qdtHILdb8WgJq#SEv2LTX1qu-G6Ss3-2im2_MzoVd7NEwSNI4hXzJ4jhs=


class AuthMiddleware(object):

    def __init__(self,get_response):
        self.get_response = get_response

        # Urls que no nececitan un token para 
        # ingresar
        self.ACCES_URL = [
            '/admin/',
            '/api/v1/auth'
        ]

    
    def __call__(self,request) -> (object):
        response = self.get_response(request)
        token = request.headers.get('token','None')
        result = AuthToken().decodeToken(token)


        for item in self.ACCES_URL:
            if request.get_full_path().count(item) > 0:
                return response

        if not result['error']:
            if not result['expirer']:
                return response

            else:
                return JsonResponse({
                    'status':'error',
                    'messege':'The token has expired',
                    'type-error':'expired-token '
                }) 

        return JsonResponse({
            'status':'error',
            'messege':'The token is not valid',
            'type-error':'token-error'
        })








