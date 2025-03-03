import streamlit as st  
import pandas as pd  
import plotly.express as px  
from etl_pipeline import fetch_esg_news, calculate_risk_score  
from nlp_model import analyze_esg_sentiment  

def main():  
    st.title("🚨 ESG Risk Prediction Dashboard")  
    company = st.text_input("Enter a company name:", "Stake")  

    if company:  
        # Fetch data  
        news_df = fetch_esg_news(company, st.secrets["GNEWS_API_KEY"])  
        risk_score = calculate_risk_score(company, "data/esg_controversies_sample.csv")  

        # Show metrics  
        col1, col2 = st.columns(2)  
        col1.metric("ESG Risk Score", f"{risk_score}%", delta="High Risk" if risk_score > 70 else "Low Risk")  
        if not news_df.empty:  
            sentiment = analyze_esg_sentiment(news_df['title'].tolist())  
            col2.metric("Negative News Sentiment", f"{sentiment['negative']}%")  

        # Show geospatial risk (mock data)  
        st.subheader("Global Risk Heatmap")  
        geo_df = pd.DataFrame({  
            "country": ["USA", "Brazil", "India", "Germany"],  
            "risk": [45, 78, 65, 32]  
        })  
        fig = px.choropleth(geo_df, locations="country", locationmode="country names", color="risk")  
        st.plotly_chart(fig)  

if __name__ == "__main__":  
    main()  
