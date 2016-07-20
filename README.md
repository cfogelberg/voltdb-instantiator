# VOLTDB-INSTANTIATOR

[VoltDB](https://voltdb.com/) is an in-memory, ACID SQL database optimised for OLTP requirements on big data scale.

But sometimes you aren't looking to run a 50-node cluster with billions of records. Instead you just want to stand up a database locally and easily for development, testing or a smaller application. The "VoltDB Instantiator" makes this easy. It has been developed and tested with VoltDB v6.4.

## Starting up a database

### Basic, single-host usage

This functionality is implemented by the `createclean` script. Any existing DB in this directory will be deleted. The behaviour is undefined if any other DB is using the same ports. Otherwise, following these steps will create an empty database with your desired configuration on your localhost.

1. Create a base directory to house your VoltDB instance (e.g. `~/my-temp-db`)
2. Copy a configuration XML file from `configurations` to `~/my-temp-db`, renaming the file to `deployment.xml`
3. Copy and edit `configurations/other-configuration.yaml` to `~/my-temp-db`
3. Run `scripts/createclean ~/my-temp-db`

## Loading stored procedure .class files into the database

// To be implemented using the `loadjar` script

## Loading tables and stored procedures into the database

This functionality is implemented by the `loadddl` script. Following these steps will load a SQL file into the database:

1. Run `scripts/loadddl ~/my-temp-db /path/to/sql/file`

If the tables or stored procedure files specified in the SQL file loaded have already been loaded the script will fail. If the DDL file specifies Java stored procedures whose classes have not been loaded into the database then the script will fail.

Note that a path to a JAR file containing one or more SQL files can also be specified. In this case the SQL files will be extracted from the JAR file and loaded into the database in the ascending sorted order of their base names.

## Issues / Todo

- Limited range of configuration examples - full stub and basic/CE only
- No stored procedure class file loading
- No --help or usage information provided
- Script output is noisy
- `loadddl` can load SQL files, but not SQL files stored in .jar files

## Changelog

v0.1.0 - Initial version, `createclean` only
v0.2.0 - Basic `loadddl` added

## License

Copyright (C) 2016 Christo Fogelberg, see the LICENSE file for details
