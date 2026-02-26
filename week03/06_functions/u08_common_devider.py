
def common_devider(x: int =0, y : int =0) -> None | int:
    """
    Tests to see if there is a common devider (not 1) between two integer.
    The return is the common devider.
     * If a none integer is entered the return is None.
     * If an integer is zero or less (negative) the return is zero.
     * If no common devider is found the return is zero.
    """

    if not isinstance(x, int) or not isinstance(y, int):
        return None
    
    if x <= 0 or y <= 0:
        return 0
    
    for devider in range(min([x, y]), 1, -1):
        if x % devider == 0 and y % devider == 0:
            break
            
        if devider == 2:
            devider = 0

    return devider

print(common_devider(14, 4))
print(common_devider())
print(common_devider(88, 12))
print(common_devider("", 12))