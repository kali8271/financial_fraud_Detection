def predict_input(model, input_data):
    return model.predict(input_data), model.predict_proba(input_data)[:, 1]