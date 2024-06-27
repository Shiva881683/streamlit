import streamlit as st
import pandas as pd
import numpy as np


st.title("Data App Assignment, on June 20th")

st.write("### Input Data and Examples")
df = pd.read_csv("Superstore_Sales_utf8.csv", parse_dates=True)
st.dataframe(df)

# This bar chart will not have solid bars--but lines--because the detail data is being graphed independently
st.bar_chart(df, x="Category", y="Sales")

# Now let's do the same graph where we do the aggregation first in Pandas... (this results in a chart with solid bars)
st.dataframe(df.groupby("Category").sum())
# Using as_index=False here preserves the Category as a column.  If we exclude that, Category would become the datafram index and we would need to use x=None to tell bar_chart to use the index
st.bar_chart(df.groupby("Category", as_index=False).sum(), x="Category", y="Sales", color="#04f")

# Aggregating by time
# Here we ensure Order_Date is in datetime format, then set is as an index to our dataframe
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df.set_index('Order_Date', inplace=True)
# Here the Grouper is using our newly set index to group by Month ('M')
sales_by_month = df.filter(items=['Sales']).groupby(pd.Grouper(freq='M')).sum()

st.dataframe(sales_by_month)

# Here the grouped months are the index and automatically used for the x axis
st.line_chart(sales_by_month, y="Sales")

st.write("## Your additions")
category = st.selectbox("Select a Category", data['Category'])
 category:
    sub_categories = data['Sub_Category'][category]
    selected_sub_categories = st.multiselect(f"Select Sub-Categories in {category}", sub_categories)
  st.write("### Sales Line Chart")
    sales_chart = filtered_df.groupby('Order_Date')['Sales'].sum().reset_index()
    st.line_chart(sales_chart, x='Order_Date', y='Sales')
 # Calculate metrics
    total_sales = filtered_df['Sales'].sum()
    total_profit = filtered_df['Profit'].sum()
    overall_profit_margin = total_profit / total_sales * 100

    # Overall average profit margin for all products across all categories
    overall_avg_profit_margin = df['Profit'].sum() / df['Sales'].sum() * 100
    delta_profit_margin = overall_profit_margin - overall_avg_profit_margin
# Step (4): Show three metrics
    st.write("### Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Sales", f"${total_sales:,.2f}")
    col2.metric("Total Profit", f"${total_profit:,.2f}")
    col3.metric("Overall Profit Margin", f"{overall_profit_margin:.2f}%", delta=f"{delta_profit_margin:.2f}%")
# Display selected options
st.write(f"Selected Category: {category}")
st.write(f"Selected Sub-Categories: {selected_sub_categories}")
