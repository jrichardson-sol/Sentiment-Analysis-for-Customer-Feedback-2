# **Customer Feedback Sentiment Analyzer**
![image](https://github.com/user-attachments/assets/865b0405-c9ff-415d-8f01-6d4332800ad5)
![image](https://github.com/user-attachments/assets/0fcf96bf-c23f-4f11-b3de-7d06769a5a33)


This project is a **Streamlit-based web application** designed to perform sentiment analysis on customer feedback. It supports both single feedback input and batch processing via CSV uploads. The project uses **TextBlob** for sentiment analysis and visualizes results using **matplotlib** and **seaborn**.

---

## **Overview**
The **Customer Feedback Sentiment Analyzer** allows businesses to understand the sentiments behind their customer feedback efficiently. Whether analyzing a single piece of feedback or processing bulk data, the app is built to provide actionable insights.

This application can be adapted for other use cases, such as analyzing feedback in mergers and acquisitions (M&A), product reviews, or employee feedback surveys.

---

## **Features**
- **Single Input Analysis**: Users can type in individual feedback and instantly analyze the sentiment.
- **Batch Processing**: Upload a CSV file with multiple feedback entries for batch sentiment analysis.
- **Visualization**: Displays a bar chart summarizing the sentiment distribution (Positive, Negative, Neutral).
- **Downloadable Results**: Users can download the analyzed results in CSV format.
- **Expandable Use Cases**: The app's framework can be adapted for various feedback scenarios.

---

## **Technologies Used**
- **Python**
- **Streamlit** (Frontend)
- **TextBlob** (Sentiment Analysis)
- **matplotlib** & **seaborn** (Data Visualization)
- **pandas** (Data Handling)

---

## **Project Structure**
```
project-folder/
│
├── app.py                 # Main Streamlit app code
├── sample_feedback.csv    # Example input CSV file
├── requirements.txt       # Python dependencies for deployment
└── README.md              # Project documentation
```

---

## **Setup Instructions**

### **1. Clone the Repository**
To replicate this project, clone the GitHub repository to your local machine:
```bash
git clone https://github.com/<your-username>/Sentiment-Analysis-for-Customer-Feedback.git
cd Sentiment-Analysis-for-Customer-Feedback
```

### **2. Install Dependencies**
Ensure Python 3.8+ is installed. Install the required dependencies using:
```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes:
```
streamlit
textblob
pandas
matplotlib
seaborn
```

### **3. Run the Application Locally**
Launch the app in your local browser using Streamlit:
```bash
streamlit run app.py
```
The app will open in your default browser at `http://localhost:8501`.

---

## **How to Use the Application**

### **Single Feedback Analysis**
1. Enter your feedback in the text box.
2. Click **Analyze Sentiment**.
3. The sentiment (Positive, Negative, or Neutral) and polarity score will be displayed.

### **Batch CSV Upload**
1. Upload a CSV file with a column named `Customer Feedback`.
   - Example format:
     ```csv
     Customer Feedback
     "The service was excellent!"
     "Very poor experience, will not recommend."
     "The product is okay but could be improved."
     ```
2. The app will analyze all feedback in the CSV and display the results in a table.
3. You can download the results as a CSV file.

---

## **Deployment**

### **Deploying to Streamlit Cloud**
1. Push your project to a GitHub repository.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud).
3. Click **New App** and connect your GitHub repository.
4. Select the branch (e.g., `main`) and the file path to `app.py`.
5. Click **Deploy**. Streamlit Cloud will provide a public URL for your app.

### **Other Deployment Options**
- **Heroku**: Use the `requirements.txt` and `Procfile` for deployment.
- **AWS/Google Cloud**: Containerize the app using Docker and deploy.

---

## **Adapting the Project for Other Use Cases**
This project can be easily modified for various use cases by updating the input format and sentiment logic. Examples include:
1. **M&A Sentiment Analysis**: Analyze feedback on mergers and acquisitions.
2. **Product Review Analysis**: Assess product feedback from e-commerce platforms.
3. **Employee Surveys**: Gauge employee sentiments from survey results.

### How to Adapt:
- Replace the `Customer Feedback` input field with your desired context (e.g., "Employee Comments").
- Update the sample CSV and README documentation to reflect the new use case.

---

## **Sample Data for Testing**
Here is sample data for an M&A use case:

### CSV Format:
```csv
Customer Feedback
"The acquisition was seamless and well-executed."
"The process was confusing and lacked transparency."
"Great communication between the teams involved."
"Very poor execution; deadlines were missed repeatedly."
```

### Results Example:
| Feedback                                    | Sentiment   | Polarity Score |
|---------------------------------------------|-------------|----------------|
| The acquisition was seamless and well-executed. | Positive    | 0.75           |
| The process was confusing and lacked transparency. | Negative    | -0.4           |
| Great communication between the teams involved.   | Positive    | 0.6            |
| Very poor execution; deadlines were missed repeatedly. | Negative    | -0.8           |

---

## **Common Issues & Troubleshooting**

### Issue: `ModuleNotFoundError`
If a module (e.g., `textblob`) is missing, ensure you’ve installed all dependencies:
```bash
pip install -r requirements.txt
```

### Issue: App Doesn't Load on Deployment
- Ensure `app.py` is in the root directory of your repository.
- Verify that the required libraries are listed in `requirements.txt`.

### Issue: Merge Conflicts During Git Push
- Resolve conflicts manually, then push the changes:
```bash
git pull origin main --allow-unrelated-histories
git push -u origin main
```

---

## **Next Steps**
- **Extend Features**: Add advanced sentiment analysis using machine learning models like `NLTK` or `transformers`.
- **Integrate APIs**: Fetch real-time feedback from platforms like Twitter or Google Reviews.
- **Improve UI**: Use Streamlit themes or integrate with a frontend framework for a polished interface.

---

## **Acknowledgments**
- **Streamlit** for an excellent platform for rapid app deployment.
- **TextBlob** for providing easy sentiment analysis tools.
- Inspiration drawn from real-world use cases like M&A feedback analysis.
