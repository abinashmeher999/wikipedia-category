import requests
from pprint import pprint
import json

with open('metadata.json') as data_file:
    data = json.load(data_file)


class WikiFile:
    def __init__(self, **reference_to_pages):
        self.base_url = "https://en.wikipedia.org/w/api.php"

        self.payload = {
            'action': 'query',
            'format': 'json',
        }
        self.headers = {
                'User-Agent': data["name"] + ' (' + data["website"] + ')'
        }

        self._parse_kwargs(**reference_to_pages)

    def _parse_kwargs(self, **kwparams):
        if 'titles' in kwparams:
            self.payload['titles'] = '|'.join(str(ID) for ID in list(kwparams['titles']))
        else:
            raise ValueError("No valid arguments passed!")

    def get_duplicatefiles(self, dflimit="max", dfdir="ascending", dflocalonly=False):
        prop = 'duplicatefiles'
        self.payload['prop'] = prop
        self.payload['dflimit'] = dflimit
        self.payload['dfdir'] = dfdir
        if dflocalonly:
            self.payload['dflocalonly'] = True

        res = requests.get(self.base_url, params=self.payload, headers=self.headers).json()

        df_list = {}
        for page_id, page_content in res['query']['pages'].items():
            if prop not in page_content:
                continue
            df_list[page_content['title']] = page_content[prop]

        while 'continue' in res:
            self.payload['dfcontinue'] = res['continue']['dfcontinue']
            res = requests.get(self.base_url, params=self.payload, headers=self.headers).json()
            for page_id, page_content in res['query']['pages'].items():
                if prop not in page_content:
                    continue
                if page_content['title'] not in df_list:
                    df_list[page_content['title']] = []
                df_list[page_content['title']] += page_content[prop]

        self.payload.pop('dfcontinue', None)
        self.payload.pop('dflimit', None)
        self.payload.pop('dfdir', None)
        self.payload.pop('dflocalonly', None)
        self.payload['prop'] = None
        return df_list

if __name__ == "__main__":
    titles = ['Image:1995.jpg', 'File:Albert Einstein Head.jpg', 'Image:Bombers.ogg']

    try:
        wk = WikiFile(titles=titles)
    except ValueError as error:
        print (error.args)
        sys.exit("Exited!")

    print("get_duplicatefiles: ")
    pprint(wk.get_duplicatefiles())
