# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
# Q01
st.title("AY's First python app")
st.subheader('2021/10/22')
# Q02
st.markdown("[AnhongYang](https://github.com/Anhong-Yang) is a link to my Github")
st.write("student ID:41845042")
# Q03
UF=st.file_uploader("choose a .csv file to upload",type='csv')
   
# Q04
if  UF is not None:
    dfo = pd.read_csv(UF)
# Q12
    if "run" not in st.session_state:
        st.session_state["run"]=0
    else:
        st.session_state["run"]=st.session_state["run"]+1
    if st.session_state["run"] ==0:
        st.balloons()
        st.balloons()
# Q05
    df=dfo.applymap(lambda x: np.nan if x ==" " else x)
# Q12
    col1, col2=st.columns(2)
    with col1:
        st.header("The original DF")
        dfo
    with col2:
        st.header("The DF after replacing with NaN")
        df
# Q06
    def can_be_numeric(c):
            try:
                pd.to_numeric(df[c])
                return True
            except:
                return False
    good_cols= [c for c in df.columns if can_be_numeric(c)]
    st.write("These are the columns that all numeric:")
    good_cols
# Q07
    df[good_cols]=df[good_cols].apply(pd.to_numeric,axis=0)
    df[good_cols]
# Q08
    st.header("We can use these data to make a graph")
    x_axis=st.selectbox("Please choose the x-value",good_cols)
    y_axis=st.selectbox("Please choose the y-value",good_cols)
# Q09
    xv=st.slider('Please choose the row(s)',0,len(df.index)-1,(0,len(df.index)-1))
# Q10
    st.write(f"the object you choose is {xv}, with x-axis {x_axis} and y-axis {y_axis}")
# Q11
    LX=list(xv)
    LS=LX[0]
    RS=LX[1]
    df2=df.iloc[LS:RS,:]
    chart=alt.Chart(df.iloc[LS:RS]).mark_circle().encode(
        x=x_axis,
        y=y_axis,
        tooltip=[x_axis,y_axis],
        ).properties(
            width = 800
    )
    st.altair_chart(chart)
    st.write(f"This is the graph from row {LS} to row {RS} about {x_axis} and {y_axis}")

