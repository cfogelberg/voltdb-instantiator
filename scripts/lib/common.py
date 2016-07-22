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

def __shexec(command, silent=False):
  if not silent:
    print(command)
  return os.system(command)

if __name__ == '__main__':
  print('This file is not configured to be run separately, it provides library functions for other scripts')
