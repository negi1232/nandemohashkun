def file_hash_start(path):
    from file2hash import File2hash
    import os 
    import glob
    import sys
    import hashlib
    #フォルダ内のファイルを取得
    with open(path, 'rb') as file:
        # ファイルを読み取る
        fileData = file.read()
    hash_sha256 = hashlib.sha256(fileData).hexdigest()
    #print(f'filename:{path},sha256:{hash_sha256}')


    #それぞれのハッシュ値を結合しハッシュ化
    return hash_sha256


if __name__ =="__main__":
    from file2hash import File2hash
    import os 
    import glob
    import sys

    args = sys.argv
    if len(args)==2:
        chpath=args[1]
        

    else:
        chpath="./"
    
    print(file_hash_start(chpath))
