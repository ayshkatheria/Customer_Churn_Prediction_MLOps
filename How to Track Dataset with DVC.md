**STEP 3 — Track Dataset with DVC**

**Run:**
```
dvc add data/churn.csv
```
```
This creates:
data/churn.csv.dvc

DVC now tracks your dataset.
```
<img width="600" height="50" alt="image" src="https://github.com/user-attachments/assets/fc33b7f2-1e5e-4059-95ed-f59daaa81265" />


**Important Concept**
```
Git tracks:
     churn.csv.dvc
```
**NOT the actual CSV file.**
**The actual data will go to S3.**
