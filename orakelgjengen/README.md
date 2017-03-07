# Orakelgjengen

Machine Learning is super hot right now, and you're finally getting in on
the action. You have just been hired by the Oslo-based startup "Orakelgjengen",
and after having signed 18 Non-Disclosure Agreements their CTO lets you in
their secret method –– the crown jewel of the company's intellectual property.
The method is as follows:

1. Clean up the customer's data
2. Use Simple Linear Regression to predict future values

However, some customers have been complaining lately that
Orakelgjengen's service ("You Can Haz A Unicorn Rainbow 1.0") isn't
really predicting much. Desperate not to scare off future customers,
Orakelgjengen wants to make sure that their method works well for all
future customers. They do so by requiring that all potential future
customers provide a data sample that Orakelgjengen can check their
method on before making any deals. Your task is to determine which
customers are likely to get interesting predictions from Orakelgjengen
by scoring how likely Orakelgjengen's simple linear model will account for
the variability in the customer's data.

You are given a table on the following form:

| Company id | X      | Y     |
|------------|--------|-------|
| A          | 4.322  | 5.33  |
| A          | 4.433  | 5.49  |
| ...        | ...    | ...   |
| B          | 15.67  | 30.23 |
| B          | 43.201 | 45.45 |
| ...        | ...    | ...   |

The first column indicates which company the data is associated with.
The second column gives an X value and the third column gives a Y value.

Your job is to

1. Figure out the *squared* [Pearson Correlation Coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient)
for each company's dataset, and

2. Submit a sorted, comma-separated list of company names whose sample data has a
squared Pearson Correlation Coefficient greater than `0.6`.

## Example

Table:

```txt
Company         X               Y
A               1               1483
A               2               2282
A               3               3081
A               4               6996
A               5               11999
A               6               5478
A               7               6277
B               1               3068
B               2               2276
B               3               2960
B               4               3644
B               5               4328
B               6               5012
C               1               1198
C               2               2087
C               3               2976
C               4               3865
C               5               4754
C               6               14673

```

Answer: `B,C`
