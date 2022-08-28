# ALL THE REQURIED FILES WHICH ARE USED TO CARRY OUT THIS PROJECT WERE ATTACHED IN THE REPOSITORY. USER INTERFACE FILES, CODING PART, RESULTS, DATA SETS, AND PPT in which all the detalis and overview of the project has been discussed. The UI has been build with the help flask server. The UI has been deployed in heroku platform.
# App Link : https://osaprediction.herokuapp.com/
# ABSTRACT
Obstructive Sleep Apnea (OSA) is a rather prevalent condition. Adult men are affected by
OSA at a rate of 14%, whereas adult women are affected at a rate of 5%. Due to upper airway
collapse, sleep fragmentation, and/or oxygen desaturation, patients with OSA experience occasional
cessation or reduction of breathing during sleep, resulting in non-restorative sleep, excessive daytime
drowsiness, and weariness.In clinical practice, predicting the severity of Obstructive Sleep Apnea (OSA) is still difficult. To tackle the challenge, a machine learning approach was used to create a predictive model for
determining OSA severity. OSA severity has been measured based on the Apnea-Hypopnea Index
(AHI). To create a prediction model, which includes 11 medical factors that aid in predicting the severity of OSA. Various
supervised machine learning classifier approaches were implemented to evaluate the model. In the
case of a balanced data set, the Random Forest classifier performed well, with the top result being
91% accuracy. A User Interface (UI) has been created for classifying OSA condition of a person by
supplying all medical factors to the UI as a numerical input.
 # OSA VS NORMAL SLEEPING
 ![OSA](https://user-images.githubusercontent.com/92075957/174732667-f001a2dc-837e-4a48-90ff-f4921fb8d039.jpg)

# PROPOSED METHOD
In the proposed method majorly focused on few techniques for predicting the model. Here,
we used other classification algorithms like gaussianNB, svm, extra trees classifier and K-Nearest
Neighbour, random forest, decision tree, logistic regression and linear svc. Apart from these we
further used a technique for predicting the model with the help of Synthetic Minority Over-sampling
Technique (SMOTE) which help to convert imbalanced data set to balanced data set. Based on these
approaches we are going to conclude that which algorithm is best algorithm and which provides the
best result for the model. A UI page has been created to test the model prediction
# BLOCK DIAGRAM
![Block Digarm](https://user-images.githubusercontent.com/92075957/174733034-24227b8a-dce5-490d-a6b4-a2b01ae87cab.PNG)
# AHI Value Labeling
ML does not give proper results in predicting the severity of OSA if the OSA value is in a
certain range (decimal values) to overcome this labeling has been done based on the severity level. The following table indicates the labeling of the OSA severity.
![ahi](https://user-images.githubusercontent.com/92075957/174733492-2c15c7d6-f529-4a78-8242-216702bf9ce9.PNG)
# TRAIN SPLIT VS TEST SPLIT
![split](https://user-images.githubusercontent.com/92075957/174733616-a5f140ff-7ec2-4124-b9b0-a6be6b04268a.PNG)
# USER INTERFACE
![USER](https://user-images.githubusercontent.com/92075957/174736397-24991d34-1536-41e1-8bd5-90becd7290b6.png)
# RESULTS
# Case - 1 
The case - 1 states the person is in normal condition and AHI value will be less than 5
![AHI0](https://user-images.githubusercontent.com/92075957/174736507-c9c72a5b-35ea-463c-9df0-d197e96051c2.png)
# Case - 2
The case - 2 states the person is in mild condition and AHI value will be between 5 to 15
![AHI1](https://user-images.githubusercontent.com/92075957/174736550-9b324238-2aaa-46cc-aac9-0986b2a5099f.png)
#  Case - 3
The case - 3 states the person is in moderate condition and AHI value will be between 15 to 30
![AHI2](https://user-images.githubusercontent.com/92075957/174736614-222a5765-3ef1-4064-86fd-888d571c0501.png)
# Case - 4
The case - 4 states the person is in serious condition and AHI value will be greater than 30
![AHI3](https://user-images.githubusercontent.com/92075957/174736654-0197f5a1-21e7-4b17-abb1-b8a4b339855a.png)
# QR CODE TO ACCESS THE WEB APPLICATION
![June17-102741AM](https://user-images.githubusercontent.com/92075957/174826765-2fb0d0e2-5c84-48cf-be61-9ab96733c29e.png)

# App Link : https://osaprediction.herokuapp.com/

