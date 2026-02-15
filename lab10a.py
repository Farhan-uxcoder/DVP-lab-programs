import plotly.express as px

df = px.data.stocks()
print(df.head(5))

fig = px.line(df,x = "date",y = df.columns,hover_data = {"date":"|%b %d,%Y"})
fig.update_xaxes(
    dtick = 'M1',
    tickformat = "%b \n %y"
)
fig.show()

fig = px.scatter(df,x="date",y=df.columns)
fig.show()

fig = px.bar(df,x="date",y=df.columns,barmode='group')
fig.show()