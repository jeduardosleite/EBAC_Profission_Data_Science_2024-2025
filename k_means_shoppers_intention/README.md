# Exercise 1 - Module 29

<img width="312" height="153" alt="image" src="https://github.com/user-attachments/assets/1730a53e-7538-49f5-b470-ced453d4f17f" />

### Objective
The database records 12,330 page access sessions, each session from a single user, over a 12-month period.

Our goal is to group customers based on their browsing behavior across administrative, informational, and product pages and answer the following questions: do customers with different browsing behaviors have different purchasing propensities?

### Columns
|Variable                |Description                                                                 | 
|------------------------|:--------------------------------------------------------------------------| 
|Administrative          | Number of accesses to administrative pages                                 | 
|Administrative_Duration | Time spent on administrative pages                                         | 
|Informational           | Number of accesses to informational pages                                  | 
|Informational_Duration  | Time spent on informational pages                                          | 
|ProductRelated          | Number of accesses to product-related pages                                | 
|ProductRelated_Duration | Time spent on product-related pages                                        | 
|BounceRates             | *Percentage of visitors who enter the site and leave without triggering other requests during the session* | 
|ExitRates               | *Number of times the page was the last viewed in a session divided by total pageviews* | 
|PageValues              | *Represents the average value of a web page a user visited before completing an e-commerce transaction* | 
|SpecialDay              | Indicates proximity to a special day (Mother’s Day, etc.)                  | 
|Month                   | Month                                                                       | 
|OperatingSystems        | Visitor’s operating system                                                 | 
|Browser                 | Visitor’s browser                                                          | 
|Region                  | Region                                                                     | 
|TrafficType             | Type of traffic                                                            | 
|VisitorType             | Type of visitor: new or returning                                          | 
|Weekend                 | Indicates weekend                                                          | 
|Revenue                 | Indicates whether a purchase was made or not                               | 

<img width="395" height="362" alt="image" src="https://github.com/user-attachments/assets/031dff9c-8ac2-4e52-90b2-b056adde8edc" />

---

### Methods and Packs
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

from sklearn.metrics import silhouette_score
from tqdm.notebook import tqdm
from sklearn.metrics import silhouette_samples
```

---

### Silhouette Score

<img width="429" height="299" alt="image" src="https://github.com/user-attachments/assets/ad8b5fd3-69fe-4cb9-b509-a0b7c1fd1bf3" />

I used log and PCA to improve the silhouette average.


### Final Question

After that, I chose three groups and worked to answer this question:

- **Which group has customers more likely to buy?**

In this notebook, I wrote down all the insights from each step to reach this answer.
Finally, i conclude that group one is this more likely to buy.

