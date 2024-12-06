# Predicting-Pollution-Filter
This project uses a deep learning time-series approach to predict future pollution, and then use these results to calculate a necessary filter for HVAC systems.

Our code is spread across multiple files

To follow it in order, start with the Predictions Network (Final Submision).zip Inside of this zip file, there is NeuralNetwroks file, which handles the inital model setup and preprocessing. 
From there, move to the LSTM_GridSearchCV to see our final tuned LSTM model. Then go to the Average file (NOTE: it must be in the same folder as the LSTM Predictions (GridSearch).csv in order to run.
Finally, the results from the averaging can be fed into the Molecular_to_MERV file to convert the results into a MERV filter level.

Spoiler alert, we are recommending a filter of MERV level 14 to the Italian city where our model is being predicted for

Find our dataset at https://archive.ics.uci.edu/dataset/360/air+quality
 
