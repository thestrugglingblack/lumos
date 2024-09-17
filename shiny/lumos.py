from pathlib import Path
from shiny import App, Inputs, render, ui, Outputs, Session
from shinywidgets import output_widget, render_widget

from analysis.characters import house_count_chart, gender_count_chart
from analysis.dialogue import dialogue_per_character_chart
from analysis.places import places_frequently_mentioned, character_place_association
from analysis.spells import spell_used_the_most, character_most_used_spell


app_ui = ui.page_navbar(
    ui.head_content(
        ui.tags.link(rel="stylesheet", href="/style.css")
    ),
    ui.nav_spacer(),
    ui.nav_panel(
        "Character",
        ui.div(
            ui.card(
                output_widget("plot_house_count_chart"),
            ),

            ui.card(
                output_widget("plot_gender_count_chart")
            ),
            style="overflow-y: auto; width:100%;"
        ),
    ),
    ui.nav_panel(
        "Dialogue",
        ui.div(
            ui.card(
                output_widget('plot_dialogue_per_character_chart')
            ),

            ui.card(
                ui.img(src="/wordcloud.png", alt="Word Cloud")
            ),
            style="overflow-y: auto; width:100%;"
        )
    ),
    ui.nav_panel(
        'Places',
        ui.div(
            ui.card(
                output_widget('plot_places_frequently_mentioned')
            ),
            ui.card(
                output_widget('plot_character_place_association')
            )

        )
    ),
    ui.nav_panel(
        'Spells',
        ui.div(
            ui.card(
                output_widget('plot_spell_used_the_most')
            ),
            ui.card(
                ui.output_ui('plot_character_spell_most')
            )
        )
    ),
    sidebar=ui.sidebar(
        ui.markdown(
            "<p>Lumos is a Shiny Python application that does basic text analysis on the Harry Potter series. Its entire stack is deployed on AWS using Amazon Cloud Development kit (aws-cdk). You can learn more about Shiny Python and AWS-CDK in the links below.</p>"
        ),
        ui.markdown("[Slides](https://github.com/thestrugglingblack/lumos/blob/main/Illuminate%20Your%20Data%20-%20Shiny%20%2B%20CDK%20Deployments.pdf)"),
        ui.markdown("[GitHub](https://github.com/thestrugglingblack/lumos)"),
        ui.markdown("[Speaker](https://github.com/thestrugglingblack)")
    ),
    id="tabs",
    title="Lumos",
    fillable=True,
)


def server(input: Inputs, output: Outputs, session: Session):
    @output
    @render_widget
    def plot_house_count_chart():
        house = house_count_chart()
        return house

    @output
    @render_widget
    def plot_gender_count_chart():
        gender = gender_count_chart()
        return gender

    @output
    @render_widget
    def plot_dialogue_per_character_chart():
        dialogue = dialogue_per_character_chart()
        return dialogue

    @output
    @render_widget
    def plot_places_frequently_mentioned():
        freq = places_frequently_mentioned()
        return freq

    @output
    @render_widget
    def plot_character_place_association():
        assoc = character_place_association()
        return assoc

    @output
    @render_widget
    def plot_spell_used_the_most():
        most_spell = spell_used_the_most()
        return most_spell

    @output
    @render.ui
    def plot_character_spell_most():
        psmc = character_most_used_spell()
        title_html = ui.div("Character Most Used Spells", class_="table-title")
        table_html = psmc.to_html(classes='table table-striped table-bordered', index=False)
        return ui.HTML(f"{title_html}{table_html}")



app_dir = Path(__file__).parent
app = App(app_ui, server, static_assets=app_dir / "www")