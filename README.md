```text

       ,gggg,                                                  
      d8" "8I                                                  
      88  ,dP                                                  
   8888888P"                                                   
      88                                                       
      88       gg      gg  ,ggg,,ggg,,ggg,    ,ggggg,   ,g,    
 ,aa,_88       I8      8I ,8" "8P" "8P" "8,  dP"  "Y8gg,8'8,   
dP" "88P       I8,    ,8I I8   8I   8I   8I i8'    ,8I,8'  Yb  
Yb,_,d88b,,_  ,d8b,  ,d8b,dP   8I   8I   Yb,d8,   ,d8,8'_   8) 
 "Y8P"  "Y88888P'"Y88P"`Y8P'   8I   8I   `YP"Y8888P" P' "YY8P8P
                                                              
```

<p align="center">

![GitHub Stars](https://img.shields.io/github/stars/thestrugglingblack/lumos?style=plastic)
![GitHub Last Commit](https://img.shields.io/github/last-commit/thestrugglingblack/lumos?style=plastic)
![GitHub Commit Activity](https://img.shields.io/github/commit-activity/m/thestrugglingblack/lumos.svg)
![GitHub Repository Size](https://img.shields.io/github/repo-size/thestrugglingblack/lumos?style=plastic)
</p>

## 📍Table of Contents
* 👋 [Overview](#overview)
* ✅ [Dependencies](#dependencies)
* 🌵 [File Structure](#file-structure)
* 💾 [Data](#data)
* 🏃 [Preliminary Steps](#preliminary-steps)
  * [AWS](#aws)
  * [Docker](#docker)
  * [Shiny](#shiny)
* 🚀 [Getting Started](#getting-started)
  * [CDK](#cdk)
  * [Shiny](#shiny-1)
* 🛠 [Deployment](#deployment)
* 🔑 [Best Practices](#best-practices)
* 📑 [Resources](#resources)

## 👋 Overview
![](lumos_architecture.png)
[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/zuri-hunter-748ba514)
[![Twitter Badge](https://img.shields.io/badge/Twitter-1DA1F2?style=flat&logo=twitter&logoColor=white)](https://x.com/ZuriHunter)
[![GitHub Badge](https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white)](https://github.com/thestrugglingblack)

## ✅ Dependencies
* AWS Account
* Docker 
* Python (v3.8)
* Node.js (v22)
* NVM

## 🌵 File Structure
```text
.
├── Dockerfile
├── cdk
│   ├── README.md
│   ├── app.py
│   ├── lumos
│   │   ├── auth
│   │   ├── compute
│   │   ├── network
│   │   ├── storage
│   │   ├── tools
│   │   └── utils
└── shiny
```


## 💾 Data
The Lumos application uses data from these two free Kaggle Datasets: [Harry Potter Movies Dataset](https://www.kaggle.com/datasets/maricinnamon/harry-potter-movies-dataset) and [Harry Potter Dataset Spells](https://www.kaggle.com/datasets/electroclashh/harry-potter-dataset?resource=download&select=Spells.csv)
The data consist of the entire script, characters, places and spells for all of 8 movies of the Harry Potter series. 

##  🏃 Preliminary Steps

### AWS
#### Install AWS-CDK Globally
> Note: Node.js and NVM must be installed to run this step.

1. Run `nvm use` to point to Node v22.
2. Run `npm install -g aws-cdk` to install AWS-CDK globally.
3. Run `cdk --version` to verify that AWS-CDK installed successfully.

#### Configure AWS Account Permissions

#### Create .env file
1. Create a file called `.env` at the root of the directory.
2. Copy the contents of `.env.template` into the newly created `.env` file.
3. Add your `AWS_ACCOUNT_ID` to the `.env.` This is needed for aws-cdk to know which AWS account to deploy resources to.

### Docker
### Shiny
## 🚀 Getting Started
### CDK

### Shiny
To run the application on local machine


To run the application with Docker
## 🛠 Deployment
There are series of steps for deploying this application. The first step is establishing the base resources before placing the application in its environment.

Deploy the that is going to hold all version of the Lumos application Docker images: Elastic Container Registry (ECR). 
```bash
$ cdk deploy EcrStack
```
> Note: This is a command that will only need to ran once.

Deploy the storage layer, this is where the Lumos application will know where to download the `*.csv` files to run analysis.
```bash
$ cdk deploy S3Stack
```

Deploy the network layer, where the VPC, Security groups and Application Load Balancers are created.

```bash
$ cdk deploy SecurityGroupStack
$ cdk deploy LoadBalancerStack
````

Finally deploy the compute layer which is placing a Fargate EC2 instance within an Elastic Container Service cluster (ECS).
```bash
$ cdk deploy FargateServiceStack
```

To destroy any of the stacks created run `cdk destroy NAME_OF_STACK`, this will remove the stack from the Lumos application architecture on AWS. 

## 🔑 Best Practices
CDK Best Practices 
Separation of concerns: It allows you to manage network security separately from your application deployment.
Reusability: You can use the same security group for multiple environments or applications if needed.
Easier troubleshooting: It simplifies the Elastic Beanstalk stack, making it easier to identify and resolve issues.
Flexibility: You can modify the security group independently of your Elastic Beanstalk deployments.

## 📑 Resources
* [Color Hunt](https://colorhunt.co/palette/8cb9bdfefbf6ecb159b67352)
* [Communicate Between R and Shiny](https://unleash-shiny.rinterface.com/shiny-intro#:~:text=In%20practice%2C%20Shiny%20does%20not,can%20produce%20a%20simple%20histogram.)





ECR AWS login
1. Verify that you have `AmazonEC2ContainerRegistryFullAccess` as a permission for you account. Thats here ` https://console.aws.amazon.com/iam/.`
2. Run to login to ECR
```
 aws ecr get-login-password --region REGION | docker login --username AWS --password-stdin ACCOUNT_ID.dkr.ecr.REGION.amazonaws.com

```
3. Tag the image
```json
 docker tag  wisd24/lumos-shiny-application:latest ACCOUNT_ID.dkr.ecr.REGION.amazonaws.com/wisd24/lumos-shiny-application:latest
```
4. Push the image
```json
docker push ACCOUNT_ID.dkr.ecr.REGION.amazonaws.com/wisd24/lumos-shiny-application:latest
```




TODO
4. Update to read data from S3
5. Implement CICD
6. Setup Logs for container
7. Clean up documentation