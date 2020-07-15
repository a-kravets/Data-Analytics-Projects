# DESCRIPTION

We want tp prepare a report for evaluating customers purchase likelihood based on acquisition time. The main question the report should answer is, if someone that was acquired
in last 12M (months) or earlier and has ordered once in last 12M, what is the likelihood of ordering again in next 12M.

We should be able to compare customers that bought once, twice or more. Then we should also be able to see the difference between
customers that were acquired in last 12-24M (and earlier) that also ordered 1, 2, 3 or more times. The report must have results shown in order numbers and revenue.

# Purchasing Likelihood

Our Purchasing Likelihood figure based on Purchase Frequency, which as a metric that shows the average number of times a customer makes a purchase within a set time frame.

It is calculated as Number of orders for the last 365 days divided by Number of unique customers for the last 365 days.

Later on we segment all customers by aquisition year, purchasing frequency and sales year.

Finally, we segment those based on retention years to get a matrix with Retention Years and Purchase Frequency as dimensions and with Median Likelihood, Sales Amount and Sales Per Customer.

# Visualization

In order to visualize the outcome we'll use Tableau. I feel that this is the rare case when tabular visualization will be the best. Even so, few charts are added as well.

The result can be found [here](https://public.tableau.com/profile/andriy.kravets#!/vizhome/PurchasingLikelihood/Dashboard).
