# Veracode API wrapper

### A python wrapper for communicating with the [Veracode](https://www.veracode.com) APIs.
This python module currently supports the following APIs.
- [Results](https://help.veracode.com/reader/LMv_dtSHyb7iIxAQznC~9w/WgCXPStuSb3isrDrHlmV9Q)
- [Upload](https://help.veracode.com/reader/LMv_dtSHyb7iIxAQznC~9w/qUW0fV37Fd~NHav8afNqMg)
- [Admin](https://help.veracode.com/reader/LMv_dtSHyb7iIxAQznC~9w/ulPQBQUmp35KhYK_qQng1A)
- [Mitigation](https://help.veracode.com/reader/LMv_dtSHyb7iIxAQznC~9w/bIVY7~q72vIVr0ytei5Nbw)
- [Flaw Report](https://help.veracode.com/reader/LMv_dtSHyb7iIxAQznC~9w/krVurK9DJnzJ7Vu3Tlieuw)
- [Sandbox](https://help.veracode.com/reader/LMv_dtSHyb7iIxAQznC~9w/WyXt9M~6SqjQ1L6LnjzJcA)


There is also a top level helper class `Application`, 
this can be instantiated with an application name which exposes properties that will lazy load data from the corresponding API. 

## Install

```
$ pip3 install veracode-python
```

## Configuration
To use this module you will need to configure your API credentials. Visit the Veracode [help center](https://help.veracode.com/reader/LMv_dtSHyb7iIxAQznC~9w/Gv1oHnvAIwMy2gQSBrF0fA) for more information.

Create a file `~/.veracode/credentials` containing your API id and secret in the following format.

```
[DEFAULT]
VERACODE_API_ID = 5318f66b17e00...
VERACODE_API_SECRET = 4dc495318f66b1037c...
```

You can setup multiple profiles if needed and select the profile via the `VERACODE_API_PROFILE` enviroment variable.

## Usage

Using the top level classes you can do fairly complex tasks with a few lines of code. Keep in mind that the structure of these modules may change as I add more classes. 

**NOTE**: You can set the `VERACODE_LOG_LEVEL` enviroment varible to any valid python logger [loglevel](https://docs.python.org/3/library/logging.html#logging-levels). The default is `NOTSET`. Of course you can set the loglevel directly in your code rather than setting an enviroment variable.  

### Application


```python
In [1]: from veracode.application import Application
In [2]: app = Application('verademo')                                                                                                                                                     
In [3]: app 
Out[3]: <Veracode Application: name='verademo', id=552948>

In [4]: app.build                                                                                                                                                                         
Out[4]: <Veracode Build: version='Wed Oct 30 18:31:14 UTC 2019 8522bfa6', id=5347783>

In[5]: app.policy  
Out[5]: 'Production - Critical + SCA'

In [6]:  app.sandbox
Out[6]: <Veracode Sandbox: name='None', id=None>

In [7]: app.sandbox = app.sandboxes[2]
In [8]: app.sandbox                                                                                                                                                                                                  
Out[8]: <Veracode Sandbox: name='CI Nightly Sandbox', id=1556344>

In [9]: app.build                                                                                                                                                                         
Out[9]: <Veracode Build: version='Wed Oct 29 Nightly Sandbox Build', id=5346981>

In [10]: app.sandbox = None
In [11]: app.build   
Out[11]: <Veracode Build: version='Wed Oct 30 18:31:14 UTC 2019 8522bfa6', id=5347783>

In [12]: app.build.report
Out[12]: <Veracode Report: application='verademo', sandbox='None', build='Wed Oct 30 18:31:14 UTC 2019 8522bfa6', flaws=160>

In [13]: list(app.build.report.flaws)[0]
Out[13]: <Veracode Flaw: CWE='78', severity=5>

```




### Direct SDK access
Returns a python object with a one-to-one mapping to the returned XML.

```python
from veracode import SDK       
    
result = SDK.results.SummaryReport(build_id=4324494) # use a valid id for your app.
print('The number of unmitigated flaws is:', result.flaws_not_mitigated)
```
```
The number of unmitigate flaws is: 160
```

### Direct API access
Returns a custom response object with properties `data`: returned XML and `status_code`: server response code.  The full response is also avialable.

If the API requires parameters you can pass them to the constructor as a python dictionary.  The parameter names match the API parameters for the coresponding API that can be found on the [help center](https://help.veracode.com/reader/LMv_dtSHyb7iIxAQznC~9w/HmF8Z4cz70Rb2y1p39tWDw).

```python
from veracode import API                                                

builds = API.results.GetAppBuilds.get()       
print('Server returned:', builds.status_code)
print('The first 20 bytes of the response XML is:', builds.data[:20])
```

```
Server returned: 200
The first 20 bytes of the response XML is: '<?xml version="1.0" '
```
