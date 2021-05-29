"""
    DS Unit 3 Sprint Challenge 2: SQL and Databases
"""

import sqlite3

# Constants and queries
demo_file = 'demo_data.sqlite3'
create_table = """
    create table if not exists demo (
        s varchar(3),
        x int,
        y int
    );"""

insert_data = """
    insert into demo values
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7);"""

row_count = """
    select count(*) from demo;"""

xy_at_least_5 = """
    select count(*) from demo
    where x >= 5 and y >= 5;"""

unique_y = """
    select count(distinct y) from demo;"""


def create_demo():
    """Creates and populates the demo database."""

    try:
        conn = sqlite3.connect(demo_file)
        cur = conn.cursor()
        cur.execute(create_table)
        cur.execute(insert_data)
        print("The demo table was successfully populated!")
        conn.commit()
        cur.close()

    except (Exception, sqlite3.DatabaseError) as err:
        print(err)

    finally:
        conn.close()


def run_tests():
    """Executes the test queries above and outputs the results."""

    try:
        conn = sqlite3.connect(demo_file)
        cur = conn.cursor()
        cur.execute(row_count)
        print(f"Total rows: {cur.fetchone()}")

        cur.execute(xy_at_least_5)
        print(f"Number of rows where x and y >= 5: {cur.fetchone()}")

        cur.execute(unique_y)
        print(f"Number of unique y values: {cur.fetchone()}")
        conn.commit()
        cur.close()

    except (Exception, sqlite3.DatabaseError) as err:
        print(err)

    finally:
        conn.close()


if __name__ == '__main__':
    create_demo()
    run_tests()
