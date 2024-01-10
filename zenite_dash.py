import streamlit as st
import pandas as pd
import numpy as np

st.title('Vai apostar? Descubra aqui as melhores linhas!')

data_file = 'zenite_data.csv'
league_dict = {
    "Premier League (Inglaterra)":39,
    "LaLiga (Espanha)":140, 
    "Bundesliga (Alemanha)":78,
    "Liga Serie A (Itália)":135,
    "League 1 (França)":61,
    "Liga Portugal (Portugal)":94,
    "Eredivisie (Holanda)":88
}

@st.cache_data
def load_data(league_id=0):
    data = pd.read_csv(data_file)
    if league_id != 0:   
        data = data[data.league_id == league_id]
    return data

option_league = st.selectbox(
   "Escolha a Liga que você vai apostar:",
   ("Premier League (Inglaterra)",
    "LaLiga (Espanha)", 
    "Bundesliga (Alemanha)",
    "Liga Serie A (Itália)",
    "League 1 (França)",
    "Liga Portugal (Portugal)",
    "Eredivisie (Holanda)"),
   index=0,
   placeholder="Escolha a liga",
)

df = load_data(league_dict[option_league])

teams = sorted(df.team_name.unique())

option_team1 = st.selectbox(
        "Escolha o Time Mandante:",
        teams,
        index=0,
        placeholder="Escolha o time"
)

option_team2 = st.selectbox(
        "Escolha o Time Visitante:",
        teams,
        index=0,
        placeholder="Escolha o time"
)

df1 = df[df.team_name == option_team1]
df2 = df[df.team_name == option_team2]

option_bet = st.selectbox(
   "Escolha o evento que você vai apostar:",
   ("Total de Gols",
    "Total de Escanteios", 
    "Total de Cartões Amarelos",
    "Total de Chutes a Gol",
    "Resultado Final",
    "Dupla Chance"),
   index=0,
   placeholder="Escolha a aposta",
)

if option_bet == 'Total de Gols':
    option_value = st.selectbox(
        "Escolha a linha que você vai apostar:",
        (0.5,1.5,2.5,3.5,4.5),
        index=0,
        placeholder="Escolha a linha"
    )
    
    option_ovr_und = st.selectbox(
        f"Acima ou Abaixo de {option_value}?",
        ("Acima (Over)","Abaixo (Under)"),
        index=0,
        placeholder="Escolha a linha"
    )

    if option_ovr_und == 'Acima (Over)':
        data_list = [
            {'Situação':f'{option_team1} na Temporada',
            'Sucesso/Partidas':f'A meta for batida {len(df1[df1.goals + df1.goals_opp > option_value])} vezes em {len(df1)} ocasiões',
            'Porcentagem de Sucesso (%)':f'{len(df1[df1.goals + df1.goals_opp > option_value])*100/len(df1):.0f}%'},
            {'Situação':f'{option_team1} em Casa',
            'Sucesso/Partidas':f'A meta for batida {len(df1[(df1.goals + df1.goals_opp > option_value) & (df1.home == 1)])} vezes em {len(df1[df1.home == 1])} ocasiões',
            'Porcentagem de Sucesso (%)':f'{len(df1[(df1.goals + df1.goals_opp > option_value) & (df1.home == 1)])*100/len(df1[df1.home == 1]):.0f}%'},
            {'Situação':f'{option_team2} na Temporada',
            'Sucesso/Partidas':f'A meta for batida {len(df2[df2.goals + df2.goals_opp > option_value])} vezes em {len(df2)} ocasiões',
            'Porcentagem de Sucesso (%)':f'{len(df2[df2.goals + df2.goals_opp > option_value])*100/len(df2):.0f}%'},
            {'Situação':f'{option_team2} Fora de Casa',
            'Sucesso/Partidas':f'A meta for batida {len(df2[(df2.goals + df2.goals_opp > option_value) & (df2.home == 0)])} vezes em {len(df2[df2.home == 0])} ocasiões',
            'Porcentagem de Sucesso (%)':f'{len(df2[(df2.goals + df2.goals_opp > option_value) & (df2.home == 0)])*100/len(df2[df2.home == 0]):.0f}%'},    
        ]
    else:
        data_list = [
            {'Situação':f'{option_team1} na Temporada',
            'Sucesso/Partidas':f'A meta for batida {len(df1[df1.goals + df1.goals_opp < option_value])} vezes em {len(df1)} ocasiões',
            'Porcentagem de Sucesso (%)':f'{len(df1[df1.goals + df1.goals_opp < option_value])*100/len(df1):.0f}%'},
            {'Situação':f'{option_team1} em Casa',
            'Sucesso/Partidas':f'A meta for batida {len(df1[(df1.goals + df1.goals_opp < option_value) & (df1.home == 1)])} vezes em {len(df1[df1.home == 1])} ocasiões',
            'Porcentagem de Sucesso (%)':f'{len(df1[(df1.goals + df1.goals_opp < option_value) & (df1.home == 1)])*100/len(df1[df1.home == 1]):.0f}%'},
            {'Situação':f'{option_team2} na Temporada',
            'Sucesso/Partidas':f'A meta for batida {len(df2[df2.goals + df2.goals_opp < option_value])} vezes em {len(df2)} ocasiões',
            'Porcentagem de Sucesso (%)':f'{len(df2[df2.goals + df2.goals_opp < option_value])*100/len(df2):.0f}%'},
            {'Situação':f'{option_team2} Fora de Casa',
            'Sucesso/Partidas':f'A meta for batida {len(df2[(df2.goals + df2.goals_opp < option_value) & (df2.home == 0)])} vezes em {len(df2[df2.home == 0])} ocasiões',
            'Porcentagem de Sucesso (%)':f'{len(df2[(df2.goals + df2.goals_opp < option_value) & (df2.home == 0)])*100/len(df2[df2.home == 0]):.0f}%'},    
        ]        


elif option_bet == 'Total de Escanteios':
    option_value = st.selectbox(
        "Escolha o a linha que você vai apostar:",
        (5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5,13.5),
        index=0,
        placeholder="Escolha a linha"
    )

    option_ovr_und = st.selectbox(
        f"Acima ou Abaixo de {option_value}?",
        ("Acima (Over)","Abaixo (Under)"),
        index=0,
        placeholder="Escolha a linha"
    )

    if option_ovr_und == 'Acima (Over)':
        data_list = [
            {'Situação':f'{option_team1} na Temporada',
            'Sucesso/Partidas':f'A meta for batida {len(df1[df1.corners + df1.corners_opp > option_value])} vezes em {len(df1)} ocasiões',
            'Porcentagem de Sucesso (%)':f'{len(df1[df1.corners + df1.corners_opp > option_value])*100/len(df1):.0f}%'},
            {'Situação':f'{option_team1} em Casa',
            'Sucesso/Partidas':f'A meta for batida {len(df1[(df1.corners + df1.corners_opp > option_value) & (df1.home == 1)])} vezes em {len(df1[df1.home == 1])} ocasiões',
            'Porcentagem de Sucesso (%)':f'{len(df1[(df1.corners + df1.corners_opp > option_value) & (df1.home == 1)])*100/len(df1[df1.home == 1]):.0f}%'},
            {'Situação':f'{option_team2} na Temporada',
            'Sucesso/Partidas':f'A meta for batida {len(df2[df2.corners + df2.corners_opp > option_value])} vezes em {len(df2)} ocasiões',
            'Porcentagem de Sucesso (%)':f'{len(df2[df2.corners + df2.corners_opp > option_value])*100/len(df2):.0f}%'},
            {'Situação':f'{option_team2} Fora de Casa',
            'Sucesso/Partidas':f'A meta for batida {len(df2[(df2.corners + df2.corners_opp > option_value) & (df2.home == 0)])} vezes em {len(df2[df2.home == 0])} ocasiões',
            'Porcentagem de Sucesso (%)':f'{len(df2[(df2.corners + df2.corners_opp > option_value) & (df2.home == 0)])*100/len(df2[df2.home == 0]):.0f}%'},    
        ]
    else:
        data_list = [
            {'Situação':f'{option_team1} na Temporada',
            'Sucesso/Partidas':f'A meta for batida {len(df1[df1.corners + df1.corners_opp < option_value])} vezes em {len(df1)} ocasiões',
            'Porcentagem de Sucesso (%)':f'{len(df1[df1.corners + df1.corners_opp < option_value])*100/len(df1):.0f}%'},
            {'Situação':f'{option_team1} em Casa',
            'Sucesso/Partidas':f'A meta for batida {len(df1[(df1.corners + df1.corners_opp < option_value) & (df1.home == 1)])} vezes em {len(df1[df1.home == 1])} ocasiões',
            'Porcentagem de Sucesso (%)':f'{len(df1[(df1.corners + df1.corners_opp < option_value) & (df1.home == 1)])*100/len(df1[df1.home == 1]):.0f}%'},
            {'Situação':f'{option_team2} na Temporada',
            'Sucesso/Partidas':f'A meta for batida {len(df2[df2.corners + df2.corners_opp < option_value])} vezes em {len(df2)} ocasiões',
            'Porcentagem de Sucesso (%)':f'{len(df2[df2.corners + df2.corners_opp < option_value])*100/len(df2):.0f}%'},
            {'Situação':f'{option_team2} Fora de Casa',
            'Sucesso/Partidas':f'A meta for batida {len(df2[(df2.corners + df2.corners_opp < option_value) & (df2.home == 0)])} vezes em {len(df2[df2.home == 0])} ocasiões',
            'Porcentagem de Sucesso (%)':f'{len(df2[(df2.corners + df2.corners_opp < option_value) & (df2.home == 0)])*100/len(df2[df2.home == 0]):.0f}%'},    
        ]
                    
elif option_bet == 'Total de Cartões Amarelos':
    option_value = st.selectbox(
        "Escolha o a linha que você vai apostar:",
        (0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5),
        index=0,
        placeholder="Escolha a linha"
    )

    option_ovr_und = st.selectbox(
        f"Acima ou Abaixo de {option_value}?",
        ("Acima (Over)","Abaixo (Under)"),
        index=0,
        placeholder="Escolha a linha"
    )

    if option_ovr_und == 'Acima (Over)':
        data_list = [
            {'Situação':f'{option_team1} na Temporada',
            'Sucesso/Partidas':f'A meta for batida {len(df1[df1.yellow_cards + df1.yellow_cards_opp > option_value])} vezes em {len(df1)} ocasiões',
            'Porcentagem de Sucesso (%)':f'{len(df1[df1.yellow_cards + df1.yellow_cards_opp > option_value])*100/len(df1):.0f}%'},
            {'Situação':f'{option_team1} em Casa',
            'Sucesso/Partidas':f'A meta for batida {len(df1[(df1.yellow_cards + df1.yellow_cards_opp > option_value) & (df1.home == 1)])} vezes em {len(df1[df1.home == 1])} ocasiões',
            'Porcentagem de Sucesso (%)':f'{len(df1[(df1.yellow_cards + df1.yellow_cards_opp > option_value) & (df1.home == 1)])*100/len(df1[df1.home == 1]):.0f}%'},
            {'Situação':f'{option_team2} na Temporada',
            'Sucesso/Partidas':f'A meta for batida {len(df2[df2.yellow_cards + df2.yellow_cards_opp > option_value])} vezes em {len(df2)} ocasiões',
            'Porcentagem de Sucesso (%)':f'{len(df2[df2.yellow_cards + df2.yellow_cards_opp > option_value])*100/len(df2):.0f}%'},
            {'Situação':f'{option_team2} Fora de Casa',
            'Sucesso/Partidas':f'A meta for batida {len(df2[(df2.yellow_cards + df2.yellow_cards_opp > option_value) & (df2.home == 0)])} vezes em {len(df2[df2.home == 0])} ocasiões',
            'Porcentagem de Sucesso (%)':f'{len(df2[(df2.yellow_cards + df2.yellow_cards_opp > option_value) & (df2.home == 0)])*100/len(df2[df2.home == 0]):.0f}%'},    
        ]
    else:
        data_list = [
            {'Situação':f'{option_team1} na Temporada',
            'Sucesso/Partidas':f'A meta for batida {len(df1[df1.yellow_cards + df1.yellow_cards_opp < option_value])} vezes em {len(df1)} ocasiões',
            'Porcentagem de Sucesso (%)':f'{len(df1[df1.yellow_cards + df1.yellow_cards_opp < option_value])*100/len(df1):.0f}%'},
            {'Situação':f'{option_team1} em Casa',
            'Sucesso/Partidas':f'A meta for batida {len(df1[(df1.yellow_cards + df1.yellow_cards_opp < option_value) & (df1.home == 1)])} vezes em {len(df1[df1.home == 1])} ocasiões',
            'Porcentagem de Sucesso (%)':f'{len(df1[(df1.yellow_cards + df1.yellow_cards_opp < option_value) & (df1.home == 1)])*100/len(df1[df1.home == 1]):.0f}%'},
            {'Situação':f'{option_team2} na Temporada',
            'Sucesso/Partidas':f'A meta for batida {len(df2[df2.yellow_cards + df2.yellow_cards_opp < option_value])} vezes em {len(df2)} ocasiões',
            'Porcentagem de Sucesso (%)':f'{len(df2[df2.yellow_cards + df2.yellow_cards_opp < option_value])*100/len(df2):.0f}%'},
            {'Situação':f'{option_team2} Fora de Casa',
            'Sucesso/Partidas':f'A meta for batida {len(df2[(df2.yellow_cards + df2.yellow_cards_opp < option_value) & (df2.home == 0)])} vezes em {len(df2[df2.home == 0])} ocasiões',
            'Porcentagem de Sucesso (%)':f'{len(df2[(df2.yellow_cards + df2.yellow_cards_opp < option_value) & (df2.home == 0)])*100/len(df2[df2.home == 0]):.0f}%'},    
        ] 

elif option_bet == 'Total de Chutes a Gol':
    option_value = st.selectbox(
        "Escolha o a linha que você vai apostar:",
        (4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5),
        index=0,
        placeholder="Escolha a linha"
    )

    option_ovr_und = st.selectbox(
        f"Acima ou Abaixo de {option_value}?",
        ("Acima (Over)","Abaixo (Under)"),
        index=0,
        placeholder="Escolha a linha"
    )

    if option_ovr_und == 'Acima (Over)':
        data_list = [
            {'Situação':f'{option_team1} na Temporada',
            'Sucesso/Partidas':f'A meta for batida {len(df1[df1.shots_on + df1.shots_on_opp > option_value])} vezes em {len(df1)} ocasiões',
            'Porcentagem de Sucesso (%)':f'{len(df1[df1.shots_on + df1.shots_on_opp > option_value])*100/len(df1):.0f}%'},
            {'Situação':f'{option_team1} em Casa',
            'Sucesso/Partidas':f'A meta for batida {len(df1[(df1.shots_on + df1.shots_on_opp > option_value) & (df1.home == 1)])} vezes em {len(df1[df1.home == 1])} ocasiões',
            'Porcentagem de Sucesso (%)':f'{len(df1[(df1.shots_on + df1.shots_on_opp > option_value) & (df1.home == 1)])*100/len(df1[df1.home == 1]):.0f}%'},
            {'Situação':f'{option_team2} na Temporada',
            'Sucesso/Partidas':f'A meta for batida {len(df2[df2.shots_on + df2.shots_on_opp > option_value])} vezes em {len(df2)} ocasiões',
            'Porcentagem de Sucesso (%)':f'{len(df2[df2.shots_on + df2.shots_on_opp > option_value])*100/len(df2):.0f}%'},
            {'Situação':f'{option_team2} Fora de Casa',
            'Sucesso/Partidas':f'A meta for batida {len(df2[(df2.shots_on + df2.shots_on_opp > option_value) & (df2.home == 0)])} vezes em {len(df2[df2.home == 0])} ocasiões',
            'Porcentagem de Sucesso (%)':f'{len(df2[(df2.shots_on + df2.shots_on_opp > option_value) & (df2.home == 0)])*100/len(df2[df2.home == 0]):.0f}%'},    
        ]
    else:
        data_list = [
            {'Situação':f'{option_team1} na Temporada',
            'Sucesso/Partidas':f'A meta for batida {len(df1[df1.shots_on + df1.shots_on_opp < option_value])} vezes em {len(df1)} ocasiões',
            'Porcentagem de Sucesso (%)':f'{len(df1[df1.shots_on + df1.shots_on_opp < option_value])*100/len(df1):.0f}%'},
            {'Situação':f'{option_team1} em Casa',
            'Sucesso/Partidas':f'A meta for batida {len(df1[(df1.shots_on + df1.shots_on_opp < option_value) & (df1.home == 1)])} vezes em {len(df1[df1.home == 1])} ocasiões',
            'Porcentagem de Sucesso (%)':f'{len(df1[(df1.shots_on + df1.shots_on_opp < option_value) & (df1.home == 1)])*100/len(df1[df1.home == 1]):.0f}%'},
            {'Situação':f'{option_team2} na Temporada',
            'Sucesso/Partidas':f'A meta for batida {len(df2[df2.shots_on + df2.shots_on_opp < option_value])} vezes em {len(df2)} ocasiões',
            'Porcentagem de Sucesso (%)':f'{len(df2[df2.shots_on + df2.shots_on_opp < option_value])*100/len(df2):.0f}%'},
            {'Situação':f'{option_team2} Fora de Casa',
            'Sucesso/Partidas':f'A meta for batida {len(df2[(df2.shots_on + df2.shots_on_opp < option_value) & (df2.home == 0)])} vezes em {len(df2[df2.home == 0])} ocasiões',
            'Porcentagem de Sucesso (%)':f'{len(df2[(df2.shots_on + df2.shots_on_opp < option_value) & (df2.home == 0)])*100/len(df2[df2.home == 0]):.0f}%'},    
        ] 


elif option_bet == 'Resultado Final':
    option_value = st.selectbox(
        "Escolha o a linha que você vai apostar:",
        ("1 - Mandante","X - Empate","2 - Visitante"),
        index=0,
        placeholder="Escolha a linha"
    )

    if option_value == '1 - Mandante':
        data_list = [
            {'Situação':f'{option_team1} na Temporada',
            'Sucesso/Partidas':f'Venceu {len(df1[df1.win == 1])} de {len(df1)} jogos na Temporada',
            'Porcentagem de Sucesso (%)':f'{len(df1[df1.win == 1])*100/len(df1):.0f}%'},
            {'Situação':f'{option_team1} em Casa',
            'Sucesso/Partidas':f'Venceu {len(df1[(df1.win == 1) & (df1.home == 1)])} de {len(df1[df1.home == 1])} jogos em Casa',
            'Porcentagem de Sucesso (%)':f'{len(df1[(df1.win == 1) & (df1.home == 1)])*100/len(df1[df1.home == 1]):.0f}%'},
            {'Situação':f'{option_team2} na Temporada',
            'Sucesso/Partidas':f'Perdeu {len(df2[df2.loss == 1])} de {len(df2)} jogos na Temporada',
            'Porcentagem de Sucesso (%)':f'{len(df2[df2.loss == 1])*100/len(df2):.0f}%'},
            {'Situação':f'{option_team2} Fora de Casa',
            'Sucesso/Partidas':f'Perdeu {len(df2[(df2.loss == 1) & (df2.home == 0)])} de {len(df2[df2.home == 0])} jogos Fora de Casa',
            'Porcentagem de Sucesso (%)':f'{len(df2[(df2.loss == 1) & (df2.home == 0)])*100/len(df2[df2.home == 0]):.0f}%'},    
        ]
    elif option_value == '2 - Visitante':
        data_list = [
            {'Situação':f'{option_team1} na Temporada',
            'Sucesso/Partidas':f'Perdeu {len(df1[df1.loss == 1])} de {len(df1)} jogos na Temporada',
            'Porcentagem de Sucesso (%)':f'{len(df1[df1.loss == 1])*100/len(df1):.0f}%'},
            {'Situação':f'{option_team1} em Casa',
            'Sucesso/Partidas':f'Perdeu {len(df1[(df1.loss == 1) & (df1.home == 1)])} de {len(df1[df1.home == 1])} jogos em Casa',
            'Porcentagem de Sucesso (%)':f'{len(df1[(df1.loss == 1) & (df1.home == 1)])*100/len(df1[df1.home == 1]):.0f}%'},
            {'Situação':f'{option_team2} na Temporada',
            'Sucesso/Partidas':f'Venceu {len(df2[df2.win == 1])} de {len(df2)} jogos na Temporada',
            'Porcentagem de Sucesso (%)':f'{len(df2[df2.win == 1])*100/len(df2):.0f}%'},
            {'Situação':f'{option_team2} Fora de Casa',
            'Sucesso/Partidas':f'Venceu {len(df2[(df2.win == 1) & (df2.home == 0)])} de {len(df2[df2.home == 0])} jogos Fora de Casa',
            'Porcentagem de Sucesso (%)':f'{len(df2[(df2.win == 1) & (df2.home == 0)])*100/len(df2[df2.home == 0]):.0f}%'},    
        ]
    elif option_value == 'X - Empate':
        data_list = [
            {'Situação':f'{option_team1} na Temporada',
            'Sucesso/Partidas':f'Empatou {len(df1[df1.draw == 1])} de {len(df1)} jogos na Temporada',
            'Porcentagem de Sucesso (%)':f'{len(df1[df1.draw == 1])*100/len(df1):.0f}%'},
            {'Situação':f'{option_team1} em Casa',
            'Sucesso/Partidas':f'Empatou {len(df1[(df1.draw == 1) & (df1.home == 1)])} de {len(df1[df1.home == 1])} jogos em Casa',
            'Porcentagem de Sucesso (%)':f'{len(df1[(df1.draw == 1) & (df1.home == 1)])*100/len(df1[df1.home == 1]):.0f}%'},
            {'Situação':f'{option_team2} na Temporada',
            'Sucesso/Partidas':f'Empatou {len(df2[df2.draw == 1])} de {len(df2)} jogos na Temporada',
            'Porcentagem de Sucesso (%)':f'{len(df2[df2.draw == 1])*100/len(df2):.0f}%'},
            {'Situação':f'{option_team2} Fora de Casa',
            'Sucesso/Partidas':f'Empatou {len(df2[(df2.draw == 1) & (df2.home == 0)])} de {len(df2[df2.home == 0])} jogos Fora de Casa',
            'Porcentagem de Sucesso (%)':f'{len(df2[(df2.draw == 1) & (df2.home == 0)])*100/len(df2[df2.home == 0]):.0f}%'},    
        ]          
    
elif option_bet == 'Dupla Chance':
    option_value = st.selectbox(
        "Escolha o a linha que você vai apostar:",
        ("1X - Vitória do Mandante ou Empate","X2 - Vitória do Visitante ou Empate","12 - Vitória do Mandante ou Vitória do Visitante"),
        index=0,
        placeholder="Escolha a linha"
    )

    if option_value == '1X - Vitória do Mandante ou Empate':
        data_list = [
            {'Situação':f'{option_team1} na Temporada',
            'Sucesso/Partidas':f'Ganhou ou Empatou em {len(df1[df1.goals >= df1.goals_opp])} de {len(df1)} jogos na Temporada',
            'Porcentagem de Sucesso (%)':f'{len(df1[df1.goals >= df1.goals_opp])*100/len(df1):.0f}%'},
            {'Situação':f'{option_team1} em Casa',
            'Sucesso/Partidas':f'Ganhou ou Empatou em {len(df1[(df1.goals >= df1.goals_opp)])} de {len(df1[df1.home == 1])} jogos em Casa',
            'Porcentagem de Sucesso (%)':f'{len(df1[(df1.goals >= df1.goals_opp) & (df1.home == 1)])*100/len(df1[df1.home == 1]):.0f}%'},
            {'Situação':f'{option_team2} na Temporada',
            'Sucesso/Partidas':f'Perdeu {len(df2[df2.loss == 1])} de {len(df2)} jogos na Temporada',
            'Porcentagem de Sucesso (%)':f'{len(df2[df2.loss == 1])*100/len(df2):.0f}%'},
            {'Situação':f'{option_team2} Fora de Casa',
            'Sucesso/Partidas':f'Perdeu {len(df2[(df2.loss == 1) & (df2.home == 0)])} de {len(df2[df2.home == 0])} jogos Fora de Casa',
            'Porcentagem de Sucesso (%)':f'{len(df2[(df2.loss == 1) & (df2.home == 0)])*100/len(df2[df2.home == 0]):.0f}%'},    
        ]
    elif option_value == 'X2 - Vitória do Visitante ou Empate':
        data_list = [
            {'Situação':f'{option_team1} na Temporada',
            'Sucesso/Partidas':f'Perdeu {len(df1[df1.loss == 1])} de {len(df1)} jogos na Temporada',
            'Porcentagem de Sucesso (%)':f'{len(df1[df1.loss == 1])*100/len(df1):.0f}%'},
            {'Situação':f'{option_team1} em Casa',
            'Sucesso/Partidas':f'Perdeu {len(df1[(df1.loss == 1)])} de {len(df1[df1.home == 1])} jogos em Casa',
            'Porcentagem de Sucesso (%)':f'{len(df1[(df1.loss == 1) & (df1.home == 1)])*100/len(df1[df1.home == 1]):.0f}%'},
            {'Situação':f'{option_team2} na Temporada',
            'Sucesso/Partidas':f'Ganhou ou Empatou em {len(df2[df2.goals >= df2.goals_opp])} de {len(df2)} jogos na Temporada',
            'Porcentagem de Sucesso (%)':f'{len(df2[df2.goals >= df2.goals_opp])*100/len(df2):.0f}%'},
            {'Situação':f'{option_team2} Fora de Casa',
            'Sucesso/Partidas':f'Ganhou ou Empatou em {len(df2[(df2.goals >= df2.goals_opp) & (df2.home == 0)])} de {len(df2[df2.home == 0])} jogos Fora de Casa',
            'Porcentagem de Sucesso (%)':f'{len(df2[(df2.goals >= df2.goals_opp) & (df2.home == 0)])*100/len(df2[df2.home == 0]):.0f}%'},    
        ]
    elif option_value == '12 - Vitória do Mandante ou Vitória do Visitante':
        data_list = [
            {'Situação':f'{option_team1} na Temporada',
            'Sucesso/Partidas':f'Ganhou ou Perdeu {len(df1[df1.draw != 1])} de {len(df1)} jogos na Temporada',
            'Porcentagem de Sucesso (%)':f'{len(df1[df1.draw != 1])*100/len(df1):.0f}%'},
            {'Situação':f'{option_team1} em Casa',
            'Sucesso/Partidas':f'Ganhou ou Perdeu {len(df1[(df1.draw != 1) & (df1.home == 1)])} de {len(df1[df1.home == 1])} jogos em Casa',
            'Porcentagem de Sucesso (%)':f'{len(df1[(df1.draw != 1) & (df1.home == 1)])*100/len(df1[df1.home == 1]):.0f}%'},
            {'Situação':f'{option_team2} na Temporada',
            'Sucesso/Partidas':f'Ganhou ou Perdeu {len(df2[df2.draw != 1])} de {len(df2)} jogos na Temporada',
            'Porcentagem de Sucesso (%)':f'{len(df2[df2.draw != 1])*100/len(df2):.0f}%'},
            {'Situação':f'{option_team2} Fora de Casa',
            'Sucesso/Partidas':f'Ganhou ou Perdeu {len(df2[(df2.draw != 1) & (df2.home == 0)])} de {len(df2[df2.home == 0])} jogos Fora de Casa',
            'Porcentagem de Sucesso (%)':f'{len(df2[(df2.draw != 1) & (df2.home == 0)])*100/len(df2[df2.home == 0]):.0f}%'},    
        ]

df_pct = pd.DataFrame(data_list)

st.table(df_pct)