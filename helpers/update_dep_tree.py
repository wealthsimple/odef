import os
import yaml
import glob 
import re 

def collect_all_queries(folders=["HUNTS","DETECTIONS"]):
    queries = dict()
    for folder in folders: 
        for f_path in glob.glob(f"./{folder}/*/*.yml"):
            if os.stat(f_path).st_size >1 and 'example' not in f_path: 
                with open(f_path) as stream:
                        ymlfile = yaml.safe_load(stream)
                        filename=f_path.split('/')[-1]
                        query_from_file = str(ymlfile.get('query',''))
                        datalocation = str(ymlfile.get('data_location',''))
                        queries[filename]={'source':datalocation,'query':query_from_file}

    return queries

def write_dep_tree(inlist, path): 
    with open(path,'w') as f:
        yaml.dump(inlist, f)

def data_source_factory(inobj):
    if inobj.get('source','') == "splunk":
        return get_splunk_fields(inobj.get('query'))
    elif inobj.get('source','') == "sentinelOne":
        return get_s1_fields(inobj.get('query'))
    else: 
        raise ValueError(inobj.get('source',''))
        
def get_splunk_fields(inquery):
    fields = re.findall(r"(\S+?)=", inquery.replace("(",""))
    fields = list(set(fields))
    if "index" in fields: 
        fields.remove("index")
    index = re.findall(r"index=(.+?) ", inquery)
    index = list(set(index))
    return index, fields
    
def get_s1_fields(inquery): 
    all_fields = re.findall(r"([A-Z].*?)\b", inquery)
    all_fields = list(set(all_fields))
    fields = list()
    commands = list()
    for i in all_fields: 
        if "OR" in i or "AND" in i or "Contains" in i: 
            commands.append(i)
        else: 
            fields.append(i)

    return "", fields

def update_dep_tree():
    dep_tree_file= './DepTree/dependency_tree.yml'

    coverage = collect_all_queries()
    for k,v in coverage.items():
        index, fields = data_source_factory(v)
        v['index'] = index
        v['fields'] = fields
    
    write_dep_tree(coverage, dep_tree_file)


if __name__ == "__main__":
    dep_tree_file= './DepTree/dependency_tree.yml'

    coverage = collect_all_queries()
    for k,v in coverage.items():
        index, fields = data_source_factory(v)
        v['index'] = index
        v['fields'] = fields
    
    write_dep_tree(coverage, dep_tree_file)