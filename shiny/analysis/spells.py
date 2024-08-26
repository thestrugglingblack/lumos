import random
import pandas as pd
import plotly.express as px
from collections import Counter, defaultdict

character_df = pd.read_csv('./data/characters.csv')
dialogue_df = pd.read_csv('./data/dialogue.csv')
spells_df = pd.read_csv('./data/spells.csv')

def spell_used_the_most():
    dialogues = dialogue_df['Dialogue'].dropna().tolist()
    spell_names = spells_df['Name'].dropna().tolist()

    spell_mentioned = Counter()

    for dialogue in dialogues:
        for spell in spell_names:
            if spell.lower() in dialogue.lower():
                spell_mentioned[spell] += 1

    spell_mentioned_df = pd.DataFrame(spell_mentioned.items(), columns=['Spells', 'Mentions'])
    spell_mentioned_df = spell_mentioned_df.sort_values(by='Mentions', ascending=False)

    colors = ['#ae0001', '#ecb939', '#222f5b', '#2a623d']

    fig = px.treemap(spell_mentioned_df,
                     path=['Spells'],
                     values='Mentions',
                     title='Spells Used the Most',
                     color='Spells',
                     color_discrete_sequence=colors
                     )

    fig.update_layout(
        title_font=dict(family='Space Mono', size=24, color='#B67352'),
        font=dict(family='Space Mono', size=14, color='black'),
        margin=dict(l=40, r=40, b=40, t=150),
        height=700,
        autosize=True,
        showlegend=True
    )

    return fig

def character_most_used_spell():
    dialogues = dialogue_df[['Character ID', 'Dialogue']].dropna()
    spell_names = spells_df['Name'].dropna().tolist()

    character_spell_counts = defaultdict(Counter)

    for _, row in dialogues.iterrows():
        char_id = row['Character ID']
        dialogue = row['Dialogue'].lower()
        for spell in spell_names:
            if spell.lower() in dialogue:
                character_spell_counts[char_id][spell] += 1

    most_used_spells = []

    for char_id, spells in character_spell_counts.items():
        most_common_spell = spells.most_common(1)[0]
        most_used_spells.append({
            'Character ID': char_id,
            'Most Used Spell': most_common_spell[0],
            'Spell Count': most_common_spell[1]
        })

    most_used_spells_df = pd.DataFrame(most_used_spells)

    final_df = most_used_spells_df.merge(character_df[['Character ID', 'Character Name']], on='Character ID', how='left')

    final_df = final_df[['Character Name', 'Most Used Spell', 'Spell Count']].sort_values(by='Character Name')

    return final_df