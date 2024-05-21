import streamlit as st
import google.generativeai as genai
import google.ai.generativelanguage as glm
from dotenv import load_dotenv
from PIL import Image
import os
import io
import requests
import json
import firebase_admin
from firebase_admin import credentials, firestore

load_dotenv()

def image_to_byte_array(image: Image) -> bytes:
    imgByteArr = io.BytesIO()
    image.save(imgByteArr, format=image.format)
    imgByteArr = imgByteArr.getvalue()
    return imgByteArr

API_KEY = os.environ.get("GOOGLE_API_KEY")
FIREBASE_API_KEY = os.environ.get("FIREBASE_API_KEY")
genai.configure(api_key=API_KEY)

# Initialize Firebase if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate("pemweb-1f265-2ed4a1c2967b.json")
    firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()

st.image("./logogeotera.png", width=200)
st.title("🦖Tera Chat")

def signup(email, password):
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={FIREBASE_API_KEY}"
    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    response = requests.post(url, data=json.dumps(payload))
    return response.json()

def login(email, password):
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_API_KEY}"
    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    response = requests.post(url, data=json.dumps(payload))
    return response.json()

def app():
    st.title('Register/ Login dulu yah  :violet[hehe...] 😅')

    choice = st.selectbox('Login/Signup', ['Login', 'Sign Up'])
    if choice == 'Login':
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')

        if st.button('Login'):
            result = login(email, password)
            if 'idToken' in result:
                st.success('Login successful')
                st.session_state['login'] = True
                st.experimental_rerun()  # Refresh the app to update the state
            else:
                st.error(result.get('error', {}).get('message', 'An error occurred'))

    else:
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')
        username = st.text_input('Enter username')

        if st.button('Create My Account'):
            result = signup(email, password)
            if 'idToken' in result:
                st.success('Account created successfully')
            else:
                st.error(result.get('error', {}).get('message', 'An error occurred'))

def save_to_firestore(collection, data):
    try:
        doc_ref = db.collection(collection).add(data)
        st.success(f"Data successfully saved to Firestore: {doc_ref.id}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def main():
    if 'login' not in st.session_state:
        st.session_state['login'] = False

    if not st.session_state['login']:
        app()
    else:
        gemini_pro, gemini_vision = st.tabs(["Tanya Tera", "Cerita Tera"])

        with gemini_pro:
            st.header("Yuk Chat bareng tera")
            st.write("")

            prompt = st.text_input("tanya apa pun tera bakal jawab ...", placeholder="Prompt", label_visibility="visible")
            model = genai.GenerativeModel("gemini-pro")

            if st.button("jawab dong!", use_container_width=True):
                response = model.generate_content(prompt)

                st.write("")
                st.header(":blue[Response]")
                st.write("")

                st.markdown(response.text)
                
                # Save to Firestore
                save_to_firestore("gemini_pro_responses", {"prompt": prompt, "response": response.text})

        with gemini_vision:
            st.header("Yuk Kirim fotomu ke tera")
            st.write("Tera bakal Ceritain kenangan indah di fotomu ...")

            image_prompt = st.text_input("sampein pesan di foto mu ...", placeholder="Prompt", label_visibility="visible")
            uploaded_file = st.file_uploader("Kirim Fotonya juga yaaah ...", accept_multiple_files=False, type=["png", "jpg", "jpeg", "img", "webp"])

            if uploaded_file is not None:
                st.image(Image.open(uploaded_file), use_column_width=True)

                st.markdown("""
                    <style>
                            img {
                                border-radius: 10px;
                            }
                    </style>
                    """, unsafe_allow_html=True)

            if st.button("Ayo Tera!", use_container_width=True):
                model = genai.GenerativeModel("gemini-pro-vision")

                if uploaded_file is not None:
                    if image_prompt != "":
                        image = Image.open(uploaded_file)

                        response = model.generate_content(
                            glm.Content(
                                parts=[
                                    glm.Part(text=image_prompt),
                                    glm.Part(
                                        inline_data=glm.Blob(
                                            mime_type="image/jpeg",
                                            data=image_to_byte_array(image)
                                        )
                                    )
                                ]
                            )
                        )

                        response.resolve()

                        st.write("")
                        st.write(":blue[Response]")
                        st.write("")

                        st.markdown(response.text)
                        
                        # Save to Firestore
                        save_to_firestore("gemini_vision_responses", {
                            "image_prompt": image_prompt,
                            "response": response.text,
                            "image_name": uploaded_file.name
                        })

                    else:
                        st.write("")
                        st.header(":red[Ceritain dulu dong]")

                else:
                    st.write("")
                    st.header(":red[Kirim Gambar Dulu Dong]")

if __name__ == "__main__":
    main()
