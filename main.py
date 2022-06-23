def file_hash_start(chpath):
    from file2hash import File2hash
    import os 
    import glob
    import sys

    #フォルダ内のファイルを取得
    path=[p for p in glob.glob(chpath+'/*', recursive=True)
       if os.path.isfile(p)]
    path+=[p for p in glob.glob(chpath+'/risumusume.8192/*', recursive=True)
       if os.path.isfile(p)]

    #print(path)
    path.sort()#ソートを実行
    #print(path)

    hash=File2hash()
    result=list()
    #print(path)
    #各ファイルに対してハッシュ化
    for p in path:
        #print(hash.run_file(p))
        result.append(hash.run_file(p))

    #それぞれのハッシュ値を結合しハッシュ化
    res=hash.run_hash(result)
    return res


if __name__ =="__main__":
    from file2hash import File2hash
    import os 
    import glob
    import sys

    args = sys.argv
    if len(args)==2:
        chpath=args[1]
        

    else:
        chpath="./risumusumu_VtubeStudio/"
    
    print(file_hash_start(chpath))
