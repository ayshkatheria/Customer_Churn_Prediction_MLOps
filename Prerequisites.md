**------------------------------------------📋 Prerequisites----------------------------------------------------**

**1. Install Python**
```
Install Python 3.10+

Verify:
 python --version
```
**2. Install Git**
```
Verify:
 git --version
```
**3. Install AWS CLI**
```
Verify:
 aws --version
```
**4. Create AWS Account**
**5. Configure AWS Credentials**
```
aws configure

Provide:

 - AWS Access Key
 - AWS Secret Key
 - Region

Test:

  aws s3 ls
```

**---------------------------------------📦 Install Required Packages------------------------------------------------**

**Create project folder:**
```
mkdir customer-churn-mlops
cd customer-churn-mlops
```

**Create virtual environment:**
```
python -m venv venv
```

**Activate:**
```
source venv/bin/activate
```

**Install packages:**
```
pip install pandas scikit-learn dvc[s3] jupyter
```


