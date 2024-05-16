import streamlit as st
import pandas as pd
import streamlit as st

st.write("how are you")
'''
# Render a hyperlink that opens in the same tab
#st.markdown("[Click here to visit Streamlit's website](https://streamlit.io/)", unsafe_allow_html=True)

def ribbon():
        st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Helvetica Neu&display=swap');
        .ribbon {
            background-color: #FFD700;
            color: black;
            padding: 10px 0;
            text-align: center;
            font-weight: bold;
            width: 100%;
            font-family: 'Helvetica Neu', sans-serif;
        }
        .ribbon img {
            float: left;
            margin-right: 10px; /* Add some spacing between the image and text */
        }
        </style>
        """
        "<div class='ribbon'><img src='https://m.media-amazon.com/images/I/61qaugdNHrL._SX342_SY445_.jpg' width='100' height='100'> This is a top ribbon</div>",
        unsafe_allow_html=True
    )
def first_page():
    st.title("CSE 231 Spring 2024 - Course Overview")
    st.markdown("""
    CSE 231 is an introduction to programming, using Python. Students will learn about the design, implementation and testing of programs to solve problems primarily in engineering, mathematics and science. The emphasis is data manipulation using real-world, practical examples.

    **Our goal:** when a student is presented with a problem their response will be "I can write a program to do that!"

    Some topics we cover are: selection and iteration, strings, functions, data structures (lists, dictionaries, tuples), file processing, and user-defined classes.

    One way to understand what this course is about is to look at [old programming projects in our project archive](https://cse.msu.edu/~cse231/).

    The course is a flipped classroom course with standard lectures replaced by readings and videos. Online Section 730 will be doing the labs online.

    Grade history can be found [here](https://cse.msu.edu/~cse231/).
    """)
# Sample data
data = {
    'WEEK': ['05/12/2024', 'Jane', 'Alice', 'Bob'],
    'Sunday': ['', 30, 35, 40],
    'Monday': ['New York', 'Proj06 Availabe', 'Paris', 'Tokyo'],
    
    'Tuesday': ['', 30, 35, 40],
    'Wednesday': ['New York', 'Proj06 Availabe', 'Paris', 'Tokyo'],
    'Thursday': ['New York', 'Proj06 Availabe', 'Paris', 'Tokyo'],
    'Friday': ['', 30, 35, 40],
    'Saturday': ['New York', 'Proj06 Availabe', 'Paris', 'Tokyo'],
    

}
print()

# Create a DataFrame
df = pd.DataFrame(data)

st.set_page_config(layout="wide")

# Define CSS to set background image and center-align column titles
def set_background(image_url):
    # CSS to set background
    background = """
    <style>
    body {
        background-image: url("%s");
        background-size: cover;
    }
    th {
        text-align: center !important; /* Center-align column titles */
    }
    </style>
    """ % image_url
    st.markdown(background, unsafe_allow_html=True)

# Main function
def main():
    # Top ribbon
    # Render top ribbon
    ribbon()
    
    first_page()
    # Streamlit content goes here
    st.title("Beautiful Table Example")
    
    # Modify the DataFrame to render the "Proj06 Availabe" location as a clickable hyperlink
    df['Monday'] = df['Monday'].apply(lambda x: f'<a href="https://cse.msu.edu/~cse231/" target="_self">Proj06 Availabe</a>' if x == 'Proj06 Availabe' else x)
    
    # Add multiple lines with numbering to a cell
    df['Monday']= df['Monday'] + "<br><ol><li>Line 1</li><li>Line 2</li><li>Line 3</li></ol>"
    
    # Render the DataFrame with clickable hyperlinks and multiple lines in one cell
    st.write("Here's a beautiful table:")
    st.write(df.to_html(escape=False), unsafe_allow_html=True)
    #set_background("PUNCH.BODY.BOOK.jpg")

    # Streamlit content goes here
    st.title("Streamlit Background Image Example")
    st.write("This is a Streamlit app with a custom background image.")

if __name__ == "__main__":
    main()'''
