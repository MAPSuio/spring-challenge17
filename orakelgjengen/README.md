# Orakelgjengen (wip)

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
by scoring how well Orakelgjengen's proposed linear model accounts for
the variability in the customer's data. You do this by computing the [R
squared])https://en.wikipedia.org/wiki/Coefficient_of_determination)
metric for each data set. Orakelgjengen will accept a new customer if
the R squared metric on the corresponding sample data is at least `0.7`
