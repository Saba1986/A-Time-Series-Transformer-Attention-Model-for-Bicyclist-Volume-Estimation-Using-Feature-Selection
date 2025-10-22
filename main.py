#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Dropout, MultiHeadAttention, LayerNormalization, Input, Layer, TimeDistributed
from tensorflow.keras.optimizers import Adam, SGD
from tensorflow.keras.regularizers import l2
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt
from tensorflow.keras import backend as K
import time
from features import strava_static_features, strava_features, static_features
import config

# GPU Configuration
physical_devices = tf.config.experimental.list_physical_devices('GPU')
if len(physical_devices) > 0:
    tf.config.experimental.set_memory_growth(physical_devices[0], True)

# Attention Layer Definition
class Attention(Layer):
    def __init__(self, **kwargs):
        super(Attention, self).__init__(**kwargs)

    def build(self, input_shape):
        self.W = self.add_weight(name="att_weight", shape=(input_shape[-1], 1), initializer="normal")
        self.b = self.add_weight(name="att_bias", shape=(input_shape[1], 1), initializer="zeros")
        super(Attention, self).build(input_shape)

    def call(self, x):
        e = K.tanh(K.dot(x, self.W) + self.b)
        a = K.softmax(e, axis=1)
        output = x * a
        return K.sum(output, axis=1)

# Transformer Encoder Block for Time Series Data
def build_transformer_model(input_shape):
    inputs = Input(shape=input_shape)

    # Transformer Encoder Layer 1
    attention_output = MultiHeadAttention(num_heads=config.heads, key_dim=input_shape[-1])(inputs, inputs)
    attention_output = Dropout(config.dropout_rate)(attention_output)
    attention_output = LayerNormalization(epsilon=1e-6)(attention_output + inputs)

    # Feed Forward Network (FFN)
    ffn_output = Dense(config.d_ff, activation=config.activation_function)(attention_output)
    ffn_output = Dense(input_shape[-1])(ffn_output)
    ffn_output = Dropout(config.dropout_rate)(ffn_output)
    encoder_output = LayerNormalization(epsilon=1e-6)(ffn_output + attention_output)

    # Optional: Additional Transformer Encoder Layers
    for _ in range(config.n_layers - 1):
        attention_output = MultiHeadAttention(num_heads=config.heads, key_dim=input_shape[-1])(encoder_output, encoder_output)
        attention_output = Dropout(config.dropout_rate)(attention_output)
        attention_output = LayerNormalization(epsilon=1e-6)(attention_output + encoder_output)

        ffn_output = Dense(config.d_ff, activation=config.activation_function)(attention_output)
        ffn_output = Dense(input_shape[-1])(ffn_output)
        ffn_output = Dropout(config.dropout_rate)(ffn_output)
        encoder_output = LayerNormalization(epsilon=1e-6)(ffn_output + attention_output)

    # Attention Layer
    context_vector = Attention()(encoder_output)
    context_vector = Dropout(config.dropout_rate)(context_vector)

    # Dense Layers
    dense_output = Dense(32, activation=config.activation_function, kernel_regularizer=l2(config.l2_reg))(context_vector)
    outputs = Dense(1)(dense_output)

    # Build Model
    model = Model(inputs, outputs)

    # Compile Model
    if config.optimizer_type == 'Adam':
        optimizer = Adam(learning_rate=config.learning_rate, beta_1=config.beta_1, beta_2=config.beta_2)
    elif config.optimizer_type == 'SGD':
        optimizer = SGD(learning_rate=config.learning_rate)
    else:
        raise ValueError(f"Unsupported optimizer type: {config.optimizer_type}")
    
    model.compile(optimizer=optimizer, loss='mse', metrics=['mae'])
    
    return model

# Sliding window function to prepare time series data
def create_sequences(data, target, seq_length):
    X = []
    y = []
    for i in range(len(data) - seq_length):
        X.append(data[i:i + seq_length])
        y.append(target[i + seq_length])
    return np.array(X), np.array(y)

# Function to add noise to the data
def add_noise(X, noise_level=config.noise_level):
    noise = np.random.normal(loc=0, scale=noise_level, size=X.shape)
    X_noisy = X + noise
    return X_noisy

# Evaluate Model for Time Series
def evaluate_model(X_train, X_test, y_train, y_test):
    start_time = time.time()

    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train.reshape(-1, X_train.shape[-1])).reshape(X_train.shape)
    X_test_scaled = scaler.transform(X_test.reshape(-1, X_test.shape[-1])).reshape(X_test.shape)

    # Build and train the model
    model = build_transformer_model((X_train_scaled.shape[1], X_train_scaled.shape[2]))
    history = model.fit(X_train_scaled, y_train, epochs=1000, batch_size=config.batch_size, validation_split=config.validation_split, verbose=config.verbose_level)

    # Evaluate on the test set
    y_pred = model.predict(X_test_scaled).flatten()
    y_test = np.nan_to_num(y_test)
    y_pred = np.nan_to_num(y_pred)

    # Compute metrics
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    prmse = (rmse / np.mean(y_test)) * 100
    mae = mean_absolute_error(y_test, y_pred)
    mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100
    mpe = np.mean((y_test - y_pred) / y_test) * 100
    r2 = r2_score(y_test, y_pred)

    end_time = time.time()
    
    results = {
        "RMSE": rmse,
        "PRMSE": prmse,
        "MAE": mae,
        "MAPE": mape,
        "MPE": mpe,
        "R²": r2,
        "Training Time": end_time - start_time
    }
    
    return results, history

# Load and merge datasets
def load_and_merge_datasets(monthly_file_path, static_file_path):
    monthly_data = pd.read_csv(monthly_file_path)
    static_data = pd.read_csv(static_file_path)
    
    # Merging on 'site_id'
    merged_data = pd.merge(monthly_data, static_data, on='site_id', suffixes=('_monthly', '_static'))
    
    return merged_data

# Process datasets
for (monthly_file, annual_file) in [(config.data_file_path_2019, '/Users/sabai/Desktop/data/static/df1-2019.csv'),
                                    (config.data_file_path_2022, '/Users/sabai/Desktop/data/static/df1-2022.csv')]:
    print(f"Processing datasets: {monthly_file} and {annual_file}")
    
    data = load_and_merge_datasets(monthly_file, annual_file)
    
    # Drop rows with NaN values
    data.dropna(inplace=True)
    
    # Print the available columns in the dataset
    print("Available columns in the merged dataset after dropping NaNs:")
    print(data.columns)
    
    data = data.select_dtypes(exclude='object')

    feature_sets = {
        'Strava + Static Features': strava_static_features,
        'Strava Features': strava_features,
        'Static Features': static_features
    }

    y = data[config.target_variable]
    y.fillna(y.median(), inplace=True)

    # Create time series data using sliding windows
    for feature_set_name, features in feature_sets.items():
        # Select only the features that are present in the dataset
        available_features = [feature for feature in features if feature in data.columns]
        
        print(f"\nEvaluating model with {feature_set_name} on the whole data...")
        if not available_features:
            print(f"No available features found for {feature_set_name}. Skipping...")
            continue

        X = data[available_features]

        # Create sequences for time series forecasting
        seq_length = config.seq_length
        X_seq, y_seq = create_sequences(X.values, y.values, seq_length)

        # Split the dataset into 80% train and 20% test
        X_train, X_test, y_train, y_test = train_test_split(X_seq, y_seq, test_size=0.2, random_state=42)

        # Augment the training data with noise
        X_train_augmented = np.vstack([X_train, add_noise(X_train)])
        y_train_augmented = np.hstack([y_train, y_train])

        # Evaluate the model
        results, history = evaluate_model(X_train_augmented, X_test, y_train_augmented, y_test)

        print(f"Results for {feature_set_name} - Whole Data:")
        for metric, score in results.items():
            print(f"{metric}: {score}")
        print()

        if config.show_plots:
            plt.plot(history.history['loss'], label='Training Loss')
            plt.plot(history.history['val_loss'], label='Validation Loss')
            plt.title(f'Training and Validation Loss for {feature_set_name} - Whole Data')
            plt.xlabel('Epoch')
            plt.ylabel('Loss')
            plt.legend()
            plt.show()

