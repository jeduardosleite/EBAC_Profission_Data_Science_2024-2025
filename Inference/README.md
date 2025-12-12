# Exercise 1 - Module 33

## Basic Inference Concepts

<p align="center">
<img width="1040" height="592" alt="image" src="https://github.com/user-attachments/assets/7c2c3e1e-ec6d-44e6-bc4c-d339b876d6e2" />
</p>

### Database
I used the famous dataset penguins, from seaborn.

<p align="center">
<img width="581" height="631" alt="image" src="https://github.com/user-attachments/assets/125805f1-8bae-4cea-9e49-167dcf2ed72e" />
</p>

In the penguin sample, we can see that there is a weight difference between males and females. But can this conclusion be extrapolated to the entire penguin population? Assuming this sample is random and representative of the penguin population, I'll run a t-test with a 5% significance level to see if we can infer this conclusion for the entire population.

---

## Question 1

<p align="center">
<img width="205" height="219" alt="image" src="https://github.com/user-attachments/assets/f955f5b6-c54d-4be2-ad94-32496af728b9" />
</p>

### Difference
Males are, on average, 683g heavier than females. Statistically speaking, we can deduce that sex strongly influences weight.

### Standard Deviation
This is the typical variation within groups. This parameter serves as a **reference scale**, that is, if the value of the ```difference``` is similar to or greater than this variation, it indicates a very strong effect.

In this case, we have a small difference (683 -> 729), corroborating the idea that the effect is strong.

### Standard Error
The uncertainty in the estimate of the difference is small, demonstrating a reliable result. This means that the difference found is unlikely to be due to chance.
- 145g (*standard error*)

### (t) Statistic
The observed difference is **4.6 times greater** than the variation expected by chance alone. This value is high, considering that values ​​above 2 are already considered strong.

### Critical Region
This is the threshold for rejecting *$H_0$*. Since its *t*(4.19) is greater than 1.677, we have very strong evidence against *$H_0$*.

### P_Value
This is the probability of observing such a large difference if *$H_0$* were true. The result, in this case, is extremely small, meaning it is unreasonable to believe in *$H_0$*.

### Conclusion
In practical terms, the difference between males and females is statistically confirmed. Its significance is real, not a coincidence.

---

## Question 2

<p align="center">
<img width="826" height="308" alt="image" src="https://github.com/user-attachments/assets/35c834c6-7f09-4b8a-a36c-c3a8e974677e" />
</p>

### Blue Curve
*t* distribution with 48 degrees of freedom, assuming $H^0$. It represents the expected variation if there is no real effect.

### Orange Area
Starts at *1.68*, which is the **critical value** for $\alpha$ = 5%. The area is equivalent to 5% of the total probability, that is, the most extreme cases that would lead to the rejection of $H^0$.

### Red Line
The statistic is at **4.68**, far from the *critical region*. This means that the observed value is **extremely unlikely** for $H^0$.

---

## Question 3

What is the p-value associated with each species?

<p align="center">
<img width="199" height="453" alt="image" src="https://github.com/user-attachments/assets/4a4bc61f-6915-439d-86b3-53b3bed9c7ac" />
</p>

### Conclusion

In general, all species reject $H^0$, since the ```p_value``` is extremely small, much smaller than $\alpha$ = 5%.
Among these species, we can highlight the **Gentoo** with the lowest value, demonstrating the greatest difference between males and females. Even the **Chinstrap**, with the "highest" value, becomes irrelevant.

With this, I conclude two propositions:
1) We can reject $H^0$;
2) The observed difference is not a mere coincidence.
