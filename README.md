https://www.kaggle.com/datasets/maricinnamon/harry-potter-movies-dataset
https://www.kaggle.com/datasets/electroclashh/harry-potter-dataset?resource=download&select=Spells.csv

Data
* spells
* characters
* places
* dialogue


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

Project Steps
1. Build docker image
2. Run docker image to verify it works
3. Launch ECR Stack
4. Push docker image to ECR
5. Verify docker image is in ECR

CDK Best Practices 
Separation of concerns: It allows you to manage network security separately from your application deployment.
Reusability: You can use the same security group for multiple environments or applications if needed.
Easier troubleshooting: It simplifies the Elastic Beanstalk stack, making it easier to identify and resolve issues.
Flexibility: You can modify the security group independently of your Elastic Beanstalk deployments.

Shiny App Completion
1. Add links to stuff for sidebar nav
2. Address Todos in all analysis
3. Add CSS and make pretty and see to add images of characters (https://colorhunt.co/palette/8cb9bdfefbf6ecb159b67352)
4. Update to read data from S3
5. Implement CICD