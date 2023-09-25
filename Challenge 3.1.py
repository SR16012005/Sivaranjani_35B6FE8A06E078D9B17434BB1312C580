#Write a function called linear_search_product that takes the list of products and a target product name as input. The function should perform a linear search to find the target product in the list and return a list of indices of all occurrences of the product if found, or an empty list if the product is not found.
def linear_search_product(product_list, target_product):
    """
    Perform a linear search to find occurrences of the target product in the list.

    Parameters:
    product_list (list): A list of product names.
    target_product (str): The product name to search for.

    Returns:
    list: A list of indices of occurrences of the target product, or an empty list if not found.
    """
    occurrences = []

    for index, product in enumerate(product_list):
        if product == target_product:
            occurrences.append(index)

    return occurrences

# Example usage
products = ["Apple", "Banana", "Orange", "Apple", "Banana"]
target_product = "Apple"
result = linear_search_product(products, target_product)
print("Indices of occurrences of", target_product, ":", result)