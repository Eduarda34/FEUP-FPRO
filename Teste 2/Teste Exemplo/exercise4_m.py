def above(tree, name):
    if isinstance(tree, str):
        if tree == name:
            return []
        return None
    
    manager, subtrees = tree
    
    for subtree in subtrees:
        result = above(subtree, name)
        
        if result is not None:
            return [manager] + result
        
    return None

#print(above(('Jeff',[('Adam', ['Alice', 'Bob']),('Paul',['Eve', 'Louis']),('Roger',[('David',['Jack', 'John']), 'Peter'])]), 'Jack'))
#print(above(('Jeff',[('Adam', ['Alice', 'Bob']),('Paul',['Eve', 'Louis']),('Roger',[('David',['Jack', 'John']), 'Peter'])]), 'Alice'))
#print(above(('Jeff',[('Adam', ['Alice', 'Bob']),('Paul',['Eve', 'Louis']),('Roger',[('David',['Jack', 'John']), 'Peter'])]), 'Adam'))
#print(above(('Jeff',[('Adam', ['Alice', 'Bob']),('Paul',['Eve', 'Louis']),('Roger',[('David',['Jack', 'John']), 'Peter'])]), 'Sophie'))