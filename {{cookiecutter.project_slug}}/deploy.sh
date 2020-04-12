#!/usr/bin/env bash

#
# Deploys the project to AWS.
#

# Confirmation prompt to avoid accidental deployments.
read -p "Continue (yes/n)? > " choice
case "$choice" in
  yes|Yes )
    # Check for zappa first
    if ! type zappa >/dev/null 2>&1
    then
        echo "zappa is not installed. Are you not in the correct virtualenv?"
        exit 1
    else
        echo "Starting deployment. Hold onto your butts..."
    fi
    ;;
  n|N|no|No )
    echo "Not deploying."
    exit 1;;
  * )
    echo "Invalid entry. Fully type out \"yes\" to deploy."
    exit 1;;
esac

# Deploy backend
echo "Deploying to AWS Lambda..."
zappa update prod

echo "Running migrations..."
zappa manage prod migrate

echo "Running collectstatic..."
zappa manage prod "collectstatic --noinput"

# Deploy frontend
echo "Deploying frontend..."
make build
cdk deploy {{cookiecutter.project_slug}}-frontend

# Sentry CLI releases
echo "Creating frontend release and uploading sourcemaps..."
export SENTRY_PROJECT={{cookiecutter.project_slug}}-frontend
export VERSION=0.1
sentry-cli releases new "{{cookiecutter.project_slug}}-frontend@$VERSION"
sentry-cli releases files "{{cookiecutter.project_slug}}-frontend@$VERSION" upload-sourcemaps frontend/dist/js/
sentry-cli releases finalize "{{cookiecutter.project_slug}}-frontend@$VERSION"

echo "Done!"
