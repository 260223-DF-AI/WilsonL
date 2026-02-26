# contact_book.py - Contact Book Application
# Starter code for e003-exercise-data-structures

"""
Contact Book Application
------------------------
A simple contact management system using Python data structures.

Data Structure:
- Each contact is a dictionary with: name, phone, email, category, created_at
- All contacts are stored in a list

Complete the TODO sections below to finish the application.
"""

from datetime import datetime, timedelta
import sys

# =============================================================================
# Initialize Contact Book
# =============================================================================
contacts = []

# =============================================================================
# TODO: Task 1 - Create the Contact Book
# =============================================================================

def add_contact(contacts:dict, name:str, phone:str, email:str, category:str):
    """
    Add a new contact to the contact book.
    
    Args:
        contacts: The list of all contacts
        name: Contact's full name
        phone: Contact's phone number
        email: Contact's email address
        category: One of: friend, family, work, other
    
    Returns:
        The created contact dictionary
    """
    # TODO: Create a contact dictionary with all fields
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "category": category
    }
    # TODO: Add created_at timestamp using datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    contact["created_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # TODO: Append to contacts list
    contacts.append(contact)
    # TODO: Return the new contact
    return contact


# =============================================================================
# TODO: Task 2 - Display Contacts
# =============================================================================

def display_all_contacts(contacts: dict) -> None:
    """
    Display all contacts in a formatted table.
    
    Output format:
    =============================================
                CONTACT BOOK (X contacts)
    =============================================
    #  | Name            | Phone         | Category
    ---|-----------------|---------------|----------
    1  | Alice Johnson   | 555-123-4567  | friend
    ...
    """
    # TODO: Print header with contact count
    print("=" * 44)
    print(f"         CONTACT BOOK ({len(contacts)} contacts)")
    print("=" * 44)
    # TODO: Print table headers
    # name = 17 total, phone = 14 total, category = 12 total
    print("#  | Name            | Phone        | Category   ")
    print("---|-----------------|--------------|------------")
    # TODO: Loop through contacts and print each row
    for i in range(len(contacts)):
        c = contacts[i]
        print(f"{i+1}  | {c.get("name")} | {c.get("phone")} | {c.get("category")}")
    # TODO: Print footer
    print ("=" * 44)

def display_contact_details(contact: dict) -> None:
    """
    Display detailed information for a single contact.
    
    Output format:
    --- Contact Details ---
    Name:     [name]
    Phone:    [phone]
    Email:    [email]
    Category: [category]
    Added:    [created_at]
    ------------------------
    """
    # TODO: Print formatted contact details
    print("--- Contact Details ---")
    print(f"Name:       {contact.get("name")}")
    print(f"Phone:      {contact.get("phone")}")
    print(f"Email:      {contact.get("email")}")
    print(f"Category:   {contact.get("category")}")
    print(f"Added:      {contact.get("created_at")}")
    print("-" * 20)

# =============================================================================
# TODO: Task 3 - Search Functionality
# =============================================================================

def search_by_name(contacts:dict, query:str):
    """
    Find contacts whose name contains the query string.
    Case-insensitive search.
    
    Returns:
        List of matching contacts
    """
    # TODO: Filter contacts where query is in name (case-insensitive)
    # Hint: Use list comprehension and .lower()
    matching = []
    for c in contacts:
        if query.lower() in c.get("name").lower():
            matching.append(c)
    return matching


def filter_by_category(contacts:dict, category:str):
    """
    Return all contacts in a specific category.
    
    Returns:
        List of contacts matching the category
    """
    # TODO: Filter contacts by category
    matching = []
    for c in contacts:
        if c.get("category") == category:
            matching.append(c)
    return matching

def find_by_phone(contacts:dict, phone:str):
    """
    Find a contact by exact phone number.
    
    Returns:
        The contact dictionary if found, None otherwise
    """
    # TODO: Search for contact with matching phone
    matching = None
    for c in contacts:
        if phone == c.get("phone"):
            matching = c
    return matching


# =============================================================================
# TODO: Task 4 - Update and Delete
# =============================================================================

def update_contact(contacts:dict, phone:str, field:str, new_value:str):
    """
    Update a specific field of a contact.
    
    Args:
        contacts: The list of all contacts
        phone: Phone number to identify the contact
        field: The field to update (name, phone, email, or category)
        new_value: The new value for the field
    
    Returns:
        True if updated, False if contact not found
    """
    # TODO: Find contact by phone
    # TODO: Update the specified field
    # TODO: Return success/failure
    contact_to_update = find_by_phone(contacts, phone)
    if contact_to_update != None:
        contact_to_update.update({field: new_value})
        return True
    return False


def delete_contact(contacts:dict, phone:str):
    """
    Delete a contact by phone number.
    
    Returns:
        True if deleted, False if not found
    """
    # TODO: Find and remove contact with matching phone
    contact_to_update = find_by_phone(contacts, phone)
    if contact_to_update != None:
        contacts.remove(contact_to_update)
        return True
    return False
    


# =============================================================================
# TODO: Task 5 - Statistics
# =============================================================================

def display_statistics(contacts:dict):
    """
    Display statistics about the contact book.
    
    Output:
    --- Contact Book Statistics ---
    Total Contacts: X
    By Category:
      - Friends: X
      - Family: X
      - Work: X
      - Other: X
    Most Recent: [name] (added [date])
    -------------------------------
    """
    print("--- Contact Book Statistics ---")
    # TODO: Count total contacts
    count = len(contacts)
    print(f"Total contacts: {count}")
    # TODO: Count contacts by category
    print("By Category:")
    friends, family, work, other = 0, 0, 0, 0
    most_recent = contacts[0]
    for c in contacts:
        match(c.get("category")):
            case "friend":
                friends += 1
            case "family":
                family += 1
            case "work":
                work += 1
            case _:
                other += 1
        if (most_recent.get("created_at")<c.get("created_at")):
            most_recent = c
    print(f"    - Friends:  {friends}")
    print(f"    - Family:   {family}")
    print(f"    - Work:     {work}")
    print(f"    - Other:    {other}")
    # TODO: Find most recently added contact
    print(f"Most recent: {most_recent.get("name")} (added {most_recent.get("created_at")[:10]})")

# =============================================================================
# STRETCH GOAL: Interactive Menu
# =============================================================================

def display_menu():
    """Display the main menu."""
    print("\n========== CONTACT BOOK ==========")
    print("1. View all contacts")
    print("2. Add new contact")
    print("3. Search contacts")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. View statistics")
    print("0. Exit")
    print("==================================")


def main():
    """Main function with interactive menu."""
    # TODO: Implement menu loop
    # Use while True and break on exit choice
    while True:
        display_menu()
        user_in = input()
        match(user_in):
            case "0":
                break
            case "1":
                display_all_contacts(contacts)
            case "2":
                name = input("Enter name: ")
                phone = input("Enter phone number: ")
                email = input("Enter email: ")
                category = input("Enter category: ")
                add_contact(contacts, name, phone, email, category)
            case "3":
                query = input("Enter name to search: ")
                query_result = search_by_name(contacts, query)
                if query_result != []:
                    for c in query_result:
                        display_contact_details(c)
                else:
                    print("No matching contact found")
            case "4":
                phone = input("Enter phone number of contact to update: ")
                field = input("Enter field to update: ")
                new_info = input("Enter what the field should be changed to: ")
                update_contact(contacts, phone, field, new_info)
            case "5":
                phone = input("Enter phone number of contact to delete: ")
                delete_contact(contacts, phone)
            case "6":
                display_statistics(contacts)
            case _:
                print("Unrecognized input.")
 


# =============================================================================
# Test Code - Add sample data and test functions
# =============================================================================

if __name__ == "__main__":
    print("Contact Book Application")
    print("=" * 40)
    
    # TODO: Add at least 5 sample contacts
    # add_contact(contacts, "Alice Johnson", "555-123-4567", "alice@example.com", "friend")
    add_contact(contacts, "Alice Jones", "123-456-7890", "alicesmith@gmail.com", "friend")
    add_contact(contacts, "Bob Smith", "908-765-4321", "bobs@yahoo.com", "family")
    add_contact(contacts, "Jane Doe", "456-123-7890", "janedoe@company.com", "work")
    add_contact(contacts, "Accident McGee", "555-664-5567", "amcgee@me.com", "other")
    add_contact(contacts, "Serious Businessperson", "777-888-9999", "srs_biz@company.net", "work")
    # TODO: Test your functions
    # display_all_contacts(contacts)
    # results = search_by_name(contacts, "alice")
    # etc.
    
    # STRETCH: Uncomment to run interactive menu
    main()
