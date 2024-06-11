import pickle
import streamlit as st
import joblib
import numpy as np

# Loading the trained model
classifier = joblib.load('Classifier.pkl')

@st.cache(suppress_st_warning=True) 
def prediction(calories, protein, category):
    # Initialize the Category variable
    Category = None
            
    # Convert category to numerical
    if category == "Chicken":
        Category = 1
    elif category == "Breakfast":
        Category = 2
    elif category == "Beverages":
        Category = 3
    elif category == "Lunch/Snacks":
        Category = 4
    elif category == "Potato":
        Category = 5
    elif category == "Pork":
        Category = 6
    elif category == "Vegetable":
        Category = 7
    elif category == "Dessert":
        Category = 8
    elif category == "Meat":
        Category = 9
    else:
        Category = 10

    # Making Predictions
    prediction = classifier.predict([[calories, protein, Category]])

    if prediction == 0:
        pred = "Low"
    else:
        pred = "High"

    return pred



# This is the main function in which we define our YearsAtCompany, TotalWorkingYears, Shift, JobLevel, JobInvolvement, Age
def main():
    # Front end elements of the web page
    html_temp = '''
    <div style="background-color: red;padding:10px">
    <h2 style="color:black;text-align:center;">Recipe Site Traffic Prediction App</h2>
    </div>
    '''

    # Display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)

    # Following lines create boxes in which user can enter data required to make prediction
    protein = st.number_input("Protein", min_value=0, step=1)
    calories = st.number_input("Calories", min_value=0, step=1)
    category = st.selectbox('Category', ("Lunch/Snacks", "Beverages", "Potato","Vegetable", "Meat", "Chicken", "Pork", "Dessert", "Breakfast", "One Dish Meal"))
    result = ""

    # When 'Predict' is clicked, make prediction and store it
    if st.button("Predict"):
        result = prediction(calories, protein, category)
    st.success("Recipe Site Traffic Rate is : {}".format(result))


if __name__ == '__main__':
    main()