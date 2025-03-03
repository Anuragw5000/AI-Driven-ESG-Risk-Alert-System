import pandas as pd  
from gnews import GNews  
import sqlite3  

def fetch_esg_news(company: str, api_key: str) -> pd.DataFrame:  
    """Fetch real-time news articles related to ESG risks for a company."""  
    try:  
        news_client = GNews(api_key=api_key, max_results=10, period='7d')  
        articles = news_client.get_news(f'{company} ESG environment social governance')  
        return pd.DataFrame(articles)  
    except Exception as e:  
        print(f"Error fetching news: {e}")  
        return pd.DataFrame()  

def calculate_risk_score(company: str, esg_data_path: str) -> float:  
    """Calculate ESG risk score using historical data and news sentiment."""  
    # Load Kaggle ESG dataset (sample)  
    esg_df = pd.read_csv(esg_data_path)  
    company_data = esg_df[esg_df['company_name'] == company]  

    # Simulate risk score (replace with your logic)  
    base_score = company_data['esg_score'].values[0] if not company_data.empty else 50  
    return round(base_score * 1.2, 2)  # Hypothetical adjustment  

if __name__ == "__main__":  
    # Example usage  
    news_df = fetch_esg_news("Stake", "YOUR_GNEWS_API_KEY")  
    risk_score = calculate_risk_score("Stake", "data/esg_controversies_sample.csv")  
    print(f"Risk Score: {risk_score}%")  
