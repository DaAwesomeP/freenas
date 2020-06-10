import json
import os


def render(service, middleware):
    sys_config = middleware.call_sync('systemdataset.config')
    if not sys_config['path']:
        return

    with open('/etc/docker/daemon.json', 'w') as f:
        f.write(json.dumps({'data-root': os.path.join(sys_config['path'], 'services/docker')}))
