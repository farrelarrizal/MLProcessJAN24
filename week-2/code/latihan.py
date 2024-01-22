import yaml

# Membaca file YAML
path_config = "../config/config.yaml"
config = yaml.safe_load(open(path_config))


nama = config['identitas']['nama']
umur = config['identitas']['umur']
print('Nama saya adalah', nama)