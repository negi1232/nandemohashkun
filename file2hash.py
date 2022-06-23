import hashlib
class File2hash :
    def __init__(self) -> None:
        pass
    def run_file(self,path):
        with open(path, 'rb') as file:
            # ファイルを読み取る
            fileData = file.read()
        hash_sha256 = hashlib.sha256(fileData).hexdigest()
        print(f'filename:{path},sha256:{hash_sha256}')

        return path,hash_sha256
    
    def run_hash(self,data):
        res=str()
        for d in data:
            res+=d[1]

        #print(res)
        #print("////")
        hs = hashlib.sha256(res.encode()).hexdigest()
        #print(hs)   
        return hs