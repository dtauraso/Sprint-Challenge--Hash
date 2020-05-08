from collections import defaultdict
def finder(files, queries):

    """
    YOUR CODE HERE
    """
    # defaultdict(list)
    filename_path = defaultdict(list)
    for file_path in files:
        key = file_path.split('/')[-1]
        filename_path[key].append(file_path)
    
    result = []
    # file_name -> file_path
    for file_name in queries:
        # collect all the pathnames associated with the filename
        result += filename_path[file_name]
    
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
