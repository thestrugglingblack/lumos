import plotly.express as px
from shiny.express import render, ui
from shinywidgets import render_plotly

from analysis.characters import house_count_chart, gender_count_chart
from analysis.dialogue import dialogue_per_character_chart, wordcloud
from analysis.places import places_frequently_mentioned, character_place_association
from analysis.spells import spell_used_the_most, character_most_used_spell
from pathlib import Path

tips = px.data.tips()

ui.page_opts(title="Lumos")

with ui.sidebar():
    ui.include_css(
        Path(__file__).parent / "style.css"
    )
    ui.h2('Welcome')
    ui.markdown("<p>Lumos is a Shiny Python application that does basic text analysis on the Harry Potter series. Its entire stack is deployed on AWS using Amazon Cloud Development kit (aws-cdk). You can learn more about Shiny Python and AWS-CDK in the links below.</p>")
    ui.markdown("[Slides](www.google.com)")
    ui.markdown("[GitHub](https://github.com/thestrugglingblack/lumos)")
    ui.markdown("[Speaker](https://github.com/thestrugglingblack)")

ui.nav_spacer()

with ui.nav_panel("Characters"):
    @render_plotly
    def plot_house_count_chart():
        house = house_count_chart()
        return house


    @render_plotly
    def plot_blood_status_chart():
        gender = gender_count_chart()
        return gender

with ui.nav_panel("Dialogue"):
    @render_plotly
    def plot_dialogue_chart():
        dialogue = dialogue_per_character_chart()
        return dialogue


    @render.ui
    def show_wordcloud():
        wc = wordcloud()
        return ui.img(src=f'data:image/png;base64,{wc}')

with ui.nav_panel("Places"):
    @render_plotly
    def plot_places_freq():
        bc = places_frequently_mentioned()
        return bc

    @render_plotly
    def plot_place_assoc():
        cpa = character_place_association()
        return cpa

with ui.nav_panel("Spells"):
    @render_plotly
    def plot_spell_most():
        psm = spell_used_the_most()
        return psm


    @render.ui
    def plot_spell_most_char():
        psmc = character_most_used_spell()
        title_html = ui.div("Character Most Used Spells", class_="table-title")

        table_html = psmc.to_html(classes='table table-striped table-bordered', index=False)

        return ui.HTML(f"{title_html}{table_html}")
