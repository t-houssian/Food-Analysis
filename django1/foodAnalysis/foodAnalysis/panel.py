import param
import panel as pn
import pandas as pd
import numpy as np
import holoviews as hv
from holoviews import opts
import io
import datetime
import sqlite3

# https://data.humdata.org/dataset/wfp-food-prices

con = sqlite3.connect("sqlite/db/pythonsqlite.db")
df = pd.read_sql_query("SELECT * from food_prices", con)
year_list = range(2000,2021)

class DataSetSelect(param.Parameterized):
    """
    This is where all the action happens. This is a self
    contained class where all the parameters are dynamic
    and watch each other for changes. 
    See https://panel.holoviz.org/ for details
    and https://discourse.holoviz.org/c/panel/5 for help

    Widgets and Parameters in this class need to be added
    to pn_app.py to be able to display.
    """

    hv.extension('bokeh')

    css = """

    .bk{
        width = 1000;
    }

    .bk.bk-btn.bk-btn-default {
        font-family: Arial;
        font-weight: bold;
        text-align: center;
        color: #0077ff
    }

    .bk-root h2 {
        font-family: Arial;
        font-weight: bold;
        text-align: center;
        color: black;
    }

    .bk-root h6 {
        font-family: Arial;
        font-weight: bold;
        text-align: center;
        color: black;
    }

    .bk-root label {
        font-family: Arial;
        font-weight: bold;
        color: black;
    }

    .bk-root .bk-tabs-header .bk-tab.bk-active {
        background-color: #0077ff;
        color: white;
        font-weight: bold;
    }
    """

    pn.extension(raw_css=[css])

    title = '##' + 'Global Food Analysis'
    message = ''

    multi_select = pn.widgets.MultiSelect(name='MultiSelect',
    options=list(df['cm_name'].unique()), size=8)

    date_select = param.ObjectSelector(objects=year_list, label='Start Date', 
        default=year_list[0],
        precedence=1)

    date_select1 = param.ObjectSelector(objects=year_list, label='End Date', 
        default=year_list[-1],
        precedence=1)

    find_country = param.Action(lambda self: self.param.trigger('find_country'), label='Find Best Countries', precedence=1)
    
    def add_title(self):
        return self.title

    @param.depends('message', watch=True)
    def outputs(self):
        return self.message
 
    @param.depends('find_country', watch=True)
    def generate_country_list(self):
        if self.multi_select.value:
            food_list = self.multi_select.value
            country_list = []
            for x in food_list: # This Loop Filters the data to get the lowest value for each food
                # temp = df.loc[df['mp_year'] == 2020]
                temp = df[(df['mp_year'] >= self.date_select) & (df['mp_year'] <= self.date_select1)]
                temp = temp.loc[temp['cm_name'] == x]
                temp = temp.sort_values('mp_price')
                temp = temp.drop_duplicates(subset=['adm0_name'], keep='first')
                temp = temp.nsmallest(5, ['mp_price'])
                country_list.append(temp)

            df_final = pd.concat(country_list) 
            df_final = df_final.reset_index(drop=True)
            df_final = df_final.sort_values('mp_price')
            mask = df_final['adm0_name'].isin(df_final['adm0_name'].value_counts()[:5].index.tolist())
            df_final = df_final.loc[mask]
            df_final = df_final.drop_duplicates(subset=['adm0_name'], keep='first')
            mes = f"If you buy {food_list} the most. You should live in the following countries:"
            self.message = '######' + mes

            return hv.Table(data=df_final['adm0_name']).opts(width=1000)
        else:
            return hv.Table(data=pd.DataFrame(columns=['adm0_name'])).opts(width=1000)
