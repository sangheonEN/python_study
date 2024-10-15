# def A():
#     return True


# def B():
#     return False


# def C():
#     return False


if __name__ == "__main__":

    """
        B가 True(참)일 경우 A가 반환됩니다.
        B가 False(거짓)일 경우 C가 반환됩니다.
    """
    A = True
    BT = True
    BF = False
    C = False

    print(A if BT else C)
    print(A if BF else C)


    """
    if not False:
        print("참입니다.")
    """
    
    if not False:
        print("참입니다.")
        
    if not False or False:
        print("False or False\n")
    
    if not True or 0:
        print("False or 0\n")
    