# 동일한 함수에서 출력을 다르게 하고 싶을때 문자열로 출력 파라미터를 정하는 방법!

def forward(x, y, z, returns):
    
    xy = x + y
    xz = x + z
    yz = y + z
    
    xyz = xy + xz + yz
    
    # variables 출력: {'x': 1, 'y': 2, 'z': 3, 'xy': 3, 'xz': 4, 'yz': 5, 'xyz': 12}
    # locals()를 사용하면, {'변수명', 변수값}으로 함수안에 모든 변수들의 정보를 가지는 딕셔너리 변수를 얻을 수 있음.
    variables = locals()
    
    return tuple(variables[r] for r in returns)
    


if __name__ == "__main__":
    

    result = forward(1, 2, 3, ("xy", "xyz"))
    
    print(result)
    