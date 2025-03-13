import streamlit as st
import cv2 as cv
import numpy as np
import keras

# Page Configuration
st.set_page_config(page_title="Plant Leaf Disease Detection", layout="centered")

# Custom Styling
st.markdown("""
    <style>
        .main-title {
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            color: #2E8B57;
        }
        .description {
            font-size: 18px;
            text-align: center;
            color: #555;
        }
        .upload-section {
            font-size: 20px;
            font-weight: bold;
            text-align: center;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)


st.markdown('<p class="main-title">Plant Leaf Disease Detection System</p>', unsafe_allow_html=True)


st.markdown('<p class="description">The leaf disease detection model is built using deep learning techniques, and it uses transfer learning to leverage the pre-trained knowledge of a base model. The model is trained on a dataset containing images of 33 different types of leaf diseases. For more information about the architecture, dataset, and training process, please refer to the code and documentation provided.</p>', unsafe_allow_html=True)


label_name = ['Apple scab','Apple Black rot', 'Apple Cedar apple rust', 'Apple healthy', 'Cherry Powdery mildew',
'Cherry healthy','Corn Cercospora leaf spot Gray leaf spot', 'Corn Common rust', 'Corn Northern Leaf Blight','Corn healthy', 
'Grape Black rot', 'Grape Esca', 'Grape Leaf blight', 'Grape healthy','Peach Bacterial spot','Peach healthy', 'Pepper bell Bacterial spot', 
'Pepper bell healthy', 'Potato Early blight', 'Potato Late blight', 'Potato healthy', 'Strawberry Leaf scorch', 'Strawberry healthy',
'Tomato Bacterial spot', 'Tomato Early blight', 'Tomato Late blight', 'Tomato Leaf Mold', 'Tomato Septoria leaf spot',
'Tomato Spider mites', 'Tomato Target Spot', 'Tomato Yellow Leaf Curl Virus', 'Tomato mosaic virus', 'Tomato healthy']
    

st.write("Please input only leaf Images of Apple, Cherry, Corn, Grape, Peach, Pepper, Potato, Strawberry, and Tomato. Otherwise, the model will not work perfectly.")

model = keras.models.load_model('model\Leaf Deases(96,88).h5')


uploaded_file = st.file_uploader("Upload an image")
if uploaded_file is not None:
    image_bytes = uploaded_file.read()
    img = cv.imdecode(np.frombuffer(image_bytes, dtype=np.uint8), cv.IMREAD_COLOR)
    normalized_image = np.expand_dims(cv.resize(cv.cvtColor(img, cv.COLOR_BGR2RGB), (150, 150)), axis=0)
    predictions = model.predict(normalized_image)
    st.image(image_bytes)
    if predictions[0][np.argmax(predictions)]*100 >= 80:
        st.write(f"Result is : {label_name[np.argmax(predictions)]}")
    else:st.write(f"Try Another Image")