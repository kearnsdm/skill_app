import streamlit as st
import pandas as pd

# Page title
st.title("Skill & Subskill Selector")

# Sample data - replace this with your actual data
data = {
    'Skill': ['Decoding', 'Decoding', 'Decoding', 'Comprehension', 'Comprehension', 'Fluency'],
    'Subskill': ['Phonics', 'Sight Words', 'Blending', 'Main Idea', 'Details', 'Rate']
}

df = pd.DataFrame(data)

# Create the filtered dropdown
skill = st.selectbox("Select a Skill:", df['Skill'].unique())

# Filter subskills based on selected skill
filtered_subskills = df[df['Skill'] == skill]['Subskill'].unique()
subskill = st.selectbox("Select a Subskill:", filtered_subskills)

# Display selection  
st.write(f"You selected: **{skill}** - **{subskill}**")

# Optional: Show all data
if st.checkbox("Show all data"):
    st.dataframe(df)
