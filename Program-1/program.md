# Mean Median and Mode using Python

---

**Mean**

 The mean is the average value of all the values in a dataset. To calculate the mean value of a dataset, we first need to find the sum of all the values and then divide the sum of all the values by the total number of values. So here’s how to calculate the mean using Python

```python

    list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
    mean = sum(list1)/len(list1)
    print(mean)
```

**Median**

The Median is the middle value among all the values in sorted order. Here we need to calculate the mid-value of all the values in a dataset. But before calculating the Median, we need to arrange all the values in sorted order. There are two different ways of calculating the median value:

* when the total number of values is even: Median  = $[(n/2)th$  + ${(n/2)+1}th]/2$
* when the total number of values is odd: Median = ${(n+1)/2}$ thterm
Now below is how you can calculate the median using Python

``` Python
# Median
    list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
    list1.sort()

    if len(list1) % 2 == 0:
        m1 = list1[len(list1)//2]
        m2 = list1[len(list1)//2 - 1]
        median = (m1 + m2)/2
    else:
        median = list1[len(list1)//2]
    print(median)

```

**Mode**

Mode is the most frequently occurring value among all the values. Below is how we can calculate the mode value of a dataset using Python:

```python

    list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
    frequency = {}
    for i in list1:
        frequency.setdefault(i, 0)
        frequency[i]+=1

    frequent = max(frequency.values())
    for i, j in frequency.items():
        if j == frequent:
            mode = i
    print(mode)
```
