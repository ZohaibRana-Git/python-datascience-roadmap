# ============================================================
# Phase 7 | Topic 1: Neural Network Basics
# ============================================================
# TensorFlow/Keras se simple neural network banao
# pip install tensorflow
# ============================================================

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

np.random.seed(42)

# ─────────────────────────────────────────
# 1. Neural Network from Scratch (concept)
# ─────────────────────────────────────────
print("=== Neural Network Concept ===")

def sigmoid(x):
    """Activation function: 0 to 1 ke beech value deta hai."""
    return 1 / (1 + np.exp(-x))

def relu(x):
    """ReLU: negative values 0 kar deta hai."""
    return np.maximum(0, x)

# Single neuron
inputs  = np.array([0.5, 0.8, 0.2])
weights = np.array([0.4, 0.6, 0.3])
bias    = 0.1

weighted_sum = np.dot(inputs, weights) + bias
output_sigmoid = sigmoid(weighted_sum)
output_relu    = relu(weighted_sum)

print(f"Inputs  : {inputs}")
print(f"Weights : {weights}")
print(f"Bias    : {bias}")
print(f"Weighted sum : {weighted_sum:.4f}")
print(f"Sigmoid output: {output_sigmoid:.4f}")
print(f"ReLU output   : {output_relu:.4f}")

# ─────────────────────────────────────────
# 2. Keras Neural Network
# ─────────────────────────────────────────
print("\n=== Keras Neural Network ===")

try:
    import tensorflow as tf
    from tensorflow import keras

    print(f"TensorFlow version: {tf.__version__}")

    # Dataset: binary classification
    n = 1000
    X = np.random.randn(n, 4)
    y = ((X[:, 0] + X[:, 1] - X[:, 2]) > 0).astype(int)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test  = scaler.transform(X_test)

    # Model define karo
    model = keras.Sequential([
        keras.layers.Dense(16, activation="relu", input_shape=(4,)),  # hidden layer 1
        keras.layers.Dense(8,  activation="relu"),                     # hidden layer 2
        keras.layers.Dropout(0.2),                                     # overfitting rokne ke liye
        keras.layers.Dense(1,  activation="sigmoid")                   # output layer
    ])

    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )

    print("\nModel Summary:")
    model.summary()

    # Train
    history = model.fit(
        X_train, y_train,
        epochs=20,
        batch_size=32,
        validation_split=0.1,
        verbose=0
    )

    # Evaluate
    loss, acc = model.evaluate(X_test, y_test, verbose=0)
    print(f"\nTest Accuracy : {acc:.4f}")
    print(f"Test Loss     : {loss:.4f}")

    # Training history
    print(f"\nTraining History (last 5 epochs):")
    print(f"  {'Epoch':>6}  {'Loss':>8}  {'Accuracy':>10}  {'Val Loss':>10}  {'Val Acc':>10}")
    for i in range(-5, 0):
        e   = len(history.history['loss']) + i + 1
        l   = history.history['loss'][i]
        a   = history.history['accuracy'][i]
        vl  = history.history['val_loss'][i]
        va  = history.history['val_accuracy'][i]
        print(f"  {e:>6}  {l:>8.4f}  {a:>10.4f}  {vl:>10.4f}  {va:>10.4f}")

except ImportError:
    print("TensorFlow install nahi hai.")
    print("Run: pip install tensorflow")
    print("\nConcept samajh lo:")
    print("  Input → [Dense(16, relu)] → [Dense(8, relu)] → [Dense(1, sigmoid)] → Output")
    print("  model.compile(optimizer='adam', loss='binary_crossentropy')")
    print("  model.fit(X_train, y_train, epochs=20)")
    print("  model.evaluate(X_test, y_test)")
