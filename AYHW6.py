# -*- coding: utf-8 -*-
# Name:Anhong Yang
# UCI ID : 41845042
# Assignment Math10 Homework6
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
st.title("Using K-Means to predict the center of cluster")
choose_iter=st.slider("Please choose the times of iteration",1,40)

X, _ = make_blobs(n_samples=1000, centers=5, n_features=2, random_state = 1)
df = pd.DataFrame(X, columns = list("ab"))
starting_points = np.array([[0,0],[-2,0],[-4,0],[0,2],[0,4]])
kmeans = KMeans(n_clusters = 5, max_iter=choose_iter, init=starting_points, n_init = 1)
kmeans.fit(X);
df["c"] = kmeans.predict(X)
chart1 = alt.Chart(df).mark_circle().encode(
    x = "a",
    y = "b",
    color = "c:N"
)

df_centers = pd.DataFrame(kmeans.cluster_centers_, columns = list("ab"))

chart_centers = alt.Chart(df_centers).mark_point().encode(
    x = "a",
    y = "b",
    color = alt.value("black"),
    shape = alt.value("diamond"),
)

st.altair_chart(chart1 + chart_centers)
st.write("We could see that expect the green one, all the cluster center move toward the red side until the 25th iteration")
# chart1 + chart_centers
