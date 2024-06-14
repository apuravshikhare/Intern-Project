# Django CSV analyzer Web APP

This project is a Django application that reads a CSV file, displays the first three rows of data, and visualizes the data using Matplotlib.

## Project Features

- Upload a CSV file and store it in the database.
- Display the first three rows of the uploaded CSV file.
- Visualize data with histograms, line plots, and pie charts using Matplotlib.

## Prerequisites

- Python 3.x
- Django 3.x or later
- Matplotlib
- Pandas

## Setup Instructions

Follow these steps to set up and run the project locally.

### 1. Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/apuravshikhare/intern-project/tree/master
```
### 2. Navigate to your Project Directory
change your directory to your project directory
```bash
cd your project directory name
```
### 3. Create and Activate a Virtual Environment
create an virtual environment to manage dependencies first install virtual environment wrapper.
```bash
pip install virtualenvwrapper-win
create an virtual environment wrapper
mkvirtualenv environment name
workon virtualenvironmentins
```
### 4. Install required packages 
django 
'bash 
pip install django
`
### 5. Apply the Migrations
``bash
python manage.py makemigrations
``
### 6. Run the Migrations
``bash
python manage.py migrate
``
### 7. Run the Development Server
``bash
python manage.py runserver
``
### 8. Upload a CSV File
``bash
CSV file
Upload a CSV File

### Project Description:
This web-application will allows user to upload any csv file after that user will see analysis File mainly histograms barplot and piechart and User will be able to view analysis of given dataset. According to dataset our system will analyze it as follows
it will display first three rows then it will display user How many missing values are There in the Dataset and it will visualize Three Types of visualizations bar plot line plot and pie chart. 








