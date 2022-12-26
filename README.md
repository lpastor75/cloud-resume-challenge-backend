## Cloud Resume Challenge Backend

This repo contains the backend services infrastructure needed for the [Cloud resume challenge](https://cloudresumechallenge.dev/). It is deployed using the [Serverless Framework](https://www.serverless.com/framework/docs/providers/aws/guide/intro/). It deploys an API Gateway which invokes a Lambda function. The Lambda function increments by 1 and retrieves the number of visitors to the website from DynamoDB. A GitHub Actions pipeline tracks changes in the repo, runs tests and deploys the stack. 

For frontend code, visit [Cloud Resume Frontend](https://github.com/lpastor75/cloud-resume).
