import re


def saveJsonAsBibtex():
    pass


def bibtex2json(bibtex):
    def searchByKey(keyword, item):
        s = keyword + """=\{(.+?)\}"""
        tmp = re.search(s, item)
        if tmp is not None:
            return tmp.group(1)
        return ''

    keywords = ['title', 'author', 'booktitle', 'volume', 'pages', 'year']
    bibTypes = ['inproceedings', 'article', 'book']

    result_list = []

    items = bibtex.strip().lower()
    for item in items.split('@'):
        tmp = {'type': ''}
        for t in bibTypes:
            if t in item:
                tmp['type'] = t
                break
        if tmp['type'] == '':
            continue

        for keyword in keywords:
            tmp[keyword] = searchByKey(keyword, item)
        result_list.append(tmp)
    return result_list


def json2bibtex():
    pass


if __name__ == '__main__':
    print(bibtex2json(''))
