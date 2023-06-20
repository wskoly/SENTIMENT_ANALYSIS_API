

# Sentiment Analysis API

This project provides an API endpoint for sentiment analysis. It allows you to analyze the sentiment of text input and get the corresponding sentiment label.

## Steps to run the project

> Note: This project was created and tested with Python version 3.11.3.
> If you encounter any issues while setting up the project with a
> different Python version, I recommend using Python 3.11.3 for optimal
> compatibility.

1.  Clone the project using the following command:   
    ```
    git clone git@github.com:wskoly/SENTIMENT_ANALYSIS_API.git
    ``` 
    Alternatively, you can unzip the attached file.
    
2.  Navigate to the project's root directory and create a virtual environment:
    ```
    python -m venv .venv
    ``` 
    
3.  Activate the virtual environment:
   -   On Windows: 
	   ```
	   .venv\Scripts\activate
	   ``` 
   -   On Linux/Mac: 
	   ```
	   source .venv/bin/activate
	   ```
        
4.  Install the project dependencies:    
    ```
    pip install -r requirements.txt
    ``` 
    
5.  Set up the sentiment analysis model by running the following command:
    ```
    python APIS/analyzer.py
    ``` 
    
6.  Apply the migrations using following command (Optional):   
    ```
    python manage.py migrate
    ```
    
7.  Run the project using the following command:   
    ```
    python manage.py runserver 0.0.0.0:8000
    ```
      
8.  You can access the API endpoint by visiting [http://127.0.0.1:8000/analyze/](http://127.0.0.1:8000/analyze/) or using a tool like Postman to interact with it.
    

## Project walkthrough

-   This project utilizes Django and Django Rest Framework for the backend.
-   The sentiment analysis is performed using the **"finiteautomata/bertweet-base-sentiment-analysis"** model from Hugging Face.
-   The API endpoint is implemented in the **APIS/views.py** file, and the sentiment analysis logic resides in the **APIS/analyzer.py** file.
-   All files are well-commented for clarity and understanding.
