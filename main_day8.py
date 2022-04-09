import pandas as pd
import streamlit as st
import pydeck as pdk

st.header('Find the opposite side of the Earth')
st.subheader('st.slider')

lat = st.slider('Latitude', -90.0, 90.0, 37.57)
lon = st.slider('Longitude', -180.0, 180.0, 126.98)
# lat = st.slider('Latitude', -90.0, 90.0, 52.23)
# lon = st.slider('Longitude', -180.0, 180.0, -1.42)
rad = st.slider('Mark radius [km]', 1, 10, 5)

columns = st.columns(2)

with columns[0]:
    st.write('Your inputs')
    df = pd.DataFrame({
        'lat': [lat],
        'lon': [lon],
    })

    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(
            latitude=lat,
            longitude=lon,
            zoom=10,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=df,
                get_position='[lon, lat]',
                opacity=0.2,
                stroked=True,
                line_width_scale=30,
                get_line_color=[0, 0, 0],
                get_fill_color=[255, 140, 0],
                get_radius=rad * 1000,
            ),
        ]
    ))

with columns[1]:
    st.write('Antipode')

    df_antipode = pd.DataFrame({
        'lat': [-lat],
        'lon': [lon - 180 if lon > 0 else lon + 180],
    })

    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(
            latitude=-lat,
            longitude=lon - 180 if lon > 0 else lon + 180,
            zoom=10,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=df_antipode,
                get_position='[lon, lat]',
                opacity=0.2,
                stroked=True,
                line_width_scale=30,
                get_line_color=[0, 0, 0],
                get_fill_color=[255, 140, 0],
                get_radius=rad * 1000,
            ),
        ]
    ))
