# Exercise 3 - Module 17

### GridSearchCV

First demonstration of the confusion matrix.

![image](https://github.com/user-attachments/assets/2a6e35a6-eb2e-4a41-b29c-6f00206c7f0c)

The tree was improved using this logic:
- Note that there are simpler and more difficult classes to identify
- Create a binary variable for one of the highest error classes
- It says a very simple classification tree for this variable:
    - use ```mean_samples_leaf=20```
    - use ```max_depth=4```
    - put all variables
- Observe the importance of the variables, and select the 3 with the greatest importance
- I ran the above algorithm again with the 3 new variables and evaluated the accuracy

![image](https://github.com/user-attachments/assets/f013753f-99e3-46c5-94fd-9951c4c3c683)
