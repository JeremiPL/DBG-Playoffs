import sqlite3
import pandas as pd 
import gradio as gr

def fetch():

    conn = sqlite3.connect('playoffs.db')
    cursor = conn.cursor()

    query = """
     SELECT *
     FROM teams;
    """

    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()

    #records_df = pd.DataFrame(records, columns = ('id','City','Name'))

    points = [(len(record[1]),len(record[2])) for record in records]
    points_df = pd.DataFrame(points, columns = ('x','y'))
    return points_df

iface = gr.Interface(fn = fetch,inputs = [], outputs = gr.LinePlot(x = 'x', y = 'y', x_lim = [0,15], y_lim = [0,15]))

iface.launch()

#records = fetch()

#points = []
#for record in records:
#    city = record[1]
#    name = record[2]
#    points.append((len(city),len(name)))

#print(points)
