// python의 여러 함수들이 Py_ssize_t 타입을 사용하게 됨! 
// -> Py_ssize_t 타입이란, 플랫폼에 따라 크기가 다를 수 있는 정수형 타입으로 일반적으로 32비트 시스템에서는 int 크기와 동일, 64비트 시스템에서는 long 크기와 동일!
// -> 즉, system의 지원 비트에 따라 정수형 타입을 가변적으로 적용!
#define PY_SSIZE_T_CLEAN
// <>와 ""의 차이!
// -> <>는 시스템 경로인 python 설치 디렉토리에 있는 Python.h를 찾습니다.
// -> ""는 로컬 경로로 현재 소스 파일이 위치한 디렉토리에서 example.h를 찾습니다. 로컬 경로에서 찾다가 없으면 시스템 경로로 가서 찾습니다.
// -> <> 이 경로에 있는 파일부터 찾습니다.
#include <Python.h>
#include "example.h"

// c코드 함수 선언 순서 : static 유무, 반환값 자료형, 함수 이름, (매개변수), {}

// static 함수란 전역 함수로 선언된 .c 소스 코드내에서만 활용 가능.
// 서로 다른 소스코드에서 중복된 함수명이 있으면, 컴파일 시 오류 발생!
// 팀프로젝트를 수행할때, 다른 소스 코드에 동일한 함수명으로 중복되는 문제에 활용됨. cpp에서는 오버로딩 기술로 해결 가능.
static PyObject* py_add(PyObject* self, PyObject* args) {

    /*
    1. description:
    - args 매개변수를 받아 add를 처리하는 함수.

    2. params:
    - PyObject* self: 이 매개변수는 모듈에 대한 참조를 나타내며, 
                    모듈의 함수나 메서드가 호출될 때 Python 해석기에 의해 전달됩니다. 
                    일반 함수에서는 보통 사용되지 않고, 메서드처럼 객체의 상태를 관리해야 할 때 주로 사용됩니다.
    - PyObject* args: Python에서 전달된 인자들을 포함한 튜플입니다. 
                      예를 들어, Python에서 example.add(10, 20)처럼 호출하면 args에는 (10, 20)이 들어있습니다.

    3. return:
    - PyObject*인 이유는 Python 객체로 반환.

    */
    int a, b;

    // args에서 Python 인자를 파싱하여 C 변수 a와 b에 저장합니다.
    // "ii"는 **형식 문자열(format string)**로, 두 개의 int 타입 인자를 기대하고 있음을 나타냅니다.
    if (!PyArg_ParseTuple(args, "ii", &a, &b)) {
        return NULL;
    }

    int result = add(a, b);

    return PyLong_FromLong(result);

}

static PyMethodDef exported_functions[] = {
    /*
    1. description:
    - 모듈에 포함된 함수들을 정의.
    - 배열 형식으로 정의
    - 정의 순서: 함수 이름(python에서 호출로 활용), C 함수 포인터(Wrapper Function -> PyObject* 함수명), 인자 처리 방식, 함수 설명

    2. 정의 파라미터 설명
    - METH_VARARGS: 튜플 형식의 인자를 받는 함수 -> py_add 함수가 PyObject* args로 인자들을 받을 수 있도록 정의
    - {NULL, NULL, 0, NULL} -> **종료 표시(Sentinel)**로, 함수 정의 배열의 끝을 나타냄

    */

    {"add", py_add, METH_VARARGS, "Add two numbers"},
    
    {NULL, NULL, 0, NULL}

};

static struct PyModuleDef examplemodule = {
    /*
        static struct PyModuleDef examplemodule:

        이 구조체는 Python에서 사용할 모듈의 기본 정보를 정의합니다.
        PyModuleDef_HEAD_INIT: 모듈 초기화 매크로로, 모든 Python 모듈 정의에서 필수로 사용됩니다.
        example: 모듈의 이름입니다. Python에서 이 모듈을 import example처럼 임포트할 때 사용됩니다.
        NULL: 모듈에 대한 문서화 문자열입니다. 문서화가 필요하지 않을 경우 NULL로 설정합니다.
        -1: 모듈의 상태 크기를 지정합니다. 여기서 -1은 모듈이 글로벌 변수만 사용하며, 인터프리터의 상태와 무관하게 작동한다는 것을 의미합니다. 만약 모듈이 상태를 각 인터프리터마다 다르게 유지해야 한다면, 양수 값을 사용합니다.
        exported_functions: 모듈에 포함된 메서드 정의입니다. 이 모듈에서 제공하는 Python 함수들을 정의한 PyMethodDef 배열을 참조합니다.
    
    */
    PyModuleDef_HEAD_INIT,
    "example",
    NULL,
    -1,
    exported_functions

};

PyMODINIT_FUNC PyInit_example(void) {
    /*
    PyMODINIT_FUNC PyInit_example(void):

    이 함수는 Python에서 모듈을 초기화하기 위해 호출됩니다. 함수명은 반드시 PyInit_<module_name> 형식을 따라야 하며, 여기서 <module_name>은 모듈 이름인 "example"과 일치해야 합니다.
    이 함수는 Python 해석기가 모듈을 임포트할 때 자동으로 호출됩니다.
    PyModule_Create(&examplemodule):

    examplemodule 구조체를 기반으로 새로운 모듈 객체를 생성하여 반환합니다.
    이렇게 반환된 모듈은 Python 해석기에 의해 등록되어, Python 코드에서 사용할 수 있게 됩니다.

    */

    return PyModule_Create(&examplemodule);
}