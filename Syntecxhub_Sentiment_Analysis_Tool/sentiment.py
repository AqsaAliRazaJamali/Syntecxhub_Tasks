import pandas as pd
import re
import joblib
import os
import random
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, classification_report
import warnings
warnings.filterwarnings('ignore')

class SentimentAnalyzer:
    def __init__(self, vectorizer_type='tfidf', classifier_type='logistic'):
        """
        Initialize Sentiment Analyzer
        
        Args:
            vectorizer_type: 'tfidf' or 'count'
            classifier_type: 'logistic' or 'naive_bayes'
        """
        self.vectorizer_type = vectorizer_type
        self.classifier_type = classifier_type
        self.model = None
        self.vectorizer = None
        self.stop_words = {
            'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", 
            "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 
            'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 
            'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'am', 'is', 
            'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 
            'do', 'does', 'did', 'doing', 'will', 'would', 'could', 'should', 'might', 
            'must', 'shall', 'may', 'can', 'a', 'an', 'the', 'and', 'but', 'or', 'for', 
            'nor', 'on', 'at', 'to', 'by', 'in', 'with', 'without', 'of', 'off', 'over', 
            'under', 'above', 'below', 'between', 'among', 'through', 'during', 'within', 
            'upon', 'towards', 'until', 'into', 'about', 'after', 'before', 'behind', 
            'beside', 'beyond', 'down', 'from', 'up', 'than', 'so', 'too', 'very', 'just'
        }
    
    def preprocess_text(self, text):
        """
        Clean and tokenize text
        
        Args:
            text: String text to preprocess
            
        Returns:
            Cleaned text string
        """
        if not isinstance(text, str):
            text = str(text)
        
        text = text.lower()
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
        text = re.sub(r'@\w+|#\w+', '', text)
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        
        tokens = re.findall(r'\b[a-zA-Z]+\b', text)
        tokens = [token for token in tokens if token not in self.stop_words and len(token) > 2]
        
        return ' '.join(tokens)
    
    def create_large_sample_data(self):
        """
        Create large sample dataset (400+ samples) for better training
        """
        print("\n Creating 400+ sample dataset for better training...")

        positive_templates = [
            # Product quality
            "amazing quality product", "excellent build quality", "superb craftsmanship",
            "durable and reliable", "premium quality material", "high quality finish",
            "top notch quality", "outstanding quality", "great quality item",
            "quality exceeded expectations", "quality is fantastic",
            
            # Performance
            "works perfectly", "performs exceptionally well", "outstanding performance",
            "fast and efficient", "excellent performance", "great speed and accuracy",
            "works like a charm", "flawless operation", "excellent functionality",
            "performs great", "works exactly as expected",
            
            # Customer service
            "excellent customer service", "friendly and helpful staff", "great support team",
            "responsive customer care", "professional service", "amazing support",
            "helpful and courteous", "service was outstanding", "great experience with staff",
            "customer support is excellent",
            
            # Value for money
            "great value for money", "worth every penny", "excellent price for quality",
            "affordable and reliable", "great deal", "best price for this quality",
            "value for money", "reasonable price", "great investment", "cost effective",
            
            # General positive
            "best product ever", "highly recommend", "absolutely love it", "very satisfied",
            "exceeded expectations", "great purchase", "happy with my decision",
            "would buy again", "very pleased", "super happy", "love this product",
            "absolutely fantastic", "wonderful experience", "brilliant product",
            "outstanding product", "favorite purchase", "superb product",
            "excellent choice", "best decision", "very impressed",
            "pleasantly surprised", "great addition", "perfect solution",
            "above and beyond", "top quality", "first class service",
            "exceptional value", "really enjoyed", "very much liked",
            "pleased to say", "happy customer", "positive experience",
        ]
        negative_templates = [
            # Product quality
            "terrible quality", "poor build quality", "flimsy material",
            "cheaply made", "low quality product", "bad quality",
            "quality is terrible", "poor craftsmanship", "poor finish",
            "cheap material", "falls apart easily", "not durable",
            
            # Performance
            "does not work", "poor performance", "stops working",
            "works poorly", "broken immediately", "completely useless",
            "failed to work", "not functioning properly", "performance issues",
            "does not perform", "not effective", "barely works",
            
            # Customer service
            "terrible customer service", "rude staff", "unhelpful support",
            "worst service ever", "ignored my request", "poor support",
            "unresponsive customer care", "bad attitude from staff",
            "service was awful", "customer service is terrible",
            
            # Value for money
            "waste of money", "overpriced", "not worth the price",
            "expensive and low quality", "bad value", "overcharged",
            "paying too much", "rip off", "money wasted", "not worth it",
            
            # General negative
            "worst product ever", "never buying again", "complete waste",
            "very disappointed", "would not recommend", "regret buying",
            "terrible experience", "hate this product", "very dissatisfied",
            "horrible product", "awful experience", "bad decision",
            "disgusting quality", "disappointing purchase", "not recommended",
            "avoid this product", "really bad", "extremely poor",
            "useless product", "don't waste money", "worst experience",
            "terrible purchase", "completely dissatisfied", "very unhappy",
            "bad purchase", "poor quality", "total disappointment",
            "negative experience", "not satisfied", "would not buy again",
            "very bad", "absolutely terrible", "completely useless",
        ]
        positive_reviews = []
        negative_reviews = []
        
        for i in range(250):
            base = random.choice(positive_templates)
            variations = [
                f"I love the {base}", f"This is {base}", f"Absolutely {base}",
                f"Really {base}", f"Just {base}", f"The {base}",
                f"Overall {base}", f"Definitely {base}", f"Truly {base}",
                base.capitalize()
            ]
            review = random.choice(variations)
            if random.random() > 0.5:
                suffix = random.choice(["!", ".", " Highly recommended.", " 5 stars."])
                review = review + suffix
            positive_reviews.append(review)
        
        for i in range(250):
            base = random.choice(negative_templates)
            variations = [
                f"I hate the {base}", f"This is {base}", f"Absolutely {base}",
                f"Really {base}", f"Just {base}", f"The {base}",
                f"Overall {base}", f"Definitely {base}", f"Truly {base}",
                base.capitalize()
            ]
            review = random.choice(variations)
            if random.random() > 0.5:
                suffix = random.choice(["!", ".", " Never again.", " 0 stars."])
                review = review + suffix
            negative_reviews.append(review)
        
        all_texts = positive_reviews + negative_reviews
        all_labels = [1] * len(positive_reviews) + [0] * len(negative_reviews)
        
        combined = list(zip(all_texts, all_labels))
        random.shuffle(combined)
        shuffled_texts, shuffled_labels = zip(*combined)
        
        df = pd.DataFrame({
            'text': shuffled_texts,
            'label': shuffled_labels
        })
        
        print(f" Created {len(df)} samples")
        print(f" Positive samples: {sum(df['label'] == 1)}")
        print(f" Negative samples: {sum(df['label'] == 0)}")
        print(f" Total: {len(df)} samples\n")
    
        print("Sample data preview:")
        print(f"  1. {df['text'].iloc[0]} → {'Positive' if df['label'].iloc[0] == 1 else 'Negative'}")
        print(f"  2. {df['text'].iloc[1]} → {'Positive' if df['label'].iloc[1] == 1 else 'Negative'}")
        print(f"  3. {df['text'].iloc[2]} → {'Positive' if df['label'].iloc[2] == 1 else 'Negative'}")
        
        return df
    
    def load_csv_data(self, filepath, text_column='text', label_column='label'):
        """
        Load data from CSV file
        
        Args:
            filepath: Path to CSV file
            text_column: Column name containing text (default: 'text')
            label_column: Column name containing labels (default: 'label')
        
        Returns:
            DataFrame with loaded data
        """
        try:
            df = pd.read_csv(filepath)
            print(f" Loaded {len(df)} rows from {filepath}")
            print(f" Columns found: {df.columns.tolist()}")
            
            if text_column not in df.columns:
                print(f"✗ Column '{text_column}' not found!")
                print(f"  Available columns: {df.columns.tolist()}")
                return None
            
            if label_column not in df.columns:
                print(f"✗ Column '{label_column}' not found!")
                print(f"  Available columns: {df.columns.tolist()}")
                return None
            
            unique_labels = df[label_column].unique()
            valid_labels = [0, 1]
            if not all(label in valid_labels for label in unique_labels):
                print(f" Labels should be 0 (negative) and 1 (positive)")
                print(f"  Found: {sorted(unique_labels)}")
                return None
            
            df[label_column] = df[label_column].astype(int)
            
            distribution = df[label_column].value_counts()
            print(f"\n Class Distribution:")
            print(f"  Positive (1): {distribution.get(1, 0)} samples")
            print(f"  Negative (0): {distribution.get(0, 0)} samples")
            print(f"  Total: {len(df)} samples")
            
            return df
            
        except Exception as e:
            print(f"✗ Error loading CSV: {e}")
            return None
    
    def train(self, df, text_column='text', label_column='label'):
        """
        Train the sentiment analysis model
        
        Args:
            df: DataFrame with text and label columns
            text_column: Column name containing text
            label_column: Column name containing labels
        """
        print("\n Preprocessing text...")
        df['cleaned'] = df[text_column].apply(self.preprocess_text)
        
        print(f"  Before: {df[text_column].iloc[0]}")
        print(f"  After:  {df['cleaned'].iloc[0]}")
        
        X_train, X_test, y_train, y_test = train_test_split(
            df['cleaned'], df[label_column], 
            test_size=0.2, 
            random_state=42, 
            stratify=df[label_column]
        )
        print(f"\n Data Split:")
        print(f"  Training samples: {len(X_train)}")
        print(f"  Test samples: {len(X_test)}")
        
        # Vectorize text
        print(f"\n Vectorizing text using {self.vectorizer_type.upper()}...")
        if self.vectorizer_type == 'tfidf':
            self.vectorizer = TfidfVectorizer(
                max_features=5000, 
                ngram_range=(1, 2),
                min_df=2,
                max_df=0.8
            )
        else:  
            self.vectorizer = CountVectorizer(
                max_features=5000, 
                ngram_range=(1, 2),
                min_df=2,
                max_df=0.8
            )
        
        X_train_vec = self.vectorizer.fit_transform(X_train)
        X_test_vec = self.vectorizer.transform(X_test)
        print(f"  Feature shape: {X_train_vec.shape}")
        
        print(f"\n Training {self.classifier_type.replace('_', ' ').title()} classifier...")
        if self.classifier_type == 'logistic':
            self.model = LogisticRegression(
                max_iter=2000, 
                random_state=42,
                class_weight='balanced',
                C=1.0
            )
        else:  
            self.model = MultinomialNB(alpha=0.5)
        
        self.model.fit(X_train_vec, y_train)
        print(f"  Model trained: {self.model.__class__.__name__}")
        
        y_pred = self.model.predict(X_test_vec)
        accuracy = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        
        print("\n" + "="*60)
        print(" MODEL EVALUATION RESULTS")
        print("="*60)
        print(f" Accuracy:  {accuracy:.4f}")
        print(f" F1 Score:  {f1:.4f}")
        print("\n Classification Report:")
        print(classification_report(y_test, y_pred, target_names=['Negative (0)', 'Positive (1)']))
        print("="*60)
        
        return X_test_vec, y_test
    
    def predict(self, text):
        """
        Predict sentiment for a single text
        
        Args:
            text: Input text string
            
        Returns:
            Dictionary with prediction results
        """
        if self.model is None or self.vectorizer is None:
            raise ValueError("Model not trained yet! Please train the model first.")
        
        cleaned = self.preprocess_text(text)
        
        vectorized = self.vectorizer.transform([cleaned])
        
        pred = self.model.predict(vectorized)[0]
        prob = self.model.predict_proba(vectorized)[0]
        
        feature_names = self.vectorizer.get_feature_names_out()
        
        return {
            'text': text,
            'cleaned': cleaned,
            'sentiment': 'Positive' if pred == 1 else 'Negative',
            'confidence': max(prob),
            'prob_negative': prob[0],
            'prob_positive': prob[1]
        }
    
    def save_model(self, path='sentiment_model.pkl'):
        """Save trained model and vectorizer to disk"""
        if self.model is None or self.vectorizer is None:
            raise ValueError("Model not trained yet!")
        
        model_data = {
            'model': self.model,
            'vectorizer': self.vectorizer,
            'vectorizer_type': self.vectorizer_type,
            'classifier_type': self.classifier_type
        }
        joblib.dump(model_data, path)
        print(f"Model saved to {path}")
    
    def load_model(self, path='sentiment_model.pkl'):
        """Load trained model and vectorizer from disk"""
        if not os.path.exists(path):
            raise FileNotFoundError(f"Model file '{path}' not found")
        
        model_data = joblib.load(path)
        self.model = model_data['model']
        self.vectorizer = model_data['vectorizer']
        self.vectorizer_type = model_data.get('vectorizer_type', 'tfidf')
        self.classifier_type = model_data.get('classifier_type', 'logistic')
        print(f"Model loaded from {path}")


def list_csv_files():
    """List all CSV files in current directory"""
    csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]
    if csv_files:
        print("\nCSV files found in current directory:")
        for i, file in enumerate(csv_files, 1):
            size = os.path.getsize(file) / 1024  #KB
            print(f"  {i}. {file} ({size:.1f} KB)")
        return csv_files
    else:
        print("\nNo CSV files found in current directory")
        return []


def main():
    print("="*60)
    print("SENTIMENT ANALYSIS TOOL")
    print("="*60)
    print("Requirements: Load data → Preprocess → Vectorize → Train → Evaluate → CLI")
    print("="*60)
    
    csv_files = list_csv_files()
    
    print("\nCONFIGURATION:")
    print("-"*60)
    
    print("\n1. Vectorizer Type:")
    print("   [1] TF-IDF ")
    print("   [2] Count Vectorizer")
    vec_choice = input("   Choose (1-2, default=1): ").strip()
    vectorizer_type = 'tfidf' if vec_choice in ['', '1'] else 'count'
    
    print("\n2. Classifier Type:")
    print("   [1] Logistic Regression")
    print("   [2] Naive Bayes")
    cls_choice = input("   Choose (1-2, default=1): ").strip()
    classifier_type = 'logistic' if cls_choice in ['', '1'] else 'naive_bayes'
    
    print(f"\nUsing: {vectorizer_type.upper()} + {classifier_type.replace('_', ' ').title()}")
    
    analyzer = SentimentAnalyzer(
        vectorizer_type=vectorizer_type,
        classifier_type=classifier_type
    )
    \
    print("\n" + "-"*60)
    print("DATA SOURCE OPTIONS:")
    print("   [1] Use large sample data (400+ samples, recommended)")
    print("   [2] Load CSV file from current directory")
    print("   [3] Load CSV file from specific path")
    print("-"*60)
    
    choice = input("\nChoose (1-3, default=1): ").strip()
    
    df = None
    
    if choice == '2' and csv_files:
        print("\nAvailable CSV files:")
        for i, file in enumerate(csv_files, 1):
            print(f"  {i}. {file}")
        
        file_num = input(f"\nSelect file number (1-{len(csv_files)}): ").strip()
        try:
            file_idx = int(file_num) - 1
            if 0 <= file_idx < len(csv_files):
                filepath = csv_files[file_idx]
                df = analyzer.load_csv_data(filepath)
            else:
                print("Invalid selection. Using sample data.")
        except:
            print("Invalid input. Using sample data.")
    
    elif choice == '3':
        filepath = input("\nEnter full path to CSV file: ").strip()
        if os.path.exists(filepath):
            df = analyzer.load_csv_data(filepath)
        else:
            print(f"File not found: {filepath}")
            print("Using sample data...")
    
    if df is None:
        print("\nUsing large sample data (400+ samples)...")
        df = analyzer.create_large_sample_data()
    
    if df is not None and len(df) > 0:
        analyzer.train(df)
        
        save = input("\nSave model for future use? (y/n, default=n): ").lower()
        if save == 'y':
            analyzer.save_model()
        
        print("\n" + "="*60)
        print("INTERACTIVE SENTIMENT ANALYSIS CLI")
        print("="*60)
        print("Commands:")
        print("  • Type any text to analyze sentiment")
        print("  • 'exit'  - Quit the application")
        print("  • 'stats' - Show model information")
        print("  • 'save'  - Save the current model")
        print("="*60)
        
        while True:
            try:
                text = input("\nEnter text: ").strip()
                
                if text.lower() == 'exit':
                    print("\nGoodbye!")
                    break
                elif text.lower() == 'stats':
                    print(f"\nModel Statistics:")
                    print(f"  Classifier: {classifier_type.replace('_', ' ').title()}")
                    print(f"  Vectorizer: {vectorizer_type.upper()}")
                    print(f"  Features: {len(analyzer.vectorizer.get_feature_names_out())}")
                    continue
                elif text.lower() == 'save':
                    analyzer.save_model()
                    continue
                elif text == '':
                    continue
                
                result = analyzer.predict(text)
                
                print("\n" + "-"*50)
                print("ANALYSIS RESULT")
                print("-"*50)
                print(f"Text: {result['text']}")
                print(f"Cleaned: {result['cleaned']}")
                print(f"Sentiment: {result['sentiment']}")
                print(f"Confidence: {result['confidence']:.3f}")
                print(f"Positive: {result['prob_positive']:.3f} | Negative: {result['prob_negative']:.3f}")
                print("-"*50)
                
            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")
    
    else:
        print("No data available to train the model.")


if __name__ == "__main__":
    main()