# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Model Development Date: 07-07-2026
Model Type: Random Forest Classifier
Link to model documentation: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
Link to model user guide (with implementation examples): https://scikit-learn.org/stable/modules/ensemble.html#forest

## Intended Use
primary intended uses:
The model's primary use is to automate the process of predicting if a person makes more or less than $50,000 per year based on available census data.

primary intended users:
This model was intended to be used by myself for learning, and evaluators, to check my work.

out of scope uses: All use cases outside of academic are out of scope for this project.

## Training Data
Link to data and information about the set: https://archive.ics.uci.edu/dataset/20/census+income
Training test size: 80% of total population.

## Evaluation Data
The data for this project is from the 1994 Census and was given to me to use for this project. I used 20% of the total data for the testing split.

Preprocessing:
The categorical variables were One-Hot encoded with sklearn's OneHotEncoder and labels were converted to binary with LabelBinarizer.

## Metrics
Precision: 0.7222 | Recall: 0.6194 | F1: 0.6669

## Ethical Considerations
Due to the predictive nature of this model, it could be used to discriminate against people who make less than $50,000 per year if a user were trying to reduce risk. There may also be bias in the data itself. The data is also from 1994 so the era the data was collected in could also introduce bias, skewing the model, and potentially labeling some groups as making less money incorrectly.

## Caveats and Recommendations
The data is old and likely is not relevant to today's world. I would recommended that effort be made to scale the $50,000 labels based on inflation since '94 before using the model. There are likely other data considerations that would likely need to be adjusted. If the model were being put to use in a production environment I would be using the most recent census data I could find.