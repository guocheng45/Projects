import requests


class GroupChat():
    def list(self,token,json):
        url = ""
        r = requests.post(
            url,
            params={'access_token':token},
            json=json
        )
        return