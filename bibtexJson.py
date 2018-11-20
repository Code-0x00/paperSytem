import re
import json


def bibtex2json(bibtex):
    def searchByKey(keyword, item):
        s = keyword + """=\{(.+?)\}"""
        tmp = re.search(s, item)
        if tmp is not None:
            return tmp.group(1)
        return ''

    keywords = ['title', 'author', 'booktitle', 'volume', 'pages', 'year']
    bibTypes = ['inproceedings', 'article', 'incollection', 'book', 'techreport', 'mastersthesis']

    result_list = []

    items = bibtex.strip().lower()
    for item in items.split('@'):
        item = item.replace(' =', '=').replace('= ', '=')
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


def saveJsonAsBibtex():
    pass


def saveBibtexAsJson(bibtex, json_filename):
    json_bib = bibtex2json(bibtex)
    with open(json_filename, 'w', encoding='utf-8') as f:
        json.dump(json_bib, f, ensure_ascii=False)


def loadBibtexAsJson(bibtex_filename):
    f = open(bibtex_filename, 'r', encoding='UTF-8')
    all_bib = f.read()
    f.close()
    return bibtex2json(all_bib)


def loadJsonAsBibtex():
    pass


def transFileBibtex2json(bibtex_filename, json_filename):
    f = open(bibtex_filename, 'r', encoding='UTF-8')
    all_bib = f.read()
    f.close()
    saveBibtexAsJson(all_bib, json_filename)


def transFileJson2Bibtex(json_filename, bibtex_filename):
    pass


if __name__ == '__main__':
    #print(bibtex2json(''))
    print(loadBibtexAsJson('xhq.bib'))
