<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README - Autogen Financial Analysis Agents</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }
        code { background: #f4f4f4; padding: 5px; border-radius: 5px; }
        pre { background: #f4f4f4; padding: 10px; border-radius: 5px; }
    </style>
</head>
<body>
    <h1>Autogen Financial Analysis Agents</h1>
    <p>This repository provides an AI-driven multi-agent system that automates financial analysis, stock performance evaluation, and report generation using <code>Autogen</code> and <code>Streamlit</code>.</p>
    
    <h2>Features</h2>
    <ul>
        <li>Retrieves stock price data and financial metrics without API keys.</li>
        <li>Performs correlation and risk analysis on selected stocks.</li>
        <li>Fetches recent market news to contextualize stock movements.</li>
        <li>Generates comprehensive financial reports with structured tables and insightful commentary.</li>
        <li>Includes multiple review agents for legal, consistency, text alignment, and completeness checks.</li>
    </ul>
    
    <h2>Installation</h2>
    <pre><code>pip install autogen streamlit</code></pre>
    
    <h2>Usage</h2>
    <pre><code>streamlit run app.py</code></pre>
    
    <h2>Agents Overview</h2>
    <ul>
        <li><b>Financial Assistant:</b> Gathers financial data and prepares normalized price figures.</li>
        <li><b>Researcher:</b> Retrieves stock market news from sources like Bing News and Google Search.</li>
        <li><b>Writer:</b> Creates structured financial reports based on gathered data.</li>
        <li><b>Critic & Reviewers:</b> Validate, review, and enhance the final financial report.</li>
    </ul>
    
    <h2>How It Works</h2>
    <ol>
        <li>Users enter stock tickers for analysis.</li>
        <li>Agents retrieve stock performance data and financial metrics.</li>
        <li>Researcher gathers news headlines for market context.</li>
        <li>Writer generates an insightful financial report.</li>
        <li>Critic and reviewers ensure high-quality output.</li>
    </ol>
    
    <h2>Output</h2>
    <p>The system generates a <b>financial report</b> with:</p>
    <ul>
        <li>Stock price performance comparisons</li>
        <li>Tables summarizing key financial ratios</li>
        <li>Visualized stock trends</li>
        <li>Insights from recent market news</li>
    </ul>
    
    <h2>License</h2>
    <p>This project is open-source and available under the MIT License.</p>
</body>
</html>
