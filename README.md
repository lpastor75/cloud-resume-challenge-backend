# ⚙️ Cloud Resume Challenge — Backend & IaC

🌐 **[Live Demo (luispastor.dev)](https://luispastor.dev)** &nbsp;|&nbsp; 💻 **[Frontend Repository](https://github.com/lpastor75/cloud-resume)** &nbsp;|&nbsp; 📝 **[Architecture Blog Post](https://blog.luispastor.dev/the-cloud-resume-challenge-aws)**

Serverless backend API, unit tests, and **Infrastructure as Code (IaC)** for Forrest Brazeal's [Cloud Resume Challenge](https://cloudresumechallenge.dev/). All cloud resources on AWS are provisioned and managed declaratively using the **Serverless Framework** and **AWS CloudFormation**, with automated testing and deployment via **GitHub Actions**.

---

## 🏗️ Backend Architecture & Flow

1. **API Endpoint (`Amazon API Gateway`):** Exposes a CORS-enabled REST API (`GET /counter`) that receives asynchronous requests from the frontend portfolio.
2. **Serverless Compute (`AWS Lambda`):** Executes a **Python 3.9** function triggered by API Gateway, operating under a least-privilege **AWS IAM** execution role.
3. **NoSQL Persistence (`Amazon DynamoDB`):** Atomically increments (`UpdateItem` with `ADD`) and retrieves the total visitor count stored in an on-demand DynamoDB table.
4. **Infrastructure as Code (`Serverless Framework` & `CloudFormation`):** The `serverless.yml` manifest and modular CloudFormation templates (`resources/`) define and deploy the entire AWS stack (API Gateway, Lambda, DynamoDB, IAM roles, S3 bucket policies, CloudFront distribution, ACM SSL certificate, and Route 53 DNS records).
5. **Automated Testing & CI/CD (`GitHub Actions`):** Pushing changes to the `main` branch triggers a workflow (`.github/workflows/`) that runs Python unit tests before deploying the updated stack via `serverless deploy`.

---

## 🛠️ Tech Stack

* **Language & Runtime:** Python 3.9 (`boto3`)
* **AWS Services:** API Gateway, Lambda, DynamoDB, IAM, CloudFormation, S3, CloudFront, Route 53, ACM
* **Infrastructure as Code (IaC):** Serverless Framework (`serverless.yml`)
* **Testing:** Python `unittest` / Mocking (`moto` / `unittest.mock`)
* **CI/CD Pipeline:** GitHub Actions

---

## 📂 Repository Structure

```text
├── .github/workflows/   # GitHub Actions CI/CD pipeline (testing & serverless deploy)
├── lambda_function/     # Python Lambda handler for atomic DynamoDB visitor counter
├── resources/           # Modular AWS CloudFormation resource & output definitions
├── test/                # Unit tests for Lambda handler logic
├── package.json         # Serverless Framework plugins & Node.js dependencies
├── serverless.yml       # Main Infrastructure as Code (IaC) configuration
└── README.md            # Project documentation
```

---

## 🚀 Local Testing & Deployment

### Run Unit Tests
```bash
python -m unittest discover -s test
```

### Deploy Stack to AWS
```bash
npm install
serverless deploy --stage prod
```

---

## 🔗 Related Resources

* 🌐 **Live Portfolio:** [luispastor.dev](https://luispastor.dev)
* 💻 **Frontend & Static Hosting Repository:** [lpastor75/cloud-resume](https://github.com/lpastor75/cloud-resume)
* 📝 **Detailed Technical Walkthrough (Spanish):** [The Cloud Resume Challenge - AWS](https://blog.luispastor.dev/the-cloud-resume-challenge-aws)
