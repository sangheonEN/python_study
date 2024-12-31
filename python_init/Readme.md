__init__.py를 활용해서 다양한 source code를 관리한다!

1. __init__.py 를 활용해서 특정 폴더(models)에 위치하는 py 파일들에 class를 임포트한다.

- 예시 __init__.py
from .LEE_models_1 import Model_1
from .LEE_models_2 import Model_2
from .LEE_models_3 import Model_3

2. 실제로 model을 활용한 py 파일에서 models에 저장된 class를 불러와 인스턴스 생성한다.

- 예시 test.py

import models

model_1 = models.Model_1()
model_2 = models.Model_2()
model_3 = models.Model_3()

보통 폴더 트리는 아래와 같다.

D:\GIT_HUB\PYTHON_STUDY\PYTHON_INIT
│  Readme.md
│  test.py
│
└─models
        LEE_models_1.py
        LEE_models_2.py
        LEE_models_3.py
        __init__.py


4. 결론: __init__.py를 활용한 프로젝트 관리 측면에서의 장점!



    - __init__.py를 활용해 특정 폴더 내에 원하는 python source 코드에 접근해서 원하는 Class를 import 하여 활용할 수 있다. 예를들어, 여러 다른 레이어로 구현한 딥러닝 모델 소스 파일을 생성하여 특정 폴더에 저장해두고 활용할 수 있는 것이죠.

    - 특정 폴더에 원하는 python source 코드를 삽입, 삭제, 업데이트가 용이하다. 예를들어, 내가 원하는 모델을 추가하고 싶으면 그냥 저 폴더 내에 source 코드를 추가하면 됩니다.