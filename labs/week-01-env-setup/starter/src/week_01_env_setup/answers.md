# Excercise 1
Differences:
- the train-test split differs
- the logistic regression starts from another random state

Problem: we cannot tell the customer the "real" numbers, if our model depends so much on the data's split and the random seed of the model. There might be serious issues with the data.


# Excercise 4
train_test_split is a function imported from a lib; we don't know its behaviour for an invalid value. Better to keep the validation of sensibel inputs in our hands.