from abc import ABC, abstractmethod
from typing import Sequence
import torch
import random

"""
python 3.3 version 이상 부터는 abstractclassmethod 대신 abstractmethod를 사용하는 것을 권장함.

1) @abstractmethod를 사용 이유: 추상클래스의 특정 함수(apply)를 자식클래스에서 무조건 오버라이드를 강제하기 위해서 사용
2) 근데 왜 오버라이드해서 정의하도록 엄격한 규칙을 세우는 거지?
    - 전략 패턴(Strategy Pattern) 적용을 위함
        1) BaseStrategy는 **"전략"**의 기본 구조만 제공하는 템플릿 역할을 함.
        2) RandomStrategy, CustomScoreStrategy 전략에서 apply 함수를 오버라이드하여 사용하기 위함.
    - 코드의 일관성과 예측 가능성 유지 : 오버라이드를 강제하지 않으면 일관성이 깨지고, 런타임 오류가 발생할 가능성이 높아짐.
    - 코드 재사용성과 유지보수성 향상 : 오버라이드를 강제하면 새로운 전략을 추가할 때 코드가 더 명확해지고, 유지보수가 쉬워짐.
    - 런타임 오류 대신 컴파일 단계에서 문제를 사전에 발견하기 위해 (abstractmethod 덕분에 객체 생성 시 오류 감지 가능)

    
3) 아래 코드는 AI 모델의 프루닝 전략을 추상화하여 구현한 코드입니다. 
    - BaseStrategy 추상클래스를 활용하여 apply 함수를 정의하고 프루닝을 처리하는 전략에 맞게 처리하는 기본 틀을 구조를 구축합니다.
    - 그리고 RandomStrategy, CustomScoreStrategy 자식 클래스에서 BaseStrategy 클래스를 상속하여 apply 함수를 오버라이드하여 전략에 맞게 apply 함수가 처리되도록 구현
"""


class BaseStrategy(ABC):
    """Base Strategy class."""

    def __call__(self, *args, **kwargs):
        """Call method."""
        return self.apply(*args, **kwargs)

    @abstractmethod  # @abstractclassmethod 대신 @abstractmethod 사용!
    def apply(self, weights, amount=0.0, round_to=1) -> Sequence[int]:
        """ Apply the strategy on weights with user specified pruning percentage."""
        raise NotImplementedError
    

class RandomStrategy(BaseStrategy):
    """Random Strategy class."""

    def apply(self, weights, amount=0.0, round_to=1) -> Sequence[int]:  # return index
        """Apply the strategy."""
        if amount <= 0:
            return []
        n = len(weights)
        n_to_prune = int(amount * n) if amount < 1.0 else amount
        n_to_prune = round_pruning_amount(n, n_to_prune, round_to)
        if n_to_prune == 0:
            return []
        indices = random.sample(list(range(n)), k=n_to_prune)
        return indices
    

class CustomScoreStrategy(BaseStrategy):
    """Custom Score Strategy.

    A helper class to execute sorting and filtering with any pruning score.

    common trick:
    - granularity. The pruned number of filters will be divisible by the granularity number.
    """

    def apply(self, scores, thresh=0.0, round_to=1) -> Sequence[int]:
        """Apply the pruning."""
        if thresh <= 0:
            return []
        n = len(scores)
        remained_idx = torch.nonzero(scores > thresh).view(-1).tolist()
        num_remained = len(remained_idx)
        # Granularity
        if num_remained % round_to > 0:
            num_remained += round_to - (num_remained % round_to)
        # keep the min idxs
        num_remained = max(num_remained, round_to)
        num_remained = min(num_remained, n)
        if num_remained == n:
            return []
        sorted_idx = torch.argsort(-scores)
        indices = torch.sort(sorted_idx[num_remained:])[0].view(-1).tolist()

        return indices
    


def round_pruning_amount(total_parameters, n_to_prune, round_to):
    """round the parameter amount after pruning to an integer multiple of `round_to`.
    """
    round_to = int(round_to)
    if round_to <= 1:
        return n_to_prune
    after_pruning = total_parameters - n_to_prune
    compensation = after_pruning % round_to
    # round to the nearest (round_to * N)
    # avoid negative n_to_prune
    if (compensation < round_to // 2 and after_pruning > round_to) or round_to > n_to_prune:
        n_to_prune = n_to_prune + compensation  # floor
    else:
        n_to_prune = n_to_prune - round_to + compensation  # ceiling
    return n_to_prune