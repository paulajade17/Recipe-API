# Recipe-API

This project is a Python-based command-line tool that allows users to search for recipes based on an **ingredient** and a **dietary requirement**. It fetches data from the [Edamam Recipe Search API](https://developer.edamam.com/) and returns a curated list of recipes that meet the given dietary filter, along with helpful metadata like meal type, cuisine, and a direct link to the full recipe.

---

## 🔧 Tech Stack

- **Python**  
- **Edamam Recipe API**  
- **Command Line Interface (CLI)**  

---

## 🎯 Project Purpose

This was a collaborative project designed to solve common frustrations around recipe discovery for people with specific dietary needs. Our goal was to create a lightweight solution that:

- Simplifies recipe browsing by dietary preference
- Avoids the tediousness of manual filtering or editing
- Provides clean, readable output in the terminal

---

## ⚙️ Key Features

- Search for recipes using an ingredient and dietary preference  
- Filters and displays only recipes that meet your dietary requirement  
- Outputs user-friendly recipe data:
  - ✅ Recipe name (with highlighted colour formatting)
  - 🌍 Cuisine Type
  - 🍽️ Dish Type (if available)
  - 🧾 Ingredient List
  - 🔗 URL to full recipe
  - 🍱 Meal Type
- Handles inconsistent or missing data in API responses gracefully  
- Custom formatting using string functions and terminal color codes  

---

## 🚧 Challenges Faced

- The **API returned inconsistent formatting** for values in dictionaries/lists.
- Some keys (e.g., `"dishType"`) were **missing entirely** in certain responses.
- Dietary filters like "nut-free" or "dairy-free" required **non-intuitive matches**, prompting us to create a reformatting function to align inputs with API expectations.

---

## 🔨 Workarounds & Enhancements

- Built a custom `reformat()` function to standardise dietary inputs for API matching  
- Used Python’s `string.capwords()` and `.join()` for correct formatting  
- Wrapped data outputs in conditions to **avoid key errors** and enhance reliability  
- Added **terminal color formatting** for an engaging and readable display  
- Next steps include:
  - Grouping ingredients into **classification buckets** (e.g. all nuts, dairy products)
  - Adding **calorie filters** for health-conscious users
  - Exporting results as a **downloadable CSV**

---

## 🏃‍♀️ How to Run

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

2. **No external packages required other than requests, which can be installed if needed:**
    ```bash
    pip install requests

3. **Run the App:**
    ```bash
    python3 your_script_name.py

## 🧠 Contributors
  Emily – Initial structure, API exploration, and logic development

  Anne – Formatting and exception handling, string manipulation

  Paula – UX enhancements, color formatting, and feature planning



