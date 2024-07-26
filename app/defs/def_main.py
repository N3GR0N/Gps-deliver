import pandas as pd
import folium
import osmnx as ox
import networkx as nx
import streamlit as st

# Coordenadas de inicio
start = '-34.926992, -57.925635'
start_lat, start_lon = map(float, start.split(', '))

def get_map(selected_addresses):
    # Cargar datos geocodificados
    df = pd.read_csv("app/files/geocoded_data.csv")
    selected_df = df[df['Address'].isin(selected_addresses)]

    # Descargar el grafo de calles de la zona
    G = ox.graph_from_place('La Plata, Argentina', network_type='drive')

    # Convertir las coordenadas a nodos
    def get_nearest_node(lat, lon):
        return ox.distance.nearest_nodes(G, lon, lat)

    selected_df['Node'] = selected_df.apply(lambda row: get_nearest_node(row['Latitude'], row['Longitude']), axis=1)

    # Agregar el punto de inicio como nodo en el grafo
    start_node = get_nearest_node(start_lat, start_lon)
    start_df = pd.DataFrame({
        'Address': ['Inicio'],
        'Latitude': [start_lat],
        'Longitude': [start_lon],
        'Node': [start_node]
    })

    selected_df = pd.concat([selected_df, start_df], ignore_index=True)

    # Calcular la ruta óptima
    route_nodes = selected_df['Node'].tolist()
    route = nx.shortest_path(G, route_nodes[0], route_nodes[1], weight='length')
    for i in range(1, len(route_nodes) - 1):
        route.extend(nx.shortest_path(G, route_nodes[i], route_nodes[i + 1], weight='length')[1:])

    # Crear el mapa con un estilo mejorado
    m = folium.Map(
        location=[start_lat, start_lon],  # Centrar el mapa en la dirección de inicio
        zoom_start=14,
        tiles='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',  # Estilo estándar de OpenStreetMap
        attr='Map data © OpenStreetMap contributors'  # Atribución estándar para OpenStreetMap
    )

    # Agregar ruta al mapa
    folium.PolyLine(
        locations=[(G.nodes[n]['y'], G.nodes[n]['x']) for n in route],
        color='blue',
        weight=5,
        opacity=0.7
    ).add_to(m)

    # Agregar marcadores para las direcciones seleccionadas
    for _, row in selected_df.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=row['Address'],
            icon=folium.Icon(color='red', icon='info-sign', icon_color='white')
        ).add_to(m)

    return m

def main_page():
    st.title("Seleccionar Direcciones y Mostrar Camino")

    df = pd.read_csv("app/files/geocoded_data.csv")
    addresses = df['Address'].tolist()

    selected_addresses = st.multiselect("Selecciona las direcciones", addresses)

    # Asegurarse de que al menos una dirección se seleccione además del punto de inicio
    if len(selected_addresses) < 1:
        st.warning("Por favor, selecciona al menos una dirección para calcular el camino.")
    else:
        # Asegurarse de que 'Inicio' esté incluido en las direcciones seleccionadas
        if 'Inicio' not in selected_addresses:
            selected_addresses.append('Inicio')
        
        st.write("Direcciones seleccionadas:", selected_addresses)
        route_map = get_map(selected_addresses)
        st.components.v1.html(route_map._repr_html_(), height=600)

if __name__ == "__main__":
    main_page()
