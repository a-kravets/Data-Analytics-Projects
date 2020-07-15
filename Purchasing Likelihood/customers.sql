SELECT
  DISTINCT a.aq_year, a.aq_freq,a.sale_year,customer_count_unique,a.sales_amount,a.avg_sale
  ,COUNT(DISTINCT sa.customer_id) OVER(PARTITION BY a.aq_year) AS aq_custom_number -- total sales per year
  ,ROUND(a.customer_count_unique/COUNT(DISTINCT sa.customer_id) OVER(PARTITION BY a.aq_year), 3) AS likelihood
FROM (
SELECT
	sa.aq_year -- aquisition year
  ,sa.aq_freq -- frequency
  ,EXTRACT(YEAR FROM s.sale_timestamp AT TIME ZONE "UTC") AS sale_year -- sales year
  ,COUNT(DISTINCT sa.customer_id) AS customer_count_unique -- number of customers with this freq, aq_year and sale_year
  ,ROUND(SUM(sale_amount), 2) AS sales_amount -- total sales in this segment
  ,ROUND(SUM(sale_amount)/COUNT(DISTINCT s.customer_id), 2) AS avg_sale -- average sales per customer
FROM `uk_malt.sales.sales` s
LEFT JOIN `uk_malt.sales.sales_aquisition_frequency` sa ON s.customer_id = sa.customer_id

GROUP BY 	aq_year,sa.aq_freq,sale_year) a

LEFT JOIN `uk_malt.sales.sales_aquisition_frequency` sa ON a.aq_year = sa.aq_year AND a.aq_freq = sa.aq_freq

ORDER BY aq_year,sale_year,aq_freq