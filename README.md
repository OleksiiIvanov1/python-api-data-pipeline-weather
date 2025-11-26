# Python Weather Data ETL Pipeline 

A simple but professional end-to-end ETL (Extract–Transform–Load) pipeline that collects real-time weather data from a public API, cleans it, analyzes it, and generates charts for insights.

This project demonstrates core junior developer skills in Python, APIs, data processing, file handling, automation structure, and clean code organisation.

---

## Project Overview

This project fetches weather data from the OpenWeather API, stores raw JSON responses, cleans and transforms the data using Pandas, and generates visual charts for analysis. 

It simulates a real-world data workflow and follows a scalable folder structure used in production ETL processes.

---

## Project Structure

/python-weather-data-pipeline
│
├── data_raw/ # Raw API JSON responses
├── data_clean/ # Cleaned CSV files
├── charts/ # Generated charts (PNG)
│
└── src/
├── fetch_data.py # API call + save raw data
├── clean_data.py # Transform and clean
├── analyze.py # Produce charts
└── main.py # Pipeline orchestrator


---

## 🛠️ Tech Stack

- **Python 3**
- **Pandas**
- **Requests**
- **Matplotlib**
- **JSON**
- **OpenWeather API**

---

## Skills Demonstrated

- API integration and authentication  
- ETL design using modular Python scripts  
- Data cleaning and preprocessing  
- Folder organisation for real projects  
- Data visualization  
- Version control (Git)  
- Writing clean, maintainable code  
- Documentation and project communication  

---

## Example Outputs (Coming Soon)

Screenshots of charts will appear here once the analysis step is completed.

---

## How to Run the Pipeline

1. Install dependencies:

pip install pandas requests matplotlib


2. Add your API key inside `fetch_data.py`.

3. Run the full pipeline:

python src/main.py


---

## 🔮 Future Improvements

- Automate daily scheduling  
- Add multiple city support  
- Export combined datasets  
- Deploy results to a web dashboard  

---

## 🧑‍💻 Author

**Oleksii Ivanov**  
Junior Python Developer / BI Developer  
GitHub: github.com/OleksiiIvanov1
