def create_sandwich(*ingredients):
    """Accepts a list of ingredients for a sammy and prints it out."""
    print(f"I want a sandwich with the following ingredients: ")
    for ingredient in ingredients:
        print(f"\t- {ingredient}")

create_sandwich('turkey')
create_sandwich('turkey', 'cheese')
create_sandwich('turkey', 'cheese', 'ham')