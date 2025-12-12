# Exercise 2 - Module 30

Continuation of the previous exercise, but this time using the Gower method for mixed data sets.

<p align="center">
<img width="948" height="627" alt="image" src="https://github.com/user-attachments/assets/4f97222f-491e-4a23-85c2-548b620e94c2" />
</p>

### Dataset

Lets use the dataset [online shoppers purchase intention](https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset) de Sakar, C.O., Polat, S.O., Katircioglu, M. et al. Neural Comput & Applic (2018). [Web Link](https://doi.org/10.1007/s00521-018-3523-0).

#### Columns
| Variable                | Description |
|--------------------------|-------------|
| **Administrative**          | Number of accesses to administrative pages |
| **Administrative_Duration** | Time spent on administrative pages |
| **Informational**           | Number of accesses to informational pages |
| **Informational_Duration**  | Time spent on informational pages |
| **ProductRelated**          | Number of accesses to product-related pages |
| **ProductRelated_Duration** | Time spent on product-related pages |
| **BounceRates**             | *Percentage of visitors who enter the site and leave without triggering other requests during the session* |
| **ExitRates**               | *Number of times a page was the last viewed in a session divided by the total number of views* |
| **PageValues**              | *Represents the average value of a web page visited by a user before completing an e-commerce transaction* |
| **SpecialDay**              | Indicates proximity to a special date (e.g., Mother’s Day) |
| **Month**                   | Month |
| **OperatingSystems**        | Visitor’s operating system |
| **Browser**                 | Visitor’s browser |
| **Region**                  | Region |
| **TrafficType**             | Traffic type |
| **VisitorType**             | Visitor type: new or returning |
| **Weekend**                 | Indicates whether the visit occurred on a weekend |
| **Revenue**                 | Indicates whether a purchase was made |

\* Variables calculated by **Google Analytics**

<p align="center">
<img width="386" height="336" alt="image" src="https://github.com/user-attachments/assets/7430a106-4bca-4fd0-b2b9-bbfd3b11e631" />
</p>

---

### Objective
Our goal now is to group portal access sessions considering access behavior and date information (special date, month, etc.)

With this, we will answer the central question:
- Do customers with different browsing behaviors have different purchasing propensities?

---

### Technology and Tools
- **Python**
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering

from scipy.spatial import distance
import scipy.cluster.hierarchy as shc
from scipy.cluster.hierarchy import linkage, fcluster, dendrogram
from gower import gower_matrix
from scipy.spatial.distance import pdist, squareform
```
- **Jupyter Notebook** for analysis and visualization 
- **Markdown** for documentation
- **Git/Git Hub** for versioning

---

### Extract Transform Load (ETL)
In this step, I treated the dataset using the classic methodology of descriptive analysis.
- variables distribution verification
- treatment of values missing
- standardization of quantitative variables
- transformation of qualitative variables in dummies

### Method Gower
The approach adopted was to evaluate the hierarchical clustering with 3 and 4 groups. Since the variables are mixed (categorical and numerical), the most appropriate method is to use the Gower method to calculate the distance.

- First, I calculated the distance with ```gower_matrix```
```python
dist_gower = gower_matrix(df_final)
```

- I adjusted the format to distance matrix, using ```squareform```
```python
matrix_distancia = squareform(dist_gower,
                            force = 'tovector')
```

- I used ```linkage``` to perform hierarchical grouping from the distance matrix.
```python
Z = linkage(matrix_distancia, 
    method='complete')
```
---

### Dendrogram
I used the dendrogram as groups analysis graph.

<p align="center">
<img width="851" height="459" alt="image" src="https://github.com/user-attachments/assets/8766596c-0521-4d93-8618-ce8ca46b198e" />
</p>

### Analysis of groups

#### Solution with 3 Groups

**Group 1 – Occasional Visitors**  
- Low browsing time (`Administrative_Duration` and `Informational_Duration` are low).  
- Low conversion rate (`Revenue` close to 0).  
- No specific seasonal pattern across months.

**Group 2 – Explorers without Purchase**  
- More pages viewed (`Administrative` higher).  
- Visit duration still low.  
- Almost none generate revenue.  

**Group 3 – Potential Customers / Buyers**  
- Higher browsing time and interaction.  
- Higher conversion rate (`Revenue` is higher).  
- Strong seasonality in specific months (November, May, October).

---

#### Solution with 4 Groups

**Group 1 – Occasional Visitors**  
- Low browsing time, little time spent on administrative and informational pages.  
- Low number of visited pages, casual behavior.  
- Very low conversion (Revenue ≈ 0).  
- Seasonality does not show a consistent monthly pattern.  
- **Interpretation:** users who visit the site sporadically, probably seeking quick information, without immediate purchase intent.

**Group 2 – Explorers without Purchase**  
- Medium-low browsing time, but visit more administrative pages compared to Group 1.  
- Almost zero conversion, even when exploring more.  
- **SpecialDay** has little effect from promotions.  
- Seasonality spread across different months.  
- **Interpretation:** curious users or those comparing products/prices, but still without purchase intent.

**Group 3 – Recurring Buyers**  
- High browsing time, both on administrative and informational pages.  
- High conversion, many complete purchases.  
- Seasonality spread across several months, without concentration in a specific one.  
- **Behavior:** consistent engagement, regular purchases, loyal customers.  
- **Interpretation:** valuable audience, accessing the site frequently and buying throughout the year.

**Group 4 – Seasonal Buyers**  
- High browsing time, similar to Group 3.  
- High conversion, many complete purchases.  
- Seasonality strongly concentrated in specific months, especially November (Black Friday) and other promotional periods.  
- **Behavior:** users responding to seasonal campaigns and promotions.  
- **Interpretation:** strategic customers for targeted campaigns and commercial dates, less recurrent than Group 3.

---

I noticed that the 4-group solution allows us to understand **when and how customers buy**, refining the strategic view.

---

- **3 groups:** simple general view — distinguishes non-buyers, explorers, and buyers.  
- **4 groups:** adds an important nuance about buyer seasonality.

---

## Suggested Group Names for "Group 4"

- **Group 1:** Occasional Visitors  
- **Group 2:** Explorers without Purchase  
- **Group 3:** Recurring Buyers  
- **Group 4:** Seasonal Buyers

---

## Why choose 4 groups?

<p align="center">
<img width="859" height="363" alt="image" src="https://github.com/user-attachments/assets/e5412087-fd74-4cb1-9d4d-95ae276fcd86" />
</p>

### Results Evaluation

- **BounceRates**: the lower, the higher the engagement.  
- **ExitRates**: the lower, the better the retention.  
- **PageValues**: the higher, the greater the average value of the visited pages (conversion indicator).  

#### 4 Clusters

| Group | BounceRates | ExitRates | PageValues | Interpretation |
|-------|-------------|-----------|------------|----------------|
| 1     | 0.0269      | 0.0489    | 5.43       | Occasional visitors, low engagement, moderate value. |
| 2     | 0.0470      | 0.0741    | 0.89       | Explorers without purchase, high bounce and exit rate, low value. |
| 3     | 0.0201      | 0.0413    | 6.83       | Recurring buyers, low bounce/exit, high value. |
| 4     | 0.0198      | 0.0399    | 6.01       | Seasonal buyers, low bounce/exit, high value in specific periods. |

## Conclusion

Based on the chart, it is clear that groups **1** and **2** are symmetrically similar; **3** shows only a minimal difference in ```BounceRates```, but stands out in ```PageValues```, where group **3** from the **4-cluster solution** demonstrates a higher conversion rate. This highlights that the **`4-cluster`** solution allows for identifying important nuances among customers. Such segmentation provides strategic insights that are not visible with only 3 clusters, justifying the choice of the more detailed solution.

With **3 clusters**, all purchasing customers are grouped together in a single cluster, mixing different profiles.  
In contrast, with **4 clusters**, we obtain a more precise division:

- **Recurring buyers**: customers who purchase throughout the year, showing consistent engagement.  
- **Seasonal buyers**: customers whose engagement is concentrated during promotions or specific months (e.g., Black Friday, holidays).

This differentiation enables a **more efficient strategic approach**, with personalized marketing actions for each customer profile, increasing **retention and loyalty**.

While the **3-cluster** solution is simpler to communicate, the **`4-cluster`** solution provides a richer and more actionable view of customer behavior, adding **strategic value** to the business. Within these clusters, **Group 3** is the most likely to purchase, as it combines the ```lowest BounceRate``` (0.0201) and the highest ```PageValue``` (6.83).

