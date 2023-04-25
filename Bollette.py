import streamlit as st
import pandas as pd
import numpy as np
import math as plt


st.header(":red[Calcolatore Bollette]")
st.subheader(
    "Puoi utilizzare quest'applicazione per visualizzare le tue bollette")
st.write('Le bollette saranno divise per tipo e verranno forniti dei grafici per visualizzarne meglio i dati in ordine cronologico')


acqua_list = []
acqua_data_list=[]

x = st.number_input(label="inserisci il valore delle utenze dell'acqua: ", max_value=100, )
acqua_date = st.date_input(label="inserisci la data")
my_button =st.button(label="Premi per salvare il costo dell'utenza e la data", on_click=acqua_list_filler())


def acqua_list_filler():
    if x != 0 :
        acqua_list.append(x)
        st.write(acqua_list)
        x = ""



    


def main():
    print('hello')
   


if __name__ == '__main__':
    main()
