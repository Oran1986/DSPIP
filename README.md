# DSPIP
Home Test


This project shows the implementation of 3 Machine Learning Algorithms:
Gradient Descent
KNN
Naive Bayes

4 files are within:
KNN_and_Naive_Bayes is a python file that implements, how surprising: KNN and Naive Bayes algorithms
GD_L2 is a python file that implements Gradient Descent, using L2 distance
2 more excel files with the data required. both python files get the data by reading eat from the excel files.
The KNN and Naive Bayes algorithms use the Iris dataset
http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html

Both the KNN and Naive Bayes are implemented seperately to classify.

The Gradient Descent uses linear regression to predict the price of a house using 3 parameters:
The area of the house, the area of its balcony and the number of parking spots.
It uses a data made up, in which the price of the house is as follows:

Price = 100 + 5 * area + 1.5 * balcony area + 25 * number_of_parking_spots

Over 400,000 iterations, one can see that the weights tend to achieve values that are close to the weights used for creating the dataset:

The Gradient Descent achieved:
W = [ 5.016,  1.511, 25.124] for area, balcony area and number of parking spots accordingly
and b = 98.252
While the dataset weights used to create the data are as follows
W = [5, 1.5, 25]
and b = 100

A graph of the weights as a function of the iteration number is produced at the end of the implementation, showing how the weights get closer to the reality as the number of iteration increases.



