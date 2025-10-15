from datetime import datetime
import streamlit as st
import altair as alt
import vega_datasets

# Load the CSS file
with open("style/style1.css") as f:
    css = f.read()

st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


cars_df = vega_datasets.data("cars")
# st.write(cars_df)

st.set_page_config(
    page_title="Cars Dataset",
    page_icon="🚗",
    layout="wide")


## Header text
"""
# Exploring the Cars Dataset
"""
""
st.write("The dataset contains information about various cars, including their horsepower, miles per gallon, weight, and year of manufacture.")
st.write("Use the chart and metrics below to explore the data.")


## Line Chart
# ##




# st.line_chart(cars_df, y="Horsepower", x="Miles_per_Gallon", x_label="Miles per Gallon (mpg)", y_label="Horsepower (hp)", height=400, width=700, use_container_width=True)

## Dataframe
# ##
# st.dataframe(cars_df, use_container_width=True,
#   column_config={
#       "Name": st.column_config.TextColumn(
#           "Car", help="The name of the car"
#       ),
#       "Miles_per_Gallon": st.column_config.NumberColumn(
#           "MPG", help="Miles per Gallon", format="%d mpg"
#       ),
#       "Weight_in_lbs": st.column_config.NumberColumn(
#           "Weight", help="Weight in pounds", format="%d lbs"
#       ),
#       "Year": st.column_config.DateColumn(
#           format="YYYY"
#       )
#   })



## Metrics
# ##

## Setting layout for charts and metrics ##
with st.container(horizontal=True, gap="small", horizontal_alignment="center", vertical_alignment="top"):
    cols = st.columns(4, gap="small", width="stretch")

    ## Getting some metrics ##
    min_year = cars_df["Year"].min()
    max_year = cars_df["Year"].max()
    min_accel = cars_df["Acceleration"].min()
    max_accel = cars_df["Acceleration"].max()
    min_mpg = cars_df["Miles_per_Gallon"].min()
    max_mpg = cars_df["Miles_per_Gallon"].max()
    min_hp = cars_df["Horsepower"].min()
    max_hp = cars_df["Horsepower"].max()
    css = " style='display: grid;grid-template-columns: 1fr 1fr;width:100%';width:100%;"
    hdrStyle = "<h3 style='color:#3c5c25;'>"
    divStyle1 = "<div class='minMax' style='width:100%;display:block;'>"
    divStyle2 = "<div class='minMax' style='width:100%;display:block;'>"



    ## Years
    # TODO: revisit-> (note: has to use st.write)
    minTxt = f"{divStyle1}<b>Min</b><br/>{min_year.year}</div>"
    maxTxt = f"{divStyle2}<b>Max</b><br/>{max_year.year}</div>"
    with cols[0].container(border=True, horizontal=True, height="stretch", width="stretch", gap="small"):
      st.markdown(f"{hdrStyle}Years</h3>", unsafe_allow_html=True)
      st.write("")
      st.write("")
      st.write("")
      st.markdown(f"<div{css}>{minTxt} {maxTxt}</div>", unsafe_allow_html=True)

    ## Acceleration
    minTxt = f"{divStyle1}<b>Min</b><br/>{f'{min_accel:0.0f} sec'}</div>"
    maxTxt = f"{divStyle2}<b>Max</b><br/>{f'{max_accel:0.0f} sec'}</div>"
    with cols[1].container(border=True, horizontal=True, height="stretch", width="stretch", gap="small"):
      st.markdown(f"{hdrStyle}Acceleration</h3>", unsafe_allow_html=True)
      st.html('<br/>')
      st.markdown(f"<div{css}>{minTxt} {maxTxt}</div>", unsafe_allow_html=True)

    ## Miles per Gallon
    minTxt = f"{divStyle1}<b>Min</b><br/>{f'{min_mpg:0.0f} mpg'}</div>"
    maxTxt = f"{divStyle2}<b>Max</b><br/>{f'{max_mpg:0.0f} mpg'}</div>"
    with cols[2].container(border=True, horizontal=True, height="stretch", width="stretch", gap="small"):
      st.markdown(f"{hdrStyle}Miles per Gallon</h3>", unsafe_allow_html=True)
      st.html('<br/>')
      st.markdown(f"<div{css}>{minTxt} {maxTxt}</div>", unsafe_allow_html=True)

    ## Horsepower
    minTxt = f"{divStyle1}<b>Min</b><br/>{min_hp} hp</div>"
    maxTxt = f"{divStyle2}<b>Max</b><br/>{max_hp} hp</div>"
    with cols[3].container(border=True, horizontal=True, height="stretch", width="stretch", gap="small"):
      st.markdown(f"{hdrStyle}Horsepower</h3>", unsafe_allow_html=True)
      st.html('<br/>')
      st.markdown(f"<div{css}>{minTxt} {maxTxt}</div>", unsafe_allow_html=True)

## Altair Charts
# ##
with st.container(horizontal=True, gap="small", horizontal_alignment="left", vertical_alignment="top", border=True):
  cols = st.columns(2, gap="small", width="stretch", border=True)

  with cols[0]:
    st.write("### Horsepower vs. Miles per Gallon")
    alt_chart1 = alt.Chart(cars_df).mark_point().encode(
      y='Horsepower',
      x='Miles_per_Gallon',
      color='Origin',
      tooltip=['Name', 'Horsepower', 'Miles_per_Gallon', 'Origin']
    ).interactive()
    st.altair_chart(alt_chart1, use_container_width=False)

  with cols[1]:
    st.write("### Horsepower vs. Cylinders")
    alt_chart2 = alt.Chart(cars_df).mark_tick().encode(
        x='Horsepower:Q',
        y='Cylinders:O'
    )
    st.altair_chart(alt_chart2, use_container_width=False)
