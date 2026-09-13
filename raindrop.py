from scipy.constants import pi, milli, g
import math 
from collections import namedtuple 
import streamlit as st 

sphere_prop= namedtuple("sphere_properties" ,["volume", "mass", "force", "csa"])
def sphere_params(r, d):
    vol = (4/3) * pi * r**3 
    mass = vol * d 
    g_force = mass *g 
    cross_sec_area =pi * r**2

    #return vol, mass , g_force, cross_sec_area  
    return sphere_prop(volume=vol, mass=mass, force=g_force, csa=cross_sec_area)
    
def terminal_velocity(gf, rho_air,d_coeff, cs_area): 
    return math.sqrt( 2 * gf/ (cs_area * d_coeff * rho_air)) 

#page setup 
st.set_page_config(page_title="Raindrop Dynamics", page_icon=":cloud_rain:", layout="wide") 
st.title("Raindrop Falling through air: :blue[Dynamics]")

raindrop_radius =st.slider("Raindrop Radius (mm)", min_value=0.1, max_value=5.0, value=1.5, step=0.1) 
starting_height =st.slider("Starting Height (m)", min_value=100.0, max_value=2000.0, value=1200.0, step=10.0) 

rho_water = 1000 #kg/m3 
drag_coeff =0.6 
air_den =1.2 #kg/m3 

col1, col2 = st.columns(2)
with col1:
    st.subheader(":blue[**Raindrop Properties**]")
    st.code(f"Raindrop radius: {raindrop_radius:.1f} mm") 
    st.code(f"Starting height: {starting_height:.1f} m")
    st.code(f"Density of water: {rho_water:.1f} kg/m3")
    st.code(f"Drag coefficient: {drag_coeff:.1f}") 
    st.code(f"Air density: {air_den:.1f} kg/m3") 

#calculations    
drop = sphere_params(raindrop_radius*milli, rho_water) 
t_vel = terminal_velocity(drop.force, air_den, drag_coeff, drop.csa) 
#no drag free fall 
impact_vel = math.sqrt(2 * g * starting_height)

with col2: 
    st.subheader(":green[**Calculated Results**]")
    st.code(f"Raindrop volume: {drop.volume:.2e} m3") 
    st.code(f"Raindrop mass: {drop.mass:.2e} kg") 
    st.code(f"Raindrop cross sectional area: {drop.csa:.2e} m2")
    st.code(f"Gravitational force on raindrop: {drop.force:.2e} N") 
    st.code(f"Terminal velocity of raindrop: {t_vel:.2f} m/s")
    st.code(f"Impact velocity of raindrop (no drag): {impact_vel:.2f} m/s")
