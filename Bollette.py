import streamlit as st
import pandas as pd
import numpy as np
import math as plt


st.header(":red[Calcolatore Bollette]")
st.subheader(
    "Puoi utilizzare quest'applicazione per visualizzare le tue bollette")
st.write('Le bollette saranno divise per tipo e verranno forniti dei grafici per visualizzarne meglio i dati in ordine cronologico')

st.button(label="Premi per salvare il costo dell'utenza e la data")

acqua = [12, 22]
data_acqua=[]

def acqua_list_filler():
    st.number_input(label="inserisci il valore delle utenze dell'acqua: ", )
    st.date_input(label="inserisci la data")

def main():
    acqua_list_filler()
   


if __name__ == '__main__':
    main()
