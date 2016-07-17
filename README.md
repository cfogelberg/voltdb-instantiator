# VOLTDB-INSTANTIATOR

[VoltDB](https://voltdb.com/) is an in-memory, ACID SQL database optimised for OLTP requirements on big data scale.

But sometimes you aren't looking to run a 50-node cluster with billions of records. Instead you just want to stand up a database locally and easily for development, testing or a smaller application. The "VoltDB Instantiator" makes this easy. It has been developed and tested with VoltDB v6.4.

## Basic, single-host usage

Following these steps will create an empty database with your desired configuration on your localhost.

1. Create a base directory to house your VoltDB instance (e.g. `~/my-temp-db`)
2. Copy a configuration XML file from `configurations` to `~/my-temp-db`, renaming the file to `deployment.xml`
3. Copy and edit `configurations/other-configuration.yaml` to `~/my-temp-db`
3. Run `scripts/createclean ~/my-type-db`

## Issues / Todo

- Limited range of examples - full stub and basic/CE only
- No DB schema population or stored procedure loading

## Changelog

v0.1.0 - Initial version

## License

Copyright (C) 2016 Christo Fogelberg, see the LICENSE file for details
