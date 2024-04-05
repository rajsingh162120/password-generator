# Random Password Generator

This is a simple Streamlit web application that generates random passwords based on user-provided inputs such as username, website, and the number of small alphabets, big alphabets, and special characters desired in the password. It also provides an option to store the generated passwords.

## Features

- Generates random passwords based on user inputs.
- Allows customization of the number of small alphabets, big alphabets, and special characters in the password.
- Option to store the generated passwords in a CSV file.
- Displays the stored passwords in a tabular format.

## How to Use

1. Clone this repository to your local machine.
2. Install the required dependencies listed in `requirements.txt` using pip:

Certainly! Below is the code for the README.md file based on the provided Streamlit application:

markdown
Copy code
# Random Password Generator

This is a simple Streamlit web application that generates random passwords based on user-provided inputs such as username, website, and the number of small alphabets, big alphabets, and special characters desired in the password. It also provides an option to store the generated passwords.

## Features

- Generates random passwords based on user inputs.
- Allows customization of the number of small alphabets, big alphabets, and special characters in the password.
- Option to store the generated passwords in a CSV file.
- Displays the stored passwords in a tabular format.

## How to Use

1. Clone this repository to your local machine.
2. Install the required dependencies listed in `requirements.txt` using pip:

```bash
pip install -r requirements.txt
```

3. Run the application using the following command:
   
```bash
streamlit run app.py
```

4. Enter the username, website, and desired characteristics of the password (number of small alphabets, big alphabets, special characters).
5. Click on the "Generate Password" button to generate the password.
6. Choose whether to store the generated password or not.
7. Stored passwords will be displayed in a table below.

## Requirements

- Python 3.x
- Streamlit
- Pandas
- Pyperclip (optional, for copying passwords to clipboard)

```plaintext
[Password-generator](http://password-generator1.streamlit.app/)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project was created as part of a learning exercise.
- Inspired by similar password generator tools and tutorials.
