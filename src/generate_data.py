import pandas as pd
import numpy as np

np.random.seed(42)

data_size = 1000

df = pd.DataFrame({
    "age": np.random.randint(18, 60, data_size),
    "salary": np.random.randint(30000, 150000, data_size),
    "tenure": np.random.randint(1, 10, data_size),
    "churn": np.random.randint(0, 2, data_size)
})

df.to_csv("data/churn.csv", index=False)

print("Dataset generated successfully!")
