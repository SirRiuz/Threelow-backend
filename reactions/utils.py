

# rest_framework

import io
import json
from rest_framework.renderers import JSONRenderer


def processReactionData(recListData) -> (list):
    recResponseData = ({})
    jsonData = json.loads(JSONRenderer().render(recListData))

    for item in jsonData:
        if item['reactionData']['name'] in recResponseData:
            recResponseData[item['reactionData']['name']]['count'] += 1 
        
        else:
            recResponseData[item['reactionData']['name']] = ({
                'id':item['reactionData']['id'],
                'count':1,
                'name':item['reactionData']['name'],
                'url':item['reactionData']['url']
            })

    result = sorted(recResponseData.items(), key=lambda items: items[1]['count'],reverse=True)
    return result
