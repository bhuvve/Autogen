# Autogen Financial Analysis Agents

## Overview
This repository contains example implementations of Autogen AI agents designed for financial data analysis and report generation. These agents collaborate to analyze stock performance, gather news insights, and generate structured financial reports.

## Features
- **Stock Data Retrieval**: Fetches stock prices and key financial ratios without requiring an API key.
- **Market News Analysis**: Retrieves relevant news headlines for stocks using web scraping.
- **Financial Report Generation**: Creates comprehensive financial reports including performance analysis, visualizations, and insights.
- **Multi-Agent Collaboration**: Different agents specialize in writing, reviewing, and ensuring data consistency.
- **Automated Review System**: Critiques and improves reports using legal, consistency, and alignment reviewers.

## Agents
- **Financial Assistant**: Retrieves stock prices, ratios, and performance metrics.
- **Researcher**: Gathers news headlines for stock trends.
- **Writer**: Generates structured financial reports.
- **Critic**: Reviews reports and provides improvement feedback.
- **Legal Reviewer**: Ensures reports comply with financial regulations.
- **Consistency Reviewer**: Checks for logical consistency in data and text.
- **Text Alignment Reviewer**: Verifies numerical accuracy within text explanations.
- **Completion Reviewer**: Ensures all required elements are present in reports.
- **Meta Reviewer**: Aggregates reviewer feedback for final suggestions.

## Usage
1. **Install Dependencies**:
   ```bash
   pip install autogen streamlit
   ```
2. **Run Streamlit Interface**:
   ```bash
   streamlit run app.py
   ```
3. **Provide Stock Tickers**: Enter comma-separated stock symbols in the Streamlit interface.
4. **Start Analysis**: Click the "Start analysis" button to initiate the agents' workflow.
5. **View Results**: The financial report and stock performance visualizations will be displayed.

## Project Structure
```
📂 autogen-financial-analysis
├── 📜 README.md
├── 📜 requirements.txt
├── 📜 app.py
├── 📂 assets
│   ├── normalized_prices.png
├── 📂 agents
│   ├── financial_agent.py
│   ├── research_agent.py
│   ├── writer_agent.py
│   ├── critic_agent.py
│   ├── reviewers.py
```

## Future Enhancements
- **Integration with Real-time Market APIs**
- **Advanced Data Visualizations**
- **Support for More Asset Classes (Crypto, ETFs, etc.)**
- **Sentiment Analysis on Market News**

## License
This project is open-source under the MIT License.
