<div align="center">
    <br><img src="https://github.com/ThiagoPanini/cloudgeass/blob/main/docs/assets/gifs/logo-animated-intro.gif?raw=true" alt="cloudgeass-animated-intro">
</div>


<div align="center">  
  <br>
  
  [![PyPI](https://img.shields.io/pypi/v/cloudgeass?color=purple)](https://pypi.org/project/cloudgeass/)
  ![PyPI - Downloads](https://img.shields.io/pypi/dm/cloudgeass?color=purple)
  ![PyPI - Status](https://img.shields.io/pypi/status/cloudgeass?color=purple)
  ![GitHub Last Commit](https://img.shields.io/github/last-commit/ThiagoPanini/cloudgeass?color=purple)
  <br>

  ![CI workflow](https://img.shields.io/github/actions/workflow/status/ThiagoPanini/cloudgeass/ci-main.yml?label=ci)
  [![Documentation Status](https://readthedocs.org/projects/cloudgeass/badge/?version=latest)](https://cloudgeass.readthedocs.io/en/latest/?badge=latest)
  [![codecov](https://codecov.io/github/ThiagoPanini/cloudgeass/branch/main/graph/badge.svg?token=7HI1YGS4AA)](https://codecov.io/github/ThiagoPanini/cloudgeass)

</div>

> **Note**
> Now *cloudgeass* has an [official documentation page on readthedocs](https://cloudgeass.readthedocs.io/en/latest/)! possui uma **documentação oficial** no readthedocs! Check it out to get access to the latest features!

## Quickstart

To start using the package, just install it using [pip](https://pypi.org/project/pip/) (or any other Python dependency management of your choose) as:

```python
pip install cloudgeass
```

You may want to install *cloudgeass* in a [Python virtual environment](https://docs.python.org/3/library/venv.html) to get a good control of your project or application dependencies. If you don't know what this is about, feel free to take a look at this excellent [article from Real Python](https://realpython.com/python-virtual-environments-a-primer/).

## Modules

Getting straight to the point, each *cloudgeass* module represents an AWS service that contains at least one class and a bunch of methods built from both boto's source client and resource for that service.

In other words, some modules that you can find here are:

- `cloudgeass.aws.s3` for working with S3 service
- `cloudgeass.aws.ec2` for working with EC2 service
- `cloudgeass.aws.secrets` for working with Secrets Manager service
- *and some others*

## Classes

Each one of the aforementioned modules have at least one class that can be imported on user's application in order to provide access to all features for that given AWS service. So, we have:

- `cloudgeass.aws.s3.S3Client` class with methods to operate with S3 service
- `cloudgeass.aws.ec2.EC2Client` class with methods to operate with EC2 service
- `cloudgeass.aws.secrets.SecretsManagerClient` class with methods to operate with Secrets Manager service
- *and some others*

## Attributes

All *cloudgeass'* service classes are initialized with a set of predefined attributes to make the work easier. Those basic attributes are:

| **Service class attribute** | **Description** |
| :-- | :-- |
| `self.logger` | A preconfigured logger object to build and stream informative log messages |
| `self.client` | A boto3 client for the given service |
| `self.resource` | A boto3 resource for the given service |

The attributes can be externally accessed for all class instances created on an application. This means users can build an application using both *cloudgeass* and source boto3 code.

## Methods

Finally, each service class has its own set of methods that, in fact, enables the power of using *cloudgeass* to do simple tasks in an AWS environment. To mention some of them, we have:

- [S3Client.get_last_date_partition()](./mkdocstrings/s3.md/#cloudgeass.aws.s3.S3Client.get_last_date_partition) to get the last date partition from a table stored in S3
- [EC2Client.get_default_vpc_id()](./mkdocstrings/ec2.md/#cloudgeass.aws.ec2.EC2Client.get_default_vpc_id) to get the default VPC ID of an AWS account
- [SecretsManagerClient.get_secret_string()](./mkdocstrings/secrets.md/#cloudgeass.aws.secrets.SecretsManagerClient.get_secret_string) to get a secret string given a secret ID

___

## Contact me

- GitHub: [@ThiagoPanini](https://github.com/ThiagoPanini)
- LinkedIn: [Thiago Panini](https://www.linkedin.com/in/thiago-panini/)
- Hashnode: [panini-tech-lab](https://panini.hashnode.dev/)
- DevTo: [thiagopanini](https://dev.to/thiagopanini)


___

## References

**Python**

- [Python - Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [Stack Overflow - Reading Pandas DataFrame from S3](https://stackoverflow.com/questions/37703634/how-to-import-a-text-file-on-aws-s3-into-pandas-without-writing-to-disk)

**Docs**

- [NumPy docstrings](https://numpydoc.readthedocs.io/en/latest/format.html)
- [Eduardo Mendes - Live de Python 189 - MkDocs](https://www.youtube.com/watch?v=GW6nAJ1NHUQ&t=2s&ab_channel=EduardoMendes)
- [MkDocs](https://www.mkdocs.org/)
- [pmdown-extensions](https://facelessuser.github.io/pymdown-extensions/)
- [GitHub - MkDocs Themes](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes)
- [GitHub - Material Theme for MkDocs](https://github.com/squidfunk/mkdocs-material)
- [Material for MkDocs - Setup](https://squidfunk.github.io/mkdocs-material/setup/changing-the-colors/)

**Github**

- [GitHub Actions - pypa/gh-action-pypi-publish](https://github.com/marketplace/actions/pypi-publish)
- [Medium - Major, Minor and Patch](https://medium.com/fiverr-engineering/major-minor-patch-a5298e2e1798)
- [Medium - Automate PyPI Releases with GitHub Actions](https://medium.com/@VersuS_/automate-pypi-releases-with-github-actions-4c5a9cfe947d)

**Tests**

- [Codecov - Setting Threshold](https://github.com/codecov/codecov-action/issues/554#issuecomment-1261250304)
- [Codecov - About the Codecov YAML](https://docs.codecov.com/docs/codecov-yaml)
- [Codecov - Status Checks](https://docs.codecov.com/docs/commit-status)
- [Codecov - codecov.yml Reference](https://docs.codecov.com/docs/codecovyml-reference)
- [Codecov - Ignore Paths](https://docs.codecov.com/docs/ignoring-paths)
