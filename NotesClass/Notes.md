# Statistics

##  Data Modelling
#### Roles of data modelling
+ Model validation
+ Relation between variable
+ Visualisation
+ Future prediction


### Descriptive Statistics
* This is measure of central tendancy of the collection of data 
1. Mean 
#### Definition of Mean (in Statistics)

The **mean** of a data set is the **average value** — it is found by **adding all the values together** and then **dividing by the number of values**.

#### Formula (for Arithmetic Mean):

\[
\text{Mean} = \frac{\text{Sum of all data values}}{\text{Number of data values}}
\]

2. Median
#### Definition of Median (in Statistics)

The **median** is the **middle value** in a data set when the values are **arranged in ascending or descending order**.

- If the number of data values is **odd**, the median is the **middle number**.
- If the number of data values is **even**, the median is the **average of the two middle numbers**.

####  Steps to Find the Median:

1. Arrange the data in order (ascending or descending).
2. Count the number of values (**n**).
3. Apply:

   - If **n** is odd:  
     \[
     \text{Median} = \text{Value at position } \frac{n + 1}{2}
     \]

   - If **n** is even:  
     \[
     \text{Median} = \frac{\text{Value at position } \frac{n}{2} + \text{Value at position } \left(\frac{n}{2} + 1\right)}{2}
     \]

3. Mode
#### Definition of Median (in Statistics)

The **median** is the **middle value** of a data set when the numbers are **arranged in order** (either ascending or descending).

- If the number of data values is **odd**, the median is the **middle value**.
- If the number of data values is **even**, the median is the **average of the two middle values**.

#### Formula (to Find the Median):

Let **n** be the number of values in the data set:

- If **n** is odd:
  \[
  \text{Median} = \text{Value at position } \frac{n + 1}{2}
  \]

- If **n** is even:
  \[
  \text{Median} = \frac{\text{Value at position } \frac{n}{2} + \text{Value at position } \left(\frac{n}{2} + 1\right)}{2}
  \]


There is different ways to find the **dispersion** of data e.g. Range of data is dispersion. It shows data deviates from some maximu range to minimum.

#### Variance:
Variance provides insight into how much the data deviates from the average, making it fundamental for understanding, interpreting, and modeling data.
#### Variance Formulas

#### 1. Population Variance

\[
\sigma^2 = \frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2
\]

Where:
- \( \sigma^2 \) = population variance  
- \( N \) = total number of data points  
- \( x_i \) = each data value  
- \( \mu \) = population mean

---

#### 2. Sample Variance

\[
s^2 = \frac{1}{n - 1} \sum_{i=1}^{n} (x_i - \bar{x})^2
\]

Where:
- \( s^2 \) = sample variance  
- \( n \) = number of data points in the sample  
- \( x_i \) = each data value  
- \( \bar{x} \) = sample mean
---

#### Standard Deviation: 

The **standard deviation** is a measure of **how spread out** the values in a data set are from the **mean**. It is the **square root of the variance** and is expressed in the **same units as the data**.
> Standard deviation is one of the most important statistical tools to understand the **spread**, **variability**, and **reliability** of data.

---


#### Standard Deviation Formulas

#### 1. **Population Standard Deviation**

\[
\sigma = \sqrt{ \frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2 }
\]

Where:  
- \( \sigma \) = population standard deviation  
- \( N \) = number of values in the population  
- \( x_i \) = each data value  
- \( \mu \) = population mean

---

#### 2. **Sample Standard Deviation**

\[
s = \sqrt{ \frac{1}{n - 1} \sum_{i=1}^{n} (x_i - \bar{x})^2 }
\]

Where:  
- \( s \) = sample standard deviation  
- \( n \) = number of values in the sample  
- \( x_i \) = each data value  
- \( \bar{x} \) = sample mean

---




