# Model Card

## Model Details

This model is a supervised binary classification model built using a Random Forest Classifier implemented with the scikit-learn library.

The model was trained using the UCI Census Income dataset to predict whether an individual's annual income exceeds $50,000 based on demographic and employment-related attributes. The model uses features such as age, education, marital status, occupation, work class, race, sex, native country, hours per week, and capital gain/loss. Categorical features were processed using OneHotEncoder, and the target variable was encoded using LabelBinarizer. The model was trained using default Random Forest parameters provided by scikit-learn.

No explicit fairness constraints or bias mitigation techniques were applied during model training. However, the model includes demographic attributes that may introduce potential bias, and predictions should be interpreted carefully.

Additional information about the dataset can be found in the UCI Machine Learning Repository Census Income dataset documentation.

Citation: Dua, D. and Graff, C. UCI Machine Learning Repository: Census Income Dataset.

This model is provided for educational and demonstration purposes only.

Questions, comments, or feedback regarding this model may be directed to the project developer through the associated GitHub repository.

## Intended Use

The primary intended users of this model include students, machine learning engineers and data scientists who are learning how to build and deploy scalable machine learning systems. The model may also be useful for instructors and reviewers who are assessing machine learning workflow implementation.

This model is not intended for high-stakes decision-making scenarios such as credit approval, housing applications, legal judgments, healthcare decisions, or other situations that may significantly impact individuals. The model should not be used as the sole basis for decisions involving protected demographic groups, as the training data may contain historical bias and fairness constraints were not explicitly applied during development.


## Training Data

The model was trained using the UCI Census Income dataset, which contains demographic, employment, and financial information used to predict whether an individual's annual income exceeds $50,000. Features include age, education, occupation, marital status, race, sex, hours worked per week, and capital gain or loss.

Approximately 80 percent of the dataset was used for training, while the remaining 20 percent was reserved for evaluation. The training data includes samples from both income classes and multiple demographic groups.

Before training, categorical features were encoded using OneHotEncoder, and the target labels were transformed using LabelBinarizer. The processed categorical features were then combined with continuous numerical features to create the final training dataset.

No explicit fairness constraints were applied during training, but slice-based evaluation was later performed to monitor model performance across different groups.



## Evaluation Data

This dataset was selected because it is a widely used benchmark dataset for supervised classification tasks and provides a realistic example for building, testing, and deploying a machine learning pipeline. The dataset contains both numerical and categorical features, making it suitable for demonstrating preprocessing, model training, evaluation, and deployment in a production-style machine learning workflow.

Prior to evaluation, the dataset was split into training and testing subsets using an 80/20 split,  to ensure the model was evaluated on previously unseen data. Categorical features were processed using OneHotEncoder to convert text-based categories into numerical. The target labels were encoded using LabelBinarizer for binary classification. In addition, model slice evaluation was performed on selected categorical features to assess model performance across different demographic groups.


## Metrics

The model was evaluated using Precision, Recall, and F1 Score. They achieved:

Precision: 0.7419
Recall: 0.6384
F1 Score: 0.6863

Precision measures how many positive predictions were correct. Recall measures how many actual positive cases were identified. The F1 score provides a balanced measure of both precision and recall. The model uses a default binary classification decision threshold of 0.5 when determining whether an input sample belongs to the income class greater than $50,000. 

Variation in model performance was further analyzed by performing slice-based evaluation across selected categorical features, including demographic and employment-related groups. Precision, Recall, and F1 Score were calculated for each slice and recorded in the slice_output.txt file. This approach helps identify differences in model behavior across population groups and supports the detection of potential bias or inconsistent performance.

## Ethical Considerations

The census dataset contains demographic and socioeconomic information that may introduce bias related to age, gender, race, or occupation. Predictions generated by this model should not be used for hiring, lending, or other high-stakes decisions without additional fairness analysis.

## Caveats and Recommendations

The model was trained on historical census data, which may not fully represent current economic conditions or demographic changes. Future improvements may include hyperparameter tuning, fairness testing and retraining on more recent data.

