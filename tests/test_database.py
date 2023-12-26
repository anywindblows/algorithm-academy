import pytest

from src.database import resolve_table_name


@pytest.mark.parametrize(
    ('input_name', 'expected_name'),
    [
        ('Users', 'users'),  # single word
        ('userAccounts', 'user_accounts'),  # camel case
        ('ProductCatalogItems', 'product_catalog_items'),  # pascal case
        ('customerOrderDetails', 'customer_order_details'),  # mixed case
    ],
)
def test_resolve_table_name(input_name: str, expected_name: str) -> None:
    """Test resolve_table_name function correct convert string."""
    result = resolve_table_name(input_name)
    assert result == expected_name
