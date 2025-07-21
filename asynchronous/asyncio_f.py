""" 
    - 비동기 프로그래밍 필요성

    1. 네트워크 통신, 파일 입출력에 발생하는 대기 시간을 낭비하지 않고 병렬적으로 CPU가 다른 작업을 처리하기 위함.
    2. 파이썬은 기본적으로 동기 방식으로 작동함. 
       -> 파이썬 3.4부터 asyncio 표준 라이브러리가 추가되어 비동기 처리 가능.
    
    - asyncio 설명
    
    1. 일반적으로 단일 Process, 단일 Thread에서 여러 asyncio 함수를 정의하여 활용함.
    2. 적합한 작업: I/O(입출력) 바운드 작업
        1] 네트워크 요청(HTTP 요청, 소켓 통신 등)
        2] 파일 입출력(특히 비동기 파일 입출력)
        3] 데이터베이스 쿼리(비동기 지원되는 DB 드라이버 사용 시)
        4] 웹 서버 응답 처리(예: FastAPI, aiohttp)
        
    - 내가 나중에 해볼거 : 파이썬 프로그램 -> TCP 소켓 서버 -> C++ 프로그램 간의 데이터 통신 기능을 asyncio로 구현 

"""
#%%
# 비동기 함수 호출을 위해서는 await 키워드 활용. 단순히 do_async()로 호출 안됨.
# asyncio.run()은 비동기 프로그램을 실행하기 위한 진입점 역할을 합니다. 비동기 함수를 호출하고 결과를 얻기 위해 이벤트 루프를 자동으로 설정하고 관리

import asyncio

def do_sync():
    return "sync"

async def do_async():
    return "async"

async def print_async():
    result = await do_async()
    print(result)

# Jupyter 노트북에서는 셀에서 ``await`` 키워드를 사용할 수 있지만 일반 파이썬 스크립트에서는
# ``asyncio.run`` 으로 비동기 함수를 실행해야 한다.
if __name__ == "__main__":
    asyncio.run(print_async())
