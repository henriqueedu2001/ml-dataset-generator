import argparse
import sys

def parse_args(args: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='ML DATASET GENERATOR',
        description='An open source didactic dataset generator for machine learning tasks',
        epilog='',
        exit_on_error=False,
    )
    
    # machine learning task
    parser.add_argument('--task', dest='task', type=str, required=True,
                        help='the machine learning task')

    # the name of the dataset
    parser.add_argument('--name', dest='name', type=str, required=False,
                        help='the save destination directory')
    
    # the directory to save the dataset
    parser.add_argument('--directory', dest='directory', type=str, required=True,
                        help='the save destination directory')    
    
    return parser.parse_args(args)


def generate_dataset(args: argparse.Namespace):
    """Generates a dataset for the given machine learning task

    Args:
        args (argparse.Namespace): arguments for the dataset creation
    """
    
    task = args.task
    name = args.name
    directory = args.directory
    
    print(f'''Generating the dataset with the following configuration:
    task: {task}
    name: {name}
    directory: {directory}''')
    
    return

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    generate_dataset(args)