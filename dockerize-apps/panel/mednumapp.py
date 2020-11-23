import panel as pn
import numpy as np
import holoviews as hv
import numpy as np
import panel as pn
from panel.widgets.select import AutocompleteInput
import param
from mednum.config import *
from mednum.loaders import read_merged_data

# from mednum.controlers.autocomplete import AutocompleteInput
from mednum.indicators.panels import TopIndicators
from pathlib import Path
import mednum

css_mednum = [str(Path(__file__).parent / "statics" / "css" / "mednum.css")]
print((Path(__file__).parent / "statics" / "css" / "mednum.css").exists())
css = [
    "https://cdn.datatables.net/1.10.19/css/jquery.dataTables.min.css",
    css_mednum[0],
]
js = {
    "$": "https://code.jquery.com/jquery-3.4.1.slim.min.js",
    "DataTable": "https://cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js",
}

# pn.config.js_files = js
# pn.config.css_files = css
# with open(css_mednum[0], 'r') as fin: raw_css = fin.read()

# pn.config.raw_css = [raw_css]
pn.extension(css_files=css_mednum)  # raw_css = [raw_css])

template = """
{% extends base %}

<!-- goes in body -->
{% block postamble %}
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
{% endblock %}

<!-- goes in body -->
{% block contents %}
{{ app_title }}
<p>This is a Panel app with a custom template allowing us to compose multiple Panel objects into a single HTML document.</p>
<br>
<div class="container">
<div class="row">
    <div class="col-sm-4">
      {{ embed(roots.sidebar) }}
    </div>
    <div class="col-sm-8">
      <div class="row">
          {{ embed(roots.top) }}
      </div>
      <div class="row">
        {{ embed(roots.main) }}
      </div>
    </div>
    
  </div>
</div>
{% endblock %}
"""

merged_path = interim_data / "data_merge_V2.csv"

df = read_merged_data(merged_path)

tmpl = pn.Template(template)
tmpl.add_variable("app_title", "<h1>Custom Template App</h1>")

pn.config.sizing_mode = "stretch_width"

xs = np.linspace(0, np.pi)
freq = pn.widgets.FloatSlider(name="Frequency", start=0, end=10, value=2)
phase = pn.widgets.FloatSlider(name="Phase", start=0, end=np.pi)


# Sidebar
class AutoComplete(param.Parameterized):
    nom_commune = param.String()


mednumapp = mednum.MedNumApp(name="Sélection")

# NOM_COMMUNES = list(df.LIBCOM.unique())

# auto_complete_param = AutoComplete()
# auto_complete = pn.Param(auto_complete_param, widgets={"string_value": {"type": pn.widgets.AutocompleteInput, "options": NOM_COMMUNES}})
# score_widget = pn.widgets.IntRangeSlider()
# sidebar = pn.Column(auto_complete, score_widget)
sidebar = pn.Column(mednumapp.lat_widgets())

# Top indicator
top_panel = TopIndicators()


def update_top_params(self):
    d = dict(self.get_param_values())
    d.pop("name")
    for k, v in d.items():
        try:
            self.top_panel.set_param(**{k: v})
        except Exception as e:
            pass


tmpl.add_panel("sidebar", mednumapp.lat_widgets())
tmpl.add_panel("top", mednumapp.top_panel.view())
tmpl.add_panel("main", hv.Curve([1, 2, 3]))

tmpl.servable()