from .blog_post import required_functionality
from fastapi import APIRouter, status, Response, Depends
from typing import Optional
from enum import Enum

router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)


@router.get(
    "/all",
    summary="Retrieve all blogs",
    description="This api call simulates fetching all blogs",
    response_description="The list of available blogs"
)
async def get_blogs(
        page=None,
        page_size: Optional[int] = 12,
        req_param: dict = Depends(required_functionality)):
    return {"message": f'All {page_size} blogs on page {page}',
            "req": req_param}


@router.get(
    "/{blog_id}/comments/{comment_id}",
    tags=["comment"],
    summary='Get a comment form a blog'
)
async def get_comment(
        blog_id: int,
        comment_id: int,
        valid: bool = True,
        username: Optional[str] = None,
        req_param: dict = Depends(required_functionality)
):
    """
    Simulates retrieving a comment form a blog

    - **id** mandatory path parameter
    - **comment_id** mandatory path parameter
    - **valid** optional query parameter
    - **username** optional query parameter
    """

    return {"message": f"{blog_id}, {comment_id}, {valid}, {username}"}


@router.get("/{blog_id}", status_code=status.HTTP_200_OK)
async def get_blog(blog_id: int, response: Response):
    if blog_id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "id not found"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"blog id: {blog_id}"}


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


@router.get("/type/{type}")
async def blog_type(type: BlogType):
    return {"msg": type}