## **Dataset**

The dataset is related to customer churn prediction, where the goal is
to predict whether a customer is likely to churn based on the given
features. Machine learning models can be trained on this dataset to
predict the churn risk of customers, helping businesses take appropriate
actions to retain customers and improve customer satisfaction.

## **Problem Statement**

Create a robust costumer churn prediction to directly intialize and
handle the appropriate actions to prevent costumers leaving our services

### EDA Conslusion

-   The dataset has an imbalance in the independent variable
    \"churn_risk_score,\" which is the target variable indicating the
    churn risk of customers. It contains two unique values: 0 and 1.
    Upon examining the dataset, we observe that there are 20,018
    instances of class 1 (indicating churn) and 16,992 instances of
    class 0 (indicating not churn).

-   majority user are lived in city and town

-   data reveals that the highest churn rate is observed among customers
    who have either \'No Membership\' or a \'Basic Membership.\'

-   accross costumer activity and loyalty : `avg_transaction_value`,
    `avg_frequency_login_days` and `points_in_wallet` indicate more on
    costumer who likely to churn

-   most of churn costumer didn\'t leave a complaint

### Model Training {#model-training}

1.  Sequential API (Sq):

-   Test Loss (MAE): 0.075261
-   Test Accuracy: 0.924480 This is the initial ANN model created using
    the Sequential API. The model achieved a test loss of approximately
    0.075 and a test accuracy of approximately 92.45%.

1.  Functional API (Fnc):

-   Test Loss (MAE): 0.118850
-   Test Accuracy: 0.915695 This is the initial ANN model created using
    the Functional API. The model achieved a test loss of approximately
    0.119 and a test accuracy of approximately 91.57%.

1.  Sequential API Improved (Sq Improve):

-   Test Loss (MAE): 0.074461
-   Test Accuracy: 0.926171 This is an improved version of the ANN model
    created using the Sequential API. The improvements resulted in a
    slightly lower test loss of approximately 0.074 and a slightly
    higher test accuracy of approximately 92.62% compared to the
    original Sq model.

1.  Functional API Improved (Fnc Improve):

-   Test Loss (MAE): 0.101553
-   Test Accuracy: 0.929544 This is an improved version of the ANN model
    created using the Functional API. The improvements resulted in a
    lower test loss of approximately 0.102 and a higher test accuracy of
    approximately 92.95% compared to the original Fnc model.

In summary, both the Sequential API and Functional API models achieved
reasonably good test accuracy on the given dataset. The improved
versions of both models (Sq Improve and Fnc Improve) show better
performance with lower test loss and higher test accuracy than their
respective initial versions. The improvements indicate that adjustments
or changes made to the models resulted in better generalization and
predictions on unseen data.

### Model Improvement {#model-improvement}

For Imporve using more Hidden Layer and Optimezer Params, and handling
imbalance data

### Model Inference {#model-inference}

as the result all X_test is fully match predictid compare to y_test
actual value
