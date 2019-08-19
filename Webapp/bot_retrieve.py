import requests
import json
class Bot:
    def retrieve(self,question):
        apidata={"question": question}
        url="https://codefundoqna.azurewebsites.net/qnamaker/knowledgebases/c4b368e1-6b7e-4d23-8136-a4df3d6ce7fc/generateAnswer"

        headers={'Authorization': 'EndpointKey  {0}'.format("85516a21-9985-46c2-afd9-3ececdad0a49")}
        # import pdb; pdb.set_trace()
        responsefromapi = requests.post(url,json=apidata,headers=headers)

        print(responsefromapi.status_code)
        if responsefromapi.status_code == 200:
            results=json.loads(responsefromapi.content.decode('utf-8'))
            print(results['answers'][0]['answer'])