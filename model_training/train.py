import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import os

def generate_dummy_data(num_samples=1000):
    np.random.seed(42)
    data = {
        'feature1': np.random.rand(num_samples),
        'feature2': np.random.rand(num_samples),
        'feature3': np.random.rand(num_samples),
        'target': np.random.randint(0, 2, num_samples)
    }
    df = pd.DataFrame(data)
    return df

def train_model():
    print("Starting model training...")
    df = generate_dummy_data()
    X = df[['feature1', 'feature2', 'feature3']]
    y = df['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression(solver='liblinear', random_state=42)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Model trained with accuracy: {accuracy:.4f}")

    # Save the model
    model_dir = "./trained_model"
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "model.joblib")
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train_model()
