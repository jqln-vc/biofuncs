import os
from Bio import Entrez

ENTREZ_API_KEY = os.environ['ENTREZ_API_KEY']
EMAIL = os.environ['EMAIL']


Entrez.api_key = ENTREZ_API_KEY
Entrez.email = EMAIL

stream = Entrez.einfo()
dblist = list(Entrez.read(stream).values())[0]


# List the Entrez databases with descriptions

def entrez_list_db(databases: list[str], output: str) -> str:
    with open(output, 'a') as file:
        for db in databases:
            stream = Entrez.einfo(db=db)
            record = Entrez.read(stream)
            file.write(f"{record['DbInfo']['DbName']} | {record['DbInfo']['MenuName']} | {record['DbInfo']['Description']}\n")
            for field in record['DbInfo']['FieldList']:
                file.write(f"{field['Name']} | {field['FullName']} : {field['Description']}\n")
            file.write("--------------------------------------------------------------\n")

    return output

entrez_list_db(dblist, 'ncbi_databases.txt')