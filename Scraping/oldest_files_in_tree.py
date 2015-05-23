import os, heapq

def oldest_files_in_tree(rootfolder, count=1):
    return heapq.nsmallest(count,
        (os.path.join(dirname, filename)
        for dirname, dirnames, filenames in os.walk(rootfolder)
        for filename in filenames),
        key=lambda fn: os.stat(fn).st_mtime)
