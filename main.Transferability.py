#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# monthly
# train on 2022 - test on 2019

import pandas as pd
import numpy as np# 
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Dropout, MultiHeadAttention, LayerNormalization, Input, Layer
from tensorflow.keras.optimizers import Adam, SGD#
from tensorflow.keras.regularizers import l2
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

# Build Transformer Model for Time Series
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

# Function to create time series sequences
def create_sequences(data, target, seq_length):
    X, y = [], []
    for i in range(len(data) - seq_length):
        X.append(data[i:i+seq_length])
        y.append(target[i+seq_length])
    return np.array(X), np.array(y)

# Evaluate Model with Time Series Sequences
def evaluate_model(X_train, X_test, y_train, y_test):
    start_time = time.time()

    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train.reshape(-1, X_train.shape[-1])).reshape(X_train.shape)
    X_test_scaled = scaler.transform(X_test.reshape(-1, X_test.shape[-1])).reshape(X_test.shape)

    # Build and train the model
    model = build_transformer_model((X_train_scaled.shape[1], X_train_scaled.shape[2]))
    history = model.fit(X_train_scaled, y_train, epochs=config.epochs, batch_size=config.batch_size, validation_split=config.validation_split, verbose=config.verbose_level)

    # Evaluate on the test set
    y_pred = model.predict(X_test_scaled).flatten()

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

# Load the data and create sequences
train_daily_file = '/path/to/combined-pc-counts-monthly-stv2022.csv'
train_static_file = '/path/to/df1-2022.csv'

test_daily_file = '/path/to/combined-pc-counts-monthly-stv2019.csv'
test_static_file = '/path/to/df1-2019.csv'

print(f"Loading training data from: {train_daily_file} and {train_static_file}")
train_data = load_and_merge_datasets(train_daily_file, train_static_file)
train_data.dropna(inplace=True)
train_data = train_data.select_dtypes(exclude='object')

print(f"Loading test data from: {test_daily_file} and {test_static_file}")
test_data = load_and_merge_datasets(test_daily_file, test_static_file)
test_data.dropna(inplace=True)
test_data = test_data.select_dtypes(exclude='object')

# Create time series sequences (for example, sequence length = 12 months)
seq_length = 12

for feature_set_name, features in feature_sets.items():
    available_features = [feature for feature in features if feature in train_data.columns and feature in test_data.columns]
    
    if not available_features:
        print(f"No available features found for {feature_set_name}. Skipping...")
        continue

    X_train = train_data[available_features]
    y_train = train_data[config.target_variable]

    X_test = test_data[available_features]
    y_test = test_data[config.target_variable]

    X_train_seq, y_train_seq = create_sequences(X_train.values, y_train.values, seq_length)
    X_test_seq, y_test_seq = create_sequences(X_test.values, y_test.values, seq_length)

    results, history = evaluate_model(X_train_seq, X_test_seq, y_train_seq, y_test_seq)

    print(f"Results for {feature_set_name}:")
    for metric, score in results.items():
        print(f"{metric}: {score}")
    print()

    if config.show_plots:
        plt.plot(history.history['loss'], label='Training Loss')
        plt.plot(history.history['val_loss'], label='Validation Loss')
        plt.title(f'Training and Validation Loss for {feature_set_name}')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.legend()
        plt.show()

