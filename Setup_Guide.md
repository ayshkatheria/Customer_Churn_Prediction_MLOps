**STEP 1 — Initialize Git + DVC**
```
Initialize Git:
  git init
```

```
Initialize DVC:
  dvc init
```
```
Commit initial setup:
   git add .
   git commit -m "Initialize Git and DVC"
```
<img width="916" height="242" alt="image" src="https://github.com/user-attachments/assets/c5287bbb-7925-4670-9703-f3490a756f9b" />


**STEP 2 — Create Synthetic Dataset**
```
Create:
  src/generate_data.py
```
**Add:**
```
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
```
**Run:**
```
mkdir data
python src/generate_data.py
```
**Verify:**
```
ls data

Output: churn.csv
```
<img width="1037" height="117" alt="image" src="https://github.com/user-attachments/assets/09c9a792-0d07-445b-9b63-ef6eeb55b62b" />
