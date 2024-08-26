import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import random

dialogue_df = pd.read_csv('./data/dialogue.csv')
character_df = pd.read_csv('./data/characters.csv')


def dialogue_per_character_chart():
    merge_dialogue_character_df = dialogue_df.merge(character_df[['Character ID', 'Character Name']], on='Character ID', how='left')
    dialogue_counts = merge_dialogue_character_df.groupby('Character Name').size().reset_index(name='Number of Dialogues')
    dialogue_counts = dialogue_counts[dialogue_counts['Number of Dialogues'] >= 40]

    dialogue_counts = dialogue_counts.sort_values(by='Number of Dialogues', ascending=False)

    colors = ['#ae0001', '#ecb939', '#222f5b', '#2a623d']
    random.shuffle(colors)

    fig = px.bar(dialogue_counts,
                 x='Character Name',
                 y='Number of Dialogues',
                 title='Number of Dialogues per Character',
                 labels={'Character Name': 'Characters', 'Number of Dialogues': 'Number of Dialogues'},
                 color='Character Name',
                 color_discrete_sequence=colors
                 )

    fig.update_layout(
        title_font=dict(family='Space Mono',  color="#B67352", size=40 ),
        xaxis_tickangle=-45,
        xaxis_title_font=dict(family='Space Mono', color='black', size=18),
        yaxis_title_font=dict(family='Space Mono', color='black', size=18),
        autosize=True,
        height=800,
        margin=dict(l=20, r=20, t=150, b=50),
        showlegend=False
    )

    return fig

def wordcloud():
    all_dialogues = ' '.join(dialogue_df['Dialogue'].dropna())
    colors = ['#ae0001', '#ecb939', '#222f5b', '#2a623d']

    def custom_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
        return random.choice(colors)

    wordcloud = WordCloud(
        width=700,
        height=400,
        background_color='white',
        color_func=custom_color_func
    ).generate(all_dialogues)

    img = BytesIO()
    plt.figure(figsize=(18, 9))

    plt.subplots_adjust(top=0.85)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')

    plt.title('Word Cloud', fontdict={'family': 'Space Mono', 'color': '#B67352', 'size': 30}, pad=20)

    plt.savefig(img, format='png', bbox_inches='tight', pad_inches=0.5)
    plt.close()
    img.seek(0)
    wc_img = base64.b64encode(img.read()).decode('utf-8')

    return wc_img