from elasticsearch import Elasticsearch
import pandas as pd


def is_index_exists(es, index_name: str) -> bool:
    return index_name in es.indices.get_alias().keys()

def create_index(es: Elasticsearch, index_name: str):
    es.indices.create(index=index_name)



def write_file(es: Elasticsearch, index_name: str, path_to_file, sep=','):
    df = pd.read_csv(path_to_file, sep=sep)
    body = []
    for i in df.index:
        entry = df.loc[i].to_dict()
        body.append({'index': {'_index': index_name, '_id': i}})
        body.append(entry)

    es.bulk(body=body)


if __name__ == "__main__":

    DELETE_INDEX = True
    es = Elasticsearch(
        hosts=['https://localhost:9200'],
        http_auth=('admin', 'admin'),
        verify_certs=False
    )

    new_index_name = "my-first-python-index"

    if DELETE_INDEX and is_index_exists(es=es, index_name=new_index_name):
        es.indices.delete(index=new_index_name)
    
    create_index(es=es, index_name=new_index_name)

    path_to_file = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
    sep = '\t'

    write_file(es=es, index_name=new_index_name, path_to_file=path_to_file, sep=sep)

    print("Done!")
