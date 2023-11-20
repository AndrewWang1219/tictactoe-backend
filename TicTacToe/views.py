import json

from .utils.MiniMax import GameDecision
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['POST'])
def getDecisionOfAI(req):
    print(req.body)
    data = req.body.decode("utf-8")
    json_data = json.loads(data)
    state = json_data.get('state')
    agent = json_data.get('agent')
    character = json_data.get('character')
    print(state)
    if state:
        decision = GameDecision(state, agent=agent)
        if character == 'me':
            terminate = decision.isSuccess(decision.state, agent=agent) >= 1
            res = {
                'terminate': terminate
            }
            return Response(data=json.dumps(res), status=status.HTTP_200_OK)
        elif character == 'ai':
            res_state = decision.res_state
            res = {
                'state': res_state,
                'terminate': decision.isSuccess(decision.res_state, agent=agent)>0
            }
            print(res)
            return Response(data=json.dumps(res), status=status.HTTP_200_OK)
    return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
