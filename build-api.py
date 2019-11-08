import yaml, os

def api_code(data, package, module, action):
    code = '''
class {module}(REST):
    """ class: {package}.API.{action}.{module}

        params: dynamic, see {package}.SDK.{action}.{module} for more info

        returns: XML data from veracode API
    """
    def __init__(self, args=None):
        super({module}, self).__init__('{module_url}.do', {version})

    @classmethod
    def get(self, **args):
        return self().GET(args, format='text')

    '''.format(
        package=package,
        action=action,
        module=module,
        module_url=module.lower(),
        version=data[package][action][module]['version']
    )
    return code

def sdk_code(data, package, module, action):
    params = data[package][action][module]['params']
    code = '''
class {module}(Base):
    """ class: {package}.SDK.{action}.{module}

        params:
{doc_params}

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
{init_args}
        ):

        super({module}, self).__init__(
            module='{action}',
            cls='{module}',
            fn='get',
            args={{
{params}
            }})
    '''.format(
            package=package,
            module=module,
            action=action,
            init_args = fmt_params(params, "{},", "{}=None,", 4),
            params = arg_params(params),
            doc_params = fmt_params(params, '{}: required', '{}: optional')
    )
    return code

def fmt_params(params, true_fmt, false_fmt, indent=3):
    if not params:
        return ''
    code = []
    for v,k in sorted((v,k) for (k,v) in params.items())[::-1]:
        if v:
            code.append('\t' * indent + true_fmt.format(k,k))
        else:
            code.append('\t' * indent + false_fmt.format(k))
    return '\n'.join(code)

def arg_params(params, indent=4):
    if not params:
        return ''
    code = []
    for v,k in sorted((v,k) for (k,v) in params.items())[::-1]:
        code.append('\t' * indent + "'{k}':{k},".format(k=k))
    return '\n'.join(code)


with open('api-spec.yaml') as f:
    data = yaml.safe_load(f)
    for package in data.keys():
        api_dir = os.path.join(package, 'API')
        sdk_dir = os.path.join(package, 'SDK')
        for d in [package, api_dir, sdk_dir]:
            #os.mkdir(d)
            pass
        # action should be module
        for action in data[package].keys():
            sdk_action = open(os.path.join(package, 'SDK', '{}.py'.format(action)), 'w')
            api_action = open(os.path.join(package, 'API', '{}.py'.format(action)), 'w')

            sdk_action.write('from veracode.SDK.core import Base\n')
            api_action.write('from veracode.API.core import REST\n')

            # module should be class
            for module in data[package][action].keys():
                api_action.write(api_code(data, package, module, action))
                sdk_action.write(sdk_code(data, package, module, action))

            sdk_action.close()
            api_action.close()
