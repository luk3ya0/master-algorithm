from abc import abstractmethod
from typing import Protocol, Any, TypeVar


class AbcComparable(Protocol):
    """Protocol for annotating comparable types."""

    @abstractmethod
    def __lt__(self, other: Any) -> bool:
        pass

    @abstractmethod
    def __gt__(self, other: Any) -> bool:
        pass

    @abstractmethod
    def __eq__(self, other: Any) -> bool:
        pass


Comparable = TypeVar("Comparable", bound=AbcComparable)
