# README

There are two folders in this directory. One is the training data for training and validating your models, the other is the test data set for evaluating the proposed predictive model.

## Evaluation Metrics

F1 score which is the trade-off between precision and recall is the main concern in the performance evaluation.

## Submission File Format

You should submit a csv file with 1392 entries plus a header row. Your submission will show an error if your file has extra columns (beyond entid and CaseType) or rows.

 Your submitted file should only contain 2 columns:

·    entid (testing entid id is listed in folder *test data*)

·    CaseType (contains your predictions: 0,1,2,3,4.  Note that 4 means the type without any risk)

## Data

Folder *test data* is the data you need to predict the results. Folder *training data*  is training data which contains the basic information of each company and its risk type.