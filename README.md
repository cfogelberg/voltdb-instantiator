# VOLTDB-INSTANTIATOR

[VoltDB](https://voltdb.com/) is an in-memory, ACID SQL database optimised for OLTP requirements on big data scale.

But sometimes you aren't looking to run a 50-node cluster with billions of records. Instead you just want to stand up a database locally and easily for development, testing or a smaller application. The "VoltDB Instantiator" makes this easy. It has been developed and tested with VoltDB v6.4.

## Starting up a database

### How to create a basic, single-host DB

This functionality is implemented by the `createclean` script. Any existing DB in this directory will be deleted. The behaviour is undefined if any other DB is using the same ports. Otherwise, following these steps will create an empty database with your desired configuration on your localhost.

1. Create a base directory to house your VoltDB instance (e.g. `~/my-db-dir`)
2. Copy a configuration XML file from `configurations` to `~/my-db-dir`, renaming the file to `deployment.xml`
3. Copy and edit `configurations/other-configuration.yaml` to `~/my-db-dir`
3. Run `scripts/createclean ~/my-db-dir`

## How to create a more complex DB

In general:

1. Specify the deployment.xml and other-configuration.yaml file identically and as appropriate on all relevant hosts
2. Execute `createclean` on each host, starting with the master host (as specified in the `host` option in  `other-configuration.yaml`)
3. Execute `loadjar` and `loadddl` as required on any one of the hosts

## Loading stored procedure .class files into the database

This functionality is implemented by the `loadjar` script. The following step will load a JAR file into the database:

- Run `scripts/loadjar ~/my-db-dir /path/to/jar/file`

SQL files contained within this JAR file can be loaded to the database separately using the `loadddl` script.

## Loading tables and stored procedures into the database

This functionality is implemented by the `loadddl` script. The following step will load a SQL file into the database:

- Run `scripts/loadddl ~/my-db-dir /path/to/sql/file`

OR

- Run `scripts/loadddl ~/my-db-dir /path/to/jar/or/zip/archive/file`

If the tables or stored procedure files specified in the SQL file loaded have already been loaded the script will fail. If the DDL file specifies Java stored procedures whose classes have not been loaded into the database then the script will fail.

Note that a path to a JAR file or ZIP file containing one or more SQL files can also be specified. In this case the SQL files will be extracted from the JAR file and loaded into the database in the ascending sorted order of their base names.

## Issues / Todo

- No --help or usage information provided
- Limited error checking / unclear failure (Are ports already being used? Has VoltDB creation failed with a FATAL error?)
- Script output is noisy

## Changelog

v0.1.0 - Initial version, `createclean` only
v0.2.0 - Basic `loadddl` added
v0.2.1 - `loadddl` extended to load SQL files stored in jar and zip archives
v0.3.0 - `loadjar` implemented

## License

Copyright (C) 2016 Christo Fogelberg, see the LICENSE file for details
