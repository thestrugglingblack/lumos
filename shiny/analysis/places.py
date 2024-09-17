import random
import plotly.express as px
import pandas as pd





def places_frequently_mentioned():
    places_df = pd.read_csv('./data/places.csv')
    character_df = pd.read_csv('./data/characters.csv')
    dialogue_df = pd.read_csv('./data/dialogue.csv')

    merged_df = dialogue_df.merge(places_df, on='Place ID', how='left')
    merged_df = merged_df.merge(character_df, on='Character ID', how='left')

    place_dialogue_freq = merged_df.groupby('Place Name')['Dialogue ID'].count().reset_index()
    place_dialogue_freq.columns = ['Place Name', 'Dialogue Frequency']

    place_character_count = merged_df.groupby('Place Name')['Character ID'].nunique().reset_index()
    place_character_count.columns = ['Place Name', 'Unique Character Count']

    place_category_count = merged_df.groupby('Place Name')['Place Category'].nunique().reset_index()
    place_category_count.columns = ['Place Name', 'Category Count']

    final_df = place_dialogue_freq.merge(place_character_count, on='Place Name')
    final_df = final_df.merge(place_category_count, on='Place Name')

    colors = ['#ae0001', '#ecb939', '#222f5b', '#2a623d']
    random.shuffle(colors)  # Randomize the colors

    fig = px.scatter(
        final_df,
        x='Dialogue Frequency',
        y='Unique Character Count',
        size='Category Count',
        color='Place Name',
        hover_name='Place Name',
        title='Frequency of Character and Places Based on Dialogue',
        labels={
            'Dialogue Frequency': 'Dialogue Frequency',
            'Unique Character Count': 'Unique Character Count'
        },
        size_max=60,
        color_discrete_sequence=colors
    )

    fig.update_layout(
        title_font=dict(family='Space Mono', size=24, color="#B67352"),
        xaxis_title_font=dict(family='Space Mono', size=18, color='black'),
        yaxis_title_font=dict(family='Space Mono', size=18, color='black'),
        font=dict(family='Space Mono', size=14, color='black'),
        margin=dict(l=40, r=40, b=40, t=150),
        height=800,
        autosize=True,
    )

    return fig

def character_place_association():
    places_df = pd.read_csv('./data/places.csv')
    character_df = pd.read_csv('./data/characters.csv')
    dialogue_df = pd.read_csv('./data/dialogue.csv')

    merged_df = dialogue_df.merge(places_df, on='Place ID', how='left')
    merged_df = merged_df.merge(character_df, on='Character ID', how='left')
    association_counts = merged_df.groupby(['Place Name', 'Character Name']).size().reset_index(name='Count')

    colors = ['#ae0001', '#ecb939', '#222f5b', '#2a623d']
    random.shuffle(colors)

    fig = px.histogram(
        association_counts,
        x='Place Name',
        y='Count',
        color='Character Name',
        barmode='group',
        title='Character-Place Associations',
        color_discrete_sequence=colors
    )

    fig.update_layout(
        title_font=dict(family='Space Mono', size=24, color='#B67352'),
        xaxis_title_font=dict(family='Space Mono', size=18, color='black'),
        yaxis_title_font=dict(family='Space Mono', size=18, color='black'),
        font=dict(family='Space Mono', size=14, color='black'),
        margin=dict(l=40, r=40, b=40, t=250),
        height=800,
        autosize=True,
        xaxis_tickangle=-45
    )

    return fig