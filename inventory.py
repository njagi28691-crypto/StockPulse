"""
StockPlulse: Inventory & Sales Intelligence Engine
Inventory Management Module (Dictionaries,Lists,& Strings)
"""

def display_inventory(inventory):
    """
    Renders the inventory dictonary into a clean, aligned ASCII table.
    Demonstrates dictionary iteration and string formatting alignment.
    """
    if not inventory:
        print(" The inventory catalog is currently empty.")
        return
    print("=" * 75)
    print(f"{'SKU':<10} | {'Product Name' :<22} | {'Category' :<12} | {'Stock':<6} | {'Price (KES)':<10}")
    print("-" * 75)
    for sku, details in sorted(inventory.items()):
        name = details["name"]
        category = details["category"]
        stock = details["stock"]
        price = details["price"]

        print(f"{sku:<10} | {name:<22} |{category:<12} | {stock:<6} | {price:<10.2f}")

    print("=" * 75)

def add_product(inventory, sku, name, price,stock, category):
    """
    Adds a new product dictionary entry.
    Demonstrates dictionary key checking and nested dictionry insertion.
    """

    sku = sku.strip().upper()

    if sku in inventory:
        return False,f"Error: SKU '{sku}' already exixts in the catalog."
    if price < 0 or stock < 0:
        return False, "Error: Price and stock cannot be negative values."

    inventory[sku] = {
        "name" : name.strip().title(),
        "price" : float(price),
        "stock" : int(stock),
        "category" : category.strip().capitalize()
    }
    return True, f"succesfully added '{name}' under SKU {sku}."

def update_stock(inventory, sku, quantity_change):
    """
    Updates the stock quantity for an existing SKU.
    Demonstrates dictionary value modification and validation checks.
    """
    sku = sku.strip().upper()

    if sku not in inventory:
        return False, f"Error: SKU '{sku}' not found in inventory."
    
    current_stock = inventory[sku]["stock"]
    new_stock = current_stock + quantity_change

    if new_stock < 0:
        return False, f"Error:Insufficient stock.Current stock for{sku} is {current_stock}."

    inventory[sku]["stock"] = new_stock
    return True, f"Updated SKU {sku}: stock changed by {quantity_change:+d} (New Total: {new_stock})"

def search_product(inventory, query):
    """
    Perfoms a case-insenstive search across product names and categories.
    Demonstrates string manipulation (.lower()), containment checks, and list building.
    """
    query = query.strip().lower()
    if not query:
        return[]

    results = []
    for sku, details in inventory.items():
        name_lower = details["name"].lower()
        category_lower = details["category"].lower()

        if query in name_lower or query in category_lower or query == sku.lower():
            match_record = {"sku":sku, **details}
            results.append(match_record)

    return results


    
