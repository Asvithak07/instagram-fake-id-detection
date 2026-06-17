import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("model/fake_account_detector.pkl")

# Streamlit app title
st.title("📷 Instagram Fake Account Detection")

# Description
st.markdown("### 🚀 Enter Instagram Account Details Below to Predict Fake/Genuine Status")

# User Input Fields
profile_pic = st.selectbox("Does the account have a profile picture?", [0, 1])
username_length = st.slider("Username Length", 3, 30, 10)
fullname_words = st.slider("Number of Words in Full Name", 1, 5, 2)
nums_in_fullname = st.slider("Numbers in Full Name", 0, 10, 1)
name_equals_username = st.selectbox("Is Full Name Same as Username?", [0, 1])
description_length = st.slider("Bio/Description Length", 0, 200, 50)
external_url = st.selectbox("Does the account have an external URL?", [0, 1])
private = st.selectbox("Is the account Private?", [0, 1])
posts = st.slider("Number of Posts", 0, 1000, 50)
followers = st.slider("Number of Followers", 0, 100000, 500)
follows = st.slider("Number of Accounts Followed", 0, 10000, 500)

# Compute Follower-Following Ratio
follower_following_ratio = (followers + 1) / (follows + 1)

# Create a DataFrame from user inputs
input_data = pd.DataFrame([[profile_pic, username_length, fullname_words, nums_in_fullname, 
                            name_equals_username, description_length, external_url, private, 
                            posts, followers, follows, follower_following_ratio]],
                          columns=['profile_pic', 'nums/length username', 'fullname words',
                                   'nums/length fullname', 'name==username', 'description length',
                                   'external_URL', 'private', '#posts', '#followers', '#follows',
                                   'follower_following_ratio'])

# Prediction Button
if st.button("🔍 Predict"):
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.error("🚨 This account is **FAKE!**")
    else:
        st.success("✅ This account is **GENUINE!**")

# Footer
st.markdown("---")
st.markdown("**Developed with ❤️ using Streamlit**")
