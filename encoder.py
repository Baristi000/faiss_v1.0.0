import numpy as np
import requests, faiss

class UniversalEncoder():

    data = [
    'What color is chameleon?',
    'When is the festival of colors?',
    'When is the next music festival?',
    'How far is the moon?',
    'How far is the sun?',
    'What happens when the sun goes down?',
    'What we do in the shadows?',
    'What is the meaning of all this?',
    'What is the meaning of Russel\'s paradox?',
    'How are you doing?'
    ]


    FEATURE_SIZE = 512
    BATCH_SIZE = 32
    storage_dir = "./search_data/faiss.index"

    def __init__(self, host, port):
        self.server_url = "http://{host}:{port}/v1/models/model:predict".format(
            host = host,
            port = port
        )
    @staticmethod
    def _standardized_input(sentence:str):
        return sentence.replace("\n", "").lower().strip()[:1000]

    def encode(self,data):
        data = [self._standardized_input(sentence=sentence) for sentence in data]
        all_vectors = []
        for i in range(0, len(data), self.BATCH_SIZE):
            batch = data[i:i+self.BATCH_SIZE]
            res = requests.post(
                url=self.server_url,
                json = {"instances":batch}
            )
            if not res.ok:
                print("FALSE")
            all_vectors += res.json()["predictions"]
        all_vectors = np.array(all_vectors,dtype="f")
        return all_vectors
    
    def build_index(self, vector, storage:bool=False):
        index = faiss.IndexFlatL2(self.FEATURE_SIZE)
        index.add(vector)
        if storage == True:
            faiss.write_index(index,self.storage_dir)
        return index
    
    def search(self, query, numb_result:int=1, index=None):
        if index == None:
            index = faiss.read_index(self.storage_dir)
        query_vector = self.encode([query])
        top_k_result = index.search(query_vector, numb_result)
        return [
            self.data[_id] for _id in top_k_result[1].tolist()[0]
        ]
    