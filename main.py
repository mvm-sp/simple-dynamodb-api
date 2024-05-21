# main.py

from api.create_tutorial import create_tutorial
from api.get_tutorial import get_tutorial
from api.update_tutorial import update_tutorial
from api.delete_tutorial import delete_tutorial
from api.list_tutorials import list_tutorials

if __name__ == "__main__":
    # Create a new tutorial
    tutorial = create_tutorial("New Tutorial", "This is a description.", True)
    print(f"Created Tutorial: {tutorial}")

    # Get the created tutorial by id
    fetched_tutorial = get_tutorial(tutorial['id'])
    print(f"Fetched Tutorial: {fetched_tutorial}")

    # Update the tutorial
    updated_tutorial = update_tutorial(tutorial['id'], description="Updated description.")
    print(f"Updated Tutorial: {updated_tutorial}")

    # List all tutorials
    tutorials = list_tutorials()
    print(f"List of Tutorials: {tutorials}")

    # Delete the tutorial
    delete_tutorial(tutorial['id'])
    print(f"Deleted Tutorial with id: {tutorial['id']}")
