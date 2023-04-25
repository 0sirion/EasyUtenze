import streamlit as st
import pandas as pd
import numpy as np
import math as plt


st.header(":red[Calcolatore Bollette]")
st.subheader(
    "Puoi utilizzare quest'applicazione per visualizzare le tue bollette")
st.write('Le bollette saranno divise per tipo e verranno forniti dei grafici per visualizzarne meglio i dati in ordine cronologico')


def main():
    print("hello")

acqua = [27, 29, 50, 30]

def acqua_list_filler():
    st.number_input(label="inserisci il valore delle utenze dell'acqua: ", )


if __name__ == '__main__':
    main()
