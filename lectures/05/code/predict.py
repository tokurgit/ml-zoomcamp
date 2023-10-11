import pickle

model_file = 'model_C1.0.bin'

# %% [markdown]
# # Load the model
# `pickle` is a built-in Python library for saving Python objects

# %%

# %%

# %%
# Open model_file and instruct that we will "rb" = Read Bytes
with open(model_file, "rb") as f_in:
    # Need also DictVectorizer, otherwise won't be able to translate a customer to feature matrix
    dv, model = pickle.load(f_in)

# %%
dv, model

# %%
customer = {
    'gender': 'female',
    'seniorcitizen': 0,
    'partner': 'yes',
    'dependents': 'no',
    'phoneservice': 'no',
    'multiplelines': 'no_phone_service',
    'internetservice': 'dsl',
    'onlinesecurity': 'no',
    'onlinebackup': 'yes',
    'deviceprotection': 'no',
    'techsupport': 'no',
    'streamingtv': 'no',
    'streamingmovies': 'no',
    'contract': 'month-to-month',
    'paperlessbilling': 'yes',
    'paymentmethod': 'electronic_check',
    'tenure': 1,
    'monthlycharges': 29.85,
    'totalcharges': 29.85
}

# %%
X = dv.transform([customer])

# %%
# Get row 0, col 1 - the positive probability (that will churn)
y_pred = model.predict_proba(X)[0,1]
print("input", customer)
print("churn probability", y_pred)