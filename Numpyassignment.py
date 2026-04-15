import numpy as np
import random
Array=np.array([range(101)])
Random=[random.randint(1,100) for i in range(50)]
print("The generated array include:" , Array)
print("The random numbers are:" , Random)
Mean=np.mean(Random)
print("The mean is:" , Mean)
Median=np.median(Random)
print("The median is:" , Median)
Standard_Deviation=np.std(Random)
print("The standard deviation is:" , Standard_Deviation)
Randommax=np.max(Random)
print("The maximum is:" , Randommax)
Randommin=np.min(Random)
print("The minimum is:" , Randommin)
Greaterthan60=Array[Array>60]
print("Arrays greater than 60 are:" , Greaterthan60)
Lessthan60=Array[Array<30]
print("Arrays less than 30 are:" , Lessthan60)


import pandas as pd
df = pd.read_csv('employee_dataset.csv')
print(df.head(5))
print(df.describe())
max_salary_row = df.loc[df['salary_year_avg'].idxmax()]
highest_job = max_salary_row['job_title']
highest_salary = max_salary_row['salary_year_avg']

print(f"\nJob title with the highest salary: {highest_job} (${highest_salary})")

unique_val=df["job_title"].nunique()
print("There are " , unique_val, "unique job titles")
salaryabove7000 = df[df['salary_year_avg'] > 70000]
print("Salaries above 70,000: [" , salaryabove7000, "]")
sorted_df = df.sort_values(by='salary_year_avg', ascending=False)
print("Sorted Job Titles by Salary: ", sorted_df[['job_title', 'salary_year_avg']])

import matplotlib.pyplot as plt
avg_salary = df.groupby('job_title')['salary_year_avg'].mean().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
avg_salary.plot(kind='bar', color='skyblue')
plt.title('Average Salary by Job Title')
plt.xlabel('Job Title')
plt.ylabel('Average Salary ($)')
plt.xticks(rotation=45, ha='right') # Rotates labels so they don't overlap
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(sorted_df['salary_year_avg'].values, marker='o', color='green')
plt.title('Salary Distribution (Sorted High to Low)')
plt.xlabel('Employees (Ranked)')
plt.ylabel('Salary ($)')
plt.grid(True)
plt.tight_layout()
plt.show()

