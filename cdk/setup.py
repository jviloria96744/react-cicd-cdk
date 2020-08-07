import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="React Static Site Stack",
    version="0.0.1",

    description="A stack to create DEV and PROD stacks for a React App",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="Jay Viloria",

    package_dir={"": "static_site_stack"},
    packages=setuptools.find_packages(where="static_site_stack"),

    install_requires=[
        "aws-cdk.core==1.56.0",
        "aws-cdk.aws_s3==1.56.0",
        "aws-cdk.aws_cloudfront==1.56.0",
        "aws-cdk.aws_route53==1.56.0",
        "aws-cdk.aws_route53_targets==1.56.0",
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
