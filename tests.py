if __name__ == '__main__':
    import doctest
    from veracode import application, sandbox, build
    from veracode.exceptions import *

    try:
        doctest.testmod(application, raise_on_error=True)
        doctest.testmod(sandbox, raise_on_error=True)
        doctest.testmod(build, raise_on_error=True)
    except:
        pass

    finally:
        app = application.Application('TEST_APPLICATION')
        app.delete()

# pycco veracode/*.py veracode/SDK veracode/API -ips
