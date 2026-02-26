
def nested_list(_list: list = []) -> None | bool:

    if not isinstance(_list, list):
        return None
    
    if not len(_list):
        return False

    found_nested_list = False

    for element in _list:
        if isinstance(element, list):
            found_nested_list = True
            break

    return found_nested_list



print(nested_list([1,2,3,4]))
print(nested_list("hello"))
print(nested_list([1,[2],3,"hello"]))
print(nested_list())
print(nested_list([[0]]))
