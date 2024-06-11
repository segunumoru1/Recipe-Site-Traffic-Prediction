# Tasty Bytes Recipe Site Traffic Prediction

![Tasty Bytes Logo](https://github.com/segunumoru1/Recipe-Site-Traffic-Prediction/blob/master/tiny-female-chef-cooking-vegan-meal-using-recipe-kitchen-cook-making-dish-from-restaurant-menu-flat-vector-illustration-healthy-food-diet-culinary-nutrition-concept-website-design_74855-22063.avif)

## About Tasty Bytes

Tasty Bytes was founded in 2020 amid the Covid Pandemic. The world wanted inspiration so we decided to provide it. We started as a search engine for recipes, helping people find ways to use up the limited supplies they had at home. Now, over two years on, we are a fully-fledged business. For a monthly subscription, we will put together a full meal plan to ensure you and your family are getting a healthy, balanced diet whatever your budget. Subscribe to our premium plan and we will also deliver the ingredients to your door.


## Project Overview

The aim of this project is to predict which recipes will have high traffic and to determine the likelihood of a recipe achieving "High" traffic with 80% probability using a Logistic Regression model.

## Business Focus & Metrics

### Business Goals
1. Predict which recipes will have high traffic.
2. Predict the "High" value of traffic of the recipes with 80% probability.

### Model Performance
The Logistic Regression model has achieved high rates of Precision, Recall, and F1 Score, all greater than or equal to 80%, ensuring reliable predictions.

### Business Recommendations
- **Deploy the Logistic Regression Model**: Implementing this model in production can ensure approximately 84% accuracy in identifying high-traffic recipes.
- **Personalized Meal Plans**: Use nutritional data to create personalized meal plans based on individual preferences and dietary needs.
- **Promote Popular Categories**: Emphasize popular recipe categories, especially chicken recipes, and introduce new and innovative options to maintain customer engagement.
- **Target Marketing Efforts**: Focus on high-traffic recipe categories like Potato, Pork, and Vegetable.
- **Optimize Serving Size Options**: Align serving sizes with customer preferences, highlighting popular options like 4 servings.

![Recipe Traffic Prediction](https://github.com/segunumoru1/Recipe-Site-Traffic-Prediction/assets/109175466/ca84f5e8-87a3-4b9b-a2f0-8f89a88e960a)

## Recommendations for Future Actions
- **Deploy the Model**: Implement the Logistic Regression Model into production to ensure high traffic predictions, boosting the Product Manager's confidence in generating more traffic.
- **Enhance Deployment**: Explore the best ways to deploy this model considering performance and cost, ideally on edge devices for convenience and security.
- **Data Collection**: Gather more data such as preparation time, cost per serving, ingredients, site duration time, incoming links, and recipe combinations.
- **Feature Engineering**: Increase the number of category values and create more meaningful features from existing variables.

## Methodology

1. **Data Collection**: Gathered recipe traffic data including various features like recipe type, ingredients, and user interactions.
2. **Data Preprocessing**: Cleaned and transformed the data for analysis.
3. **Feature Selection**: Identified key features that influence recipe traffic.
4. **Model Training**: Used a Logistic Regression model to predict high-traffic recipes.
5. **Model Evaluation**: Evaluated the model using metrics such as Precision, Recall, and F1 Score.
6. **Deployment**: Prepared the model for deployment to make real-time traffic predictions.

## Libraries and Technologies Used

- **Python**: Programming language used for model development.
- **Pandas**: Data manipulation and analysis.
- **NumPy**: Numerical computing.
- **Scikit-learn**: Machine learning library for model building.
- **Streamlit**: Framework for creating interactive web applications.
- **Matplotlib & Seaborn**: Data visualization.

## Skills Applied

- **Data Analysis**: Analyzing recipe traffic data to extract insights.
- **Machine Learning**: Developing and evaluating the Logistic Regression model.
- **Data Preprocessing**: Cleaning and transforming raw data.
- **Feature Engineering**: Creating and selecting meaningful features for the model.
- **Web Development**: Building an interactive web application using Streamlit.
- **Model Deployment**: Preparing the model for real-time predictions.

## How to Clone the Repository

To clone the repository and get started with the project, follow these steps:

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/segunumoru1/Recipe-Site-Traffic-Prediction.git
    ```

2. **Navigate to the Project Directory**:
    ```sh
    cd Recipe-Site-Traffic-Prediction
    ```

3. **Install Dependencies**:
    Ensure you have Python and pip installed. Then, install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the Streamlit App**:
    ```sh
    streamlit run app.py
    ```

5. **Access the Application**:
    Open your browser and go to `http://localhost:8501` to access the Streamlit application.

## Additional Resources

- **Project Demo**: [Streamlit App](https://segunumoru1-recipe-site-traffic-prediction-app-zu4pwy.streamlit.app/)

## Contact

For any questions or inquiries, please reach out via the project's GitHub Issues page.

---

Thank you for your interest in the Tasty Bytes Recipe Site Traffic Prediction project! We hope this README provides a comprehensive overview and helps you get started with the project.
