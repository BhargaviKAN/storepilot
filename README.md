# StorePilot

StorePilot is a beginner-friendly retail analytics project that turns store sales,
staffing, traffic, and customer experience data into useful management insights.

## Business problem

Retail managers need to understand:

- whether the store is meeting sales targets,
- whether staffing matches customer demand,
- which periods are underperforming,
- which employees may need recognition or coaching,
- what actions should be prioritised next.

StorePilot will combine these signals into one clear analysis and dashboard.

## Current progress

### Version 0.1
- [x] Create repository structure
- [x] Define project problem
- [x] Generate an initial synthetic retail dataset
- [ ] Clean and validate the data
- [ ] Calculate core KPIs
- [ ] Explore sales and staffing patterns
- [ ] Detect possible understaffing and overstaffing
- [ ] Build a Streamlit dashboard
- [ ] Generate management recommendations

## Dataset

The current dataset is synthetic and represents hourly retail-store performance.

Main columns include:

- `date`
- `hour`
- `employee_id`
- `employee_name`
- `hours_worked`
- `customer_traffic`
- `transactions`
- `sales_revenue`
- `sales_target`
- `product_category`
- `units_sold`
- `accessory_sales`
- `customer_rating`
- `wait_time_minutes`

The data is fictional and is intended only for portfolio and learning purposes.

## Planned KPIs

- Target achievement percentage
- Conversion rate
- Average transaction value
- Sales per labour hour
- Accessory attachment rate
- Average customer rating
- Average wait time
- Staffing-to-traffic ratio

## Project structure

```text
storepilot/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
├── dashboard/
├── tests/
├── images/
├── README.md
├── requirements.txt
└── .gitignore
```

## Tools

- Python
- pandas
- NumPy
- matplotlib
- Streamlit
- scikit-learn (later, if useful)

## Next step

Create the first analysis notebook and inspect the synthetic dataset for data quality,
missing values, distributions, and obvious inconsistencies.
