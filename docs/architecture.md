```text
                    +------------------+
                    |   Raw Dataset    |
                    | customer.csv     |
                    +--------+---------+
                             |
                             v
                +-------------------------+
                | Data Quality Framework  |
                +-------------------------+
                             |
         +-------------------+-------------------+
         |                   |                   |
         v                   v                   v

 +---------------+   +---------------+   +---------------+
 | Null Check    |   | Duplicate     |   | Schema        |
 | Validation    |   | Detection     |   | Validation    |
 +---------------+   +---------------+   +---------------+
         |                   |                   |
         +-------------------+-------------------+
                             |
                             v
                +-------------------------+
                | Data Cleansing Layer    |
                | Remove Errors           |
                | Remove Duplicates       |
                +-------------------------+
                             |
                             v
                +-------------------------+
                | Validated Dataset       |
                | validated_customer.csv  |
                +-------------------------+
                             |
                             v
                +-------------------------+
                | Analytics / Reporting   |
                | Dashboards / BI Tools   |
                +-------------------------+
