# 🐶 Dog Image Gallery

<img width="1785" height="991" alt="Screenshot 2025-11-11 at 10 00 05 AM" src="https://github.com/user-attachments/assets/98af0089-7b23-43b8-a542-1e80f3891324" />

---

## Description

This full-stack web application, built with **Flask**, allows users to browse dog images by breed, utilizing the **Dog CEO API**. It serves as a portfolio piece demonstrating proficiency in front-end design (HTML/CSS), server-side routing, API integration, and dynamic web content rendering.

---

## 🛠 Technologies Used

* **Backend Framework:** Python / Flask
* **Frontend:** HTML5, Jinja Templating, CSS3
* **External API:** Dog CEO API (a free dog image API)
* **Libraries:** `requests` (for making HTTP API calls)

---

## ✨ Key Features

This application showcases the following technical skills:

* **API Integration:** Successfully makes **GET** requests to the external Dog CEO API to fetch images based on user selection or to retrieve a single random image.
* **Dynamic Routing & Templating:** Uses Flask routes (`@app.route`) to handle both `GET` (initial load) and `POST` (form submission) requests. Content is dynamically rendered using **Jinja templates**.
* **Form Handling & Validation (Backend):** Processes user input from a form (breed and number selection) and includes basic **server-side validation** to ensure both fields are selected before making an API call.
* **Structured Data Handling:** Manages and prettifies breed names using a dedicated Python dictionary (`dog_breeds.py`) for cleaner display on the frontend.
* **User Interface:** Features a responsive design with custom typography and clean CSS, utilizing a dropdown menu for breed selection.

---

## 🚀 Installation & Setup

Follow these steps to set up and run the project locally.

### Prerequisites

You need **Python 3** installed on your machine.

### 1. Clone the Repository

```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME
````

*(Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your actual details.)*

### 2\. Install Dependencies

It is recommended to use a virtual environment.

```bash
# Create a virtual environment
python3 -m venv venv
# Activate the environment
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
# Install required libraries
pip install Flask requests
```

### 3\. Run the Application

Execute the main application file:

```bash
python app.py
```

The application will now be running on your local server. Open your web browser and navigate to: **`http://127.0.0.1:5000/`**

-----

## 💡 Usage

The application presents two main ways to view dog images:

1.  **Select by Breed:** Choose a specific breed from the dropdown menu and select the desired number of images to fetch.

![dog_smallimage](https://github.com/user-attachments/assets/8343bd82-86c7-48fd-97f9-98d71da99327)


2.  **Random Image:** Click the "Random Image" button to instantly retrieve a single, random image from the entire collection.

![dog_randomimage](https://github.com/user-attachments/assets/2894b02a-04f0-4299-89e0-735141426674)

-----

## 🚧 Future Enhancements

  * Implement client-side JavaScript validation for a better user experience.
  * Add image caching to improve load times for frequently requested breeds.
  * Allow users to filter images by sub-breed (e.g., different types of poodles).
  * Add a testing suite (e.g., using `unittest` or `pytest`) for backend routes.

-----

## 📜 API Credit

Data and images provided by the **Dog CEO API**.
