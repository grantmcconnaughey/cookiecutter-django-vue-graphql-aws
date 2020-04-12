# Django + Vue + GraphQL + AWS Cookiecutter

A _highly_ opinionated [cookiecutter](https://github.com/cookiecutter/cookiecutter) template that fuses together Django, Vue.js, GraphQL, and AWS into one full-stack web application.

## Features

- Backend
  - [Python 3.7](https://www.python.org/)
  - [Django 2.2 LTS](https://www.djangoproject.com/)
  - [GraphQL](https://graphql.org/)
  - [Postgres](https://www.postgresql.org/)
- Frontend
  - [ES6](http://es6-features.org/#Constants)
  - [Vue.js](https://vuejs.org/)
  - [Apollo](https://vue-apollo.netlify.com/)
- Deployment
  - [AWS](https://aws.amazon.com/)
    - Lambda
    - S3
    - CloudFront
    - RDS
    - VPC w/ public and private subnets, NAT Gateway, and more
  - [Zappa](https://github.com/Miserlou/Zappa/) (packaging and deployment to AWS Lambda)
  - [CDK](https://aws.amazon.com/cdk/) (infrastructure-as-code scripting)
  - [Sentry](https://sentry.io/) (error monitoring)

Originally based on [cookiecutter-django-vue](https://github.com/vchaptsev/cookiecutter-django-vue) and extracted from the Reddit scheduling application [Postpone](https://www.postpone.app).

## Usage

First, get `cookiecutter`:

    $ pip install cookiecutter

Now run it against this repo:

    $ cookiecutter gh:grantmcconnaughey/cookiecutter-django-vue-graphql-aws

You'll be prompted for some values. Provide them, then a project
will be created for you.

Now you can start the project with
[docker-compose](https://docs.docker.com/compose/):

    $ docker-compose up --build

Open http://0.0.0.0:8000 in your browser to view the application.
