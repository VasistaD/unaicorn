def fake_predict(user_age):
    if user_age > 10:
        prediction = "Survived"
    else:
        prediction = "Super Survive"
    return prediction
