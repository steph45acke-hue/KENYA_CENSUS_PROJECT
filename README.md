# 🇰🇪 Kenya Census Data Analysis & Pipeline Project

This project takes raw 2019 Kenya census data, cleans it using Python, stores it in a relational database, and presents the insights through an interactive web app.

---

## 🚀 What This Project Does
* **Data Processing**: Reads and cleans a large raw census dataset using Python.
* **Statistical Analysis**: Computes key metrics like population averages, county rankings, and percentage shares.
* **Database Integration**: Automatically uploads clean data into a local MySQL database using SQLAlchemy.
* **Advanced Querying**: Uses SQL to segment counties into population tiers and identify those above the national average.
* **Interactive Dashboard**: Displays all insights through a custom, browser-based dashboard built with Streamlit.

---

## 🎯 Why I Built It
As a graduate with a background in statistics and economics, I wanted a project that goes beyond just writing scripts in a notebook. I built this to demonstrate a complete, end-to-end data pipeline—from raw files to a database and a live web app—that mirrors the work a professional data scientist does in the real world.

---

## 💻 Technology Used
* **Python**: For data cleaning, stats, and scripting (using Pandas and NumPy).
* **Matplotlib**: For drawing clean data visualization charts.
* **MySQL & MySQL Workbench**: For hosting and querying the relational database.
* **SQLAlchemy**: To connect Python directly to the MySQL database.
* **Streamlit**: For building the interactive web app dashboard.

---

## 📸 Visual Walkthrough

| Visual | Explanation |
| :--- | :--- |
| ![Raw Data](Screenshot%20(107).png) | **Inspecting Raw Data**: Running a diagnostic script in VS Code to see the structure of our raw dataset. |
| ![Stats](Screenshot%20(108).png) | **Descriptive Statistics**: Checking core metrics like the mean, standard deviation, and summary values. |
| ![Top Counties](Screenshot%20(109).png) | **County Ranking**: Isolating the top 5 most populated counties in Kenya. |
| ![Percentage Share](Screenshot%20(110).png) | **Proportional Analysis**: Computing each county's percentage contribution to the total national population. |
| ![Chart](Screenshot%20(111).png) | **Visualizations**: Plotting a clean bar chart of the top 10 most populated counties using Matplotlib. |
| ![SQL Upload](Screenshot%20(112).png) | **Database Migration**: Running our script to push the cleaned data into our local MySQL database. |
| ![Workbench](Screenshot%20(114).jpg) | **Querying**: Interacting with our data live inside MySQL Workbench. |
| ![SQL Avg](Screenshot%20(115).jpg) | **Advanced SQL (Average)**: Using subqueries to find counties with populations above the national average. |
| ![SQL Tiers](Screenshot%20(116).png) | **Advanced SQL (Tiers)**: Categorizing counties into tiers like "Mega County" using conditional logic. |
| ![Dashboard Top](Screenshot%20(117).png) | **Web App (Metrics)**: Our interactive dashboard showing summary metrics and a live data table. |
| ![Dashboard Chart](Screenshot%20(118).png) | **Web App (Charts)**: Dynamic bar charts that update as you interact with filters. |

---

## 🧠 Skills Learned
* **Data Wrangling**: Handling missing values, cleaning headers, and structuring raw data.
* **Database Management**: Designing tables and building automated insertion pipelines via Python.
* **Advanced SQL**: Writing subqueries and conditional statements for complex data segmentation.
* **Web App Deployment**: Turning static Python scripts into interactive, user-friendly browser dashboards.

---

## 🛠️ How to Use It

1. **Clone** this repository to your computer.
2. **Install** the required libraries:
   ```bash
   pip install pandas numpy matplotlib sqlalchemy mysql-connector-python streamlit

   Run the main data script to process the data:

Bash
python kenya_stats_project.py
Load the database (remember to update your password in the script):

Bash
python upload_to_sql.py
Launch the interactive dashboard:

Bash
streamlit run app.py