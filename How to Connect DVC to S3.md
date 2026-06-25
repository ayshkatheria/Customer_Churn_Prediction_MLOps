**STEP 4 — Create S3 Bucket**

Create bucket:

```
customer-churn-dvc-storage
```
CLI:
```
aws s3 mb s3://customer-churn-dvc-storage
```

**STEP 5 — Connect DVC to S3**

Configure remote:
```
dvc remote add -d myremote s3://customer-churn-dvc-storage
```
Verify:
```
dvc remote list
```
<img width="1453" height="180" alt="image" src="https://github.com/user-attachments/assets/689d9fbb-abcd-40b3-aee7-66a3429cd081" />


Commit configuration:
```
git add .dvc/config
git commit -m "Configure DVC remote"
```

**STEP 6 — Push Dataset to S3**

Now upload data
```
dvc push
```
**DVC uploads dataset into S3.**

Check:
```
aws s3 ls s3://customer-churn-dvc-storage --recursive
```
You’ll see hashed DVC files.

<img width="1473" height="76" alt="image" src="https://github.com/user-attachments/assets/e62ad613-99d1-4d79-829a-6f3d43b0b0eb" />

<img width="1355" height="54" alt="image" src="https://github.com/user-attachments/assets/e7027584-d552-4101-b122-8975040a1eaf" />







