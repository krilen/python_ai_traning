

def print_list(_list: list =[]) -> None:
    
    if not isinstance(_list, list):
        print(_list)
        return
    
    else:
        for item in _list:
            if isinstance(item, list):
                print(" - found nested list -  ")
                print_list(item)
                
            else:
                print(item, end=", ")
    
        print()
        
        
print_list()
print_list("hello")
print_list([])
print_list([1])
print_list([1,2,3,4])
print_list([1,["a","b", "c"],2,3])
print_list([1,["a",["!", "%", "("],"b"],2,3,[["-", "+", "*"]]])