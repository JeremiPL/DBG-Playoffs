import sqlite3

conn = sqlite3.connect('playoffs.db')
cursor = conn.cursor()

query = """
    INSERT INTO teams(city,name)
    VALUES
    ('Denver', 'Broncos'),
    ('New England', 'Patriots'),
    ('Los Angeles', 'Rams'),
    ('Seattle', 'Seahawks');
"""

cursor.execute(query)
conn.commit()
conn.close()