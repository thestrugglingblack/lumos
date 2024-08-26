import pandas as pd
import plotly.express as px

characters_df = pd.read_csv('./data/characters.csv')
characters_df.columns = characters_df.columns.str.strip()



def house_count_chart():
    filtered_df = characters_df[~characters_df['House'].isin(['Beauxbatons Academy of Magic', 'Durmstrang Institute'])]
    house_counts = filtered_df['House'].value_counts().reset_index()
    house_counts.columns = ['House', 'Number of Characters']

    color_mapping = {
        'Gryffindor': '#ae0001',
        'Hufflepuff': '#ecb939',
        'Ravenclaw': '#222f5b',
        'Slytherin': '#2a623d'
    }

    fig = px.bar(house_counts,
                 x='House',
                 y='Number of Characters',
                 title='Characters By House',
                 color='House',  # Use the 'House' column to determine the color
                 color_discrete_map=color_mapping  # Apply the custom color mapping
                 )

    icons = {
        'Gryffindor': '/gryffindor.png',
        'Hufflepuff': '/hufflepuff.png',
        'Ravenclaw': '/ravenclaw.png',
        'Slytherin': '/slytherin.png'
    }
    max_y = house_counts['Number of Characters'].max()
    y_range = max_y * 1.2

    for i, row in house_counts.iterrows():
        fig.add_layout_image(
            dict(
                source=icons[row['House']],
                x=row['House'],
                y=row['Number of Characters'],
                xref="x",
                yref="y",
                sizex=6,
                sizey=0.2 * max_y,
                xanchor="center",
                yanchor="middle",
                opacity=1.0,
                layer="above",
            )
        )

    fig.update_layout(
        title_font=dict(family='Space Mono', color='#B67352', size=40),
        xaxis_title_font=dict(family='Space Mono', color='black', size=18),
        yaxis_title_font=dict(family='Space Mono', color='black', size=18),
        font=dict(family='Space Mono', color='black', size=14),
        yaxis=dict(range=[0, y_range]),
        autosize=True,
        width=None,
        height=800,
        template='plotly_white',
        margin=dict(l=20, r=20, t=100, b=50)
    )
    return fig

def gender_count_chart():
    filtered_df = characters_df[characters_df['Gender'] != 'Human']
    gender_counts = filtered_df['Gender'].value_counts().reset_index()
    gender_counts.columns = ['Gender', 'Count']

    gender_counts['Gender'] = gender_counts['Gender'].replace({
        'Female': 'Female',
        'Male': 'Male'
    })

    color_mapping = {
        'Female': '#FF8DA1',
        'Male': '#89CFF0'
    }

    fig = px.pie(
        gender_counts,
        values='Count',
        names='Gender',
        title='Distribution of Characters by Gender',
        color='Gender',
        color_discrete_map=color_mapping
    )

    fig.update_layout(
        title_font=dict(family='Space Mono, monospace', color='#B67352', size=40),
        font=dict(family='Space Mono, monospace', color='black', size=14),
        margin=dict(l=20, r=20, t=200, b=20),
        height=600,
        showlegend=True,
    )
    return fig