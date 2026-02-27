import streamlit as st
import os

FILE_NAME = "contacts.txt"

# Ensure file exists
if not os.path.exists(FILE_NAME):
    open(FILE_NAME, "w").close()

# ---------- FUNCTIONS ----------

def add_contact(name, phone):
    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{phone}\n")

def get_contacts():
    with open(FILE_NAME, "r") as file:
        return file.readlines()

def search_contact(search_name):
    results = []
    with open(FILE_NAME, "r") as file:
        for line in file:
            name, phone = line.strip().split(",")
            if search_name.lower() in name.lower():
                results.append((name, phone))
    return results

def delete_contact(delete_name):
    lines = get_contacts()
    with open(FILE_NAME, "w") as file:
        for line in lines:
            name, phone = line.strip().split(",")
            if delete_name.lower() != name.lower():
                file.write(line)

# ---------- STREAMLIT UI ----------

st.title("📞 Simple Contact Book")

menu = st.sidebar.selectbox(
    "Menu",
    ["Add Contact", "View Contacts", "Search Contact", "Delete Contact"]
)

# ADD CONTACT
if menu == "Add Contact":
    st.subheader("➕ Add New Contact")
    name = st.text_input("Enter Name")
    phone = st.text_input("Enter Phone Number")

    if st.button("Add"):
        if name and phone:
            add_contact(name, phone)
            st.success("Contact added successfully!")
        else:
            st.error("Please fill all fields")

# VIEW CONTACTS
elif menu == "View Contacts":
    st.subheader("📋 All Contacts")
    contacts = get_contacts()

    if contacts:
        for contact in contacts:
            name, phone = contact.strip().split(",")
            st.write(f"**{name}** : {phone}")
    else:
        st.info("No contacts found")

# SEARCH CONTACT
elif menu == "Search Contact":
    st.subheader("🔍 Search Contact")
    search_name = st.text_input("Enter name to search")

    if st.button("Search"):
        results = search_contact(search_name)
        if results:
            for name, phone in results:
                st.write(f"**{name}** : {phone}")
        else:
            st.warning("No contact found")

# DELETE CONTACT
elif menu == "Delete Contact":
    st.subheader("❌ Delete Contact")
    delete_name = st.text_input("Enter exact name to delete")
import streamlit as st
import os

FILE_NAME = "contacts.txt"

# Ensure file exists
if not os.path.exists(FILE_NAME):
    open(FILE_NAME, "w").close()

# ---------- FUNCTIONS ----------

def add_contact(name, phone):
    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{phone}\n")

def get_contacts():
    with open(FILE_NAME, "r") as file:
        return file.readlines()

def search_contact(search_name):
    results = []
    with open(FILE_NAME, "r") as file:
        for line in file:
            name, phone = line.strip().split(",")
            if search_name.lower() in name.lower():
                results.append((name, phone))
    return results

def delete_contact(delete_name):
    lines = get_contacts()
    with open(FILE_NAME, "w") as file:
        for line in lines:
            name, phone = line.strip().split(",")
            if delete_name.lower() != name.lower():
                file.write(line)

# ---------- STREAMLIT UI ----------

st.title("📞 Simple Contact Book")

menu = st.sidebar.selectbox(
    "Menu",
    ["Add Contact", "View Contacts", "Search Contact", "Delete Contact"]
)

# ADD CONTACT
if menu == "Add Contact":
    st.subheader("➕ Add New Contact")
    name = st.text_input("Enter Name")
    phone = st.text_input("Enter Phone Number")

    if st.button("Add"):
        if name and phone:
            add_contact(name, phone)
            st.success("Contact added successfully!")
        else:
            st.error("Please fill all fields")

# VIEW CONTACTS
elif menu == "View Contacts":
    st.subheader("📋 All Contacts")
    contacts = get_contacts()

    if contacts:
        for contact in contacts:
            name, phone = contact.strip().split(",")
            st.write(f"**{name}** : {phone}")
    else:
        st.info("No contacts found")

# SEARCH CONTACT
elif menu == "Search Contact":
    st.subheader("🔍 Search Contact")
    search_name = st.text_input("Enter name to search")

    if st.button("Search"):
        results = search_contact(search_name)
        if results:
            for name, phone in results:
                st.write(f"**{name}** : {phone}")
        else:
            st.warning("No contact found")

# DELETE CONTACT
elif menu == "Delete Contact":
    st.subheader("❌ Delete Contact")
    delete_name = st.text_input("Enter exact name to delete")

    if st.button("Delete"):
        delete_contact(delete_name)
        st.success("Contact deleted successfully!")
    if st.button("Delete"):
        delete_contact(delete_name)
        st.success("Contact deleted successfully!")