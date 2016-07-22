import os
import yaml

def load_configuration(dir_path):
  '''
  Loads the other configuration from {dir_path}/other-configuration.yaml, returning a dict
  '''
  configuration_path = os.path.join(dir_path, 'other-configuration.yaml')
  with open(configuration_path, 'r') as configure_yaml:
    configuration = yaml.load(configure_yaml)
    if not os.path.exists(configuration['voltdb_bindir']):
      raise Exception('Could not find VoltDB bin dir specified: ' + configuration['voltdb_bindir'])
    print('Other configuration loaded')
    return configuration

def check_voltdb_is_running(dir_path, other_configuration):
  '''
  Attempt to execute a system stored procedure on the VoltDB using the port specified in the YAML configuration file via
  sqlcmd. Raise an exception if the sqlcmd return code is non-zero.
  '''
  check_cmd = 'echo "exec @SystemInformation OVERVIEW" | sqlcmd --port={client} >> {dir_path}/log/loadddl.log' \
      .replace('{client}', str(other_configuration['ports']['client'])) \
      .replace('{dir_path}', dir_path) \
      .strip()
  os.chdir(dir_path)
  if __shexec(check_cmd) == 0:
    print('VoltDB appears to be running normally')
  else:
    raise Exception('Error, unable to connect to VoltDB client port')

def __shexec(command, silent=False):
  if not silent:
    print(command)
  return os.system(command)

if __name__ == '__main__':
  print('This file is not configured to be run separately, it provides library functions for other scripts')
