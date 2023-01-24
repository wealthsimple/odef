#

## Goal

The goal of the example event is to guide you while you are building your own data dictionaries for many of your products.

## Data Dictionary Folder Structure

```bash
├── DataDictionary
│   └── example
│       ├── README.MD
│       └── events
│           └── example_data_dict.yml
```

- Create new folder (like `example`) for each data source
- Create README.MD and populate with general description of the data source and most common fields
- In the `events` you can create a `yml` file which can be used by automation and for easy visualization and searches

## YML file structure

`title`: Title of the log format\
`description`: Description - human readable\
`platform`: the platform where the logs are generated\
`log_source`: where the data is generated\
`event_code`: how the data is indexed\
`event_version`: the version of the event\
`event_fields`:

- `standard_name`: the standard field name if you have applied data transformations
- `standard_type`: type of the field as per standard
- `name`: original field name
- `type`: type of the field (datetime etc)
- `description`: For example: "The date and time request was made, in coordinated universal time(UTC)."
- `sample_value`: for example: '2020-03-17T06: 07: 08Z'
