import panel as pn

from .panel import DataSetSelect

def app(doc):
    food = DataSetSelect()

    col = pn.Column(food.param.date_select, food.param.date_select1, food.multi_select,
        food.param.find_country, food.outputs, food.generate_country_list)

    col.server_doc(doc)
