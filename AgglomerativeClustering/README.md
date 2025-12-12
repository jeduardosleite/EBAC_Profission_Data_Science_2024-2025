# Exercise 1 - Module 30

<p align="center">
<img width="581" height="374" alt="image" src="https://github.com/user-attachments/assets/3831636c-adda-4cfd-a342-8b9a7af06ded" />
</p>

Using Seaborn "penguins" dataset, I conducted an activity using three groups as clusters. I analyzed the results and defined the clusters.

### How to better define penguin groups?

First, I wondered: 
- How many groups do I need to better define the groups?
- And what does "better define" mean?

With three groups, I defined the species: Adelie, Chinstrap, and Gentoo. Now I needed to separate each species by sex, that is, to highlight sexual dimorphism—the physical difference between males and females. For this, grouping into six clusters would be ideal.

### Clusters

- ```Cluster 0```: 70 Chinstrap, 9 female e 61 male.
- ```Cluster 1```: 51 Gentoo, 28 female e 23  male.
- ```Cluster 2```: 92 Adelie e 5 Chinstrap, 77 female e 20 male
- ```Cluster 3```: 49 Gentoo, 49 female.
- ```Cluster 4```: 53 Adelie e 1 Chinstrap, 52 male e 2 female.
- ```Cluster 5```: 12 Chinstrap, 12 female


Sex distribution in percentage
<p align="center">
<img width="303" height="182" alt="image" src="https://github.com/user-attachments/assets/16d5e058-fe09-4e87-8d6b-f5159290ebfa" />
</p>

Although the separation is not perfect (in **cluster 0**, for example, there is a balanced sex ratio), compared to the **3-cluster** solution, this approach provides **more information**, allowing us to largely distinguish groups according to **sex**, mainly through the **body_mass_g** variable.

#### Distribution by species and sex:
- **Gentoo** → Cluster 0 (**males**) and Cluster 3 (**females**)
- **Adélie** → Cluster 2 (**females**) and Cluster 4 (**males**)
- **Chinstrap** → Cluster 1 (**males**) and Cluster 5 (**females**)
