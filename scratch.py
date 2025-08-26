import dataclasses
from typing import Literal, Never, overload


@dataclasses.dataclass(frozen=True)
class A:
    a: int

    
    @property
    @overload
    def t(self) -> Never: ...

    @property
    def t(self) -> str:
        raise NotImplementedError
    


@dataclasses.dataclass(frozen=True)
class B(A):
    b: int

    @property
    def t(self) -> Literal["B"]:
        return "B"


@dataclasses.dataclass(frozen=True)
class C(A):
    c: int

    @property
    def t(self) -> Literal["C"]:
        return "C"


b = B(a=1, b=2)
c = C(a=1, c=3)

values: list[B | C | A] = [b, c]

for v in values:
    match v.t:
        case "B":
            v.
