**Plant Leaf Disease Detection System**
🚀 An AI-powered solution to detect plant leaf diseases using deep learning.
📌 **About the Project**
This project is a deep learning-based system that identifies 33 different types of plant leaf diseases using image classification techniques. The model is trained on a dataset of leaf images and can classify diseases in crops such as:
🌱 Apple, Cherry, Corn, Grape, Peach, Pepper, Potato, Strawberry, and Tomato.

✅ **Key Features:**

- AI-Powered: Uses a CNN model trained with Keras & TensorFlow.
- User-Friendly: Upload an image and get an instant disease diagnosis.
- Fast & Accurate: Over 80% accuracy in real-time predictions.
- Web App: Deployable using Streamlit/Hugging Face Spaces.

📂 **Project Structure**
```
Leaf-Disease-Detection/
│── dataset/                     # Training dataset (optional)
│── model/                       # Trained model files
│   ├── Leaf_Deases(96,88).h5    # Pretrained model
│── scripts/                      # Python scripts
│   ├── main.py                   # Streamlit app
│   ├── Make_API.py               # Flask API
│   ├── Request_API.py            # API request script
│── notebooks/                    # Jupyter Notebook for training
│   ├── Leaf_Deases.ipynb         # Model training/testing
│── requirements.txt              # Dependencies
│── README.md                     # Documentation
```

🛠 **Installation & Setup**

1️⃣ Install Dependencies
Run the following command in CMD or Terminal:
`pip install -r requirements.txt`

2️⃣ Run the Web App
To start the Streamlit app, run:
`streamlit run main.py`

3️⃣ Run the API
To start the Flask API, run:
`python Make_API.py`

Then test it using:
`python Request_API.py`



🎯 **Usage Guide**

1️⃣ Upload an image of a leaf in the web app.

2️⃣ The model analyzes the image and predicts the disease type.

3️⃣ The result & accuracy score is displayed instantly.

📌 Supported Image Types: .jpg, .png, .jpeg

📜 **Model Details**

📌 Model Used: Convolutional Neural Networks (CNN)

📌 Frameworks: TensorFlow, Keras

📌 Dataset: 33 classes of diseased and healthy leaves


**Deploy the Model**

1. Deploy on Streamlit Cloud
2. Push the project to GitHub.
3. Go to Streamlit Cloud and select your repo.
4. Click Deploy, and get a public URL! 🎉
