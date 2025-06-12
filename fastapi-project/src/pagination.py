from typing import Generic, TypeVar, List
from pydantic import BaseModel
from pydantic.generics import GenericModel

T = TypeVar("T")

class PageParams(BaseModel):
    limit: int = 10
    offset: int = 0


class Pagination(GenericModel, Generic[T]):
    total: int
    items: List[T]
    page: int
    size: int


def paginate(items: List[T], total: int, limit: int, offset: int) -> PaginatedResponse[T]:
    return PaginatedResponse(
        total=total,
        limit=limit,
        offset=offset,
        items=items
    )