import streamlit as st
import random
import string
import pyperclip
import pandas as pd

# Function to generate a random password
def generate_password(username, website, num_small, num_big, num_special):
    if not username:
        st.error("Please enter a username")
        return None
    if not website:
        st.error("Please enter a website")
        return None

    total_length = num_small + num_big + num_special
    if total_length > 12:
        st.error("Total length of the password cannot exceed 12 characters")
        return None

    # Generating remaining characters randomly if the total length is less than 12
    remaining_length = 12 - total_length
    remaining_characters = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=remaining_length))

    # Generating a random password
    password_characters = (string.ascii_lowercase * num_small) + (string.ascii_uppercase * num_big) + (string.punctuation * num_special) + remaining_characters
    password = ''.join(random.sample(password_characters, 12))

    # Displaying the password
    st.success("Password generated successfully")
    st.write("Generated Password:", password)

    # Copy password to clipboard
    copy_password(password)

    # Store password
    if st.session_state.store_password_option == "Yes" and password:
        store_password(username, website, password)

    return password

# Function to copy password to clipboard
def copy_password(password):
    pyperclip.copy(password)
    st.success("Password copied to clipboard")

# Function to store password
def store_password(username, website, password):
    with open("passwords.csv", "a") as file:
        file.write(f"{username},{website},{password}\n")
    st.success("Password stored successfully")

# Function to load stored passwords from Excel file
def load_passwords():
    try:
        passwords_df = pd.read_csv("passwords.csv", names=["Username", "Website", "Password"])
    except FileNotFoundError:
        passwords_df = pd.DataFrame(columns=["Username", "Website", "Password"])
    return passwords_df

# Main page
def main():
    st.title("Random Password Generator")
    st.write("Please enter the details below to generate a password.")

    # Username entry
    username = st.text_input("Username:")

    # Website entry
    website = st.text_input("Website:")

    # Number of small alphabets entry
    num_small = st.number_input("Number of Small Alphabets:", min_value=0, step=1, value=0)

    # Number of big alphabets entry
    num_big = st.number_input("Number of Big Alphabets:", min_value=0, step=1, value=0)

    # Number of special characters entry
    num_special = st.number_input("Number of Special Characters:", min_value=0, step=1, value=0)

    # Store password option
    st.session_state.store_password_option = st.selectbox("Store Password?", ["Yes", "No"], index=0)

    # Generate button
    if st.button("Generate Password"):
        password = generate_password(username, website, num_small, num_big, num_special)

    # Display stored passwords
    st.subheader("Stored Passwords")
    passwords_df = load_passwords()
    if not passwords_df.empty:
        st.write("Below are the passwords generated and stored:")
        st.table(passwords_df)
    else:
        st.write("No passwords generated and stored yet.")

# Run the application
if __name__ == "__main__":
    main()
