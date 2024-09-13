# Password Generator
<img src='https://cdn-icons-png.flaticon.com/512/5850/5850971.png' width='200'>

This project is a password generator web app built using **Streamlit**. The app allows users to generate three types of passwords:
- **PIN-based passwords**: Numeric-only passwords with customizable length.
- **Random character passwords**: Passwords composed of letters, with optional inclusion of numbers and symbols.
- **Random word-based passwords**: Passwords created using random words from the English language.

The generated password can be copied to the clipboard directly from the web interface.

## Features

- **PIN Password Generator**: Allows users to generate a PIN with a length between 8 and 50 digits.
- **Random Password Generator**: Allows users to generate a random password with options to include numbers and special symbols.
- **Random Words Generator**: Allows users to generate a password made up of random English words.

Each password type has a simple interface for setting its parameters, such as length, inclusion of special characters, or number of words.

## Installation

### Prerequisites
- nltk==3.4.5
- pyperclip==1.9.0
- streamlit==1.23.1


### Step-by-step Setup


1. Clone the repository:

    ```shell
    git clone https://github.com/alirezasaberi20/Python-Project.git
    ```

2. Navigate to the project directory:

    ```shell
    cd password_generator
    ```

3. Install the required dependencies:

    ```shell
    pip install -r requirements.txt
    ```

## Usage

To generate a password, run the following command:

```shell
streamlit run src/dashboard.py
```

Follow the prompts to specify the desired length and character types for the password.


## Contributing

Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
