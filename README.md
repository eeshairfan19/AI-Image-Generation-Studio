# AI Image Generation Studio

Streamlit-based web application that generates images from natural language prompts using the DeepAI Text-to-Image API. The application provides an intuitive interface where users can describe an image, choose artistic settings, and generate AI-created artwork.

---

## Features

-  Generate AI images from text prompts
-  Natural language prompt input
-  Multiple artistic style selections
-  Image resolution selection
-  Number of image variations selection
-  Built-in example prompts
-  Secure API key management using Streamlit Secrets
-  Clean and responsive Streamlit interface
-  Loading spinner during image generation
-  Basic API error handling

---

## Technologies Used

- Python
- Streamlit
- DeepAI Text-to-Image API
- Requests
- Pillow (PIL)

---

## Project Structure

```
AI-Image-Generation-Studio/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── .streamlit/
    ├── secrets.toml
    └── secrets.example.toml
```
