from django.urls import reverse


def test_starter_home_uses_the_prepared_theme(client):
    response = client.get(reverse("starter-home"))

    assert response.status_code == 200
    assert "De theme estático a tienda Django" in response.content.decode()
    assert "accounts" in response.content.decode()
    assert "products" in response.content.decode()
