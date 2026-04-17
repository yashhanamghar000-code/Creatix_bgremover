# 🎨 Creatix Background Remover

A powerful AI-based web app that removes image backgrounds instantly using deep learning. Built with **Streamlit** and **rembg**, this tool is fast, simple, and perfect for designers, marketers, and businesses.

---

## 🚀 Live Demo

👉 *(https://creatixbgremover-bxmb4uch2acrh75jbfuyg5.streamlit.app/)*

---

## ✨ Features

* 🧠 AI-powered background removal
* ⚡ Fast and lightweight processing
* 📤 Easy image upload (PNG, JPG, JPEG)
* 🖼 Side-by-side preview (Original vs Processed)
* ⬇ One-click download (PNG with transparent background)
* 🎨 Clean UI with Creatix branding

---

## 🛠 Tech Stack

* **Frontend & UI**: Streamlit
* **AI Model**: rembg (U²-Net)
* **Image Processing**: Pillow (PIL)
* **Language**: Python

---

## 📂 Project Structure

```
Creatix_bgremover/
│── bg_remove.py        # Main Streamlit App
│── requirements.txt    # Dependencies
│── runtime.txt         # Python version (for deployment)
│── README.md           # Project Documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yashhanamghar000-code/Creatix_bgremover.git
cd Creatix_bgremover
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the App

```bash
streamlit run bg_remove.py
```

---

## 🌐 Deployment (Streamlit Cloud)

1. Push your code to GitHub
2. Go to Streamlit Cloud
3. Select your repo
4. Set:

   * **Main file** → `bg_remove.py`
5. Click **Deploy**

---

## 🧠 How It Works

* The app uses the **rembg** library
* It applies a pre-trained deep learning model (U²-Net)
* The model detects foreground objects and removes the background
* Output is generated as a transparent PNG

---

## 🔮 Future Improvements

* 🎨 Custom background color selection
* 🖼 Bulk image processing
* 💼 User authentication & dashboard
* 💰 Paid API / SaaS model for Creatix

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and improve the project.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Yash Hanamghar**
📍 Pune, India
🚀 Founder of Creatix

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
