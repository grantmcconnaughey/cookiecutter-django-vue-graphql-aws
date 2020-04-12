# {{cookiecutter.project_name}}

<a href="https://github.com/grantmcconnaughey/cookiecutter-django-vue-graphql-aws">
    <img src="https://img.shields.io/badge/built%20with-Django%20Vue%20GraphQL%20AWS%20Cookiecutter-blue.svg" />
</a>

## Development

Install [Docker](https://docs.docker.com/install/) and [Docker-Compose](https://docs.docker.com/compose/). Start your virtual machines with the following shell command:

`docker-compose up --build`

If all works well, you should be able to create an admin account with:

`docker-compose run backend python manage.py createsuperuser`

## Testing

### E-mail

View sent e-mails in Mailgun.

http://0.0.0.0:8025

## Deployment

Deployment occurs in a series of steps. Some deployment steps do not need to be performed very often.

At a high-level, the steps are:

1. Deploy VPC and RDS (once)
2. Deploy frontend (as-needed)
3. Deploy backend (as-needed)

### Deploying with CDK

First, install the CDK dependencies:

- `npm install -g aws-cdk`
- `cd deploy`
- `pip install -r deploy/requirements.txt`

Next, deploy using `cdk`.

- `cdk deploy {{cookiecutter.project_slug}}-networking-db`
- `cdk deploy {{cookiecutter.project_slug}}-frontend`

### Deploying the backend

Update the backend Lambda instance by running the following commands:

- `cd backend`
- `source .venv/bin/activate`
- `pip install -r requirements/deploy.txt`
- `zappa update prod`

You'll also want to perform some post-deployment tasks:

- Migrate the DB: `zappa manage prod migrate`
- Build static files and copy to S3: `zappa manage prod "collectstatic --noinput`
- Copy secret env variables to S3: `aws s3 cp env.json s3://prod.{{cookiecutter.project_slug}}.app/`

### Deploying the frontend

The frontend has to be built before it can be deployed.

Run `make build` to build the frontend from the project directory.

Next, `cd deploy` then run `cdk deploy {{cookiecutter.project_slug}}-frontend`, which will handle creating/updating
an S3 bucket and Cloudfront distribution, upload the frontend files to S3, and invalidate the
Cloudfront cache.

Finally, mark the release on Sentry:

- `sentry-cli releases new <version>`
- `sentry-cli releases files <version> upload-sourcemaps frontend/dist/js/`
- `sentry-cli releases finalize <version>`

## Resources

- https://benjamincongdon.me/blog/2017/06/13/How-to-Deploy-a-Secure-Static-Site-to-AWS-with-S3-and-CloudFront/
- https://medium.com/swlh/register-an-external-domain-with-aws-api-gateway-using-an-aws-certificate-414a1568d162
- https://simonecarletti.com/blog/2016/08/redirect-domain-http-https-www-cloudfront/
- https://medium.com/@P_Lessing/single-page-apps-on-aws-part-1-hosting-a-website-on-s3-3c9871f126
- https://testdriven.io/blog/storing-django-static-and-media-files-on-amazon-s3/
