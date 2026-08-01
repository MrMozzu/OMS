import uuid
import pytest

@pytest.mark.asyncio 
async def test_create_category(client):

    category_name = f"Cat_{uuid.uuid4().hex[:6]}"

    response = await client.post(
        "/api/v1/categories/",
        json = {
            "name": category_name
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == category_name

    assert "id" in data