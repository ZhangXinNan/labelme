import os.path as osp
import shutil

import yaml

<<<<<<< HEAD
from labelme import logger
=======
from labelme.logger import logger
>>>>>>> upstream/master


here = osp.dirname(osp.abspath(__file__))


def update_dict(target_dict, new_dict, validate_item=None):
    for key, value in new_dict.items():
        if validate_item:
            validate_item(key, value)
        if key not in target_dict:
<<<<<<< HEAD
            logger.warn('Skipping unexpected key in config: {}'
                        .format(key))
            continue
        if isinstance(target_dict[key], dict) and \
                isinstance(value, dict):
=======
            logger.warn("Skipping unexpected key in config: {}".format(key))
            continue
        if isinstance(target_dict[key], dict) and isinstance(value, dict):
>>>>>>> upstream/master
            update_dict(target_dict[key], value, validate_item=validate_item)
        else:
            target_dict[key] = value


# -----------------------------------------------------------------------------


def get_default_config():
<<<<<<< HEAD
    config_file = osp.join(here, 'default_config.yaml')
    with open(config_file) as f:
        config = yaml.load(f)

    # save default config to ~/.labelmerc
    user_config_file = osp.join(osp.expanduser('~'), '.labelmerc')
=======
    config_file = osp.join(here, "default_config.yaml")
    with open(config_file) as f:
        config = yaml.safe_load(f)

    # save default config to ~/.labelmerc
    user_config_file = osp.join(osp.expanduser("~"), ".labelmerc")
>>>>>>> upstream/master
    if not osp.exists(user_config_file):
        try:
            shutil.copy(config_file, user_config_file)
        except Exception:
<<<<<<< HEAD
            logger.warn('Failed to save config: {}'.format(user_config_file))
=======
            logger.warn("Failed to save config: {}".format(user_config_file))
>>>>>>> upstream/master

    return config


def validate_config_item(key, value):
<<<<<<< HEAD
    if key == 'validate_label' and value not in [None, 'exact', 'instance']:
        raise ValueError('Unexpected value `{}` for key `{}`'
                         .format(value, key))


def get_config(config_from_args=None, config_file=None):
    # Configuration load order:
    #
    #   1. default config (lowest priority)
    #   2. config file passed by command line argument or ~/.labelmerc
    #   3. command line argument (highest priority)

    # 1. default config
    config = get_default_config()

    # 2. config from yaml file
    if config_file is not None and osp.exists(config_file):
        with open(config_file) as f:
            user_config = yaml.load(f) or {}
        update_dict(config, user_config, validate_item=validate_config_item)

    # 3. command line argument
    if config_from_args is not None:
        update_dict(config, config_from_args,
                    validate_item=validate_config_item)
=======
    if key == "validate_label" and value not in [None, "exact"]:
        raise ValueError(
            "Unexpected value for config key 'validate_label': {}".format(
                value
            )
        )
    if key == "shape_color" and value not in [None, "auto", "manual"]:
        raise ValueError(
            "Unexpected value for config key 'shape_color': {}".format(value)
        )
    if key == "labels" and value is not None and len(value) != len(set(value)):
        raise ValueError(
            "Duplicates are detected for config key 'labels': {}".format(value)
        )


def get_config(config_file_or_yaml=None, config_from_args=None):
    # 1. default config
    config = get_default_config()

    # 2. specified as file or yaml
    if config_file_or_yaml is not None:
        config_from_yaml = yaml.safe_load(config_file_or_yaml)
        if not isinstance(config_from_yaml, dict):
            with open(config_from_yaml) as f:
                logger.info(
                    "Loading config file from: {}".format(config_from_yaml)
                )
                config_from_yaml = yaml.safe_load(f)
        update_dict(
            config, config_from_yaml, validate_item=validate_config_item
        )

    # 3. command line argument or specified config file
    if config_from_args is not None:
        update_dict(
            config, config_from_args, validate_item=validate_config_item
        )
>>>>>>> upstream/master

    return config
