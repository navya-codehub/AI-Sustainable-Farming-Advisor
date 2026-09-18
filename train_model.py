import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# ---------------------------------------------------------
# LOAD DATASET
# ---------------------------------------------------------

df = pd.read_csv("Crop_recommendation.csv")

print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)

# ---------------------------------------------------------
# FEATURES AND TARGET
# ---------------------------------------------------------

features = [
    "N",
    "P",
    "K",
    "temperature",
    "humidity",
    "ph",
    "rainfall"
]

target = "label"

X = df[features]
y = df[target]

# ---------------------------------------------------------
# SPLIT DATA
# ---------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("Training records:", len(X_train))
print("Testing records:", len(X_test))

# ---------------------------------------------------------
# TRAIN RANDOM FOREST MODEL
# ---------------------------------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("Model training completed!")

# ---------------------------------------------------------
# PREDICTION
# ---------------------------------------------------------

y_pred = model.predict(X_test)

# ---------------------------------------------------------
# MODEL EVALUATION
# ---------------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ---------------------------------------------------------
# SAVE MODEL
# ---------------------------------------------------------

joblib.dump(model, "crop_recommendation_model.pkl")

print("\nModel saved successfully!")
print("File: crop_recommendation_model.pkl")