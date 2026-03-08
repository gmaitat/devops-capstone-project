# Devops Capstone Project

[![Build Status](https://github.com/gmaitat/devops-capstone-project/actions/workflows/ci-build.yaml/badge.svg)](https://github.com/gmaitat/devops-capstone-project/actions/workflows/ci-build.yaml)

## Overview

This repository contains the code for the **Customer Accounts Microservice** for an e-commerce website. The microservice provides a RESTful API to manage customer account information (names and addresses) with full CRUD operations.

## Scenario

> You have been asked by the customer account manager at your company to develop an account microservice to keep track of the customers on your e-commerce website. Since it is a microservice, it is expected to have a well-formed REST API that other microservices can call. This service initially needs to create, read, update, delete, and list customers.

## Tech Stack

- **Language:** Python 3.9
- **Framework:** Flask
- **Database:** PostgreSQL (via SQLAlchemy)
- **Testing:** nose, coverage
- **Linting:** Flake8, Pylint
- **Containerization:** Docker
- **Orchestration:** Kubernetes / OpenShift
- **CI/CD:** GitHub Actions, Tekton Pipelines

## Project Structure

```
├── .github/
│   ├── ISSUE_TEMPLATE/      # User story templates
│   └── workflows/           # GitHub Actions CI/CD
├── bin/                     # Setup scripts
├── deploy/                  # Kubernetes manifests
├── service/                 # Main microservice package
│   ├── common/              # Error handlers and logging
│   ├── __init__.py
│   ├── config.py            # Flask configuration
│   ├── models.py            # Database models
│   └── routes.py            # REST API routes
├── tekton/                  # Tekton pipeline definitions
├── tests/                   # Unit tests
│   ├── factories.py
│   ├── test_models.py
│   └── test_routes.py
├── Dockerfile
├── Makefile
├── Procfile
├── requirements.txt
└── setup.cfg
```

## REST API Endpoints

| Method | Endpoint | Description | Status Code |
|--------|----------|-------------|-------------|
| POST   | /accounts | Create an account | 201 |
| GET    | /accounts/{id} | Read an account | 200 |
| PUT    | /accounts/{id} | Update an account | 200 |
| DELETE | /accounts/{id} | Delete an account | 204 |
| GET    | /accounts | List all accounts | 200 |

## Development Setup

### Prerequisites

- Python 3.9+
- PostgreSQL
- Docker

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Tests

```bash
nosetests
```

### Start the Service

```bash
flask run
```

## License

Licensed under the Apache License. See [LICENSE](LICENSE) for details.
