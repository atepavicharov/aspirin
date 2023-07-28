import xml.etree.ElementTree as ET
from simple_ddl_parser import parse_from_file

# Inputs
print('Path to file must be with forward slashes \'/\' and no quotes')
ddl_file = input("path to ddl:")
print("Supported dialects are listed here https://pypi.org/project/simple-ddl-parser/: 'mssql','mysql'")
print("Example: mssql,mysql")
sql_dialect = input("sql dialect:")


def rm_brackets(instr):
    return instr.replace("[", "").replace("]", "").replace(")", "").replace("(", "")


"""
datatype_map() is supposed to translate 'exotic' data types into
DeZign native ones, but turns out that DeZign support a lot of them
so this might not need to be used for anything else than int -> integer
"""


def datatype_map(data_type):
    if data_type == "int":
        return "integer"
    elif data_type == "datetime":  # example how to continue it if needed
        return "datetime"
    else:
        return rm_brackets(data_type)


# Parse the DDL
result = parse_from_file(file_path=ddl_file, output_mode=sql_dialect, group_by_type=True)
# print(result)
# Build the XML
root = ET.Element('entities')
entity_id = 0

# Start building the .xml
# 1. Main (table name, schema)
for table in result['tables']:
    entity_id = entity_id + 1
    ent = ET.SubElement(root, 'ent')
    entity_name = ET.SubElement(ent, 'name').text = rm_brackets(table['table_name'])
    ET.SubElement(ent, 'id').text = str(entity_id)
    entity_schema = ET.SubElement(ent, 'schema').text = rm_brackets(table['schema'])

    attributes = ET.SubElement(ent, 'attributes')
    col_id = 0
    column_dict = {}

    # 2. Columns
    for column in table['columns']:
        col_id = col_id + 1
        column_dict[rm_brackets(column['name'])] = col_id  # holds column positions {'loan_id':1, 'customer_id':2}

        attr = ET.SubElement(attributes, 'attr')
        ET.SubElement(attr, 'name').text = rm_brackets(column['name'])
        ET.SubElement(attr, 'id').text = str(col_id)
        dt = ET.SubElement(attr, 'dt')
        ET.SubElement(dt, 'dtlistname').text = datatype_map(rm_brackets(column['type']))

        if rm_brackets(column['type']) in ['varchar', 'nvarchar']:
            ET.SubElement(dt, 'le').text = str(column['size'])

        # columns size value of decimals are parsed by the simple_ddl_parser as "size":(18,2)
        # bellow they are allocated to size and precision
        if rm_brackets(column['type']) in ['decimal']:
            ET.SubElement(dt, 'le').text = rm_brackets(str(column['size']).split(",")[0])
            ET.SubElement(dt, 'pr').text = rm_brackets(str(column['size']).split(",")[1]).strip()

        # no idea what <sd> and <inc> tags are for, but I saw they were in the xml
        ET.SubElement(dt, 'sd').text = '1'
        ET.SubElement(dt, 'inc').text = '1'

    # 3. Primary Keys
    if table['primary_key']:  # this checks if the list is not empty
        pkcon = ET.SubElement(ent, 'pkcon')  # primary key
        # [0] because it is contraints{ primary_keys [ {contraint_name:"name"} ] }
        if 'primary_keys' in table['constraints']:
            ET.SubElement(pkcon, 'name').text = rm_brackets(table['constraints']['primary_keys'][0]['constraint_name'])
            ET.SubElement(pkcon, 'nametemplate').text = rm_brackets(
                table['constraints']['primary_keys'][0]['constraint_name'])
        else:  # Generic constraint name
            ET.SubElement(pkcon, 'name').text = "PK_" + rm_brackets(table['table_name'])
            ET.SubElement(pkcon, 'nametemplate').text = "PK_%table%"
        if 'clustered_primary_key' in table:
            ET.SubElement(pkcon, 'pkconclustering').text = 'clustered'
        else:
            ET.SubElement(pkcon, 'pkconclustering').text = 'nonclustered'

        # 3.1. Link columns to PK via <attributeid>
        attributeids = ET.SubElement(pkcon, 'attributeids')
        for pk in table['primary_key']:
            ET.SubElement(attributeids, 'attributeid').text = str(column_dict[rm_brackets(pk)])

tree = ET.ElementTree(root)
ET.indent(tree, space="\t", level=0)  # prettify the xml with indent
try:
    tree.write('entities.xml', encoding="utf-8")
    print("'entities.xml' created successfully")
except Exception as err:
    print("Failed to create the xml")
    print(err)
