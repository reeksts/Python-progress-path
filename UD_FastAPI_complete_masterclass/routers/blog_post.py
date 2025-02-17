from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel
from typing import Optional, List, Dict

router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)


class Image(BaseModel):
    url: str
    alias: str


class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    tags: List[str] = []
    metadata: Dict[str, str] = {"key": "val1"}
    image: Optional[Image]


@router.post("/new/{id}")
async def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        "id": id,
        "data": blog,
        "version": version,
    }


@router.post("/new/{id}/comment/{comment_id}")
async def create_comment(
        blog: BlogModel,
        id: int,
        comment_title: int = Query(
            ...,
            title="Id of the comment",
            description="Some description for the comment_title",
            alias="commentTitle",
            deprecated=True,
        ),
        content: str = Body(
            ...,
            min_length=10,
            max_length=50,
            regex='^[a-z/s]*$'
        ),
        v: Optional[List[str]] = Query(["1.0", "1.2", "1.4"]),
        comment_id: int = Path(None, gt=5, le=10)
):
    return {
        "body": blog,
        "id": id,
        "comment_title": comment_title,
        "content": content,
        "v": v,
        "comment_id": comment_id
    }


def required_functionality():
    return {"message": "Learning FastAPI is important"}

