"""Transaction extension endpoints"""
from fastapi import APIRouter, Depends

from stac_api.clients.postgres.transactions import (
    TransactionsClient,
    transactions_client_factory,
)
from stac_api.models import schemas
from stac_api.utils.dependencies import discover_base_url

router = APIRouter()


@router.post(
    "/collections/{collectionId}/items",
    response_model=schemas.Item,
    response_model_exclude_unset=True,
    response_model_exclude_none=True,
)
def create_item_by_id(
    item: schemas.Item,
    crud_client: TransactionsClient = Depends(transactions_client_factory),
    base_url: str = Depends(discover_base_url),
):
    """Create item (transactions extension)"""
    row_data = crud_client.create_item(item)
    row_data.base_url = base_url
    return row_data


@router.put(
    "/collections/{collectionId}/items",
    response_model=schemas.Item,
    response_model_exclude_unset=True,
    response_model_exclude_none=True,
)
def update_item_by_id(
    item: schemas.Item,
    crud_client: TransactionsClient = Depends(transactions_client_factory),
    base_url: str = Depends(discover_base_url),
):
    """Update item (transactions extension)"""
    row_data = crud_client.update_item(item)
    row_data.base_url = base_url
    return row_data


@router.delete(
    "/collections/{collectionId}/items/{itemId}",
    response_model=schemas.Item,
    response_model_exclude_unset=True,
    response_model_exclude_none=True,
)
def delete_item_by_id(
    itemId: str,
    crud_client: TransactionsClient = Depends(transactions_client_factory),
    base_url: str = Depends(discover_base_url),
):
    """Delete item (transactions extension)"""
    row_data = crud_client.delete_item(itemId)
    row_data.base_url = base_url
    return row_data


@router.post(
    "/collections",
    summary="Create a new collection",
    response_model=schemas.Collection,
    response_model_exclude_unset=True,
    response_model_exclude_none=True,
)
def create_collection(
    collection: schemas.Collection,
    crud_client: TransactionsClient = Depends(transactions_client_factory),
    base_url: str = Depends(discover_base_url),
):
    """Create a new collection (transactions extension)"""
    row_data = crud_client.create_collection(collection)
    row_data.base_url = base_url
    return row_data


@router.put(
    "/collections",
    summary="Update a collection if it exists, otherwise create a new collection",
    response_model=schemas.Collection,
    response_model_exclude_unset=True,
    response_model_exclude_none=True,
)
def update_collection_by_id(
    collection: schemas.Collection,
    crud_client: TransactionsClient = Depends(transactions_client_factory),
    base_url: str = Depends(discover_base_url),
):
    """Update collection (transactions extension)"""
    row_data = crud_client.update_collection(collection)
    row_data.base_url = base_url
    return row_data


@router.delete(
    "/collections/{collectionId}",
    summary="Delete a collection by id",
    response_model=schemas.Collection,
    response_model_exclude_unset=True,
    response_model_exclude_none=True,
)
def delete_collection_by_id(
    collectionId: str,
    crud_client: TransactionsClient = Depends(transactions_client_factory),
    base_url: str = Depends(discover_base_url),
):
    """Delete a collection (transactions extension)"""
    row_data = crud_client.delete_collection(collectionId)
    row_data.base_url = base_url
    return row_data