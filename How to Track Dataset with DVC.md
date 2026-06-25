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
**Important Concept**
```
Git tracks:
     churn.csv.dvc
```
**NOT the actual CSV file.**
**The actual data will go to S3.**
