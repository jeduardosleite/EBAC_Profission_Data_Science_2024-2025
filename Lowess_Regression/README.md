# Exercise 1 - Module 34

<img width="531" height="359" alt="image" src="https://github.com/user-attachments/assets/0d98620b-3971-4d69-9690-069ee51f9206" />


In this exercise, I addressed concepts basics about lowess and make a comparison with transformation in log.

### With Log

<img width="443" height="534" alt="image" src="https://github.com/user-attachments/assets/2ae198f0-42e6-43bf-9c55-741fa1fa132b" />

---

### Lowess

<img width="427" height="528" alt="image" src="https://github.com/user-attachments/assets/79a231bc-3afa-45ff-a0aa-18a3b8ee3860" />

---

### Conclusion

<img width="850" height="533" alt="image" src="https://github.com/user-attachments/assets/9d426259-ab42-40fa-aba5-8ddd5667ac3b" />

Regarding the adjusted $R^2$, I noticed that using the Lowess method, the fit was almost perfect (0.993). Comparing it to the No_Transformations method, we see an increase of nearly 90% in $R^2$, and with the Log_Transformation method, a 37.5% increase.

This is a significant increase. The graph below corroborates the idea that, in this case, the Lowess model performed better, fitting the data better across the entire range and capturing the nonlinearity that the other model failed to do.
