```text

         ,.  '          .-,             ,'´¨';'        ,·'´¨;.  '                          , ·. ,.-·~·.,   ‘                 ,. -,    
       /   ';\          ;  ';\          ,'   ';'\'      ;   ';:\           .·´¨';\         /  ·'´,.-·-.,   `,'‚           ,.·'´,    ,'\   
     ,'   ,'::'\        ';   ;:'\        ,'   ,'::'\    ;     ';:'\      .'´     ;:'\       /  .'´\:::::::'\   '\ °     ,·'´ .·´'´-·'´::::\' 
    ,'    ;:::';'       ';  ';::';      ,'   ,'::::;    ;   ,  '·:;  .·´,.´';  ,'::;'    ,·'  ,'::::\:;:-·-:';  ';\‚    ;    ';:::\::\::;:'  
    ';   ,':::;'        ';  ';::;     ,'   ,'::::;'    ;   ;'`.    ¨,.·´::;'  ;:::;    ;.   ';:::;´       ,'  ,':'\‚   \·.    `·;:'-·'´     
    ;  ,':::;' '        ';  ';::;    ,'   ,'::::;'     ;  ';::; \*´\:::::;  ,':::;‘     ';   ;::;       ,'´ .'´\::';‚   \:`·.   '`·,  '     
   ,'  ,'::;'            \   '·:_,'´.;   ;::::;‘    ';  ,'::;   \::\;:·';  ;:::; '     ';   ':;:   ,.·´,.·´::::\;'°     `·:'`·,   \'      
   ;  ';_:,.-·´';\‘      \·,   ,.·´:';  ';:::';     ;  ';::;     '*´  ;',·':::;‘        \·,   `*´,.·'´::::::;·´         ,.'-:;'  ,·\     
   ',   _,.-·'´:\:\‘      \:\¯\:::::\`*´\::;  '   \´¨\::;          \¨\::::;          \\:¯::\:::::::;:·´       ,·'´     ,.·´:::'\    
    \¨:::::::::::\';        `'\::\;:·´'\:::'\'   '    '\::\;            \:\;·'            `\:::::\;::·'´  °         \`*'´\::::::::;·'‘   
     '\;::_;:-·'´‘                      `*´°         '´¨               ¨'                  ¯                     \::::\:;:·´        
       '¨                                '                                                  ‘                       '`*'´‘            

```

## Table of Contents
* [Overview](#overview)
* [Dependencies](#dependencies)
* [File Structure](#file-structure)
* [Data](#data)
* [Preliminary Steps](#preliminary-steps)
  * [AWS](#aws)
  * [Docker](#docker)
  * [Shiny](#shiny)
* [Getting Started](#getting-started)
  * [CDK](#cdk)
  * [Shiny](#shiny-1)
* [Deployment](#deployment)
* [Best Practices](#best-practices)
* [Resources](#resources)

## Overview
![](lumos_architecture.png)

## Dependencies
* AWS Account
* Docker 
* Python (v3.8)
* 
## File Structure
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


## Data
https://www.kaggle.com/datasets/maricinnamon/harry-potter-movies-dataset
https://www.kaggle.com/datasets/electroclashh/harry-potter-dataset?resource=download&select=Spells.csv
Data
* spells
* characters
* places
* dialogue
## Preliminary Steps
### AWS
### Docker
### Shiny
## Getting Started
### CDK
### Shiny
## Deployment
## Best Practices
CDK Best Practices 
Separation of concerns: It allows you to manage network security separately from your application deployment.
Reusability: You can use the same security group for multiple environments or applications if needed.
Easier troubleshooting: It simplifies the Elastic Beanstalk stack, making it easier to identify and resolve issues.
Flexibility: You can modify the security group independently of your Elastic Beanstalk deployments.
## Resources
* https://colorhunt.co/palette/8cb9bdfefbf6ecb159b67352




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