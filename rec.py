

reactions = {}
queryDictList = [
    {
        'id':10,
        'reaction':5,
        'name':':w:',
        'url':'UWL_REC'
    },    {
        'id':10,
        'reaction':5,
        'name':':w:',
        'url':'UWL_REC'
    },    {
        'id':10,
        'reaction':5,
        'name':':w:',
        'url':'UWL_REC'
    },    {
        'id':10,
        'reaction':5,
        'name':':ahhh:',
        'url':'UWL_REC'
    },    {
        'id':10,
        'reaction':5,
        'name':':mee:',
        'url':'UWL_REC'
    },    {
        'id':10,
        'reaction':5,
        'name':':mee:',
        'url':'UWL_REC'
    }
]


for item in queryDictList:
    if item['name'] in reactions:
        reactions[item['name']]['count'] = reactions[item['name']]['count'] + 1

    else:
        reactions[item['name']] = ({
            'count':1,
            'url':item['url'],
            'reaction':''
        })


print(reactions)

# for item in queryDictList:
#     if item['reaction'] in reactions:
#         reactions[item['reaction']]['count'] = reactions[item['reaction']]['count'] + 1
#     else:
#         reactions[item['reaction']] = {
#             'count':0
#         }


# print(reactions)