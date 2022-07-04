from cytomine import CytomineJob

def main(argv):
     with CytomineJob.from_cli(argv) as cj:
        # Implements your software here.
        
        # Will print the parameters with their values
        print(cj.parameters)

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])