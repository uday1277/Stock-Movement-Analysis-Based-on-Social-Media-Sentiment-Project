import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_model():
    """Train machine learning model."""
    # Load data
    df = pd.read_csv(r"C:\Users\Administrator\Downloads\StockMovementPrediction\data\processed_data1.csv")
    
    # Prepare features and labels
    X = df[['Sentiment']]  # Feature: Sentiment score
    y = df['Label']  # Labels: 1 for positive, 0 for negative sentiment
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train Random Forest model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    # Evaluate model with a test set
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy on Test Set: {accuracy}")
    
    # Evaluate model using cross-validation (this will give a more reliable estimate)
    cross_val_accuracy = cross_val_score(model, X, y, cv=5, scoring='accuracy')
    print(f"Cross-validation Accuracy: {cross_val_accuracy.mean()}")
    
    return model

if __name__ == "__main__":
    train_model()
