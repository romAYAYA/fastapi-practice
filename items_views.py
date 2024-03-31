from fastapi import APIRouter, Path
from typing import Annotated

router = APIRouter(prefix="/items")


@router.get("/")
def list_items():
    return [{"item1": "item1"}, {"item2": "item2"}, {"item3": "item3"}]


@router.get("/latest/")
def get_latest_items():
    return [{"item1": "latest"}, {"item2": "latest"}, {"item3": "latest"}]


@router.get("/{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {"item_id": item_id}
