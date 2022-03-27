import bs4, requests
import json
import io

class Site:
    def __init__(self, name):
        self.url = Site.make_url(name.lower().split()) 
        site = Site.data_collection(self)
        
        print(f"[INFO]: FEATURES: {site}")
        Site.update(site)
    
    def make_url(name):
        symbs = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e',
                 'ё':'yo','ж':'zh','з':'z','и':'i','й':'y','к':'k',
                 'л':'l','м':'m','н':'n','о':'o','п':'p','р':'r',
                 'с':'s','т':'t','у':'u','ф':'f','х':'h','ц':'c',
                 'ч':'ch','ш':'sh','щ':'shya','ъ':'','ы':'i','ь':'','э':'e','ю':'yu','я':'ya'}
        
        for num in range(len(name)):
        
            for symb in name[num]:
                name[num] = name[num].replace(symb,symbs[symb])
        
        q = ""
        for word in name:
            q += f"{word}+"
        url=f"https://www.google.com/search?q={q[:-1]}&oq={q[:-1]}"
        
        print(f"Url made: {url}")
        return url

    def data_collection(self):
        """ Collect site`s data """
        html = requests.get(self.url).text
        soup = bs4.BeautifulSoup(html,features="lxml")
        
        features = {}
        def find_element(element,group,parameter="text"):
            print("[LOG]:",element,group,parameter)
            
            # Получение текста
            result = {}
            if parameter == 'text':
                if group == "named":
                    result[element["name"]] = soup.find(element["tag"], element["attribute"]).text
                    print("[LOG]: RESULT=",result)
                elif group == "unnamed":
                    element = soup.find(name["tag"], name["attribute"])
                    print("[LOG]: ELEMENT=",element)
            
                filt_symbs = ['⋅']
                for filt_symb in filt_symbs:
                    result[name] = result[name].replace(filt_symb,"|")
            else:
                pass
        
        # Elements
        elems = {
        "named": {
            "Название": {
                        "tag": 'div',
                        "attribute": {"class": 'BNeawe deIvCb AP7Wnd'},
                        "name": "Название"
                        },
            "Рейтинг": {
                        "tag": 'span',
                        "attribute": {"class": 'Eq0J8 oqSTJd'},
                        "name": "Рейтинг"
                        }
            },
        "unnamed": {
            "info": {
                "tag": 'span',
                "attribute": {"class": 'BNeawe tAd8D AP7Wnd'},
                "name": {"tag": 'a', "attribute": {"class": 'fl'}}
                }
            }
        }
        
        
        # Get site`s features
        for group in elems.keys():
            print("[Group]:"+group)
            for elem in elems[group]:
                print("[elem]:"+elem)
                try:
                    find_element(element=elem, group=group,)
                except IndexError as error:
                    print(f'[ERROR]: CANNOT FIND <{elem}> ON PAGE! FOR MORE DETAILS: {error}')
        
        return features  
        
    def update(site):
        # read data what we have
        with open('data.json','r') as file:
            data = eval(file.read())
        
        # update data
        data[site['Название'].lower()] = site
        with open('data.json','w') as file:
            json.dump(data, file, ensure_ascii=False)

if __name__ == '__main__':
    names = ["додо пицца", "космос", "старый замок"]
    for name in names:
        Site(name)