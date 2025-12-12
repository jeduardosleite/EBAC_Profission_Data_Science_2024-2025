# Exercise 2 - Module 27

## Standardization with PCA

I did two main component analyzes for the HAR base - with and without standardization and compared:

- The variance explained by component
- The accumulated explained variance per component
- The percentage variance per component
- The accumulated percentage variance per component
- How many components in each case to explain 90% of the variance?

<img width="841" height="491" alt="image" src="https://github.com/user-attachments/assets/2e92f378-7a90-408d-a281-75585639d71f" />

### Conclusion  

The variances **without standardization** appear to be more efficient, since the **cumulative sum** reaches high levels of explained variance with fewer components.  
However, this efficiency is misleading: variables with larger scales or numerical variability end up dominating the first components, leading to a biased result.  

On the other hand, when applying **standardization**, all variables are brought to the same scale, preventing some from standing out just because of the size of their variance.  
The outcome is a fairer and more balanced representation of the dataset, although it requires using a larger number of components to reach the same level of explained variance.  

<img width="617" height="382" alt="image" src="https://github.com/user-attachments/assets/0afc65e4-78a6-45c7-82a6-ce6d1454b046" />

---

<img width="506" height="97" alt="image" src="https://github.com/user-attachments/assets/7a4fd70d-71c8-407c-ad53-e1652b364cec" />

## Conclusion

The **non-standardized** model maintained better performance, both on **training** and **test** sets, with only *0.02 seconds* more than the **standardized** model.  

This shows that with few components, even though biased, the non-standardized model achieved higher performance, since the computational cost is negligible in this case.  

With standardization, the model requires more components to reach the same level of explained variance, but it provides a fairer and more balanced representation.
