# Veracode SDK / API

This is a work in progress.  It currently only supports the [Results API](https://help.veracode.com/reader/LMv_dtSHyb7iIxAQznC~9w/WgCXPStuSb3isrDrHlmV9Q) and partial support for the [Upload API](https://help.veracode.com/reader/LMv_dtSHyb7iIxAQznC~9w/qUW0fV37Fd~NHav8afNqMg). There is also a top level helper class `Application`,
this can be instantiated with an application name which exposes properties that will zazy load data from the corresponding API.

New modules will be added as time permits.

Tests and a proper setup comming soon. For now read the docs, source, or use your tab key 🤪.

## Install

I will add a `setup.py` shortly.  Currently you can do the following to test.

```bash
$ git clone https://github.com/chuckorde/veracode-SDK.git
$ cd veracode-SDK
$ export PYTHONPATH=${PYTHONPATH}:$(pwd)
```

<img src='/public/Application.svg' width=100% />
![Application](/public/Application.svg)

## Usage

### Top level classes

```python
In [1]: from veracode.application import Application

In [2]: app = Application('WebGoat')

In [3]: summary = app.summary

In [4]: summary
Out[4]: <veracode.SDK.results.SummaryReport at 0x109604be0>

In [5]: details = app.details

In [6]: details
Out[6]: <veracode.SDK.results.DetailedReport at 0x1096f10f0>

In [7]: app.details.first_build_submitted_date
Out[7]: datetime.date(2018, 10, 23)
```

### Direct SDK access
Returns a python object with a one-to-one mapping to the returned XML

```python
In [1]: from veracode import SDK

In [2]: result = SDK.results.SummaryReport(build_id=2412498) # use a valid id for your app.

In [3]: print(result.flaws_not_mitigated)
161

```

### Direct API access
Returns a constom response object with properties `data`: returned XML and `status_code`: server response code.  The full response is also avialable.

```python
In [1]: from veracode import API

In [2]: builds = API.results.GetAppBuilds.get()

In [3]: builds
Out[3]: <veracode.API.core.REST.response at 0x107f57c88>

In [4]: builds.status_code
Out[4]: 200

In [5]: builds.data[:20]
Out[5]: '<?xml version="1.0" '

```

