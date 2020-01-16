def File_Reset_Search(date,paths):
    path = paths
    with open(path,'w') as f:
        key = date
        ustr = '%s' % str(key)
        f.write(ustr)
        f.close()
