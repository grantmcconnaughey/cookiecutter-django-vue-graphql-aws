import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="{{cookiecutter.project_slug}}",
    version="0.1",
    description="{{cookiecutter.project_name}} CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="{{cookiecutter.author_name}}",
    package_dir={"": "{{cookiecutter.project_slug}}"},
    packages=setuptools.find_packages(where="{{cookiecutter.project_slug}}"),
    install_requires=[
        "aws-cdk.core==1.32.2",
        "aws-cdk.aws-s3==1.32.2",
        "aws_cdk.aws_rds==1.32.2",
        "aws_cdk.aws_cloudfront==1.32.2",
        "aws_cdk.aws_s3_deployment==1.32.2",
        "aws_cdk.aws_route53==1.32.2",
        "aws_cdk.aws_route53_targets==1.32.2",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
