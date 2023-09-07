import os
import yaml
import argparse


def main(args):
    update_yaml_with_model_version(args.model_name)


def update_yaml_with_model_version(model_name):
    file_path = os.path.join(os.getcwd(), 'src/deploy.yml')
    with open(file_path, 'r') as f:
        content = yaml.safe_load(f)

    content['model'] = model_name

    with open(file_path, 'w') as file:
        yaml.safe_dump(content, file)


def parse_args():
    # setup arg parser
    parser = argparse.ArgumentParser()

    # add arguments
    parser.add_argument("--model_name",
                        dest='model_name',
                        type=str)

    # parse args
    args = parser.parse_args()

    # return args
    return args


# run script
if __name__ == "__main__":

    # parse args
    args = parse_args()

    # run main function
    main(args)
