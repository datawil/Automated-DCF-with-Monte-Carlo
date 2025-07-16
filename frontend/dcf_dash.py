@app.callback(
    Output('monte-carlo-plot', 'figure'),
    Input('run-simulation', 'n_clicks'),
    [State('ticker-input', 'value'),
     State('wacc-input', 'value')]
)
def update_monte_carlo(n_clicks, ticker, wacc):
    response = requests.get(f"{API_URL}/dcf-analysis/{ticker}?wacc={wacc}")
    data = response.json()
    
    fig = px.histogram(
        data['monte_carlo']['simulations'],
        title=f"DCF Value Distribution (95% CI: {data['monte_carlo']['confidence_interval']})"
    )
    fig.add_vline(x=data['point_estimate'], line_dash="dash")
    return fig