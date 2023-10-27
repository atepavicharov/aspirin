1. Create an "empty" DeZign file with the db type and version
2. Replace the content enclosed by the `<ENTITIES>` tag
    ```xml
    ...
    <?xml version="1.0" encoding="iso-8859-1"?>
    <dezign>
    ...
    <DOMAINS>
    </DOMAINS>
    
    <ENTITIES> <!--REPLACE FROM HERE (incl.)-->
    ...
    </ENTITIES> <!--REPLACE TO HERE (incl.)-->
    
    <SUBCATEGORIES>
    </SUBCATEGORIES>
    ...
    </dezign>
    ```

The script is using [simple_ddl_parser](https://pypi.org/project/simple-ddl-parser/) which should pick the target SQL dialect.
