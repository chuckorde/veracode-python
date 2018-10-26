# Veracode SDK / API 

This is a work in progress.  It currently only supports the [Results API](https://help.veracode.com/reader/LMv_dtSHyb7iIxAQznC~9w/WgCXPStuSb3isrDrHlmV9Q). New modules will be added as time permits.

Documentation, test, and a proper setup comming soon. For now read the source, or use your tab key 🤪.

## Install

I will add a `setup.py` shortly.  Currently you can do the following to test.

```bash
$ git clone https://github.com/chuckorde/veracode-SDK.git 
$ cd veracode-SDK
$ export PYTHONPATH=${PYTHONPATH}:$(pwd)
```

## Configuration
```bash
$ python3 -m veracode.configure
```

## Usage

```python
In [1]: from veracode import SDK                                                                     
In [2]: result = SDK.results.SummaryReport(2412498)
In [3]: print(result.flaws_not_mitigated)                                                            
161

```
