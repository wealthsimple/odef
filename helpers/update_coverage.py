import os
import yaml
import glob 

def write_coverage(inlist, path): 
    with open(path,'w') as f:
        yaml.dump(inlist, f)


def collect_all_queries(folders=["HUNTS","DETECTIONS"]):
    coverage = dict()
    for folder in folders: 
        for f_path in glob.glob(f"./{folder}/*/*.yml"):
            if os.stat(f_path).st_size >1 and 'example' not in f_path: 
                with open(f_path) as stream:
                        ymlfile = yaml.safe_load(stream)
                        filename=f_path.split('/')[-1]
                        mitre_id = str(ymlfile.get('mitre_id',''))
                        val = coverage.get(mitre_id, [])
                        val.append(filename)
                        coverage[mitre_id] = val
    
    return coverage

def update_coverage():

    coverage_file= './MitreNavigatorMap/mitre_coverage.yml'
   
    coverage = collect_all_queries()

    write_coverage(coverage, coverage_file)

if __name__ == "__main__":
    coverage_file= './MitreNavigatorMap/mitre_coverage.yml'
   
    coverage = collect_all_queries()

    write_coverage(coverage, coverage_file)