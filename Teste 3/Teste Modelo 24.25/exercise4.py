def list_paths(dirtree):
    def lists(dirtree, curpath):
        paths = []
        
        if isinstance(dirtree, str):
            paths.append(curpath + dirtree)
            
        elif isinstance(dirtree, tuple):
            direc, subtrees = dirtree
            curpath = curpath + direc + "/"
            
            for subtree in subtrees:
                paths.extend(lists(subtree, curpath))
                
        return paths
    return lists(dirtree, "")