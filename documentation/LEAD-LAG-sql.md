# Syntax of the LAG() Function:
```
LAG(return_value, offset [, default_value]) OVER (
    PARTITION BY partition_expression, ...
    ORDER BY sort_expression [ASC | DESC], ...
)
```
* <b>return_value:</b> The value from the previous row based on the specified offset.
* <b>offset:</b> The number of rows back from the current row. It defaults to 1 if you don’t specify it explicitly.
* <b>default_value:</b> What to return if the offset goes beyond the partition. If not specified, it defaults to NULL.

#### Example A: 
Net Sales Comparison Suppose we have a view called sales.vw_netsales_brands with monthly net sales data.<br> 
We want to compare net sales for the current month with the previous month in the year 2018. Here’s how:

```
WITH cte_netsales_2018 AS (
    SELECT month, SUM(net_sales) AS net_sales
    FROM sales.vw_netsales_brands
    WHERE year = 2018
    GROUP BY month
)
SELECT
    month,
    net_sales,
    LAG(net_sales, 1) OVER (ORDER BY month) AS previous_month_sales
FROM cte_netsales_2018;
```

#### This query gives you the net sales for each month in 2018 along with the sales from

#### Example B: 
Comparing Sales by Brand Let’s say we have an employee_salary table with salary history. <br>
We want to compare the salary of each employee in a given fiscal year with their salary from the previous year. Here’s the magic:
```
SELECT
    employee_id,
    fiscal_year,
    salary,
    LAG(salary, 1) OVER (PARTITION BY employee_id ORDER BY fiscal_year) AS previous_year_salary
FROM basic_pays;
```
#### Now you’ve got the salary history and can spot those raises (or lack thereof).
* Remember the PARTITION and ORDER BY Clauses:<br>
The PARTITION BY clause divides your result set into logical chunks. Without it, the whole result set is treated as a single partition.<br>
The ORDER BY clause specifies the order of rows within each partition.<br>
# Syntax of the LEAD() Function:
```
LEAD(return_value, offset [, default]) OVER (
    [PARTITION BY partition_expression, ...]
    ORDER BY sort_expression [ASC | DESC], ...
)
```
* <b>return_value:</b> The value from the following row based on a specified offset. It must evaluate to a single value and can’t be another window function.
* <b>offset:</b> The number of rows forward from the current row. If not explicitly specified, it defaults to 1.
* <b>default:</b> The value returned if the offset goes beyond the partition scope. If not specified, it defaults to NULL.<br>

Remember the PARTITION and ORDER BY Clauses:<br>
* The PARTITION BY clause divides your result set into logical chunks. Without it, the whole result set is treated as a single partition.<br>
* The ORDER BY clause specifies the order of rows within each partition.<br>
#### Example 1:
Suppose we have a view called sales.vw_netsales_brands that calculates net sales for different brands each month.<br>
```
CREATE VIEW sales.vw_netsales_brands AS
SELECT
    c.brand_name,
    MONTH(o.order_date) AS month,
    YEAR(o.order_date) AS year,
    CONVERT(DEC(10, 0), SUM((i.list_price * i.quantity) * (1 - i.discount))) AS net_sales
FROM sales.orders AS o
INNER JOIN sales.order_items AS i ON i.order_id = o.order_id
INNER JOIN production.products AS p ON p.product_id = i.product_id
INNER JOIN production.brands AS c ON c.brand_id = p.brand_id
GROUP BY c.brand_name, MONTH(o.order_date), YEAR(o.order_date);
```
Let’s use the LEAD() function to compare net sales between the current month and the next month in the year 2017:<br>
```
WITH cte_netsales_2017 AS (
    SELECT
        month,
        year,
        brand_name,
        net_sales,
        LEAD(net_sales, 1) OVER (PARTITION BY brand_name ORDER BY year, month) AS next_month_sales
    FROM sales.vw_netsales_brands
    WHERE year = 2017
)
SELECT *
FROM cte_netsales_2017
ORDER BY year, month, brand_name;
```