# SnapSeek - AI-Powered Image Search for Windows 

## 📌 Overview
SnapSeek is a Windows application that lets you **search for images using a text prompt**. It leverages the **OpenAI CLIP model** to index images and allows users to find specific images in large folders without manually browsing through thousands of files.

[Demo Video](https://github.com/user-attachments/assets/7fa662e3-f9ef-4d9c-af9b-c087c9e71b61)

## ✨ Features
- **AI-powered image search** using text prompts.
- **Fast and efficient indexing** of images using the CLIP model.
- **Direct navigation** to found images in the folder.
- **Simple UI** for selecting a folder and searching images.
- **Lightweight and easy to use** with minimal dependencies.

## 🚀 Installation
### **1. Clone the Repository**
```sh
git clone https://github.com/avgvcoding/SnapSeek.git
cd SnapSeek
```

### **2. Create a Virtual Environment (Optional but Recommended)**
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

## 🖥️ Usage
### **Run the Application**
```sh
python gui.py
```
This will open the SnapSeek application.

### **How It Works**
1. **Select a folder** containing images.
2. The app **indexes images** using the CLIP model and stores them in text format.
3. **Enter a text prompt** describing the image you’re looking for (e.g., *"A boy wearing a hat"*).
4. SnapSeek will **display matching images** instantly.
5. Click the **arrow icon** to open the image directly in your folder.

## 📸 Demo
### **Image Search in Action**
*Demo images and video will be added here.*

## 📂 Repository Structure
```
📦 SnapSeek
├── 📂 __pycache__
├── 📄 gui.py             # Main GUI Application
├── 📄 main.py            # Core Image Processing Logic
├── 📄 requirements.txt   # Dependencies
├── 📄 README.md          # Documentation
├── 📄 logo.png           # App Logo
├── 📄 arrow.png          # Navigation Icon
├── 📄 open-folder.png    # Folder Selection Icon
├── 📄 search_icon.png    # Search Icon
```

## 🛠️ Technologies Used
- **Python** (Backend)
- **Tkinter** (GUI)
- **OpenAI CLIP Model** (AI-based Image Search)

## 🙌 Contributing
Feel free to fork this repository, submit issues, and send pull requests!

## 📧 Contact
For any queries or suggestions, reach out via [GitHub Issues](https://github.com/avgvcoding/SnapSeek/issues).

---
Made with ❤️ by **Aviral Gupta**

