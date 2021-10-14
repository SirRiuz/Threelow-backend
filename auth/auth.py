


# Libs
import datetime
import json
import base64
from cryptography.fernet import Fernet



class AuthToken(object):


    def __generateDate(self) -> (str):
        actual = datetime.datetime.now()
        expirer = actual + datetime.timedelta(hours=24)
        restant = expirer.day - actual.day
        data = ({
            'created':actual.__str__(),
            'expirer':expirer.__str__(),
            'restant':restant
        })

        return data


    def __checkDateToken(self,data) -> (bool):
        expirer = data['expirer']
        actual = datetime.datetime.now()

        result = datetime.datetime.strptime(expirer, '%Y-%m-%d %H:%M:%S.%f') - actual
        if result.days >= 0:
            return False

        return True


    def decodeToken(self,token:str) -> (dict):
        try:
            data = {}
            decodeToken = None
            encodeToken = token.split('#')[0]
            payload = token.split('#')[1]
            fObject = Fernet(payload)

            decodeToken = fObject.decrypt(
                encodeToken.encode()
            ).decode()[::-1]
            
            decodeToken = base64.b64decode(
                decodeToken.encode()
            ).decode().replace("'",'"')

            jsonDictObject = json.loads(decodeToken)
            result = self.__checkDateToken(jsonDictObject['date'])

            data = ({
                'error':False,
                'expirer':result
            })

            if result:
                data['messege'] = 'Expired token '

            return data

            
        except Exception as e:
            return ({
                'error':True,
                'type-error':'invalid-token',
                'messege':'The token not is valid ...'
            })




    def generateToken(self,requestData:dict) -> (str):
        tokenDate = self.__generateDate()
        print(tokenDate)
        token = ({
            'ip-client':requestData['ip-client'],
            'client-name':requestData['client-name'],
            'date':tokenDate
        })
        serializeToken = str(base64.b64encode(
            str(token).encode()
        ).decode())[::-1]
        payload = Fernet.generate_key().decode()
        
        fObject = Fernet(payload).encrypt(
            serializeToken.encode()
        )


        return (f'{fObject.decode()}#{payload}')




token = AuthToken().generateToken({
    'ip-client':'xxx.xxx.xxx-xxx',
    'client-name':'xxx-xxx-xx'
})
print(token)

#x = AuthToken().decodeToken('gAAAAABhXfvQ_FwzZGje7gAMRgTZoTwNh_UVAXK2HysvHx_7X7o9TqHM7G0eUYq2UtswtUHb5STBMl2tKrYgl6eNy9TNMZweD2ac8khVMoo_ZCr4133PyULbRkTxboDLi6nJcEszao0W33Pm7OotPljJyTicmvpaMtSn9zgGyJbV2X9HcBUmbeGmNNvn7DZ0frxzwwi14IGRmzdA5F_i-GUwB1U2aeDGI-FGU5B2LuvtIf20H1jN_GRfsBjppVqBy9tnLvy3yC7vV9cOa2gjUbs2nCBx4h0Gxg81gShKrVMV8mSfihMIerHPAWhQidQ9Ff9zYIvQmSTgOpuTMldcv8RG3atWageqxXaPiwtqhjxUCAUun-WX_ckM27ujom0qdtHILdb8WgJq#SEv2LTX1qu-G6Ss3-2im2_MzoVd7NEwSNI4hXzJ4jhs=')
#print(x)
# Cerializa con base64
# se voltea el
# Se cifra con la payload