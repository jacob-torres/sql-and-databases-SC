"""
    DS Unit 3 Sprint Challenge SQL and Databases: Northwind Data
"""

import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
cur = conn.cursor()

# Queries
expensive_items = """
    select * from Product
    order by UnitPrice desc limit 10;
"""

avg_hire_age = """
    select round(avg(HireDate - BirthDate), 0) from Employee;
"""

ten_most_expensive = """
    select Product.ProductName, Supplier.CompanyName, Product.UnitPrice from Product
    inner join Supplier on Product.SupplierId = Supplier.Id
    order by UnitPrice desc limit 10;
"""

largest_category = """
    select Category.CategoryName from Product
    inner join Category on Product.CategoryId = Category.Id
    where count(distinct Product.ProductName) > 12;
"""

# Execute queries
try:
    cur.execute(expensive_items)
    cur.execute(avg_hire_age)
    cur.execute(ten_most_expensive)
    cur.execute(largest_category)
    conn.commit()

except (Exception, sqlite3.DatabaseError)as error:
    print(error)

finally:
    cur.close()
    conn.close()
