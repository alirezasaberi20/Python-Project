import streamlit as st
from src.main import PinPasswordGenerator, RandomPasswordGenerator, RandomWordsGenerator
import pyperclip

# Title of the Streamlit app
st.title('Password Generator')

# Display an image (icon) at the top of the page
st.image('https://cdn-icons-png.flaticon.com/512/5850/5850971.png', width=200)

# Function to copy the generated password to the clipboard
def copy_to_clipboard(text):
    pyperclip.copy(text)  # Copy the provided text to the clipboard
    st.success("Copied to clipboard!")  # Display success message in Streamlit

# Let the user choose the type of password to generate
user_choice = st.radio('Select Password Type', ['PIN', 'Random', 'Random Words'])

# Logic for generating a PIN password
if user_choice == 'PIN':
    # Slider to choose the length of the PIN (between 8 and 50)
    length = st.slider('Select Length of PIN', 8, 50, 8)
    
    # Create a PinPasswordGenerator object with the chosen length
    pin_gen = PinPasswordGenerator(length)
    
    # Generate the PIN
    password = pin_gen.generate()
    
    # Display the generated PIN
    st.write(f'Your PIN is: {password}')
    
    # Styling for the "Copy Password to Clipboard" text
    st.markdown(
        """
        <style>
        .bold-text {
            font-size:30px;
            font-weight:bold;
        }
        </style>
        <p class="bold-text">Copy Password to Clipboard</p>
        """, 
        unsafe_allow_html=True
    )
    
    # Store the password to copy it later
    text_to_copy = password
    
    # Button to copy the PIN to the clipboard
    if st.button("Copy"):
        copy_to_clipboard(text_to_copy)

# Logic for generating a random character password
elif user_choice == 'Random':
    # Slider to choose the length of the password (between 8 and 50)
    length = st.slider('Select Length of Password', 8, 50, 8)
    
    # Checkbox to include numbers in the password
    include_num = st.checkbox('Include Numbers')
    
    # Checkbox to include symbols in the password
    include_symbols = st.checkbox('Include Symbols')
    
    # Create a RandomPasswordGenerator object with the chosen parameters
    random_gen = RandomPasswordGenerator(length, include_num, include_symbols)
    
    # Generate the random password
    password = random_gen.generate()
    
    # Display the generated password
    st.write(f'''Your Password is: {password}''')
    
    # Styling for the "Copy Password to Clipboard" text
    st.markdown(
        """
        <style>
        .bold-text {
            font-size:30px;
            font-weight:bold;
        }
        </style>
        <p class="bold-text">Copy Password to Clipboard</p>
        """, 
        unsafe_allow_html=True
    )
    
    # Store the password to copy it later
    text_to_copy = password
    
    # Button to copy the random password to the clipboard
    if st.button("Copy"):
        copy_to_clipboard(text_to_copy)

# Logic for generating a random words password
else:
    # Slider to choose the number of words in the password (between 4 and 24)
    num_words = st.slider('Select Number of Words', 4, 24, 4)
    
    # Create a RandomWordsGenerator object with the chosen number of words
    words_gen = RandomWordsGenerator(num_words)
    
    # Generate the random words password
    password = words_gen.generate()
    
    # Display the generated password, joining the words with " - "
    st.write(f'''Your Password is:  { '  -  '.join(password)}''')
    
    # Styling for the "Copy Password to Clipboard" text
    st.markdown(
        """
        <style>
        .bold-text {
            font-size:30px;
            font-weight:bold;
        }
        </style>
        <p class="bold-text">Copy Password to Clipboard</p>
        """, 
        unsafe_allow_html=True
    )
    
    # Store the password to copy it later
    text_to_copy = password
    
    # Button to copy the word-based password to the clipboard
    if st.button("Copy"):
        copy_to_clipboard(text_to_copy)
