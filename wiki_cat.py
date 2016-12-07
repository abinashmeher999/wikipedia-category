import requests
import re


class WikiCatQuery(object):
    def __init__(self):
        self.base_url = "https://en.wikipedia.org/w/api.php"

        self.payload = {
            'action': 'query',
            'prop': 'categories',
            'pageids': None,
            'format': 'json',
            'clshow': '!hidden'
        }

    @staticmethod
    def __strip_cat(text):
        return re.sub("Category:", "", text, count=1)

    def __res_cat_list(self, res):
        return res['query']['pages'][str(self.payload['pageids'])]['categories']

    def get_cat(self, pageid=None,include_hidden=False):
        if pageid is None:
            return []
        if include_hidden==True:
            self.payload['clshow']='hidden'
        self.payload['pageids'] = pageid
        res = requests.get(self.base_url, params=self.payload).json()

        cat_list = [self.__strip_cat(item['title']) for item in self.__res_cat_list(res)]
        while 'continue' in res:
            self.payload['clcontinue'] = res['continue']['clcontinue']
            res = requests.get(self.base_url, params=self.payload).json()
            cat_list += [self.__strip_cat(item['title']) for item in self.__res_cat_list(res)]

        self.payload['pageids'] = None
        return cat_list

if __name__ == "__main__":
    from pprint import pprint
    print("Do you want to include hidden categories? Enter True or False!!")
    val=input()
    wk = WikiCatQuery()
    pprint(wk.get_cat(843158,input))
    pprint(wk.get_cat(20715044,input))
