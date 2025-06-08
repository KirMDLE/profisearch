from typing import Generic, TypeVar, List
from pydantic.generics import GenericModel

T = TypeVar("T")

class Pagination(GenericModel, Generic[T]):
    total: int
    items: List[T]
    page: int
    size: int
