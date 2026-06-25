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








