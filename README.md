# ExpenseTracker 

This is a simple command-line Python script to help you keep track of your expenses and manage your monthly budget. 
The script allows you to input your expense details, saves them to a csv file, and provides a summary of your spending based on expense categories. 


# Features 
- Record expenses with name category, and amount
- Categorize expenses into Food, Home, Work, Fun, & Misc. 
- Calculate the total amount spent and remaining budget
- Provide the remaining number of days in the current month and calculate daily budget


# Requirements  
- Git
- Docker

# Use
1. First clone this repository to your local machine by running the following command in your terminal:   
```git clone https://github.com/rojerdu-dev/ExpenseTracker.git``` 

2. Navigate to the project directory   
Change the current working directory to the "ExpenseTracker" folder:   
```cd ExpenseTracker``` 

3. Build the Docker image   
Next, build the Docker image by running the following command (replace <image_name> with a name of your choice):     
```docker build -t <image_name>``` 

For instance:   
```docker build -t expense-tracker-image``` 

4. Run the Docker container   
Next, start a Docker container with the image you've built with the following command (again, replace <image_name> with whichever name you used in the last step):   
```docker run -it expense-tracker-image /bin/bash```

5. Run the Python app     
Now that you're in the container, run the expense tracker app with this command:    
```python app.py``` 

You should see the app running in the terminal (in the container). 
Follow the prompts to start tracking your expenses!

